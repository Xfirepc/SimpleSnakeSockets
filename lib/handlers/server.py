import socket
import threading
import sys
import pickle
from pygame.locals import *
grid = 20

class Server():
    def __init__(self, host="localhost", port=4000):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((str(host), int(port)))
        self.sock.listen(10)
        self.sock.setblocking(False)

        self.clients = []
        self.stateClients = []
        aceptar = threading.Thread(target=self.aceptarCon)
        processar = threading.Thread(target=self.processarCon)

        aceptar.daemon = True
        aceptar.start()

        processar.daemon = True
        processar.start()

        while True:
            msg = input('')
            if msg == 'salir':
                self.sock.close()   
                sys.exit()
            else:
                pass

    def aceptarCon(self):
        print("AceptarCon iniciado")
        while True:
            try:
                conn, addr = self.sock.accept()
                conn.setblocking(False)
                self.clients.append(conn)
                self.stateClients.append({
                        'player_body': [],
                        'player_direction': 273,
                        'apples': [],
                        'enemies': []
                    })
                print("Se conecto un jugador: ", addr)
            except:
                pass

    def processarCon(self):
        print("ProcessarCon iniciado")
        while True:
            if len(self.clients) > 0:
                for client in self.clients:
                    try:
                        data = client.recv(1024)
                        if data:
                            print("[Jugador]:", pickle.loads(data))
                            self.stateClients[0] = pickle.loads(data)
                            msg = self.setNewState(self.stateClients[0])
                            self.responseToPlayer(msg, client)
                    except:
                        pass

    def setNewState(self, state):
        body = state['player_body']
        direction = state['player_direction']

        for i in range(len(body) - 1, 0, -1):
            body[i] = (body[i-1][0], body[i-1][1])

        if direction == 273:  
            body[0] = (body[0][0], body[0][1] - grid)
        if direction == 274:
            body[0] = (body[0][0], body[0][1] + grid)
        if direction == 275:
            body[0] = (body[0][0] + grid, body[0][1])
        if direction == 276:
            body[0] = (body[0][0] - grid, body[0][1])

        state['player_body'] = body
        state['player_direction'] = direction

        return state

    def responseToPlayer(self, data, client):
        client.send(pickle.dumps(data))

    def msg_to_all(self, msg, client):
        for c in self.clients:
            try:
                if c != client:
                    c.send(msg)
            except:
                self.clients.remove(c)


Server()