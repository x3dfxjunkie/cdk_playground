import aws_cdk


def Iam(principal: str, value=None) -> aws_cdk.aws_iam.IPrincipal:
    """Iam: create an iprincipal interfact of "principal" type, using "value" lookup.

    Args:
        principal (str): Type of IAM principal to return
        value (str - optional): ID of IAM principal to return

    Returns:
        aws_cdk.aws_iam.IPrincipal:
    """
    if principal.lower() == "any":
        return aws_cdk.aws_iam.AnyPrincipal()
    elif principal.lower() == "account":
        return aws_cdk.aws_iam.AccountPrincipal(value)
    elif principal.lower() == "accountroot":
        return aws_cdk.aws_iam.AccountRootPrincipal()
    elif principal.lower() == "arn":
        return aws_cdk.aws_iam.ArnPrincipal(value)
    else:
        print("Bad unit passed")
        raise
