ARG REPO_NAME
ARG IMAGE_TAG

FROM ${REPO_NAME}:${IMAGE_TAG}

COPY load_testing/requirements.txt ./
USER root
RUN python -m venv /opt/venv
RUN source /opt/venv/bin/activate && pip install -r requirements.txt
ENV PATH="/opt/venv/bin:$PATH"

# turn off python output buffering
ENV PYTHONUNBUFFERED=1
RUN useradd --create-home locust
# ensure correct permissions
RUN chown -R locust /opt/venv
USER locust
WORKDIR /home/locust

RUN mkdir -p app/src/load_testing/app && \
    touch __init__.py && \
    touch app/__init__.py && \
    touch app/src/__init__.py && \
    touch app/src/load_testing/__init__.py

COPY load_testing/app app/src/load_testing/app

COPY data_structures app/src/data_structures/

EXPOSE 5557

ENTRYPOINT ["/opt/venv/bin/locust"]