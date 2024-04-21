import uuid
from broker import Broker
from producer import Producer, Message
from consumer import Consumer
import threading
import time

def main():
    # Crear el broker
    broker = Broker()

    # Crear el productor y el consumidor
    producer = Producer(broker)
    consumer = Consumer('localhost', 8090)

    # Crear una cola
    broker.create_queue('messages')

    # Contador de mensajes enviados
    sent_messages = 0

    def dequeue_messages(broker: Broker):
        while True:
            broker.dequeue('localhost', 8090)
            time.sleep(1)

    # Función para enviar mensajes
    def send_messages():
        nonlocal sent_messages
        while sent_messages < 10:  # Enviar solo 10 mensajes
            timestamp = time.time()
            message_id = str(uuid.uuid4())
            header = {'type': 'info'}
            body = {'text': 'Hello, world!'}
            message = Message(timestamp, message_id, header, body)
            producer.send_message(message)
            sent_messages += 1
            time.sleep(5)

    # Función para recibir mensajes
    def receive_messages():
        while True:
            print("Receiver")
            #message = consumer.receive_messages()
            consumer.receive_messages()
            if message:
                pass
                #print("Received message:", message)

    # Crear hilos para enviar y recibir mensajes
    send_thread = threading.Thread(target=send_messages)
    dequeue_thread = threading.Thread(target=dequeue_messages, args=(broker,))
    receive_thread = threading.Thread(target=receive_messages)

    # Iniciar los hilos
    send_thread.start()
    dequeue_thread.start()
    receive_thread.start()

    # Esperar a que los hilos terminen
    send_thread.join()
    dequeue_thread.join()
    receive_thread.join()

if __name__ == "__main__":
    main()
