import threading
import time
import queue
import avro.schema
from avro.io import DatumReader, DatumWriter, BinaryEncoder, BinaryDecoder
import socket

class Broker:
    def __init__(self):
        self.queues = {}

    def create_queue(self, queue_name: str, max_size: int = 1000) -> None:
        if queue_name not in self.queues:
            self.queues[queue_name] = queue.Queue(max_size)
        else:
            raise ValueError("Queue with name {} already exists".format(queue_name))

    def delete_queue(self, queue_name: str) -> None:
        if queue_name in self.queues:
            del self.queues[queue_name]
        else:
            raise ValueError("Queue with name {} does not exist".format(queue_name))

    def flush_queue(self, queue_name: str, n: int = None) -> None:
        if queue_name in self.queues:
            if n is None:
                self.queues[queue_name].queue.clear()
            else:
                for _ in range(min(n, self.queues[queue_name].qsize())):
                    self.queues[queue_name].get()
        else:
            raise ValueError("Queue with name {} does not exist".format(queue_name))

    def enqueue(self, queue_name: str, msg) -> None:
        if queue_name in self.queues:
            try:
                self.queues[queue_name].put(msg, block=False)
                print("all right")
                return True
            except queue.Full:
                print("Queue {} is full. Message discarded.".format(queue_name))
                return False
        else:
            raise ValueError("Queue with name {} does not exist".format(queue_name))

    def dequeue(self, host: str, port: int) -> None:
        while True:
            try:
                # Iterar sobre las colas
                for queue_name, q in self.queues.items():
                    # Verificar si la cola no está vacía
                    if not q.empty():
                        # Sacar un mensaje de la cola
                        message = q.get()
                        try:
                            # Establecer conexión con el productor
                            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                                print("Waiting for producer to connect...")
                                s.bind((host, port))
                                s.listen(1)
                                conn, addr = s.accept()
                                with conn:
                                    print("Producer connected from:", addr)
                                    # Enviar acknowledgment al productor
                                    conn.sendall(b'1')  # Acknowledgment
                                print("Acknowledgment sent to producer")
                        except Exception as e:
                            print("Error sending acknowledgment to producer:", str(e))
            except Exception as e:
                print("Error in dequeue:", str(e))
            time.sleep(5)
