import avro.schema
from avro.io import DatumReader, DatumWriter, BinaryEncoder, BinaryDecoder
from broker import Broker
import socket
import json

class Consumer:
    """
    Clase que representa un consumidor de mensajes.
    """

    def __init__(self, host: str, port: int):
        """
        Constructor de la clase Consumer.

        Args:
            host (str): El host donde escuchará el consumidor.
            port (int): El puerto donde escuchará el consumidor.
        """
        self.host = host
        self.port = port

    def receive_messages(self):
        """
        Método que escucha continuamente en el puerto especificado para recibir mensajes.
        """
        try:
            # Crear un socket TCP/IP
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                # Enlazar el socket al puerto
                s.bind((self.host, self.port))
                # Escuchar conexiones entrantes
                s.listen(1)
                print("Consumer listening on {}:{}".format(self.host, self.port))
                
                while True:
                    # Aceptar la conexión entrante
                    conn, addr = s.accept()
                    with conn:
                        print("Connected by", addr)
                        # Recibir datos del socket
                        data = conn.recv(1024)
                        if data:
                            # Procesar el mensaje recibido
                            decoded_message = json.loads(data.decode('utf-8'))
                            print("Received message:", decoded_message)
                        else:
                            print("No data received")
        except Exception as e:
            print("Error in consumer:", e)
