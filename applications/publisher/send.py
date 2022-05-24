#Recuperado de: https://www.rabbitmq.com/tutorials/tutorial-two-python.html
#Recuperado de: https://stackoverflow.com/questions/46187647/socket-gaierror-gaierror-errno-2-name-or-service-not-known-pika-rabbitmq


#Se realizan los importes necesarios, incluida la librería Pika para comunicarse con RabbitMQ
import os, pika, sys

#Se definen las variables de entorno: Puerto, Usuario, Contraseña y Host
PORT = os.getenv('RABBIT_PORT')
USER = os.getenv('RABBIT_USER')
PASSWORD = os.getenv('RABBIT_PASSWORD')
HOST = os.getenv('RABBIT_HOST')

#Se reciben las credenciales del localhost de RabbitMQ
credentials = pika.PlainCredentials(USER, PASSWORD)
#Se reciben los parámetros del localhost de RabbitMQ
parameters = pika.ConnectionParameters(HOST, PORT, '/', credentials)
#Se establece la conexión con RabbitMQ
connection = pika.BlockingConnection(parameters)
channel = connection.channel()

#Se declara la cola
channel.queue_declare(queue='task_queue', durable=True)

#Se le entrega un mensaje de inicio del programa a la cola
message = ' '.join(sys.argv[1:]) or "Start the program!"

#Publica un mensaje a la cola definiendo el ID de la misma y el cuerpo del mensaje
channel.basic_publish(
    exchange='',
    routing_key='task_queue',
    body=message,
    properties=pika.BasicProperties(
        delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE
    ))

print(" [x] Sent %r" % message)
#Cierra la conexión
connection.close()