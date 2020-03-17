import socket
import threading
import sys
import pickle


class Client():
    def __init__(self, host = "localhost", port = 4000):

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((str(host), int(port)))

        # Hilo que recibe los mensajes
        msg_recv = threading.Thread(target = self.recvData)
        msg_recv.daemon = True
        msg_recv.start()
        
        self.direction = 276

    # Funcion pendiente de los mensajes que se reciben
    def recvData(self):
        while True:
            try:
                data = self.sock.recv(8000)
                if data:
                    self.direction = pickle.loads(data)
            except:
                pass

    # Funcion que enviara los mensajes
    def sendData(self, data):
        self.sock.send(pickle.dumps(data))

    def getDirection(self):
        return self.direction

    def close(self):
        self.sock.close()

