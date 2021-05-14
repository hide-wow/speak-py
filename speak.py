from ui import Menu
import requests, re, json
import os, sys, time, terminaltables
from terminaltables import SingleTable
from colorama import Fore, init
from time import sleep
import random
import getpass
from rpc import speakrpc, stats, speakchatrpc
import base64

speakrpc()

stop_thread = False

warn = ("  [" + Fore.LIGHTRED_EX + "!" + Fore.RESET + "] ")

user = getpass.getuser()

def times():
	times = time.strftime("%H:%M:%S")
	times = str(times)
	return(times)

def clear():
	if os.name == 'nt':
		return os.system('cls')
	else:
		return os.system('clear')

clear()

if os.name == 'nt':
    init(convert=True)
else:
    init(convert=False)

print(Menu.design_ui)

def Messages():
    TABLE_DATA = []
    private_messages = (Fore.LIGHTYELLOW_EX + "Speak Main" + Fore.RESET, "Nom D'utilisateur : " + user)
    TABLE_DATA.append(private_messages)
    private_messages = ("News :", Fore.LIGHTBLACK_EX + "Grosse Update :" + Fore.RESET)
    TABLE_DATA.append(private_messages) 
    private_messages = (" ", Fore.LIGHTBLACK_EX + "Encrypté de bout en bout" + Fore.RESET)
    TABLE_DATA.append(private_messages)
    private_messages = (" ", Fore.LIGHTBLACK_EX + "Problème Api des noms randoms :/" + Fore.RESET)
    TABLE_DATA.append(private_messages)
    private_messages = ("----------------", "-----------------------" + Fore.RESET)
    TABLE_DATA.append(private_messages)
    private_messages = ("Conversations :", Fore.LIGHTBLACK_EX + "Serveur" + Fore.LIGHTBLACK_EX + " (" + Fore.LIGHTRED_EX + "1" + Fore.LIGHTBLACK_EX + ")" + Fore.RESET)
    TABLE_DATA.append(private_messages)
    table = SingleTable(TABLE_DATA)
    print("\n"+table.table)
Messages()

