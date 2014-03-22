import sys
import string
from Crypto.Cipher import DES
from Crypto import Random


def main(args):
    try:
        plain_text = args[0]
        cipher_text = args[1]
        partial_key = args[2]
    except:
        print "Unexpected error:", sys.exc_info()[0], sys.exc_info()[1]


#Starts the program.
if __name__ == "__main__":
    main(sys.argv[1:])