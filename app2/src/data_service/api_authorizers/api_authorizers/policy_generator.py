"""
Policy Generator
classes and functions used to generate a valid aws apigateway iam policy
"""

import re
from enum import Enum
from typing import Optional

from aws_lambda_powertools import Logger

logger = Logger(service=__name__)


class PolicyEffect(Enum):
    """
    Aws Policy Effect Enum
    """

    ALLOW = "Allow"
    DENY = "Deny"


class HttpVerb(Enum):
    """
    Http Verb Enum
    """

    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    PATCH = "PATCH"
    HEAD = "HEAD"
    DELETE = "DELETE"
    OPTIONS = "OPTIONS"
    ALL = "*"


class AuthPolicy:
    """
    AWS Authorization Policy Generator Class
        builds an iam policy for aws custom authorizor
    """

    # The policy version used for the evaluation. This should always be '2012-10-17'
    version = "2012-10-17"
    # The regular expression used to validate resource paths for the policy
    pathRegex = r"^[/.a-zA-Z0-9-\*]+$"

    def __init__(
        self,
        principal_id: str,
        account_id: str,
        rest_api_id: str = "*",
        region: str = "*",
        stage: str = "*",
    ):
        # The AWS account id the policy will be generated for. This is used to create the method ARNs.
        self.account_id = account_id

        # The principal used for the policy, this should be a unique identifier for the end user.
        self.principal_id = principal_id

        """these are the internal lists of allowed and denied methods. These are lists
        of objects and each object has 2 properties: A resource ARN and a nullable
        conditions statement.
        the build method processes these lists and generates the approriate
        statements for the final policy"""
        self.allow_methods = []
        self.deny_methods = []

        # The API Gateway API id. By default this is set to '*'
        self.rest_api_id = rest_api_id

        # The region where the API is deployed. By default this is set to '*'
        self.region = region

        # The name of the stage used in the policy. By default this is set to '*'
        self.stage = stage

    def _add_method(
        self, effect: PolicyEffect, verb: HttpVerb, resource: str, conditions: list
    ):
        """Adds a method to the internal lists of allowed or denied methods. Each object in
        the internal list contains a resource ARN and a condition statement. The condition
        statement can be null."""
        resource_pattern = re.compile(self.pathRegex)
        if not resource_pattern.match(resource):
            raise NameError(
                "Invalid resource path: "
                + resource
                + ". Path should match "
                + self.pathRegex
            )

        if resource[:1] == "/":
            resource = resource[1:]

        resource_arn = (
            f"arn:aws:execute-api:"
            f"{self.region}:{self.account_id}:"
            f"{self.rest_api_id}/{self.stage}/{verb.value}/{resource}"
        )
        logger.debug("effect.name=%s", effect.name)
        if effect == PolicyEffect.ALLOW:
            self.allow_methods.append(
                {"resource_arn": resource_arn, "conditions": conditions}
            )
        elif effect == PolicyEffect.DENY:
            self.deny_methods.append(
                {"resource_arn": resource_arn, "conditions": conditions}
            )
        else:
            raise ValueError

    def _get_empty_statement(self, effect: PolicyEffect):
        """Returns an empty statement object prepopulated with the correct action and the
        desired effect."""
        statement = {
            "Action": "execute-api:Invoke",
            "Effect": effect,
            "Resource": [],
        }

        return statement

    def _get_statement_for_effect(self, effect: PolicyEffect, methods: list):
        """This function loops over an array of objects containing a resource_arn and
        conditions statement and generates the array of statements for the policy."""
        statements = []

        if len(methods) > 0:
            statement = self._get_empty_statement(effect)

            for method in methods:
                if method["conditions"] is None or len(method["conditions"]) == 0:
                    statement["Resource"].append(method["resource_arn"])
                else:
                    conditional_statement = self._get_empty_statement(effect)
                    conditional_statement["Resource"].append(
                        method["resource_arn"])
                    conditional_statement["Condition"] = method["conditions"]
                    statements.append(conditional_statement)

            statements.append(statement)

        return statements

    def allow_all_methods(self):
        """Adds a '*' allow to the policy to authorize access to all methods of an API"""
        self._add_method(PolicyEffect.ALLOW, HttpVerb.ALL, "*", [])

    def deny_all_methods(self):
        """Adds a '*' allow to the policy to deny access to all methods of an API"""
        self._add_method(PolicyEffect.DENY, HttpVerb.ALL, "*", [])

    def allow_method(self, verb, resource):
        """Adds an API Gateway method (Http verb + Resource path) to the list of allowed
        methods for the policy"""
        self._add_method(PolicyEffect.ALLOW, verb, resource, [])

    def deny_method(self, verb: HttpVerb, resource):
        """Adds an API Gateway method (Http verb + Resource path) to the list of denied
        methods for the policy"""
        self._add_method(PolicyEffect.DENY, verb, resource, [])

    def allow_method_with_conditions(self, verb: HttpVerb, resource, conditions):
        """Adds an API Gateway method (Http verb + Resource path) to the list of allowed
        methods and includes a condition for the policy statement. More on AWS policy
        conditions here: http://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements.html#Condition"""
        self._add_method(PolicyEffect.ALLOW, verb, resource, conditions)

    def deny_method_with_conditions(self, verb: HttpVerb, resource, conditions):
        """Adds an API Gateway method (Http verb + Resource path) to the list of denied
        methods and includes a condition for the policy statement. More on AWS policy
        conditions here: http://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements.html#Condition"""
        self._add_method(PolicyEffect.DENY, verb, resource, conditions)

    def build(self):
        """Generates the policy document based on the internal lists of allowed and denied
        conditions. This will generate a policy with two main statements for the effect:
        one statement for Allow and one statement for Deny.
        Methods that includes conditions will have their own statement in the policy."""
        if (self.allow_methods is None or len(self.allow_methods) == 0) and (
            self.deny_methods is None or len(self.deny_methods) == 0
        ):
            raise NameError("No statements defined for the policy")

        policy = {
            "principalId": self.principal_id,
            "policyDocument": {"Version": self.version, "Statement": []},
        }

        policy["policyDocument"]["Statement"].extend(
            self._get_statement_for_effect("Allow", self.allow_methods)
        )
        policy["policyDocument"]["Statement"].extend(
            self._get_statement_for_effect("Deny", self.deny_methods)
        )

        return policy


