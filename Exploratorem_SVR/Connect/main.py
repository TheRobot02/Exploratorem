import socket
import threading as thread

class ServerConnection:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = None
        self.ipadress = None

    def start(self):
        if self.sock is None:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sock.bind((self.host, self.port))
            self.sock.listen(1)
            print(f"Server started on {self.host}:{self.port}")
            self.listenForConnection()

        else:
            print(f"Server is already running")
    
    def listenForConnection(self):
        while True:
            conn, addr = self.sock.accept()
            thread.Thread(target=self.handle_client(conn, addr))
            if addr != None:
                self.ipadress = addr

    def handle_client(self, conn, addr):
        with conn:
            print(f"Connected by {addr}")
            while conn == True:
                data = conn.recv(1024)
                if not data:
                    break
                print(f"Received {data.decode('utf-8').strip()} from {addr}")
                conn.send(b"OK")
            print(f"{addr} disconnected")

    def ipReturn(self):
        return self.ipadress