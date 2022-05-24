#Recuperado de: https://hub.docker.com/_/python
FROM python:3

WORKDIR /src

RUN python3 -m pip install pika --upgrade

COPY send.py /src/

CMD ["python3", "./send.py" ]
