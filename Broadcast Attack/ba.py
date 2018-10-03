import sys
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256
import tools
import codecs

#publickey1 to int
file_pubkey1 = open(sys.argv[1], 'r')
publickey1 = file_pubkey1.read()
file_pubkey1.close()
pk1 = RSA.importKey(publickey1,None)


#publickey2 to int
file_pubkey2 = open(sys.argv[2], 'r')
publickey2 = file_pubkey2.read()
file_pubkey2.close()
pk2 = RSA.importKey(publickey2,None)



#publickey3 to int
file_pubkey3 = open(sys.argv[3], 'r')
publickey3 = file_pubkey3.read()
file_pubkey3.close()
pk3 = RSA.importKey(publickey3,None)



#ciphertext1 to int
file_cipher1 = open(sys.argv[4], 'r')
ciphertext1 = file_cipher1.read()
file_cipher1.close()
ciphertext1_int = ''.join(x for x in ciphertext1 if x.isdigit())



#ciphertext2 to int
file_cipher2 = open(sys.argv[5], 'r')
ciphertext2 = file_cipher2.read()
file_cipher2.close()
ciphertext2_int = ''.join(x for x in ciphertext2 if x.isdigit())



#ciphertext3 to int
file_cipher3 = open(sys.argv[6], 'r')
ciphertext3 = file_cipher3.read()
file_cipher3.close()
ciphertext3_int = ''.join(x for x in ciphertext3 if x.isdigit())



#main part
cm1 = tools.combine_moduli(pk1.n,pk3.n,int(ciphertext1_int),int(ciphertext3_int))
cm2 = tools.combine_moduli(pk1.n*pk3.n,pk2.n,int(cm1),int(ciphertext2_int))
message1 = tools.find_root(int(cm2),3)
message1_words = tools.int_to_text(message1)
print "The message is: " + message1_words