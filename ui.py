import socket
import threading
from colorama import Fore

# Connection Data
host = ''
port = 55555

# Server Name
servername = "hidden-fs"

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
            broadcast(message)
        except:
            # Removing And Closing Clients
            if client in clients:
                index = clients.index(client)
                clients.remove(client)
                client.close()
                nickname = nicknames[index]
                broadcast(f' {(Fore.LIGHTBLUE_EX + nickname + Fore.RESET)} A Quitté le salon speak ({(Fore.LIGHTBLUE_EX + servername + Fore.RESET)})'.encode('utf-8'))
                nicknames.remove(nickname)
                break

# Receiving / Listening Function
def receive():
    while True:
        # Accept Connection
        client, address = server.accept()
        print("Connected with {}".format(str(address)))

        # Request And Store Nickname
        client.send('NICK'.encode('utf-8'))
        nickname = client.recv(1024).decode('utf-8')

        if nickname == 'admin':
            client.send('PASS'.encode('utf-8'))
            password = client.recv(1024).decode('utf-8')

            if password != 'bruteforcepasfd@166':
                client.send("NAHBRO".encode('utf-8'))
                client.close()
                continue

        nicknames.append(nickname)
        clients.append(client)

        # Print And Broadcast Nickname
        print("Nickname is {}".format(nickname))
        broadcast(f" {(Fore.LIGHTBLUE_EX + nickname + Fore.RESET)} A Rejoint le server speak ({(Fore.LIGHTBLUE_EX + servername + Fore.RESET)})".encode('utf-8'),)
        client.send(f' Connecté au serveur {(Fore.LIGHTBLUE_EX + servername + Fore.RESET)}'.encode('utf-8'))

        # Start Handling Thread For Client
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

print("Serveur Speak Ouvert et attends des connections")
receive()