def Choix():
    print(f"""

    [{Fore.LIGHTBLUE_EX + str("1") + Fore.RESET}] Connection a un serveur speak

    """
    )
    choice = input(" Salon choisi : ")

    #Général
    if choice == '1':
        clear()
        print(Menu.design_ui)
        import socket
        import threading

        # Choosing Nickname
        print(f"""
        Nom d'utilisateur :

        [{Fore.LIGHTBLUE_EX + str("1") + Fore.RESET}] : Au hazard
        [{Fore.LIGHTBLUE_EX + str("2") + Fore.RESET}] : Nom au choix
        [{Fore.LIGHTBLUE_EX + str("3") + Fore.RESET}] : Nom de l'user du pc

        """)
        nick_choice = input(" Votre choix : ")

        if nick_choice == '1':
            url = "http://names.drycodes.com/10?nameOptions=all"
            data = requests.get(url).content.decode('utf-8')
            values = json.loads(data)
            randomchoice = random.choice(values)
            nickname = str(randomchoice)
            print(" ")
            print(" Votre nom d'utilisateur : %s" % (nickname))
            sleep(3.0)
            clear()
            print(Menu.design_ui)
            # Connecting To Server
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            print(" ")
            ip = input(" Ip du serveur speak : ")
            print(" ")
            port = input(" Port du serveur speak : ")
            clear()
            print(Menu.design_ui)
            print(" ")
            server_connection = client.connect((str(ip),int(port)))
            serv = client.recv(1024).decode('utf-8')
            decryptserv = base64.b85decode(serv)
            decodeserv = decryptserv.decode('utf-8')
            speakchatrpc(servername=decodeserv,username=nickname)
            # Listening to Server and Sending Nickname
            def receive():
                while True:
                    global stop_thread
                    if stop_thread:
                        break
                    try:
                        # Receive Message From Server
                        # If 'NICK' Send Nickname
                        message = client.recv(1024).decode('utf-8')
                        if message == 'NICK':
                            encodenick = nickname.encode('utf-8')
                            cryptnick = base64.b85encode(encodenick)
                            client.send(cryptnick)
                            next_message = client.recv(1024).decode('utf-8')
                            if next_message == 'BAN':
                                print(Fore.LIGHTRED_EX + " Vous avez été Banni de speak par un Administrateur")
                                client.close()
                                stop_thread = True
                        else:
                            print(" ")
                            messagedecrypt = base64.b85decode(message)
                            messagedecode = messagedecrypt.decode('utf-8')
                            print(messagedecode)
                            print(" ")
                    except:
                        # Close Connection When Error
                        print(warn + "Une erreure s'est produite!")
                        client.close()
                        break

            # Sending Messages To Server
            def write():
                while True:
                    if stop_thread:
                        break
                    message = ' - {}: {}'.format(Fore.LIGHTBLUE_EX + nickname + Fore.RESET, getpass.getpass(Fore.LIGHTBLACK_EX +" Vous ↓ :"+ Fore.RESET))
                    encoded_message = message.encode('utf-8')
                    msgcrypt = base64.b85encode(encoded_message)
                    client.send(msgcrypt)

            # Starting Threads For Listening And Writing
            receive_thread = threading.Thread(target=receive)
            receive_thread.start()

            write_thread = threading.Thread(target=write)
            write_thread.start()

        elif nick_choice == '2':
            print(" ")
            name = input(" Nouveau nom d'utilisateur : ")
            nickname = str(name)
            if nickname == '':
                print(" ")
                print("  " + warn + "Erreur x-x")
                sleep(3.0)
                clear()
                print(Menu.design_ui)
                Messages()
                Choix()
                pass
            else:
                sleep(3.0)
                clear()
                print(Menu.design_ui)
                # Connecting To Server
                client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                print(" ")
                ip = input(" Ip du serveur speak : ")
                print(" ")
                port = input(" Port du serveur speak : ")
                clear()
                print(Menu.design_ui)
                print(" ")
                server_connection = client.connect((str(ip),int(port)))
                serv = client.recv(1024).decode('utf-8')
                decryptserv = base64.b85decode(serv)
                decodeserv = decryptserv.decode('utf-8')
                speakchatrpc(servername=decodeserv,username=nickname)
                # Listening to Server and Sending Nickname
                def receive():
                    while True:
                        global stop_thread
                        if stop_thread:
                            break
                        try:
                            # Receive Message From Server
                            # If 'NICK' Send Nickname
                            message = client.recv(1024).decode('utf-8')
                            if message == 'NICK':
                                encodenick = nickname.encode('utf-8')
                                cryptnick = base64.b85encode(encodenick)
                                client.send(cryptnick)
                                next_message = client.recv(1024).decode('utf-8')
                                if next_message == 'BAN':
                                    print(Fore.LIGHTRED_EX + " Vous avez été Banni de speak par un Administrateur")
                                    client.close()
                                    stop_thread = True
                            else:
                                print(" ")
                                messagedecrypt = base64.b85decode(message)
                                messagedecode = messagedecrypt.decode('utf-8')
                                print(messagedecode)
                                print(" ")
                        except:
                            # Close Connection When Error
                            print(warn + "Une erreure s'est produite!")
                            client.close()
                            break

                # Sending Messages To Server
                def write():
                    while True:
                        if stop_thread:
                            break
                        message = ' - {}: {}'.format(Fore.LIGHTBLUE_EX + nickname + Fore.RESET, getpass.getpass(Fore.LIGHTBLACK_EX +" Vous ↓ :"+ Fore.RESET))
                        encoded_message = message.encode('utf-8')
                        msgcrypt = base64.b85encode(encoded_message)
                        client.send(msgcrypt)

                # Starting Threads For Listening And Writing
                receive_thread = threading.Thread(target=receive)
                receive_thread.start()

                write_thread = threading.Thread(target=write)
                write_thread.start()

        elif nick_choice == '3':
            nickname = str(user)
            print(" ")
            print(" Votre nom d'utilisateur : %s" % (nickname))
            sleep(3.0)
            clear()
            print(Menu.design_ui)
            # Connecting To Server
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            print(" ")
            ip = input(" Ip du serveur speak : ")
            print(" ")
            port = input(" Port du serveur speak : ")
            clear()
            print(Menu.design_ui)
            print(" ")
            server_connection = client.connect((str(ip),int(port)))
            serv = client.recv(1024).decode('utf-8')
            decryptserv = base64.b85decode(serv)
            decodeserv = decryptserv.decode('utf-8')
            speakchatrpc(servername=decodeserv,username=nickname)
            # Listening to Server and Sending Nickname
            def receive():
                while True:
                    global stop_thread
                    if stop_thread:
                        break
                    try:
                        # Receive Message From Server
                        # If 'NICK' Send Nickname
                        message = client.recv(1024).decode('utf-8')
                        if message == 'NICK':
                            encodenick = nickname.encode('utf-8')
                            cryptnick = base64.b85encode(encodenick)
                            client.send(cryptnick)
                            next_message = client.recv(1024).decode('utf-8')
                            if next_message == 'BAN':
                                print(Fore.LIGHTRED_EX + " Vous avez été Banni de speak par un Administrateur")
                                client.close()
                                stop_thread = True
                        else:
                            print(" ")
                            messagedecrypt = base64.b85decode(message)
                            messagedecode = messagedecrypt.decode('utf-8')
                            print(messagedecode)
                            print(" ")
                    except:
                        # Close Connection When Error
                        print(warn + "Une erreure s'est produite!")
                        client.close()
                        break

            # Sending Messages To Server
            def write():
                while True:
                    if stop_thread:
                        break
                    message = ' - {}: {}'.format(Fore.LIGHTBLUE_EX + nickname + Fore.RESET, getpass.getpass(Fore.LIGHTBLACK_EX +" Vous ↓ :"+ Fore.RESET))
                    encoded_message = message.encode('utf-8')
                    msgcrypt = base64.b85encode(encoded_message)
                    client.send(msgcrypt)

            # Starting Threads For Listening And Writing
            receive_thread = threading.Thread(target=receive)
            receive_thread.start()

            write_thread = threading.Thread(target=write)
            write_thread.start()
        else:
            print(" ")
            print("  " + warn + "Erreur x-x")
            sleep(3.0)
            clear()
            print(Menu.design_ui)
            Messages()
            Choix()
            pass

    else:
        print(" ")
        print("  " + warn + "Erreur x-x")
        sleep(3.0)
        clear()
        print(Menu.design_ui)
        Messages()
        Choix()
        pass

Choix()
