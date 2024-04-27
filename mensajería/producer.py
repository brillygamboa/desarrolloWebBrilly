import json
import socket
import uuid
from broker import Broker

class Message:
    def __init__(self, timestamp: float, id: str, header: dict, body: dict):
        """
        Inicializa un objeto de mensaje.

        Args:
            timestamp (float): La marca de tiempo del mensaje.
            id (str): El identificador único del mensaje.
            header (dict): El encabezado del mensaje.
            body (dict): El cuerpo del mensaje.
        """
        self.timestamp = timestamp
        self.id = id
        self.header = header
        self.body = body

class Producer:
    def __init__(self, broker: Broker, host: str, port: int):
        """
        Inicializa un productor con el broker y la información de conexión.

        Args:
            broker (Broker): El broker al que se conectará el productor.
            host (str): El host del broker.
            port (int): El puerto del broker.
        """
        self.broker = broker
        self.host = host
        self.port = port

    def send_message(self, message: Message) -> bool:
        """
        Envía un mensaje al broker.

        Args:
            message (Message): El mensaje a enviar.

        Returns:
            bool: True si el mensaje se envió y encoló con éxito, False en caso contrario.
        """
        try:
            serialized_message = json.dumps({
                'timestamp': message.timestamp,
                'id': message.id,
                'header': message.header,
                'body': message.body
            }).encode('utf-8')

            # Establecer conexión con el broker
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((self.host, self.port))

                # Enviar el mensaje al broker
                s.sendall(serialized_message)

                # Intentar encolar el mensaje en el broker
                return self.broker.enqueue('messages', serialized_message)
        except Exception as e:
            print("Error sending message:", e)
            return False
