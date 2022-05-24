FROM python:3

WORKDIR /src

RUN python3 -m pip install pika --upgrade

#COPY images.jpeg /src/

#RUN mkdir results
RUN mkdir result-saver
WORKDIR /result-saver

# RUN mkdir -p ./results/ \
#     && chmod 775 ./results -R

#Se necesita arreglar esta línea
COPY . /result-saver/

#COPY test.py /src/
#CMD ["python3", "./test.py" ]

CMD ["python3", "./output.py" ]
# docker stop result-saver; 
# docker rm result-saver; 
# docker rmi result-saver:service; 
# docker build -t "result-saver:service" .; 
# docker run -d -v /home/zuckerberg/Escritorio/Github/Proyecto-2/applications/result-saver/:/result-saver
# --name result-saver result-saver:service python3 output.py