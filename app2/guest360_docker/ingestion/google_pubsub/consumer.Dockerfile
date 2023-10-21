ARG REPO_NAME
ARG IMAGE_TAG

FROM --platform=linux/amd64 ${REPO_NAME}:${IMAGE_TAG}

WORKDIR /app

COPY runner.py environment_variables.py pubsub_interface.py requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "runner.py"]
