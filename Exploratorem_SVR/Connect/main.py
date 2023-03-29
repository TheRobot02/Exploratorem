import socket

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
    
    def handle_client(self, conn, addr):
        with conn:
            print(f"Connected by {addr}")
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                print(f"Received {data.decode('utf-8').strip()} from {addr}")
                conn.sendall(b"OK")
    
    def listenForConnection(self):
        while True:
            conn, addr = self.sock.accept()
            self.handle_client(conn, addr)
            if addr != None:
                self.ipadress = addr

    def ipReturn(self):
        return self.ipadress