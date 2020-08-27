# Gowther Ransomware 

This is a simple program designed in Python,
to learn about how some ransomware works, using AES symmetric encryption.

**The project is under development, any suggestion is welcome!**

![Screenshot](https://img.shields.io/badge/Platform-Linux-brightgreen)
![Screenshot](https://img.shields.io/badge/License-GPL-red)
![Screenshot](https://img.shields.io/badge/Language-Python%203-blue)
![Screenshot](/Screenshots/test.png)

## How does it work ?
Once run from the console, Gowther checks all the system paths with a valid extension, adds them to a list, generates a text file with the affected items on the machine, and proceeds to encrypt each one.

Then it generates a file containing: decryption key, public IP address, system username, random ID and date.

Finally the data is sent to an SMTP server or MySQL database.

When the program is executed again, only show the GUI, asking the key to retrieve the files.

For security reasons and to avoid script kiddies, the key is stored on the victim machine.

## How to use it ?
Edit the lines 67 and 68, change the boolean values to select the way in which the data will be sent.

In the case of using SMTP, create a Google account and in settings enable "Access to less secure applications". Then insert the data of the configuration you want to use.

## In Development
- [x] Send logs to SMTP server.
- [x] Graphical Interfaces.
- [x] Send information to MySQL database.
- [ ] Multithreading for fast encryption.
- [ ] Support for Windows.
- [ ] Encrypt external storage drives.


## References
 * [Symmetric encryption with Fernet](https://www.pythoninformer.com/python-libraries/cryptography/fernet/)
 * [Ransomware explained](https://www.csoonline.com/article/3236183/what-is-ransomware-how-it-works-and-how-to-remove-it.html)
 * [What is AES encryption and how does it work?](https://www.comparitech.com/blog/information-security/what-is-aes-encryption/)
 
## Disclaimer
Perform tests only on virtual machines, never run this on your main system.

This program was made for educational purposes only. I am not responsible for damages.
 
 ## Screenshots
 ![Screenshot](/Screenshots/image.png)
 
 
