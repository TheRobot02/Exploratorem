import socket
import time
#from Exploratorem_CL.Microphone.Microphone_record.main import microphoneRecord
#from Webcam.webcam_live.main import webcamLive

        

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

    try:
        serverHost = '127.0.0.1'    # the IP address or hostname of the server
        port = 5000                 # the port used by the server
        client = SocketClient(serverHost, port)
        client.connect()
    
    except:
        print("CONNECTION COULD NOT BE MADE")
        exit()

    print(f"Connection has been made")

    time.sleep(7)
    
    
    
    
    try:
        client.close()
        print("Connection closed")
    except:
        print("Connection could not be closed")


