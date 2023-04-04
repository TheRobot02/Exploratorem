import socket
import selectors
import types

import threading as thread



class ServerConnection:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.ipadress = None
        self.connection = None
        self.selector = selectors.DefaultSelector()
        
    def start(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((self.host, self.port))
        self.sock.listen(1)
        print(f"Server started on {self.host}:{self.port}")
        self.sock.setblocking(False)
        self.selector.register(self.sock, selectors.EVENT_READ, data=None)
        try:
            while True:
                events = self.selector.select(timeout=None)
                for key, mask in events:
                    if key.data is None:
                        self.accept_wrapper(key.fileobj)
                    else:
                        self.service_connection(key, mask)
        except:
            print("A exception has occurred")
            self.selector.close
            
        #self.listenForConnection()

    
    def accept_wrapper(self):
        conn, addr = self.sock.accept()  # Should be ready to read
        print(f"Accepted connection from {addr}")
        conn.setblocking(False)
        data = types.SimpleNamespace(addr=addr, inb=b"", outb=b"")
        events = selectors.EVENT_READ | selectors.EVENT_WRITE
        self.selector.register(conn, events, data=data)

    def service_connection(self, key, mask):
        self.sock = key.fileobj
        data = key.data
        if mask & selectors.EVENT_READ:
            recv_data = self.sock.recv(1024)  # Should be ready to read
            if recv_data:
                data.outb += recv_data
            else:
                print(f"Closing connection to {data.addr}")
                self.selector.unregister(self.sock)
                self.sock.close()
        if mask & selectors.EVENT_WRITE:
            if data.outb:
                print(f"Echoing {data.outb!r} to {data.addr}")
                sent = self.sock.send(data.outb)  # Should be ready to write
                data.outb = data.outb[sent:]

        if mask & selectors.EVENT_WRITE:
            if data.outb:
                print(f"Echoing {data.outb!r} to {data.addr}")
                sent = self.sock.send(data.outb)  # Should be ready to write
                data.outb = data.outb[sent:]



#    def listenForConnection(self):
#        while True:
#            conn, addr = self.sock.accept()
#            thread.Thread(target=self.handle_client(conn, addr))
#            if addr != None:
#                self.ipadress = addr
#            if conn != None:
#                self.connection = conn
#
#
#    def handle_client(self, conn, addr):
#        with conn:
#            print(f"Connected by {addr}")
#            while True:
#                data = conn.recv(1024)
#                if not data:
#                    print(f"{addr} disconnected")
#                    break
#
            
            #if conn.recv() != None:
            #    print(f"Connected by {addr}")
            #if conn.recv == None:
            #    print(f"{addr} disconnected")


    def getIp(self):
        return self.ipadress

class dataHandling:
    class outgoingData:
        def sendData(self, messege):

            #print(f"Received {data.decode('utf-8').strip()} from {addr}")
            self.connection.send(messege.encode('utf-8'))

    class incommingData:
        def getData(self):
            print("#")