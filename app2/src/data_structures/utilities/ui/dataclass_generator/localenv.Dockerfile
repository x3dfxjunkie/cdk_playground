FROM containers.disney.com/python:3.10

LABEL image_name="dataclass-app"
LABEL image_version="v1.0.0"

RUN adduser --disabled-login auto-mater-user
RUN mkdir -p /dataclass-app && chown -R auto-mater-user:auto-mater-user /dataclass-app

ENV ENVIRONMENT="DOCKER"
WORKDIR /dataclass-app
COPY app/src/data_structures/utilities/ui/dataclass_generator/requirements.txt /dataclass-app/app/src/data_structures/utilities/ui/dataclass_generator/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /dataclass-app/app/src/data_structures/utilities/ui/dataclass_generator/requirements.txt

COPY pyproject.toml /dataclass-app/pyproject.toml
COPY app/src/data_structures/utilities/ui/dataclass_generator/ /dataclass-app/app/src/data_structures/utilities/ui/dataclass_generator/
RUN chown -R auto-mater-user:auto-mater-user /dataclass-app
RUN chmod -R 755 /dataclass-app
ENV PYTHONPATH "${PYTHONPATH}:/dataclass-app/"
USER auto-mater-user
CMD ["python", "app/src/data_structures/utilities/ui/dataclass_generator/data_contract_automater.py"]