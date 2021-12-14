##################################################################################
# this script will generate an ECC private key from a computer generate 256 bit random number
# the key is saved to an AEC encrypted (password protected) file
#
# run at the terminal using the following
# > python ecc_generate.py <PRIVKEY_PATH> <PRIVKEY_PASSWORD>
# <PRIVKEY_PATH>: path to generated private key
# <PRIVKEY_PASSWORD>: password for private key file
#
#EXAMPLE:
#>python ecc_generate.py keys\privkey.bin password123
#
# IF <PRIVKEY_PASSWORD> IS NOT INCLUDED USER WILL BE PROMPTED TO ENTER IT SECURELY
##################################################################################

from sys import argv
import getpass
import ecies
import eth_keys
import hashlib
from Crypto.PublicKey import ECC
from Crypto.Random import get_random_bytes


if len(argv)==3:
    _, privkey_path, privkey_password = argv
elif len(argv)==2:
    _, privkey_path = argv
    while True:
        privkey_password = getpass.getpass("Input password for encrypting keyfile: ")
        privkey_password_2 = getpass.getpass("Repeat password for encrypting keyfile: ")
        if privkey_password==privkey_password_2:
            print('\nPasswords match...')
            break
        else:
            print('\nPasswords do not match...')
else:
    print('Wrong number arguments. 1 or 2 expected.')
    print('>python ecc_generate.py <PRIVKEY_PATH> <PRIVKEY_PASSWORD>')
    print('IF <PRIVKEY_PASSWORD> IS NOT INCLUDED USER WILL BE PROMPTED TO ENTER IT SECURELY')
    exit()

def gen_privKey():
    privKey=eth_keys.keys.PrivateKey(get_random_bytes(32) )
    return privKey

def save_key(key,path,password):
    if type(password)!=bytes:
        password=password.encode()
    encrypted_bytes=ecies.aes_encrypt(key=hashlib.sha256(password).digest(),plain_text=key.to_bytes())
    f=open(path,'wb')
    f.write(encrypted_bytes)
    f.close()
    return encrypted_bytes

#generate key
privKey=gen_privKey()

#generate password protected file
encrypted_bytes=save_key(privKey,privkey_path,privkey_password)

print('Private key generation complete') 
print('Private key encrypted and written to binary file:', privkey_path)
print(encrypted_bytes.hex())