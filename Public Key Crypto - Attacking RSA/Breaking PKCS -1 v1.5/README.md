# Breaking PKCS #1 v1.5

When PKSC #1 v1.5 is used, an RSA signature on the following padded message hash is generated. 

 00  01  |   FF....FF  |   00 | 3021300906052B0E03021A05000414     |    XX....XX 
 ------- | ----------- |  ---- |------- |------- 
 | k/8 - 38 bytes   |      | ASN.1 "magic" bytes   |    20-byte SHA-1 digest |


When PKCS padding is used, it is important for implementations to verify that every bit of the padded, signed message is exactly as it should be. It is tempting for an implementor to validate the signature by first stripping off the 00 01 bytes, then some number of padding FF bytes, then 00, and then parse the ASN.1 and verify the hash. If the implementation does not check the length of the FF bytes and that the hash is in the least significant bits of the message, then it the public verification exponent e is low, is possible for an attacker to forge values that pass this validation check.

If the length of the required padding, ASN.1 bytes, and hash value is significantly less than n^(1/3) then an attacker can construct a cube root over the integers whose most significant bits will validate as a correct signature, ignoring the actual key. To construct a forged signature that will validate against such implementations, an attacker simply needs to construct an integer whose most significant bytes have the correct format, including the hashed message, pad the remainder of this value with zeros or other garbage that will be ignored by the vulnerable implementation, and then take a cube root over the integers, rounding as appropriate.

Alice uses a broken implementation of signature verification given in the code: broken.py

We have Bob's public verification key and we write a program to use signature forgery technique and produce an RSA signature on the message “retreat immediately" that will be accepted by Alice.

## Example:
### Input:
python pkcs.py pkey.pub 'retreat immediately!'

### Output:
###### Successfully forged a signature on 'retreat immediately!':
###### 000000000000000000000000000000000000000000000000000000000
###### 000000000000000000000000000000000000000000000000000000000
###### 000000000000000000000000000000000000000000000000000000000
###### 000000000000000000000000000000000000000000000000000000000
###### 000000000000000000000000000000000000000000000000000000000
###### 000000000000000000000000000000000000000000000000000000000
###### 2853cc9cf8c785651a3f5dcdea7c4ff005af90887d7c0fbaba09a4cf1
###### 5276fe10d4cffe86db8fcc7efa92ab0138eff20b6c1eb175728afa269
###### 36a4f00aabad04939057c5f363409ba0a28b3e1b5716d088f673e161
