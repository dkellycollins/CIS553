import sys
from Crypto.Cipher import DES


def main(args):
    try:
        plain_text = args[1].decode("hex")
        key = args[0].decode("hex")
        cipher_text = encrypt(plain_text, key)
        print cipher_text.encode("hex").upper()
    except:
        print "Unexpected error:", sys.exc_info()[0], sys.exc_info()[1]

#Encrypts the plain test using Double DES
def encrypt(plain_text, key):
    key1 = key[:7]
    key2 = key[7:]
    #Round 1
    cipher = DES.new(key1, DES.MODE_ECB)
    cipher_text = cipher.encrypt(plain_text)
    #Round 2
    cipher = DES.new(key2, DES.MODE_ECB)
    cipher_text = cipher.encrypt(cipher_text)
    return cipher_text

#Decrypts the cipher test using DES
def decrypt(cipher_text, key):
    key1 = key[:7]
    key2 = key[7:]
    #Round 1
    cipher = DES.new(key2, DES.MODE_ECB)
    plain_text = cipher.decrypt(cipher_text)
    #Round 2
    cipher = DES.new(key1, DES.MODE_ECB)
    plain_text = cipher.decrypt(plain_text)
    return plain_text

#Starts the program.
if __name__ == "__main__":
    main(sys.argv[1:])
