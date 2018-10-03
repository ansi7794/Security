# Broadcast Attack

Alice sends a message to three people. All of them have the same low  low encryption exponent, *e* = 3. All of them have different public keys. 
Use the fact that all three ciphertexts use the same low encryption exponent to figure out what the message.
_Hint: Use the provided function combine_moduli in tools.py._
This program takes in 3 public keys and 3 ciphertexts and outputs the message.

## Example: 
### Input:
$ python ba.py pkey1.pub pkey2.pub pkey3.pub ctext1 ctext2 ctext3

### Output:
The message is 'xxxxx'.
