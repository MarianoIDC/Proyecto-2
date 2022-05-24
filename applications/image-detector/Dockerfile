FROM python:3

WORKDIR /src

RUN python3 -m pip install --upgrade google-cloud-vision

#COPY images.jpeg /src/

#RUN mkdir results
RUN mkdir image-detector
WORKDIR /image-detector

# RUN mkdir -p ./results/ \
#     && chmod 775 ./results -R

#Se necesita arreglar esta línea
COPY . /image-detector/

#COPY test.py /src/
CMD ["/bin/bash"]
#CMD ["python3", "./test.py" ]