#!/usr/bin/python

import sys
from Crypto.Cipher import AES
from Crypto import Random
from Crypto.Util import Counter

def pad(s):

    return s + b"\0" * (AES.block_size - len(s) % AES.block_size)

length = len(sys.argv)
commandargs = str(sys.argv)

file_cipher = open(sys.argv[1], 'rb')
ciphertext = file_cipher.read()
file_cipher.close()

file_iv = open(sys.argv[2], 'r')
iv = file_iv.read()
file_cipher.close()


key = Random.new().read(16)
ctr = Counter.new(128, initial_value=long(iv, 16))
cipher = AES.new(key, AES.MODE_CTR, counter=ctr)
print "The new cipher text=", cipher.encrypt(pad(ciphertext))

