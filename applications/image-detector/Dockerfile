FROM python:3

WORKDIR /src

RUN python3 -m pip install --upgrade google-cloud-vision

COPY images.jpeg /src/

#Se necesita arreglar esta línea
COPY ../proyecto1-luis-8153e212374a.json /src/

COPY test.py /src/

CMD ["python3", "./test.py" ]