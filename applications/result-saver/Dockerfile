#Recuperado de: https://hub.docker.com/_/python
FROM python:3

WORKDIR /src

RUN python3 -m pip install pika --upgrade

RUN mkdir result-saver
WORKDIR /result-saver

COPY . /result-saver/

CMD ["python3", "./output.py" ]