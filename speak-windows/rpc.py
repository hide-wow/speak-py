from pypresence import Presence
from ui import Menu
import sys, os, time, random
from colorama import Fore, init
from time import sleep

warn = ("[" + Fore.LIGHTRED_EX + "!" + Fore.RESET + "] ")

client_id = "817762863514517524"
rpc = Presence(client_id)

class stats():
    rpcstat = False

def clear():
	if os.name == 'nt':
		return os.system('cls')
	else:
		return os.system('clear')

def speakrpc():
    clear()
    print(Menu.design_ui)
    print(f"""
    Rich Presence Discord:
    {str(warn) + str("(Vous devez avoir Discord d'installé)") + Fore.RESET}
    {str(warn) + str("(Les gens pourront voir votre pseudo + serveur connecté)") + Fore.RESET}

    {str("[") + Fore.LIGHTBLUE_EX + str("1") + Fore.RESET + str("]") + str(" Activer la RichPresence.")}
    {str("[") + Fore.LIGHTBLUE_EX + str("2") + Fore.RESET + str("]") + str(" Ne pas Activer.")} """)
    print(" ")
    rpc_choice = input(" RPC : ")
    if rpc_choice == '1':
        stats.rpcstat = True
        rpc.connect()
        rpc.update(state="In the menus",details=f"terminal chat",large_image="logo",large_text="secure, encrypted", start=time.time(), buttons = [{"label": "Git", "url": "https://github.com/Steraky/speak-py"}])
        pass
    elif rpc_choice == '2':
        pass
    else:
        print("  " + warn + "Erreur x-x")
        sleep(3.0)
        speakrpc()

def speakchatrpc(servername,username,description):
    if stats.rpcstat == True:
        rpc.update(state=f"In a server : {servername}",details=f"Name is : {username}",large_image="logo",large_text=description, start=time.time(), buttons = [{"label": "Git", "url": "https://github.com/Steraky/speak-py"}])
    else:
        pass
