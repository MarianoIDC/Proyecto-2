FROM python:3

WORKDIR /src

RUN python3 -m pip install pika --upgrade

COPY . /src/

CMD ["python3", "./receive.py" ]