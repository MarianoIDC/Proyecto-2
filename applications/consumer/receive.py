#Recuperado de: https://www.rabbitmq.com/tutorials/tutorial-two-python.html
#Recuperado de: https://stackoverflow.com/questions/46187647/socket-gaierror-gaierror-errno-2-name-or-service-not-known-pika-rabbitmq

#Se realizan los importes necesarios, incluida la librería Pika para comunicarse con RabbitMQ
import pika, sys, os, time

#Función que recibe un mensaje de la cola y escribe la respuesta
def callback(ch, method, properties, body):
    #Imprime el mensaje recibido
    print(" [x] Received %r" % body.decode())
    time.sleep(body.count(b'.'))
    print(" [x] Done")
    #Hace un reconocimiento del mensaje recibido de la cola
    ch.basic_ack(delivery_tag=method.delivery_tag)
    message = "Process the images!"
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

def main():
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
    print(' [*] Waiting for messages. To exit press CTRL+C')
    #Empieza a consumir de la cola de forma indefinida
    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue='task_queue', on_message_callback=callback)
    channel.start_consuming()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)