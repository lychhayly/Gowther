# Ravage Ransomware 

This is a simple program designed in Python,
to learn about how some ransomware works, using AES symmetric encryption. 
**The project is under development, any suggestion is welcome!**

## How does it work ?
Once run from the console, ravage checks all the system paths with a valid extension, adds them to a list, generates a text file with the affected items on the machine, and proceeds to encrypt each one.

Then it generates a file containing: decryption key, public IP address, system username, random ID and date.

Finally the data is sent to an FTP or SMTP server.

For security reasons, the key is stored on the victim machine.

## How to use it ?
Edit the lines 87 and 88, change the boolean values to select the way in which the data will be sent.

In the case of using SMTP, create a Google account and in settings enable "Access to less secure applications". Then insert the data of the configuration you want to use.

## In Development
- [x] Send logs to FTP and SMTP server.
- [ ] Multithreading for fast encryption
- [ ] Support for Windows.
- [ ] Send information to MySQL database.
- [ ] Graphical Interfaces.

## References
 * [Symmetric encryption with Fernet](https://www.pythoninformer.com/python-libraries/cryptography/fernet/)
 * [Ransomware explained](https://www.csoonline.com/article/3236183/what-is-ransomware-how-it-works-and-how-to-remove-it.html)
 * [What is AES encryption and how does it work?](https://www.comparitech.com/blog/information-security/what-is-aes-encryption/)
 
## Disclaimer
Perform tests only on virtual machines, never run this on your main system.
This program was made for educational purposes only. I am not responsible for damages.
 
 ## Screenshots
 ![Screenshot](/Screenshots/ravage.png)
 
 
