FROM python:3

WORKDIR /src

RUN python3 -m pip install --upgrade google-cloud-vision

#Se necesita arreglar esta línea
#COPY home/zuckerberg/proyecto1-luis-8153e212374a.json /src/

COPY . /src/

CMD ["python3", "./test.py" ]