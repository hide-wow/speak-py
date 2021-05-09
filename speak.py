from ui import Menu
import requests, re, json
import os, sys, time, terminaltables
from terminaltables import SingleTable
from colorama import Fore, init
from time import sleepfrom ui import Menu
import requests, re, json
import os, sys, time, terminaltables
from terminaltables import SingleTable
from colorama import Fore, init
from time import sleep
import random
import getpass

stop_thread = False

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

if os.name == 'nt':
    init(convert=True)
else:
    init(convert=False)

print(Menu.design_ui)

def Messages():
    TABLE_DATA = []
    private_messages = (Fore.LIGHTYELLOW_EX + "Speak Main" + Fore.RESET, "Nom D'utilisateur : " + user)
    TABLE_DATA.append(private_messages)
    private_messages = ("News :", Fore.LIGHTBLUE_EX + "Serveur speak (par ip)" + Fore.RESET)
    TABLE_DATA.append(private_messages) 
    private_messages = (" ", Fore.LIGHTBLUE_EX + "Fix du bug majeur des inputs" + Fore.RESET)
    TABLE_DATA.append(private_messages)
    private_messages = (" ", Fore.LIGHTBLUE_EX + "Fix de 2 - 3 bugs non grave" + Fore.RESET)
    TABLE_DATA.append(private_messages)
    private_messages = ("----------------", "-----------------------" + Fore.RESET)
    TABLE_DATA.append(private_messages)
    private_messages = ("Conversations :", Fore.LIGHTBLUE_EX + "Serveur" + Fore.LIGHTBLUE_EX + " (" + Fore.LIGHTRED_EX + "1" + Fore.LIGHTBLUE_EX + ")" + Fore.RESET)
    TABLE_DATA.append(private_messages)
    table = SingleTable(TABLE_DATA)
    print("\n"+table.table)
Messages()

