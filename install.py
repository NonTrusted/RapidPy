import os
import platform
import subprocess
import getpass

if platform.system() == 'Windows':
    os.system('cls')
else:
    os.system('clear')

subprocess.call(['pip', 'install', 'requests', 'ping3', 'discord_webhook', 'colorama', 'Pillow'])

if platform.system() == 'Windows':
    os.system('cls')
else:
    os.system('clear')

print('Requirements Installed...')
getpass.getpass('Press Enter To Exit...')