#!/bin/bash
echo "Active DBT Project Directory: $DBT_PROJECT_DIR"
if [ -d "/workspace" ]
# if the local volume for dbt development exists (/workspace), navigate to said directory with the git pathing for docker dbt development,
# otherwise just navigate to the analytics engineering built part of the docker image (no volume)
then
    echo "Executing with a shell..."
    # the below scripts wrapped with "( )" are fired as background processes so as to not bloat the terminal
    # 1. check_extensions: will just do another check in case VSCODE extensions that should be installed, are not.
    #    for whatever reason, extensions can sometimes randomly not populate, especially when attaching to various containers in the g360 setup.
    #    this doesn't appear to be an issue when just using the analytics engineering container, because the extensions have the default .devcontainer.json file.
    #    if the extensions were all fully installed using the typical devcontainer.json file it passes.
    #    Zach mentioned this not uncommon today with the g360 contianer for other containers.
    # 2. safe.directory: is just to make the docker user trust git in local directory so users can make pushes to github without issue.
    #    this is also done as a shell script in the other main g360 contagitiner already
    # 3. status.relative: enforces git to always print out the full path of changed files in the container, as opposed to relative paths
    # 4. cd: automatically navigate to the "dbt project context" so users can immediately run dbt commands
    #    the "if" is for local work as of now, and the "else" is the built container that could be fired in an orchestrationt tool for example
    #    in either case, as long as user has configured their credentials correctly they should be able to execute "dbt debug", to show a successful connection
    #    know users need credentials FIRST before having a successful "dbt debug"
    target_file="/home/$RUNNER_USER_NAME/.bashrc"
    echo "git config --global --add safe.directory /workspace"      >> "$target_file"
    echo "git config status.relativePaths false"                    >> "$target_file"
    echo "source /home/$RUNNER_USER_NAME/post/synthetic_alias_generation.sh" >> "$target_file"
    echo "cd /workspace/app/analytics_engineering/$DBT_PROJECT_DIR" >> "$target_file"
    #trap : TERM INT; sleep infinity & wait &'
    sleep infinity
else
    echo "Executing without a shell..."
    # this would only fire in an orchestrator, same data just isolated to strictly analytics engineering files
    cd "$DBT_PROJECT_DIR"
    eval "$ARGS"
fi