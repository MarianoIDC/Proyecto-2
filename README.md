# RabbitMQ

# Run a standalone instance

```
docker network create rabbits
docker run -d --rm --net rabbits --hostname rabbit --name rabbit rabbitmq:3.8 
```

# Clean up

```
docker rm -f rabbit
```

# Management

```
docker run -d --rm --net rabbits -p 8080:15672 --hostname rabbit --name rabbit rabbitmq:3.8
docker exec -it rabbit bash
docker exec -it rabbit rabbitmq-plugins enable rabbitmq_management

```

# Message Publisher

```

cd ..\publisher
docker build . -t emotion-publisher:v1.0.0

docker run -it --rm --net rabbits -e RABBIT_HOST=rabbit -e RABBIT_PORT=5672 -e RABBIT_USER=guest -e RABBIT_PASSWORD=guest emotion-publisher:v1.0.0
```

# Message Consumer

```

cd ..\consumer
docker build . -t emotion-consumer:v1.0.0

docker run -it --rm --net rabbits -e RABBIT_HOST=rabbit -e RABBIT_PORT=5672 -e RABBIT_USER=guest -e RABBIT_PASSWORD=guest -p 80:80 emotion-consumer:v1.0.0
```

# Clustering

```
minikube start
kubectl create ns rabbits
kubectl get storageclass
```
