import json
import socket
import uuid
from broker import Broker

class Message:
    def __init__(self, timestamp: float, id: str, header: dict, body: dict):
        self.timestamp = timestamp
        self.id = id
        self.header = header
        self.body = body

class Producer:
    def __init__(self, broker: Broker, host: str, port: int):
        self.broker = broker
        self.host = host
        self.port = port

    def send_message(self, message: Message) -> int:
        try:
            serialized_message = json.dumps({
                'timestamp': message.timestamp,
                'id': message.id,
                'header': message.header,
                'body': message.body
            }).encode('utf-8')

            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((self.host, self.port))
                s.sendall(serialized_message)
                acknowledgment = s.recv(1024).decode('utf-8')
                return int(acknowledgment)
        except Exception as e:
            print("Error sending message:", e)
            return 0
