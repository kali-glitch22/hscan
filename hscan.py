#!/bin/python3

import socket, sys
argumentos = sys.argv
red   = "\033[1;31m"
blue  = "\033[1;34m"
cyan  = "\033[1;36m"
green = "\033[0;32m"
reset = "\033[0;0m"
bold  = "\033[;1m"
reverse = "\033[;7m"
branco = "\033[37m"
gray = "\033[0;37m"
orange = "\033[0;49;33m"
yellow = "\033[0;49;93m"
ports = list(argumentos[4])
domain = argumentos[2]
def ini():
    print("-" * 65)
    print(yellow, """'\n\n __  __     ______     ______     ______     __    __    
/\ \_\ \   /\  ___\   /\  ___\   /\  __ \   /\ "-./  \   
\ \  __ \  \ \___  \  \ \ \____  \ \  __ \  \ \ \-./\ \  
 \ \_\ \_\  \/\_____\  \ \_____\  \ \_\ \_\  \ \_\ \ \_\ 
  \/_/\/_/   \/_____/   \/_____/   \/_/\/_/   \/_/  \/_/ 
                                                         \n""",reset)
    if 'hH' in argumentos or len(argumentos) <= 1 or len(argumentos) > 6:
        print(branco,"""       ./hscan.py       -d host -p portas ou -a
        --help -h        Mostra as instrunçoes
        -p --port port   portas para scanear
        -d --domain host   host para scanear
        -a               buscar portas pré-definidas
        -T1...T5 lento...rapido(quanto mais lento mais precisão)
        
        example:
        ./hscan.py -d google.com -p 80,90,123,12323 -T4
        ./hscan.py -d 192.168.0.100 -p 80-1000 -T3
        ./hscan.py -d 192.168.0.0-30 -a -T1
        """.capitalize(),reset)
ini()

def main():
    try:
        for port in ports:
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.settimeout(0.1)
            code = client.connect_ex((domain, ports))
            if code == 0:
                print(red,f'porta {port} aberta'.title(),reset)
            else:
                print(red,f'porta {port} fechada'.title(),reset)
    except Exception as e:
        ini()
        print(e)

main()
print('-' * 65)
