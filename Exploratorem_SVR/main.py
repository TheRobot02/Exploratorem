import tkinter as tk
import socket
import threading

host = socket.gethostname()
port = 5000

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Connected Clients")
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.client_list = tk.Listbox(self)
        self.client_list.pack(fill="both", expand=True)

    def update_client_list(self, client_addr):
        self.client_list.insert(tk.END, client_addr)

class SocketServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = None
    
    def start(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((self.host, self.port))
        self.sock.listen(1)
        print(f"Server started on {self.host}:{self.port}")
    
    def handle_client(self, conn, addr):
        with conn:
            print(f"Connected by {addr}")
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                print(f"Received {data.decode('utf-8').strip()} from {addr}")
                conn.sendall(b"OK")
    
    def enable(self):
        if self.sock is None:
            self.start()
        #while True:
        #    conn, addr = self.sock.accept()
        #    self.handle_client(conn, addr)

if __name__ == "__main__":
    server = SocketServer(host, port)
    server.enable()

    mainWindow = tk.Tk()
    app = Application(master=mainWindow)

    client_handler = threading.Thread(target=SocketServer.handle_client, args=(server, app))
    client_handler.daemon = True
    client_handler.start()

    app.mainloop()