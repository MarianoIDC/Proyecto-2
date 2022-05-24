FROM python:3

WORKDIR /src

RUN python3 -m pip install --upgrade google-cloud-vision

RUN python3 -m pip install pika --upgrade

#COPY images.jpeg /src/

#Se necesita arreglar esta línea
COPY . /src/

#COPY test.py /src/

CMD ["python3", "./sendImage.py" ]