from pypresence import Presence
from ui import Menu
import sys, os, time, random
from colorama import Fore, init
from time import sleep

def clear():
	if os.name == 'nt':
		return os.system('cls')
	else:
		return os.system('clear')

def speakrpc():
    clear()
    print(Menu.design_ui)
    print(f"""
    Rich Presence Discord
    {Fore. LIGHTBLACK_EX + str("(Vous devez avoir Discord d'installé)") + Fore.RESET}

    {str("[") + Fore.LIGHTBLUE_EX + str("1") + Fore.RESET + str("]") + str(" Activer la RichPresence.")}
    {str("[") + Fore.LIGHTBLUE_EX + str("2") + Fore.RESET + str("]") + str(" Ne pas Activer.")}""")
    print(" ")
    rpc_choice = input(" RPC : ")
    if rpc_choice == '1':
        client_id = "817762863514517524"
        rpc = Presence(client_id)
        rpc.connect()
        rpc.update(state="terminal chat",large_image="logo",large_text="speak")
        pass
    elif rpc_choice == '2':
        pass
    else:
        print(Fore.LIGHTRED_EX + "  Erreur :/" + Fore.RESET)
        sleep(3.0)
        speakrpc()

speakrpc()
