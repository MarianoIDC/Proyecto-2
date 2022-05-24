#Recuperado de: https://www.rabbitmq.com/tutorials/tutorial-two-python.html
#Recuperado de: https://stackoverflow.com/questions/46187647/socket-gaierror-gaierror-errno-2-name-or-service-not-known-pika-rabbitmq

#Se realizan los importes necesarios, incluida la librería Pika para comunicarse con RabbitMQ y el archivo de reconocimiento de imágenes
import os, sys, json, pika
import test as t

#Se definen las variables de entorno: Puerto, Usuario, Contraseña y Host
PORT = os.getenv('RABBIT_PORT')
USER = os.getenv('RABBIT_USER')
PASSWORD = os.getenv('RABBIT_PASSWORD')
HOST = os.getenv('RABBIT_HOST')

#Se define una lista con todos los filenames que va a procesar el reconocimiento de imágenes
filenames = ["sorpresa1.jpeg", "sorpresa2.jpg", "feliz1.jpg", "feliz2.jpg", "furia1.jpg", "furia2.png", "triste1.jpg", "triste2.jpeg", "pensando1.png", "pensando2.jpg"]

#Se reciben las credenciales del localhost de RabbitMQ
credentials = pika.PlainCredentials(USER, PASSWORD)
#Se reciben los parámetros del localhost de RabbitMQ
parameters = pika.ConnectionParameters(HOST, PORT, '/', credentials)
#Se establece la conexión con RabbitMQ
connection = pika.BlockingConnection(parameters)
channel = connection.channel()

#Función que detecta las caras de todos los archivos, recibe la lista y retorna una lista con los resultados
def detectAllFaces(filenames):
    results = []
    for i in range(len(filenames)):
        result = t.detect_faces(filenames[i])
        results.append(result)
    return results

#Función que recibe un mensaje de la cola y escribe la respuesta, si no recibe mensaje no puede escribir el resultado a la cola
def callback(ch, method, properties, body):
    #Imprime el mensaje recibido
    print(" [x] Received %r" % body.decode())
    #Hace un reconocimiento del mensaje recibido de la cola
    ch.basic_ack(delivery_tag=method.delivery_tag)
    #Publica un mensaje a la cola definiendo el ID de la misma y el cuerpo del mensaje
    ch.basic_publish(
        exchange='',
        routing_key='task_queue',
        body=message,
        #Define el mensaje enviado como persistente en la cola
        properties=pika.BasicProperties(
            delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE
    ))
    ch.close()

#Variable con los resultados del algoritmo
result = detectAllFaces(filenames)
#Convierte el resultado en un string que se puede enviar a la cola
message = str(json.dumps(result, indent=4, sort_keys=True))

#Se declara la cola
channel.queue_declare(queue='task_queue', durable=True)
#Empieza a consumir de la cola de forma indefinida
channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='task_queue', on_message_callback=callback)
channel.start_consuming()

connection.close()