def generate_policy_object(
    scope_map: dict,
    principal: str,
    account_id: str,
    rest_api_id: str,
    region: str = "*",
    stage: str = "*",
    client_scopes: Optional[list] = None,
    deny_all: bool = False,
) -> AuthPolicy:
    """
    generatePolicy: utilizes api_authorizer classes to generate an aws api gateway iam policy

    Attributes:
        s3_object (boto3 s3 resource): boto3 s3 object resource object
        principal (str): principal used for generating the iam policy
        account_id (str): aws account_id (utilize the lambda context object context.
        rest_api_id (str): aws rest api id
        region (str): default: "*" aws region to set policy for
        stage (str): default: "*" aws api gateway stage
        client_scopes (Optional[list]): list of client scopes
        deny_all (bool): default false
        s3_object_extra_args (Optional[dict]): used to provide extra arguments to object download example: {"VersionId": "my_version"}
    Return:
        AuthPolicy
    """

    if client_scopes is None:
        # lists are mutable and therefore cannot be handled with default empty list use none
        client_scopes = []

    policy = AuthPolicy(principal, account_id, rest_api_id, region, stage)

    for auth in scope_map["authorization"]:
        url_pattern = auth["urlPattern"]
        contexts = auth["scopes"]

        for context in contexts:
            # convert json string method to HttpVerbe Enum
            verb = HttpVerb[context["method"]]
            scopes_required = context["scopesRequired"]
            # Check if token has access to all required scopes:
            if all(scope in client_scopes for scope in scopes_required):
                policy.allow_method(
                    verb,
                    resource=url_pattern,
                )
            else:
                policy.deny_method(
                    verb,
                    resource=url_pattern,
                )
    # if deny_all override all policies and deny all
    if deny_all:
        policy.deny_all_methods()

    return policy


def generate_policy(
    scope_map: dict,
    principal: str,
    account_id: str,
    rest_api_id: str,
    region: str = "*",
    stage: str = "*",
    client_scopes: Optional[list] = None,
    deny_all: bool = False,
) -> dict:
    """
    generatePolicy: utilizes api_authorizer classes to generate an aws api gateway iam policy

    Attributes:
        s3_object (boto3 s3 resource): boto3 s3 object resource object
        principal (str): principal used for generating the iam policy
        account_id (str): aws account_id (utilize the lambda context object context.
        rest_api_id (str): aws rest api id
        region (str): default: "*" aws region to set policy for
        stage (str): default: "*" aws api gateway stage
        client_scopes (Optional[list]): list of client scopes
        deny_all (bool): default false
        s3_object_extra_args (Optional[dict]): used to provide extra arguments to object download example: {"VersionId": "my_version"}
    Return:
        dict
    """
    return generate_policy_object(
        scope_map,
        principal,
        account_id,
        rest_api_id,
        region,
        stage,
        client_scopes,
        deny_all,).build()
