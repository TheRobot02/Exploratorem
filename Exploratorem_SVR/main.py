import tkinter as tk
import socket
import threading

from Connect.main import ServerConnection
#from GUI.main import Application
    
if __name__ == "__main__":
    host = "127.0.0.1" #socket.gethostname()""
    port = 5000
    server = ServerConnection(host, port)
    #server_thread = threading.Thread(target=server.start)
    #server_thread.daemon = True
    
    
    server.start()
    