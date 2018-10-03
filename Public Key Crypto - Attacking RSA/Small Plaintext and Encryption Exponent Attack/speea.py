import sys
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256
import tools

file_cipher = open(sys.argv[1], 'r')
ciphertext = file_cipher.read()
file_cipher.close()

ciphertext_int = ''.join(x for x in ciphertext if x.isdigit())

#finding answer
message = tools.find_root(int(ciphertext_int),3)
message_words = tools.int_to_text(message)
print "The message is: " + message_words
