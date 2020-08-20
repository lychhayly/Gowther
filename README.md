# Ravage Ransomware 🐍 
This is a simple program designed in Python,
to learn about how some ransomware works, using AES symmetric encryption.
Only for Linux systems.

![Screenshot](/Screenshots/ravage.png)

## Operation
Once run from the console, ravage checks all the system paths with a valid extension, adds them to a list, generates a text file with the affected items on the machine, and proceeds to encrypt each one. Then it generates a file containing: decryption key, public IP address, system username, random ID and date.
Finally the data is sent to an FTP or SMTP server.
For security reasons, the key is stored on the victim machine.

## In Development
* Multithreading for fast encryption
* Support for Windows systems
* Send information to SQL databases
* Graphical Interfaces

## Attention
Perform tests only on virtual machines, use this program with educational purposes and not for evil.

## Installation
```text
git clone https://www.github.com/intrackeable/Ravage-Ransomware.git
cd Ravage-Ransomware
pip install -r requirements.txt
```
![Screenshot](/Screenshots/decryptor.png)
## References
 * [Symmetric encryption with Fernet](https://www.pythoninformer.com/python-libraries/cryptography/fernet/)
 * [Ransomware explained](https://www.csoonline.com/article/3236183/what-is-ransomware-how-it-works-and-how-to-remove-it.html)
 * [What is AES encryption and how does it work?](https://www.comparitech.com/blog/information-security/what-is-aes-encryption/)
