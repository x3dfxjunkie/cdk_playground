ARG REPO_NAME
ARG IMAGE_TAG

FROM --platform=linux/amd64 ${REPO_NAME}:${IMAGE_TAG}

USER root
WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY main.py .

USER helix

CMD ["python", "main.py"]
