##################################################################################
# this script will encrypt a file using AES to create a password protected file
# the AES key is the SHA256 hash of the user provided password
#
# run at the terminal using the following
# > python aes_encrypt.py <PASSWORD> <PLAINTEXT_PATH> <CIPHERTEXT_PATH>
# <PASSWORD>: password used to generate AES key
# <PLAINTEXT_PATH>: path to file that will be encrypted
# <CIPHERTEXT_PATH>: path to newly generated encrypted file
#
#EXAMPLE:
#>python aes_encrypt.py Password123 file2enc.jpg cipher.aes
#
# IF <PASSWORD> IS NOT INCLUDED USER WILL BE PROMPTED TO ENTER IT SECURELY
##################################################################################

from sys import argv
import getpass
import ecies
import eth_keys
import hashlib


if len(argv)==4:
    _, password, plaintext_path, ciphertext_path = argv
elif len(argv)==3:
    _, plaintext_path, ciphertext_path  = argv
    while True:
        password = getpass.getpass("Input password for encryption: ")
        password_2 = getpass.getpass("Repeat password for encryption: ")
        if password==password_2:
            print('\nPasswords match...')
            break
        else:
            print('\nPasswords do not match...')
else:
    print('Incorrect number of arguments. 2 or 3 expected')
    print('> python aes_encrypt.py <PASSWORD> <PLAINTEXT_PATH> <CIPHERTEXT_PATH>')
    print('IF <PASSWORD> IS NOT INCLUDED USER WILL BE PROMPTED TO ENTER IT SECURELY')
    exit()

def aes_encrypt_file(plainfile_path,cipherfile_path,password):
    plain = open(plainfile_path,'rb').read()
    bytekey = hashlib.sha256( password.encode() ).digest()
    cipher = ecies.aes_encrypt(key=bytekey,plain_text=plain)
    open(cipherfile_path,'wb').write(cipher)



aes_encrypt_file(plaintext_path,ciphertext_path,password):
    print('Success:',plaintext_path, 'AES encryption complete')
    print('Written to:', ciphertext_path)

