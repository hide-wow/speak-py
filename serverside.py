import socket
import threading
from colorama import Fore
import base64
from time import sleep

# Connection Data
host = ''
port = 6677

# Server Name
servername = "Secure Speak"

# Server Stat
serverstat = "Server Dystopique par Hide"

# Starting Server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

# Lists For Clients and Their Nicknames
clients = []
nicknames = []

# Sending Messages To All Connected Clients
def broadcast(message):
    for client in clients:
        client.send(message)

# Handling Messages From Clients
def handle(client):
    while True:
        try:
            # Broadcasting Messages
            message = client.recv(1024)
            uncodemsg = message.decode('utf-8')
            broadcast(message)
        except:
            # Removing And Closing Clients
            if client in clients:
                index = clients.index(client)
                clients.remove(client)
                client.close()
                nickname = nicknames[index]
                quitbrodmsg = (f' {(Fore.LIGHTBLUE_EX + nickname + Fore.RESET)} A Quitté le salon speak ({(Fore.LIGHTBLUE_EX + servername + Fore.RESET)})'.encode('utf-8'))
                quitbrodmsgcrypt = base64.b85encode(quitbrodmsg)
                broadcast(quitbrodmsgcrypt)
                nicknames.remove(nickname)
                break

# Receiving / Listening Function
def receive():
    while True:
        # Accept Connection
        client, address = server.accept()
        print(" ")

        version = client.recv(1024).decode('utf-8')
        print(f"Version is : {version}")
        if version == 'DISCORDi':
            encodeserv = servername.encode('utf-8')
            cryptserv = base64.b85encode(encodeserv)
            client.send(cryptserv)
            encodestat = serverstat.encode('utf-8')
            cryptstat = base64.b85encode(encodestat)
            client.send(cryptstat)
            sleep(0.3)
            pass
        elif version == 'DEFINITIVE':
            pass
        else:
            print(Fore.LIGHTRED_EX + 'SUSPICIOUS VERSION' + Fore.RESET)

        # Request And Store Nickname
        client.send('NICK'.encode('utf-8'))
        nick = client.recv(1024).decode('utf-8')
        uncryptnick = base64.b85decode(nick)
        decodenick = uncryptnick.decode('utf-8')
        nickname = decodenick

        nicknames.append(nickname)
        clients.append(client)

        # Print And Broadcast Nickname
        print("Nickname is {}".format(nickname))
        joinbrodmsg = (f" {(Fore.LIGHTBLUE_EX + nickname + Fore.RESET)} A Rejoint le server speak ({(Fore.LIGHTBLUE_EX + servername + Fore.RESET)})".encode('utf-8'))
        joinbrodmsgecrypt = base64.b85encode(joinbrodmsg)
        broadcast(joinbrodmsgecrypt)
        clientmsg = (f' Connecté au serveur {(Fore.LIGHTBLUE_EX + servername + Fore.RESET)}'.encode('utf-8'))
        clientmsgcrypt = base64.b85encode(clientmsg)
        client.send(clientmsgcrypt)

        # Start Handling Thread For Client
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

print("Serveur Speak Ouvert et attends des connections")
receive()