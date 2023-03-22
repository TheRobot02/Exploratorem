import tkinter as tk
import socket
import threading

class Application(tk.Frame):
    #A Tkinter GUI application that displays a list of connected clients.

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Connected Clients")
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        #Create the GUI widgets.
 
        self.client_list = tk.Listbox(self)
        self.client_list.pack(fill="both", expand=True)

    def update_client_list(self, client_addr):
        #Update the client list in the GUI with the given client address.

        self.client_list.insert(tk.END, client_addr)

class SocketServer:
    #A simple socket server that listens for incoming connections on a given host and port.

    def __init__(self, host, port):
        self.host = host
        self.port = port
        
    
    def start(self):
        #Start the socket server.

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((self.host, self.port))
        self.sock.listen(1)
        print(f"Server started on {self.host}:{self.port}")
    
        while True:
            conn, addr = self.sock.accept()
            print(f"Connected by {addr}")
            client_handler = threading.Thread(target=self.handle_client, args=(conn, addr))
            client_handler.daemon = True
            client_handler.start()

    def handle_client(self, conn, addr):
        #Handle incoming data from a client connection.

        with conn:
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                print(f"Received {data.decode('utf-8').strip()} from {addr}")
                conn.sendall(b"OK")
            print(f"Disconnected from {addr}")
    
if __name__ == "__main__":
    host = '127.0.0.1' #socket.gethostbyname(socket.gethostname())
    port = 5000
    server = SocketServer(host, port)
    server_thread = threading.Thread(target=server.start)
    server_thread.daemon = True
    server_thread.start()

    mainWindow = tk.Tk()
    app = Application(master=mainWindow)

    def update_list():
        #Update the client list in the GUI whenever a new client connects.

        while True:
            if server.sock is not None:
                conn, addr = server.sock.accept()
                app.update_client_list(addr)

    client_handler = threading.Thread(target=update_list)
    client_handler.daemon = True
    client_handler.start()

    app.mainloop()
