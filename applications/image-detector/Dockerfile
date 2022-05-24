FROM python:3

WORKDIR /src

RUN python3 -m pip install --upgrade google-cloud-vision

#COPY images.jpeg /src/

#RUN mkdir results
WORKDIR /src/results

#Se necesita arreglar esta línea
COPY . /src/results

#COPY test.py /src/

CMD ["python3", "./test.py" ]