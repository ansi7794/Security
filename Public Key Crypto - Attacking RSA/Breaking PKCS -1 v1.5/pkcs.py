import sys
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256, SHA
import tools
import re

def pad(s):
	return "0001" + "ff" + s + "ff"*217

ASN1_MAGIC = "003021300906052b0e03021a05000414"
def verify_rsa(sig_hex, message, public_key):
	sig_int = int(sig_hex, 16)
	m_int = pow(sig_int, public_key.e, public_key.n)
	m_hex = "%0512x" % m_int
	h = SHA.new(message).hexdigest()
	return re.match('0001f*' + ASN1_MAGIC + h, m_hex) is not None

#publickey to int
file_pubkey = open(sys.argv[1], 'r')
publickey = file_pubkey.read()
file_pubkey.close()
pubkey= RSA.importKey(publickey,None)

#input message
message = sys.argv[2]

h = SHA.new(message).hexdigest()
sign1 = pad(ASN1_MAGIC+h)
sign_int = int(sign1, 16)
sign_hex = "%0512x" % sign_int
sign = (tools.find_root(sign_int,3))%pubkey.n

ver = verify_rsa(format(sign,'x'),message,pubkey)
if ver == True:
	print "Successfully forged a signature on " + "'" + message + "'"
	print format(sign,'x')
else:
	print "Not Successful"