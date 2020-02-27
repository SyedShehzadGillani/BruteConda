#!/usr/bin/python
import requests
from time import sleep
from colorama import Back,Fore,init
import sys
import argparse
import os.path
init(autoreset=True)
arguments = argparse.ArgumentParser()
arguments.add_argument('--url','-u',type=str,help='Target URL',required=True)
arguments.add_argument('--wordlist','-w',type=str,help='Path Of The Wordlist',required=True)
arguments.parse_args()
line = Fore.GREEN + '''
            ============================================================================================
'''
print(line)
banner = print(Fore.BLUE + '''
		██████╗ ██████╗ ██╗   ██╗████████╗███████╗ ██████╗ ██████╗ ███╗   ██╗██████╗  █████╗ 
		██╔══██╗██╔══██╗██║   ██║╚══██╔══╝██╔════╝██╔════╝██╔═══██╗████╗  ██║██╔══██╗██╔══██╗
		██████╔╝██████╔╝██║   ██║   ██║   █████╗  ██║     ██║   ██║██╔██╗ ██║██║  ██║███████║
		██╔══██╗██╔══██╗██║   ██║   ██║   ██╔══╝  ██║     ██║   ██║██║╚██╗██║██║  ██║██╔══██║
		██████╔╝██║  ██║╚██████╔╝   ██║   ███████╗╚██████╗╚██████╔╝██║ ╚████║██████╔╝██║  ██║
		╚═════╝ ╚═╝  ╚═╝ ╚═════╝    ╚═╝   ╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝╚═════╝ ╚═╝  ╚═╝
		''' + Fore.WHITE + '''
	                              +-+ Codded By AkDevil Hunter +-+
	                                  +-+ Team Pak Black Army +-+
	                           +-+ https://facebook.com/PakBlackArmy +-+''')
print(line)
def start():
	avatar = Fore.BLUE + "[" + Fore.RED + "+" + Fore.BLUE + "] " + Fore.WHITE
	print(avatar + "Starting Attack On : " + sys.argv[2])
	sleep(2)
	print(avatar + "Loading Wordlist...")
	if os.path.isfile(str(sys.argv[4])) == True: 
		print(avatar + "Wordlist Loaded Succesfully")
		sleep(2)
		with open(str(sys.argv[4])) as wordlist:
			read_line = wordlist.readlines()
		for read_each_line in read_line:
			path_of_url = sys.argv[2] + "/" + read_each_line
			get_url = requests.get(path_of_url).status_code
			if get_url == 200:
				print(avatar + path_of_url + Fore.BLUE + " => " + Fore.WHITE + "Found!" + "\n")
			elif get_url == 404:
				print(avatar + path_of_url + Fore.BLUE + " => " + Fore.WHITE + "Not Found!" + "\n")
			else:
				print(avatar + path_of_url + Fore.BLUE + " => " + Fore.WHITE + get_url + "\n")
	else:
		print(avatar + "Error In Loading Wordlist,Check Permissions Or Path Of Your File")
start()
