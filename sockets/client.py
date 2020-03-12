import sockets
import threading
import sys
import pickle


class Client():
    def __init__(self, host = 'localhost', port = 3000):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((str(host), int(port)))

        # Hilo que recibe los mensajes
        msg_recv = threading.Thread(target = self.msg_recv)
        msg_recv.daemon = True
        msg_recv.start()

        while True:
            msg = input('>>')
            if msg != 'salir':
                self.send_msg(msg)
            else
                self.sock.close()
                sys.exit()

        # Funcion pendiente de los mensajes que se reciben
        def msg_recv(self):
            while True:
                try:
                    data = self.sock.recv(1024)
                    if data:
                        print(pickle.loads(data))
                except:
                    pass

        # Funcion que enviara los mensajes
        def send_msg(self, msg):
            self.sock.send(pickle.dumps(msg))


client = Client()