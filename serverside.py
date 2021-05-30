import socket
import threading
from colorama import Fore
import base64
from time import sleep
import random

# Connection Data
host = ''
port = 6677

Msg1 = " Un {} Sauvage a join !"
Msg2 = " Hey {} !, Passez lui le bonjour !"
Msg3 = " Sanoude mon petit Hypocampe {} (cai gaynen)"
Msg4 = " {} est arrive, apportez lui une part de pizza !"
Msg5 = " Puceau n'1 ({}) a join le GANG GANG"
Msg6 = " Salut {} !, On est a court de Pizza, t'en as ?"

Quit1 = " Au revoir {}, Tu va nous manquer ;("
Quit2 = " Ah non hun, {} A leave, ptn les boules eh"
Quit3 = " Ciao mi amigo {}"
Quit4 = " {} a quitter, t'facon, tu puais"
Quit5 = " Bon, {} nous laisse en plan :/"

# Server Name
servername = "Speak.py Official"

# Server Stat
serverstat = "Serveur Officiel de Speak.py"

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

                Quitz1 = Quit1.format(Fore.LIGHTYELLOW_EX + nickname + Fore.RESET)
                Quitz2 = Quit2.format(Fore.LIGHTYELLOW_EX + nickname + Fore.RESET)
                Quitz3 = Quit3.format(Fore.LIGHTYELLOW_EX + nickname + Fore.RESET)
                Quitz4 = Quit4.format(Fore.LIGHTYELLOW_EX + nickname + Fore.RESET)
                Quitz5 = Quit5.format(Fore.LIGHTYELLOW_EX + nickname + Fore.RESET)

                QuitMsgs = [Quitz1, Quitz2, Quitz3, Quitz4, Quitz5]

                QuitMsg = (Fore.LIGHTRED_EX + str(" (System) " + Fore.RESET + "-") + (random.choice(QuitMsgs))).encode('utf-8')
                quitbrodmsgcrypt = base64.b85encode(QuitMsg)
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
        if version == 'HOST_CHECK':
            print(Fore.LIGHTGREEN_EX + "Checking The Server" + Fore.RESET)
            pass
        else:
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

            Join1 = Msg1.format(Fore.LIGHTYELLOW_EX + nickname + Fore.RESET)
            Join2 = Msg2.format(Fore.LIGHTYELLOW_EX + nickname + Fore.RESET)
            Join3 = Msg3.format(Fore.LIGHTYELLOW_EX + nickname + Fore.RESET)
            Join4 = Msg4.format(Fore.LIGHTYELLOW_EX + nickname + Fore.RESET)
            Join5 = Msg5.format(Fore.LIGHTYELLOW_EX + nickname + Fore.RESET)
            Join6 = Msg6.format(Fore.LIGHTYELLOW_EX + nickname + Fore.RESET)

            JoinMsgs = [Join1, Join2, Join3, Join4, Join5, Join6]

            # Print And Broadcast Nickname
            print("Nickname is {}".format(nickname))
            def JOINMSGLIKEAPRO():
                JoinMsg = ((Fore.LIGHTRED_EX + str(" (System) " + Fore.RESET + "-") + Fore.RESET) + (random.choice(JoinMsgs))).encode('utf-8')
                joinbrodmsgecrypt = base64.b85encode(JoinMsg)
                broadcast(joinbrodmsgecrypt)
            JOINMSGLIKEAPRO()
            clientmsg = (f'{Fore.LIGHTRED_EX + str(" (System) " + Fore.RESET + "- ") + Fore.RESET}Connecté au serveur {(Fore.LIGHTBLUE_EX + servername + Fore.RESET)}'.encode('utf-8'))
            clientmsgcrypt = base64.b85encode(clientmsg)
            client.send(clientmsgcrypt)

            # Start Handling Thread For Client
            thread = threading.Thread(target=handle, args=(client,))
            thread.start()

print("Serveur Speak Ouvert et attends des connections")
receive()
