# Imports
import os # You're insecure :)
import psutil
from colorama import Fore, Back, init
import shutil
from time import sleep
import ctypes
import pyperclip as pc

# CONSTANTS
HOME_PATH = os.path.expanduser("~")
ROBLOX_PATH = HOME_PATH + "\\AppData\\Local\\Roblox"
USER_TEMP = HOME_PATH + "\\AppData\\Local\\Temp"
PREFETCH = "C:\\Windows\\Prefetch"
SYS_TEMP = "C:\\Windows\\Temp"

# Check if running as Administrator
if ctypes.windll.shell32.IsUserAnAdmin() == 0:
    print("Open as Administrator...")
    sleep(2)
    exit()

# Start
print("By ROOT44x")
print("https://github.com/ROOT44x (Copied to clipboard)")

pc.copy("https://github.com/ROOT44x")

sleep(5)
os.system("cls")

init()  # Colorama init

# Killing roblox
print(Fore.RED + "Killing Roblox process")

for proc in psutil.process_iter():
    if proc.name() == "RobloxPlayerBeta.exe":
        proc.kill()

print(Fore.GREEN + "Killed process\n")

print(Fore.WHITE + "--------------------\n")

# Method ONE
print(Fore.GREEN + "Trying Method #1 - Deleting GlobalBasicSettings_13.xml")

if os.path.exists(ROBLOX_PATH + "\\GlobalBasicSettings_13.xml"):
    os.remove(ROBLOX_PATH + "\\GlobalBasicSettings_13.xml")
    print(Fore.GREEN + "File successfully deleted\n")
else:
    print(Fore.RED + "File doesn't exist\n")

print(Fore.WHITE + "--------------------\n")

# Method TWO
print(Fore.GREEN + "Trying Method #2 - Deleting Temp files")

try:
    shutil.rmtree(USER_TEMP, ignore_errors=True)
    shutil.rmtree(PREFETCH, ignore_errors=True)
    shutil.rmtree(SYS_TEMP, ignore_errors=True)
    print(Fore.GREEN + "Temporary files deleted successfully\n")
except:
    print(Fore.RED + "An error ocurred - Please make sure you run this tool as Administrator\n")

print(Fore.WHITE + "--------------------\n")

# Method THREE
print(Fore.GREEN + "Trying Method #3 - Deleting every file in ROBLOX Folder" + Fore.RESET)

print(Back.RED + f"WARNING: EVERY FILE IN {ROBLOX_PATH} WILL BE DELETED" + Back.RESET)

if str(input("\nDo you want to continue (Y/N) ")).upper() == "Y":
    for file in os.listdir(ROBLOX_PATH):
        try:
            os.remove(os.path.join(ROBLOX_PATH, file))
        except:
            pass
    print(Fore.GREEN + "Files successfully deleted\n")
else:
    print("Omitting...")

sleep(3)

# Finish
os.system("cls")
print(Fore.YELLOW + "If doesn't work remove your Roblox client" + Fore.RESET)
input("Press any key for exit...")