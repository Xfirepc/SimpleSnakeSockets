import socket
import threading
import sys
import pickle


class Client():
    def __init__(self, host="localhost", port=4000):

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((str(host), int(port)))

        # Hilo que recibe los mensajes
        msg_recv = threading.Thread(target=self.recvData)
        msg_recv.daemon = True
        msg_recv.start()
        
        self.state =  {
            'player_body': [],
            'player_direction': 273,
            'apples': [],
            'enemies': []
        }

    # Funcion pendiente de los mensajes que se reciben
    def recvData(self):
        while True:
            try:
                data = self.sock.recv(1024)
                if data:
                    self.state = pickle.loads(data)
            except:
                pass

    # Funcion que enviara los mensajes
    def sendStatus(self):
        self.sock.send(pickle.dumps(self.state))

    def close(self):
        self.sock.close()

