"""
Guest360Stage
"""
from aws_cdk import Stage
from app.src.reliability.utils import StackName

from app.infrastructure.pipeline.guest360_stack import Guest360Stack
from app.infrastructure.pipeline.guest360_docker import Docker


class Guest360Stage(Stage):
    """Guest360Stage

    Args:
        Stage (aws_cdk.Stage): AWS CDK stage
    """

    def __init__(
        self, scope, construct_id, environment_config: dict, stack_tags: dict, env=None, outdir=None, stage_name=None
    ) -> None:
        super().__init__(scope, construct_id, env=env, outdir=outdir)

        stack_name = self.node.try_get_context("stack_name")
        environment = self.node.try_get_context("environment")

        # Create the main stage with app stacks
        if stage_name == "main":
            self.g360_main_stack = Guest360Stack(
                self,
                "Guest360Stack",
                env=env,
                stack_name=StackName(stack_name, f"{stage_name}-{environment}").name(),
                tags=stack_tags,
                termination_protection=environment == "prod",
                environment_config=environment_config,
            )
        elif stage_name == "docker":
            self.g360_docker_stack = Docker(
                self,
                "Guest360Docker",
                env=env,
                stack_name=StackName(stack_name, f"{stage_name}-{environment}").name(),
                tags=stack_tags,
                termination_protection=environment == "prod",
                environment_config=environment_config,
            )
