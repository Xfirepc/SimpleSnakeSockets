import socket
import threading
import sys
import pickle
from lib.config import *
from pygame.locals import *

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
                self.clients.append({
                    'client': conn,
                    'data': {}
                })
                print("Se conecto un jugador: ", addr)
            except:
                pass

    def processarCon(self):
        print("ProcessarCon iniciado")
        while True:
            if len(self.clients) > 0:
                for c in self.clients:
                    try:
                        data = c['client'].recv(1024)
                        if data:
                            received = pickle.loads(data)
                            c['data'] = received
                            print("[" + received['name'] + "]:", received)
                            status = self.setNewState(received, c['client'])
                            self.responseToPlayers(c['client'])
                    except: 
                        pass

    def setNewState(self, state, client):
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
        state['enemies'] = self.appendEnemies(client)
        state['apples'] = self.getPositionApple();
        return state

    def responseToPlayers(self, client):
         for sclient in self.clients:
            try:
                sclient['client'].send(pickle.dumps(sclient['data']))
            except:
                self.clients.remove(sclient)

    def getPositionApple(self):
        some_one_ate = False
        new_position = getRandomPosition()
        for sclient in self.clients:
            if sclient['data']['player_eat']:
                sclient['data']['player_eat'] = False
                some_one_ate = True

        for sclient in self.clients:
            if some_one_ate:
                sclient['data']['apples'] = new_position
            else:
                if len(sclient['data']['apples']) > 0:
                    return sclient['data']['apples']

        if some_one_ate:
            return new_position
        return getRandomPosition()
        
    def appendEnemies(self, client):
        enemies = []
        for sclient in self.clients:
            if (sclient['client'] != client):
                enemies.append(sclient['data']['player_body'])
        
        return enemies

Server()