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

# docker stop image-detector; 
# docker rm image-detector; 
# docker rmi image-detector:service; 
# docker build -t "image-detector:service" .; 
# docker run -d -v D:\Users\Mariano\Documents\GitHub\SOA2022\Proyecto-2\applications\image-detector\results:/image-detector/results/ 
# --name image-detector image-detector:service python3 tresting.py