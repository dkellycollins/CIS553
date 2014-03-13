import sys
from Crypto.Cipher import AES


def main(args):
    try:
        plain_text = args[0]
        key = args[1]
        cipher_text = encrypt(plain_text, key)
        print cipher_text
    except:
        print "Unexpected error:", sys.exc_info()[0]


def encrypt(plain_text, key):
    obj = AES.new(key, AES.MODE_ECB)
    cipher_text = obj.encrypt(plain_text)
    return cipher_text

#Starts the program.
if __name__ == "__main__":
    main(sys.argv[1:])
