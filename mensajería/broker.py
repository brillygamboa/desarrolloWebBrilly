import threading
import time
import queue
import avro.schema
from avro.io import DatumReader, DatumWriter, BinaryEncoder, BinaryDecoder
import socket

class Broker:
    """
    Clase que representa un Broker para la gestión de colas de mensajes.
    """

    def __init__(self):
        """
        Constructor de la clase Broker.
        """
        self.queues = {}
        self.host = None
        self.port = None

    def create_queue(self, queue_name: str, max_size: int = 1000) -> None:
        """
        Crea una nueva cola con el nombre especificado.

        Args:
            queue_name (str): El nombre de la cola a crear.
            max_size (int, optional): Tamaño máximo de la cola. Por defecto es 1000.
        """
        if queue_name not in self.queues:
            self.queues[queue_name] = queue.Queue(max_size)
        else:
            raise ValueError("Queue with name {} already exists".format(queue_name))

    def delete_queue(self, queue_name: str) -> None:
        """
        Elimina la cola con el nombre especificado.

        Args:
            queue_name (str): El nombre de la cola a eliminar.
        """
        if queue_name in self.queues:
            del self.queues[queue_name]
        else:
            raise ValueError("Queue with name {} does not exist".format(queue_name))

    def flush_queue(self, queue_name: str, n: int = None) -> None:
        """
        Elimina los mensajes de la cola especificada.

        Args:
            queue_name (str): El nombre de la cola a vaciar.
            n (int, optional): El número máximo de mensajes a eliminar. Si es None,
                se eliminan todos los mensajes. Por defecto es None.
        """
        if queue_name in self.queues:
            if n is None:
                self.queues[queue_name].queue.clear()
            else:
                for _ in range(min(n, self.queues[queue_name].qsize())):
                    self.queues[queue_name].get()
        else:
            raise ValueError("Queue with name {} does not exist".format(queue_name))

    def enqueue(self, queue_name: str, msg) -> bool:
        """
        Encola un mensaje en la cola especificada.

        Args:
            queue_name (str): El nombre de la cola donde se encolará el mensaje.
            msg: El mensaje a encolar.

        Returns:
            bool: True si el mensaje se encoló con éxito, False si la cola está llena.
        """
        if queue_name in self.queues:
            try:
                self.queues[queue_name].put(msg, block=False)
                return True  # Se encoló el mensaje con éxito
            except queue.Full:
                print("Queue {} is full. Message discarded.".format(queue_name))
                return False  # La cola está llena, el mensaje no se pudo encolar
        else:
            raise ValueError("Queue with name {} does not exist".format(queue_name))

    def dequeue(self, host: str, port: int) -> None:
        """
        Método que escucha continuamente en la cola para enviar acknowledgments a los productores.

        Args:
            host (str): El host donde se enviará el acknowledgment.
            port (int): El puerto donde se enviará el acknowledgment.
        """
        self.host = host
        self.port = port
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
                                s.connect((self.host, self.port))
                                # Enviar acknowledgment al productor
                                s.sendall(b'1')  # Acknowledgment
                                print("Acknowledgment sent to producer")
                        except Exception as e:
                            print("Error sending acknowledgment to producer:", str(e))
            except Exception as e:
                print("Error in dequeue:", str(e))
            time.sleep(5)
