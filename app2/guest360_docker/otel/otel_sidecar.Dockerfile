ARG REPO_NAME
ARG IMAGE_TAG

FROM ${REPO_NAME}:${IMAGE_TAG}

ENV AWS_REGION=us-east-1

COPY collector-config.yaml /etc/otel-agent-config.yaml

EXPOSE 1777 55679 4317 13133

CMD ["--config=/etc/otel-agent-config.yaml"]