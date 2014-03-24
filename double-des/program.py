import sys
from Crypto.Cipher import DES


def main(args):
    try:
        plain_text = args[1].decode("hex")
        key = parse_key_input(args[0])
        cipher_text = encrypt(plain_text, key[0])
        cipher_text = encrypt(cipher_text, key[1])
        print cipher_text.encode("hex").upper()
    except:
        print "Unexpected error:", sys.exc_info()[0], sys.exc_info()[1]

#Splits and decodes the key input.
def parse_key_input(input_key):
    output_key = [input_key[:16], input_key[16:]]
    output_key[0] = parse_key(output_key[0].decode("hex"))
    output_key[1] = parse_key(output_key[1].decode("hex"))
    return output_key

#Adds parity bits to the given key.
def parse_key(input_key):
    return input_key

#Encrypts the plain test using DES
def encrypt(plain_text, key):
    cipher = DES.new(key, DES.MODE_ECB)
    cipher_text = cipher.encrypt(plain_text)
    return cipher_text

#Decrypts the cipher test using DES
def decrypt(cipher_text, key):
    cipher = DES.new(key, DES.MODE_ECB)
    plain_text = cipher.decrypt(cipher_text)
    return plain_text

#Starts the program.
if __name__ == "__main__":
    main(sys.argv[1:])
