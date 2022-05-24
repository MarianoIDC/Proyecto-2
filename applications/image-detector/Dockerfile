#Recuperado de: https://hub.docker.com/_/python

FROM python:3

WORKDIR /src

RUN python3 -m pip install --upgrade google-cloud-vision

RUN python3 -m pip install pika --upgrade

RUN mkdir image-detector
WORKDIR /image-detector

COPY . /image-detector/

CMD ["python3", "./sendImage.py" ]