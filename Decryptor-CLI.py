#!/usr/bin/env python
#Author: Intrackeable
#Github: https://github.com/intrackeable

import time, os
from os import path

try:
    import argparse, pyfiglet
    from colorama import Fore, Style
    from cryptography.fernet import Fernet

except ImportError:
    print('Use pip install -r requirements')
    exit()

#COLORS
E = Fore.LIGHTGREEN_EX + Style.NORMAL
W = Fore.LIGHTWHITE_EX + Style.NORMAL
G = Fore.LIGHTGREEN_EX + Style.BRIGHT
R = Fore.LIGHTRED_EX + Style.BRIGHT

def Options():

    parser = argparse.ArgumentParser()
    parser.add_argument('-K','--key', help='Your secret key to decrypt files.', type=str)
    parser.add_argument('-F','--files', help='File name with path list.')
    args = parser.parse_args()

    return args.key, args.files

def Decrypt_File_List(key,victims):

    with open(victims,'r') as victimspaths:
        pathlist = victimspaths.read().split('\n')
        pathlist = [x for x in pathlist if not x == '']
        victimspaths.close()

    for i in pathlist:

        time.sleep(0.1)
        print(G + '[-] '+ W + 'Decrypting: {}'.format(i))

        Decrypt_File(key,i)
    
def Decrypt_File(key,filename):
    try:
        f = Fernet(key)

        with open(filename,'rb') as file:
            file_content = file.read()
            file.close()

        decrypted_data = f.decrypt(file_content)
        
        with open(filename, 'wb') as file:
            file.write(decrypted_data)
            file.close()

    except:
        print(R + 'INVALID KEY!')
        exit()

def Show_Banner():
    logo = pyfiglet.figlet_format('Decryptor',font='slant')
    os.system('clear')
    print(E + logo)

def main():
    Show_Banner()
    key, victims = Options()

    if key and victims:
        if path.isfile(victims):
            Decrypt_File_List(key,victims)
        else:
            print(R + 'Invalid File!')
    else:
        print(R + 'TRY IT AGAIN!')

if __name__ == '__main__':
    main()



