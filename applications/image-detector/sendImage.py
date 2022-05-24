import os, sys, json, pika
import test as t

PORT = os.getenv('RABBIT_PORT')
USER = os.getenv('RABBIT_USER')
PASSWORD = os.getenv('RABBIT_PASSWORD')
HOST = os.getenv('RABBIT_HOST')

credentials = pika.PlainCredentials(USER, PASSWORD)
parameters = pika.ConnectionParameters(HOST, PORT, '/', credentials)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()

channel.queue_declare(queue='task_queue', durable=True)

filenames = ["sorpresa1.jpeg", "sorpresa2.jpg", "feliz1.jpg", "feliz2.jpg", "furia1.jpg", "furia2.png", "triste1.jpg", "triste2.jpeg", "pensando1.png", "pensando2.jpg"]

def detectAllFaces(filenames):
    results = []
    for i in range(len(filenames)):
        result = t.detect_faces(filenames[i])
        results.append(result)
    return results

result = detectAllFaces(filenames)
message = str(json.dumps(result, indent=4, sort_keys=True))

channel.basic_publish(
    exchange='',
    routing_key='task_queue',
    body=message,
    properties=pika.BasicProperties(
        delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE
    ))

print(message)
connection.close()