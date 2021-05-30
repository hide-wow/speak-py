from ui import Menu
import requests, re, json
import os, sys, time
from terminaltables import SingleTable
from colorama import Fore, init
from time import sleep
import random
import getpass
from rpc import speakrpc, stats, speakchatrpc
import base64
import socket
import threading

class state():
    need_ip_port = True

version = "DISCORDi"

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
    private_messages = (Fore.LIGHTYELLOW_EX + "News :" + Fore.RESET, Fore.LIGHTBLACK_EX + "Grosse Update :" + Fore.RESET)
    TABLE_DATA.append(private_messages) 
    private_messages = (" ", Fore.LIGHTBLACK_EX + "Messages Randoms de bienvenue ect" + Fore.RESET)
    TABLE_DATA.append(private_messages)
    private_messages = (" ", Fore.LIGHTBLACK_EX + "Amelioration de la rpc" + Fore.RESET)
    TABLE_DATA.append(private_messages)
    table = SingleTable(TABLE_DATA)
    print("\n"+table.table)
Messages()

def client_speak(nickname, ip, port):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_connection = client.connect((str(ip),int(port)))
    ver = client.send(version.encode('utf-8'))

    serv = client.recv(1024).decode('utf-8')
    decryptserv = base64.b85decode(serv)
    decodeserv = decryptserv.decode('utf-8')

    description = client.recv(1024).decode('utf-8')
    decrypt_description = base64.b85decode(description)
    decode_description = decrypt_description.decode('utf-8')

    speakchatrpc(servername=decodeserv,username=nickname,description=decode_description)
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

def Ip_Select(nick):
    if state.need_ip_port == True:
        print(" ")
        ip = input(" Ip du serveur speak : ")
        print(" ")
        port = input(" Port du serveur speak : ")
        clear()
        print(Menu.design_ui)
        print(" ")
        client_speak(nickname=nick, ip=ip, port=port)
    else:
        ip = 'vps-1f21facc.vps.ovh.net'
        port = 6677
        client_speak(nickname=nick, ip=ip, port=port)


def Nick_Choice():
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
        sleep(1.5)
        clear()
        print(Menu.design_ui)
        Ip_Select(nick=nickname)

    elif nick_choice == '2':
        print(" ")
        name = input(" Nouveau nom d'utilisateur : ")
        nickname = str(name)
        if nickname == '':
            print(" ")
            print("  " + warn + "Erreur x-x")
            sleep(1.5)
            clear()
            print(Menu.design_ui)
            Messages()
            Choix()
            pass
        else:
            sleep(1.5)
            clear()
            print(Menu.design_ui)
            Ip_Select(nick=nickname)

    elif nick_choice == '3':
        nickname = str(user)
        print(" ")
        print(" Votre nom d'utilisateur : %s" % (nickname))
        sleep(1.5)
        clear()
        print(Menu.design_ui)
        Ip_Select(nick=nickname)
    else:
        print(" ")
        print("  " + warn + "Erreur x-x")
        sleep(1.5)
        clear()
        print(Menu.design_ui)
        Messages()
        Choix()
        pass

def Choix():
    print(f"""

    [{Fore.LIGHTBLUE_EX + str("1") + Fore.RESET}] Serveur speak Officiel
    
    [{Fore.LIGHTBLUE_EX + str("2") + Fore.RESET}] Connection a un Serveur Speak non-officiel

    """
    )
    choice = input(" Salon choisi : ")

    #Général
    if choice == '1':
        clear()
        print(Menu.design_ui)
        state.need_ip_port = False
        Nick_Choice()

    elif choice == '2':
        clear()
        print(Menu.design_ui)
        state.need_ip_port = True
        Nick_Choice()

    else:
        print(" ")
        print("  " + warn + "Erreur x-x")
        sleep(1.5)
        clear()
        print(Menu.design_ui)
        Messages()
        Choix()
        pass

Choix()
