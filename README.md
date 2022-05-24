# RabbitMQ

# Run a standalone instance

```
docker network create rabbits
docker stop rabbit; docker rm rabbit; docker run -d --rm --net rabbits --hostname rabbit --name rabbit rabbitmq:3.8 

```

# Clean up

```
docker rm -f rabbit
```

# Management

```
docker stop rabbit; docker rm rabbit; docker run -d --rm --net rabbits -p 8080:15672 --hostname rabbit --name rabbit rabbitmq:3.8
docker exec -it rabbit bash
docker exec -it rabbit rabbitmq-plugins enable rabbitmq_management 

```

# Message Publisher

```

cd ..\publisher
docker stop emotion-publisher; docker rm emotion-publisher; docker rmi emotion-publisher:service; docker build -t "emotion-publisher:service" .; docker run -d --rm --net rabbits -e RABBIT_HOST=rabbit -e RABBIT_PORT=5672 -e RABBIT_USER=guest -e RABBIT_PASSWORD=guest --name emotion-publisher emotion-publisher:service tail -f /dev/null
docker exec -it emotion-publisher python3 ./send.py

```

# Message Consumer

```

cd ..\consumer
docker stop emotion-consumer; docker rm emotion-consumer; docker rmi emotion-consumer:service; docker build -t "emotion-consumer:service" .; docker run -d --rm --net rabbits -e RABBIT_HOST=rabbit -e RABBIT_PORT=5672 -e RABBIT_USER=guest -e RABBIT_PASSWORD=guest --name emotion-consumer emotion-consumer:service tail -f /dev/null
docker exec -it emotion-consumer python3 ./receive.py
```

# Create the image detector

```
docker stop image-detector; docker rm image-detector; docker rmi image-detector:service; docker build -t "image-detector:service" .; docker run -d --rm --net rabbits -e RABBIT_HOST=rabbit -e RABBIT_PORT=5672 -e RABBIT_USER=guest -e RABBIT_PASSWORD=guest --name image-detector image-detector:service tail -f /dev/null
docker exec -it image-detector python3 ./sendImage.py
```
