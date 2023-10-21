ARG REPO_NAME
ARG IMAGE_TAG

FROM --platform=linux/amd64 ${REPO_NAME}:${IMAGE_TAG}

LABEL image_name="dataclass-app"
LABEL image_version="v1.0.1"

RUN yum update -y && \
    yum install -y shadow-utils && \
    yum clean all
RUN /usr/sbin/adduser --system auto-mater-user
RUN mkdir -p /dataclass-app && chown -R auto-mater-user:auto-mater-user /dataclass-app

ENV ENVIRONMENT="DOCKER"
WORKDIR /dataclass-app/app/src/data_structures/utilities/ui/dataclass_generator
COPY config config/
COPY custom_templates /custom_templates
COPY static static/
COPY templates templates/
COPY ui_scripts ui_scripts/
COPY utils utils/
COPY requirements.txt .
COPY pyproject.toml .
COPY *.py ./
RUN mkdir output
RUN pip install --no-cache-dir --upgrade -r requirements.txt

RUN chown -R auto-mater-user:auto-mater-user /dataclass-app
RUN chmod -R 755 /dataclass-app
ENV PYTHONPATH "${PYTHONPATH}:/dataclass-app/"
USER auto-mater-user
CMD ["data_contract_automater.lambda_handler"]