def Choix():
    print("""

        [1] %s

    """ % (
        str(Fore.LIGHTBLUE_EX + "Serveur" + Fore.RESET)
    ))
    choice = input(" Salon choisi : ")

    #Général
    if choice == '1':
        clear()
        print(Menu.design_ui)
        import socket
        import threading

        # Choosing Nickname
        print("""
        Nom d'utilisateur :

        [1] : Au hazard
        [2] : Nom au choix
        [3] : Nom de l'user du pc

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
            print(" ")
            client.connect((str(ip),int(port)))

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
                            client.send(nickname.encode('utf-8'))
                            next_message = client.recv(1024).decode('utf-8')
                            if next_message == 'PASS':
                                client.send(password.encode('utf-8'))
                                if client.recv(1024).decode('utf-8') == "NAHBRO":
                                    print(" Conection fermée, mot de passe incorrect.")
                                    stop_thread = True
                                
                            elif next_message == 'BAN':
                                print(Fore.LIGHTRED_EX + " Vous avez été Banni de speak par un Administrateur")
                                client.close()
                                stop_thread = True
                        else:
                            print(" ")
                            print(message)
                            print(" ")
                    except:
                        # Close Connection When Error
                        print(" Une erreure s'est produite!")
                        client.close()
                        break

            # Sending Messages To Server
            def write():
                while True:
                    if stop_thread:
                        break
                    message = ' - {}: {}'.format(Fore.LIGHTBLUE_EX + nickname + Fore.RESET, getpass.getpass(Fore.LIGHTBLACK_EX +" Vous :"+ Fore.RESET))
                    client.send(message.encode('utf-8'))

            # Starting Threads For Listening And Writing
            receive_thread = threading.Thread(target=receive)
            receive_thread.start()

            write_thread = threading.Thread(target=write)
            write_thread.start()

        elif nick_choice == '2':
            print(" ")
            name = input(" Nouveau nom d'utilisateur : ")
            nickname = str(name)
            sleep(3.0)
            clear()
            print(Menu.design_ui)
            # Connecting To Server
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            print(" ")
            ip = input(" Ip du serveur speak : ")
            print(" ")
            port = input(" Port du serveur speak : ")
            print(" ")
            client.connect((str(ip),int(port)))

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
                            client.send(nickname.encode('utf-8'))
                            next_message = client.recv(1024).decode('utf-8')
                            if next_message == 'PASS':
                                client.send(password.encode('utf-8'))
                                if client.recv(1024).decode('utf-8') == "NAHBRO":
                                    print(" Conection fermée, mot de passe incorrect.")
                                    stop_thread = True
                                
                            elif next_message == 'BAN':
                                print(Fore.LIGHTRED_EX + " Vous avez été Banni de speak par un Administrateur")
                                client.close()
                                stop_thread = True
                        else:
                            print(" ")
                            print(message)
                            print(" ")
                    except:
                        # Close Connection When Error
                        print(" Une erreure s'est produite!")
                        client.close()
                        break

            # Sending Messages To Server
            def write():
                while True:
                    if stop_thread:
                        break
                    message = ' - {}: {}'.format(Fore.LIGHTBLUE_EX + nickname + Fore.RESET, getpass.getpass(Fore.LIGHTBLACK_EX +" Vous :"+ Fore.RESET))
                    client.send(message.encode('utf-8'))

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
            print(" ")
            client.connect((str(ip),int(port)))

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
                            client.send(nickname.encode('utf-8'))
                            next_message = client.recv(1024).decode('utf-8')
                            if next_message == 'PASS':
                                client.send(password.encode('utf-8'))
                                if client.recv(1024).decode('utf-8') == "NAHBRO":
                                    print(" Conection fermée, mot de passe incorrect.")
                                    stop_thread = True
                                
                            elif next_message == 'BAN':
                                print(Fore.LIGHTRED_EX + " Vous avez été Banni de speak par un Administrateur")
                                client.close()
                                stop_thread = True
                        else:
                            print(" ")
                            print(message)
                            print(" ")
                    except:
                        # Close Connection When Error
                        print(" Une erreure s'est produite!")
                        client.close()
                        break

            # Sending Messages To Server
            def write():
                while True:
                    if stop_thread:
                        break
                    message = ' - {}: {}'.format(Fore.LIGHTBLUE_EX + nickname + Fore.RESET, getpass.getpass(Fore.LIGHTBLACK_EX +" Vous :"+ Fore.RESET))
                    client.send(message.encode('utf-8'))

            # Starting Threads For Listening And Writing
            receive_thread = threading.Thread(target=receive)
            receive_thread.start()

            write_thread = threading.Thread(target=write)
            write_thread.start()
        else:
            print(" ")
            print(Fore.LIGHTRED_EX + " Erreur :/" + Fore.RESET)
            sleep(3.0)
            clear()
            print(Menu.design_ui)
            Messages()
            Choix()
            pass

    else:
        print(" ")
        print(Fore.LIGHTRED_EX + " Erreur :/" + Fore.RESET)
        sleep(3.0)
        clear()
        print(Menu.design_ui)
        Messages()
        Choix()
        pass

Choix()
import random
import getpass

stop_thread = False

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

if os.name == 'nt':
    init(convert=True)
else:
    init(convert=False)

print(Menu.design_ui)

def Messages():
    TABLE_DATA = []
    private_messages = (Fore.LIGHTYELLOW_EX + "Speak Main" + Fore.RESET, "Nom D'utilisateur : " + user)
    TABLE_DATA.append(private_messages)
    private_messages = ("News :", Fore.LIGHTBLUE_EX + "Serveur speak (par ip)" + Fore.RESET)
    TABLE_DATA.append(private_messages) 
    private_messages = (" ", Fore.LIGHTBLUE_EX + "Fix du bug majeur des inputs" + Fore.RESET)
    TABLE_DATA.append(private_messages)
    private_messages = (" ", Fore.LIGHTBLUE_EX + "Fix de 2 - 3 bugs non grave" + Fore.RESET)
    TABLE_DATA.append(private_messages)
    private_messages = ("----------------", "-----------------------" + Fore.RESET)
    TABLE_DATA.append(private_messages)
    private_messages = ("Conversations :", Fore.LIGHTBLUE_EX + "Serveur" + Fore.LIGHTBLUE_EX + " (" + Fore.LIGHTRED_EX + "1" + Fore.LIGHTBLUE_EX + ")" + Fore.RESET)
    TABLE_DATA.append(private_messages)
    table = SingleTable(TABLE_DATA)
    print("\n"+table.table)
Messages()

def Choix():
    print("""

        [1] %s

    """ % (
        str(Fore.LIGHTBLUE_EX + "Serveur" + Fore.RESET)
    ))
    choice = input(" Salon choisi : ")

    #Général
    if choice == '1':
        clear()
        print(Menu.design_ui)
        import socket
        import threading

        # Choosing Nickname
        print("""
        Nom d'utilisateur :

        [1] : Au hazard
        [2] : Nom au choix
        [3] : Nom de l'user du pc

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
            ip = input(" Ip du serveur speak : ")
            port = input(" Port du serveur speak : ")
            client.connect((str(ip),int(port)))

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
                            client.send(nickname.encode('utf-8'))
                            next_message = client.recv(1024).decode('utf-8')
                            if next_message == 'PASS':
                                client.send(password.encode('utf-8'))
                                if client.recv(1024).decode('utf-8') == "NAHBRO":
                                    print(" Conection fermée, mot de passe incorrect.")
                                    stop_thread = True
                                
                            elif next_message == 'BAN':
                                print(Fore.LIGHTRED_EX + " Vous avez été Banni de speak par un Administrateur")
                                client.close()
                                stop_thread = True
                        else:
                            print(" ")
                            print(message)
                            print(" ")
                    except:
                        # Close Connection When Error
                        print(" Une erreure s'est produite!")
                        client.close()
                        break

            # Sending Messages To Server
            def write():
                while True:
                    if stop_thread:
                        break
                    message = ' - {}: {}'.format(Fore.LIGHTBLUE_EX + nickname + Fore.RESET, getpass.getpass(""))
                    client.send(message.encode('utf-8'))

            # Starting Threads For Listening And Writing
            receive_thread = threading.Thread(target=receive)
            receive_thread.start()

            write_thread = threading.Thread(target=write)
            write_thread.start()

        elif nick_choice == '2':
            print(" ")
            name = input(" Nouveau nom d'utilisateur : ")
            nickname = str(name)
            sleep(3.0)
            clear()
            print(Menu.design_ui)
            # Connecting To Server
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            ip = input(" Ip du serveur speak : ")
            port = input(" Port du serveur speak : ")
            client.connect((str(ip),int(port)))

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
                            client.send(nickname.encode('utf-8'))
                            next_message = client.recv(1024).decode('utf-8')
                            if next_message == 'PASS':
                                client.send(password.encode('utf-8'))
                                if client.recv(1024).decode('utf-8') == "NAHBRO":
                                    print(" Conection fermée, mot de passe incorrect.")
                                    stop_thread = True
                                
                            elif next_message == 'BAN':
                                print(Fore.LIGHTRED_EX + " Vous avez été Banni de speak par un Administrateur")
                                client.close()
                                stop_thread = True
                        else:
                            print(" ")
                            print(message)
                            print(" ")
                    except:
                        # Close Connection When Error
                        print(" Une erreure s'est produite!")
                        client.close()
                        break

            # Sending Messages To Server
            def write():
                while True:
                    if stop_thread:
                        break
                    message = ' - {}: {}'.format(Fore.LIGHTBLUE_EX + nickname + Fore.RESET, getpass.getpass(""))
                    client.send(message.encode('utf-8'))

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
            ip = input(" Ip du serveur speak : ")
            port = input(" Port du serveur speak : ")
            client.connect((str(ip),int(port)))

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
                            client.send(nickname.encode('utf-8'))
                            next_message = client.recv(1024).decode('utf-8')
                            if next_message == 'PASS':
                                client.send(password.encode('utf-8'))
                                if client.recv(1024).decode('utf-8') == "NAHBRO":
                                    print(" Conection fermée, mot de passe incorrect.")
                                    stop_thread = True
                                
                            elif next_message == 'BAN':
                                print(Fore.LIGHTRED_EX + " Vous avez été Banni de speak par un Administrateur")
                                client.close()
                                stop_thread = True
                        else:
                            print(" ")
                            print(message)
                            print(" ")
                    except:
                        # Close Connection When Error
                        print(" Une erreure s'est produite!")
                        client.close()
                        break

            # Sending Messages To Server
            def write():
                while True:
                    if stop_thread:
                        break
                    message = ' - {}: {}'.format(Fore.LIGHTBLUE_EX + nickname + Fore.RESET, getpass.getpass(""))
                    client.send(message.encode('utf-8'))

            # Starting Threads For Listening And Writing
            receive_thread = threading.Thread(target=receive)
            receive_thread.start()

            write_thread = threading.Thread(target=write)
            write_thread.start()
        else:
            print(" ")
            print(Fore.LIGHTRED_EX + " Erreur :/" + Fore.RESET)
            sleep(3.0)
            clear()
            print(Menu.design_ui)
            Messages()
            Choix()
            pass

    else:
        print(" ")
        print(Fore.LIGHTRED_EX + " Erreur :/" + Fore.RESET)
        sleep(3.0)
        clear()
        print(Menu.design_ui)
        Messages()
        Choix()
        pass

Choix()
