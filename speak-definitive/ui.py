import os, time
from colorama import Fore, init
import getpass
import socket
import subprocess as sp

def times():
	times = time.strftime("%H:%M:%S")
	times = str(times)
	return(times)

def clear():
	if os.name == 'nt':
		return os.system('cls')
	else:
		return os.system('clear')

def check_host():
    version = 'HOST_CHECK'
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex(('vps-1f21facc.vps.ovh.net', 6677))
    if result == 0:
        ver = sock.send(version.encode('utf-8'))
        return str(Fore.LIGHTGREEN_EX + "Online" + Fore.RESET)
    else:
        return str(Fore.LIGHTRED_EX + "Offline" + Fore.RESET)

if os.name == 'nt':
    init(convert=True)
else:
    init(convert=False)

user = getpass.getuser()

smoke_layer1 = (Fore.LIGHTBLACK_EX+'('+Fore.RESET)
smoke_layer2 = (Fore.LIGHTBLACK_EX+')'+Fore.RESET)

class Menu():
    design_txt_layer_1 = ("                          _    ")
    design_txt_layer_2 = ("     ___ _ __   ___  __ _| | __")
    design_txt_layer_3 = ("    / __| '_ \ / _ \/ _` | |/ /")
    design_txt_layer_4 = ("    \__ \ |_) |  __/ (_| |   < ")
    design_txt_layer_5 = ("    |___/ .__/ \___|\__,_|_|\_\ ")
    design_txt_layer_6 = ("        |_|                    ")
    design_ui = ("""
         %s
        %s
       __%s__
    C\|     \  %s
      \     /  %s
       \___/   %s

%s
%s
%s
%s
%s
%s

    """ %(
            str(smoke_layer2),
            str(smoke_layer1),
            str(smoke_layer2),
            str("     Heure : [" + Fore.LIGHTBLUE_EX + times() + Fore.RESET + str("]")),
            str("     Utilisateur (PC) : [" + Fore.LIGHTBLUE_EX + str(user) + Fore.RESET + str("]")),
            str("     Statut Serveur : [") + check_host() + str("]"),
            str(design_txt_layer_1),
            str(design_txt_layer_2),
            str(design_txt_layer_3),
            str(design_txt_layer_4),
            str(design_txt_layer_5),
            str(design_txt_layer_6)

         ))
clear()
