import socket
import threading
import sys
import pickle


class Server():
  def __init__(self, host="localhost", port=4000):
    self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    self.sock.bind((str(host), int(port)))
    self.sock.listen(10)
    self.sock.setblocking(False)

    self.clients = []

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
        print("Se conecto un usuario: ", addr)
      except:
        pass

  def processarCon(self):
    print("ProcessarCon iniciado")
    while True:
      if len(self.clients) > 0:
        for c in self.clients:
          try:
            data = c.recv(1024)
            if data:
              self.msg_to_all(data, c)
          except:
            pass

  def msg_to_all(self, msg, client):
    for c in self.clients:
            try:
              if c != client:
                c.send(msg)
            except:
                self.clients.remove(c)


s = Server()