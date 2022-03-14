# ❤️in name of god❤️
import colorama
from pyautogui import alert
import subprocess
import os


alert("❤️In Name Of God❤️")

os.system("cls")
print(colorama.Fore.YELLOW + """\n█     █░ ██▓  █████▒██▓    ██▓███   ▄▄▄        ██████   ██████  █     █░ ▒█████   ██▀███  ▓█████▄  ▐██▌ 
▓█░ █ ░█░▓██▒▓██   ▒▓██▒   ▓██░  ██▒▒████▄    ▒██    ▒ ▒██    ▒ ▓█░ █ ░█░▒██▒  ██▒▓██ ▒ ██▒▒██▀ ██▌ ▐██▌ 
▒█░ █ ░█ ▒██▒▒████ ░▒██▒   ▓██░ ██▓▒▒██  ▀█▄  ░ ▓██▄   ░ ▓██▄   ▒█░ █ ░█ ▒██░  ██▒▓██ ░▄█ ▒░██   █▌ ▐██▌ 
░█░ █ ░█ ░██░░▓█▒  ░░██░   ▒██▄█▓▒ ▒░██▄▄▄▄██   ▒   ██▒  ▒   ██▒░█░ █ ░█ ▒██   ██░▒██▀▀█▄  ░▓█▄   ▌ ▓██▒ 
░░██▒██▓ ░██░░▒█░   ░██░   ▒██▒ ░  ░ ▓█   ▓██▒▒██████▒▒▒██████▒▒░░██▒██▓ ░ ████▓▒░░██▓ ▒██▒░▒████▓  ▒▄▄  
░ ▓░▒ ▒  ░▓   ▒ ░   ░▓     ▒▓▒░ ░  ░ ▒▒   ▓▒█░▒ ▒▓▒ ▒ ░▒ ▒▓▒ ▒ ░░ ▓░▒ ▒  ░ ▒░▒░▒░ ░ ▒▓ ░▒▓░ ▒▒▓  ▒  ░▀▀▒ 
  ▒ ░ ░   ▒ ░ ░      ▒ ░   ░▒ ░       ▒   ▒▒ ░░ ░▒  ░ ░░ ░▒  ░ ░  ▒ ░ ░    ░ ▒ ▒░   ░▒ ░ ▒░ ░ ▒  ▒  ░  ░ 
  ░   ░   ▒ ░ ░ ░    ▒ ░   ░░         ░   ▒   ░  ░  ░  ░  ░  ░    ░   ░  ░ ░ ░ ▒    ░░   ░  ░ ░  ░     ░ 
    ░     ░          ░                    ░  ░      ░        ░      ░        ░ ░     ░        ░     ░    
                                                                                            ░            """)
print(colorama.Fore.CYAN + "\nWIFI PASSWORD: ")
replace_1 = subprocess.getoutput("netsh wlan show profiles").replace("Profiles on interface Wi-Fi:", "").replace("Group policy profiles (read only)", "").replace("---------------------------------", "").replace("\n", "").replace("\t", "").replace("<None>", "").replace("User profiles", "").replace("-------------", "").replace("All User Profile ", "").replace("            :", "")
split_text = replace_1.split(":")
for i in split_text:
    password = subprocess.getoutput("netsh wlan show profile "+i+" key=clear")
    wifi_password = ("\n" + password.split("\n")[10] + "\n" + password.split("\n")[32].replace("Cost settings", ""))
    print(colorama.Fore.BLUE + wifi_password)
