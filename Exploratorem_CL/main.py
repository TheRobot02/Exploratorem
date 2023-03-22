import socket
import time
from Microphone.Microphone_record.main import record


class SocketClient:
    def __init__(self, host, port):
        self.serverHost = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
    def connect(self):
        self.socket.connect((self.serverHost, self.port))
        
    def send(self, message):
        self.socket.sendall(message.encode('utf-8'))
        
    def receive(self):
        data = self.socket.recv(1024)
        return data.decode('utf-8')
        
    def close(self):
        self.socket.close()

if __name__ == "__main__":
    serverHost = '127.0.0.1'    # the IP address or hostname of the server
    port = 5000                 # the port used by the server
    client = SocketClient(serverHost, port)
    client.connect()
    time.sleep(5)
    client.close()
    
