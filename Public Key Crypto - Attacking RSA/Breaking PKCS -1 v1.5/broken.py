ASN1_MAGIC = '003021300906052b0e03021a05000414'
def verify_rsa(sig_hex, message, public_key):
    """
    Verifies an RSA signature.
    inputs:
        sig_hex: a digital signature, in hexadecimal
        message: the message string to which sig_hex corresponds
        public_key: the public verification key (a Crypto.PublicKey.RSA._RSAobj value)
    output: true or false
    """
    sig_int = int(sig_hex , 16)
    m_int = pow(sig_int, public_key.e, public_key.n)
    m_hex = "%0512x" % m_int
    h = SHA.new(message).hexdigest()
    return re.match('0001f*' + ASN1_MAGIC + h, m_hex) is not None
