import sys
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256
import tools


file_pubkey = open(sys.argv[1], 'r')
publickey = file_pubkey.read()
file_pubkey.close()

pubkey= RSA.importKey(publickey,None)
file_cipher = open(sys.argv[2], 'r')
ciphertextmain = file_cipher.read()
file_cipher.close()

file_msg = open(sys.argv[3], 'r')
msglist = file_msg.read()
file_msg.close()

msgs = msglist.split("\n")

for message in msgs:
	message_int = tools.text_to_int(message)
	ciphertext = pubkey.encrypt(message_int, None)
	if(str(ciphertextmain) == str(ciphertext)):
		print "the message is : " + message