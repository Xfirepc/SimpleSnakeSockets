# Server chat con socket en python
import socket
import select
import sys
from thread import *

""" EL primer argumento AF_INET es el dominio de la dirección del socket. ESto se usa cuando tenemos un dominio de internet con dos hosts. El segundo argumento es el tipo socket. SOCK_STREAM siginifica que los datos caracteres se leen en un flujo continuo"""
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Vamos a verificar si tenemos los argumentos necesarios
if len(sys.argv)!=3:
	print("Error: Debe introducir server.py ip puerto")
	exit()

# El primer argumento que recibimos será la ip
IP_address = str(sys.argv[1])

# El segundo para el puerto
Port = int(sys.argv[2])

"""Vinculamos el server a una ip y a un puerto que deben ser los mismos que el del cliente """
server.bind((IP_address, Port))

"""Escuchamos 100 conexiones activas pero podemos aumentarlo """
server.listen(100)

#Aquí guardaremos los clientes que se conecten
list_of_clients = []

# Y aquí sus nicks, pongo admin para que no pueda usarse
nicks = {"admin":"admin"}

def clientthread(conn, addr):
	# Le enviamos un mensaje al nuevo cliente conectado
	conn.send("Bienvenido al chat {0}!!!".format(nicks[conn]))

	while True:
		try:
			message = conn.recv(2048)
			if message:
			# Imprime direccion y mensaje del usuario
				print("<" + addr[0] + " " + nicks[conn] + " > " + message)
		
			# Llamamos a la funcion broadcast que pondré ahora para enviar mensaje a todos
				message_to_send = "<" + nicks[conn] +"> " + message
				broadcast(message_to_send, conn)
			else:
				"""El mensaje puede no tener contenido si la conexion
				está rota, en este caso eliminamos la conexión """
				# La función remove la escribiré ahora
				remove(conn) 

			
		except:
			continue

"""Usando la función de aquí abajo, transmitimos el mensaje a todos los clientes  """ 
def broadcast(message, connection):
	for clients in list_of_clients:
		if clients != connection:
			try:
				clients.send(message)
			except:
				clients.close()
			# Si el enlace esta roto eliminamos el cliente
			remove(clients)

"""La siguiente función simplemente elimina el objeto de la lista que se creara al comienzo, ahora 
escribiré esa parte """
def remove(connection):
	if connection in list_of_clients:
		list_of_clients.remove(connection)

while True:
	"""Acepta una solicitud de conexión y almacena dos parámetros, conn que un objeto socket
	y addr que contiene la dirección IP del cliente """
	conn, addr = server.accept()
	# El primer mensaje que recibamos será el nick, lo veremos en el cliente cuando termine el server
	nick = conn.recv(2048)

	"""Metemos al cliente en la lista de clientes """
	list_of_clients.append(conn)


	"""Comprobamos que el nick no esta en nuestro diccionario de nicks para que no se repita """
	t = True
	for i in nicks:
		if nicks[i] == nick:
			t = True
		else:
			t = False
	# Si esta disponible lo añadimos
	if t == False:
		nicks[conn] = nick
		# Enviamos una confirmación al cliente
		conn.send("1")
	else:
	# Si no esta disponible le enviamos una denegación al server y creamos un bucle hasta que este disponible
		while t:
			conn.send("0")
			nick = conn.recv(2048)
			if nicks[i] == nick:
				t = True
			else:	
				t = False
				nicks[conn] = nick
				conn.send("1")
	# Ahora imrimos la direccion y el nick del usuario que se acaba de conectar
	print(addr[0] + " " + nick + " conectado")
		
	# Creamos un proceso individual para el cliente que se conecta
	start_new_thread(clientthread, (conn,addr))
conn.close()
server.close()