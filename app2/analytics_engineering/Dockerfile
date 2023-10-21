FROM containers.disney.com/python:3.10-slim

LABEL image_name="analytics-engineering"
LABEL image_version="v1.0.0"

# Define the build argument, necessary for github actions export into a volume without permission errors
ARG ARG_RUNNER_USER_NAME=helix-user
ARG ARG_RUNNER_USER_UID=1100
ENV RUNNER_USER_NAME=$ARG_RUNNER_USER_NAME
ENV RUNNER_USER_UID=$ARG_RUNNER_USER_UID

ENV RUNNING_IN_DOCKER true
ENV DBT_PROJECT_NAME='mono'
ENV DBT_PROFILES_DIR=/helix/dbt/${DBT_PROJECT_NAME}/profile
ENV DBT_PROJECT_DIR=/helix/dbt/${DBT_PROJECT_NAME}/helix_${DBT_PROJECT_NAME}

RUN adduser --group ${RUNNER_USER_NAME} && adduser --shell /bin/bash --uid ${RUNNER_USER_UID} --ingroup ${RUNNER_USER_NAME} --disabled-login ${RUNNER_USER_NAME}
RUN apt-get update && apt-get install -y curl git jq wget

WORKDIR /
COPY --chown=${RUNNER_USER_NAME}:${RUNNER_USER_NAME} shell/ /home/${RUNNER_USER_NAME}/
COPY --chown=${RUNNER_USER_NAME}:${RUNNER_USER_NAME} /helix /helix/
COPY --chown=${RUNNER_USER_NAME}:${RUNNER_USER_NAME} ./requirements.txt .
RUN pip install -r requirements.txt --no-cache-dir --upgrade && \
    rm requirements.txt && \
    cd /helix/dbt/mono/helix_mono && \
    dbt deps && \
    mkdir /home/${RUNNER_USER_NAME}/artifacts && \
    cd / && \
    chown -R ${RUNNER_USER_NAME}:${RUNNER_USER_NAME} /helix && \
    chown -R ${RUNNER_USER_NAME}:${RUNNER_USER_NAME} /home/${RUNNER_USER_NAME} && \
    chmod -R 755 /helix && \
    chmod -R 755 /home/${RUNNER_USER_NAME} && \
    chmod -R 755 /home/${RUNNER_USER_NAME}/artifacts
    
# BASH_ENV allows for non-shell users to have init scripts
ENV BASH_ENV=/home/${RUNNER_USER_NAME}/post/synthetic_alias_generation.sh
USER ${RUNNER_USER_NAME}
ENTRYPOINT /home/$RUNNER_USER_NAME/entrypoint.sh
#CMD exec /bin/bash -c "trap : TERM INT; sleep infinity & wait"
# know this docker was downgraded... a great inspiration for future state would be:
# https://robertwinters.nl/post/tech/developer-workstation-devcontainers/