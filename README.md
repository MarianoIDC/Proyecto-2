# RabbitMQ

# run a standalone instance
docker network create rabbits
docker run -d --rm --net rabbits --hostname rabbit-1 --name rabbit-1 rabbitmq:3.8 

# clean up
docker rm -f rabbit-1
```

# Management

```
docker run -d --rm --net rabbits -p 8080:15672 --hostname rabbit-1 --name rabbit-1 rabbitmq:3.8
docker exec -it rabbit-1 bash
docker exec -it rabbit-1 rabbitmq-plugins enable rabbitmq_management

```

# Message Publisher

```

cd ..\publisher
docker build . -t emotion-publisher:v1.0.0

docker run -it --rm --net rabbits -e RABBIT_HOST=rabbit-1 -e RABBIT_PORT=5672 -e RABBIT_USER=guest -e RABBIT_PASSWORD=guest -p 80:80 emotion-publisher:v1.0.0
```

# Message Consumer

```

cd ..\consumer
docker build . -t emotion-publisher:v1.0.0

docker run -it --rm --net rabbits -e RABBIT_HOST=rabbit-1 -e RABBIT_PORT=5672 -e RABBIT_USER=guest -e RABBIT_PASSWORD=guest -p 80:80 emotion-consumer:v1.0.0
```


