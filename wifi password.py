# import librari Required!
import subprocess
import time
from colorama import Fore
import os

# clear 
os.system('cls')
# banner script
print(Fore.BLUE,"""\n█     █░ ██▓  █████▒██▓    ██▓███   ▄▄▄        ██████   ██████  █     █░ ▒█████   ██▀███  ▓█████▄  ▐██▌ 
▓█░ █ ░█░▓██▒▓██   ▒▓██▒   ▓██░  ██▒▒████▄    ▒██    ▒ ▒██    ▒ ▓█░ █ ░█░▒██▒  ██▒▓██ ▒ ██▒▒██▀ ██▌ ▐██▌ 
▒█░ █ ░█ ▒██▒▒████ ░▒██▒   ▓██░ ██▓▒▒██  ▀█▄  ░ ▓██▄   ░ ▓██▄   ▒█░ █ ░█ ▒██░  ██▒▓██ ░▄█ ▒░██   █▌ ▐██▌ 
░█░ █ ░█ ░██░░▓█▒  ░░██░   ▒██▄█▓▒ ▒░██▄▄▄▄██   ▒   ██▒  ▒   ██▒░█░ █ ░█ ▒██   ██░▒██▀▀█▄  ░▓█▄   ▌ ▓██▒ 
░░██▒██▓ ░██░░▒█░   ░██░   ▒██▒ ░  ░ ▓█   ▓██▒▒██████▒▒▒██████▒▒░░██▒██▓ ░ ████▓▒░░██▓ ▒██▒░▒████▓  ▒▄▄  
░ ▓░▒ ▒  ░▓   ▒ ░   ░▓     ▒▓▒░ ░  ░ ▒▒   ▓▒█░▒ ▒▓▒ ▒ ░▒ ▒▓▒ ▒ ░░ ▓░▒ ▒  ░ ▒░▒░▒░ ░ ▒▓ ░▒▓░ ▒▒▓  ▒  ░▀▀▒ 
  ▒ ░ ░   ▒ ░ ░      ▒ ░   ░▒ ░       ▒   ▒▒ ░░ ░▒  ░ ░░ ░▒  ░ ░  ▒ ░ ░    ░ ▒ ▒░   ░▒ ░ ▒░ ░ ▒  ▒  ░  ░ 
  ░   ░   ▒ ░ ░ ░    ▒ ░   ░░         ░   ▒   ░  ░  ░  ░  ░  ░    ░   ░  ░ ░ ░ ▒    ░░   ░  ░ ░  ░     ░ 
    ░     ░          ░                    ░  ░      ░        ░      ░        ░ ░     ░        ░     ░    
                                                                                            ░            """)
while True:
    # name wifi to password
    name_wifi = input(Fore.CYAN+"\nPlese You r Name Wifi To Password(ls to see the name of the connected WiFi) :>> ")
    # list wifi connected
    if name_wifi == "ls":
        list_wifi = subprocess.getoutput("netsh wlan show profiles").replace("Group policy profiles (read only)", "").replace("---------------------------------", "").replace("<None>", "").replace("All User Profile", "*Name WIFI*").replace("Profiles on interface Wi-Fi:", "").replace("is not found on the system.", "")
        print(Fore.RED+(list_wifi))
    # command cmd password wifi
    command = "netsh wlan show profile "+name_wifi+" key=clear"
    # Hit the command with subprocss
    password = subprocess.getoutput(command).replace("Key Content", "*Password WiFi*") # To replace 
    # print password wifi
    print(Fore.GREEN+(password))
    # ======================================================================= Warning
    print(Fore.RED,"\n If there is no Wi-Fi password, the desired Wi-Fi can not be password-protected and has high security!")

    # the whole
