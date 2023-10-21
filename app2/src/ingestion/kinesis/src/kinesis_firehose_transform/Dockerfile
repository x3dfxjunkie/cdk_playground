FROM public.ecr.aws/lambda/python:3.9

COPY decode_base64.py /asset/
COPY requirements.txt /tmp/
RUN pip3 install -r /tmp/requirements.txt -t /asset
