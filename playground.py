import time

n = 21971
e = 131
d = 17867

message = "Hello World!"
encrypted_message = ""
decrypted_message = ""

start = time.time()
########Encryption########
for i in message:
    numerize = ord(i)
    encrypt = pow(numerize, e, n)
    denumerize = unichr(encrypt)
    encrypted_message += denumerize

print encrypted_message

########Decryption########
for t in encrypted_message:
    numerize = ord(t)
    decrypt = pow(numerize,d,n)
    denumerize = chr(decrypt)
    decrypted_message += denumerize
    
print decrypted_message
end = time.time()

print(end - start)    

encrypted_message2 = ""
decrypted_message2 = ""
LUT_encryption = dict()
LUT_decryption = dict()

start = time.time()
########Encryption V2########
for i in message:
    if i in LUT_encryption:
        encrypted_message2 += LUT_encryption[i]
    else:
        numerize = ord(i)
        encrypt = pow(numerize, e, n)
        denumerize = unichr(encrypt)
        encrypted_message2 += denumerize
        LUT_encryption[i] = denumerize

print encrypted_message2


########Decryption V2########
for t in encrypted_message2:
    if t in LUT_decryption:
        decrypted_message2 += LUT_decryption[t]
    else:
        numerize = ord(t)
        decrypt = pow(numerize,d,n)
        denumerize = chr(decrypt)
        decrypted_message2 += denumerize
        LUT_decryption[t] = denumerize
        
print decrypted_message2
end = time.time()

print(end - start)  























