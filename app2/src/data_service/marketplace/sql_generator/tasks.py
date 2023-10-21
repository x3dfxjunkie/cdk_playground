"""
Executes Marketplace SQL generators based on configuration files.
"""
import json

import invoke


@invoke.Task
def generate_pipeline(
    environment: str,
):
    print("Placeholder for build entry point.")
    invoke.run("ls")
