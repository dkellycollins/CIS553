import sys
import string
from Crypto.Cipher import DES
from Crypto import Random


def main(args):
    try:
        plain_text = args[1].decode("hex")
        key = parse_key(args[0])
        print key
        cipher_text = encrypt(plain_text, key[0])
        cipher_text = encrypt(cipher_text, key[1])
        print cipher_text.encode("hex")
    except:
        print "Unexpected error:", sys.exc_info()[0], sys.exc_info()[1]





def parse_key(input_key):
    output_key = ["\x01" + input_key[:14].decode("hex"), "\x01" + input_key[14:].decode("hex")]
    #output_key = [input_key[:14].decode("hex") + "\x01", input_key[14:].decode("hex") + "\x01"]
    return output_key


def encrypt(plain_text, key):
    cipher = DES.new(key, DES.MODE_ECB)
    cipher_text = cipher.encrypt(plain_text)
    return cipher_text

def decrypt(cipher_text, key):
    cipher = DES.new(key, DES.MODE_ECB)
    plain_text = cipher.decrypt(cipher_text)
    return plain_text

#Starts the program.
if __name__ == "__main__":
    main(sys.argv[1:])
