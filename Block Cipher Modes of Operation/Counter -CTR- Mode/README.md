# Counter (CTR) Mode of operation

In Counter Mode - A random initialization vector IV is chosen and IV, IV+1, IV+2 etc. is fed to the block cipher encyption to produce a stream of random-looking bits to XOR the message with.
Counter Mode is CPA-Secure. 
In the program we use the AES in CTR mode ciphertext: CTR_ciphertext and the IV: CTR_iv.
We know that the ciphertext encrypts a four digit number n that is a multiple of 10. 
To find a ciphertext (using the same IV) encrypting n+5. 

## Example
### Input:
python CTR_solution.py CTR_ciphertext CTR_iv

### Output:
The new ciphertext is 941b3b25eda87cac89af30f78e4cd32e.
