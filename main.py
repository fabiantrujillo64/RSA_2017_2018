import time
def encrypt(e,n):#public_key(n,e)
    message = ''
    encrypted_message = ''
    LUT_encryption = dict()
    message = input('Please type your message:')
    start = time.time()
    for i in message:
       if i in LUT_encryption:
        encrypted_message += LUT_encryption[i]
       else:  
          numerize = ord(i)
          encrypt = pow(numerize, e, n)
          denumerize = chr(encrypt)
          encrypted_message += denumerize

    print(encrypted_message)
    end = time.time()

    print(end - start)

def decrypt(d,n):
    decrypted_message = ''
    LUT_decryption = dict()
    encrypted_message= input("Hello, please type in the encrypted message:")
    start = time.time()
    for t in encrypted_message:
       if t in LUT_decryption:
        decrypted_message += LUT_decryption[t]
       else:
          print(t)
          numerize = ord(t)
          decrypt = pow(numerize,d,n)
          denumerize = chr(decrypt)
          decrypted_message += denumerize
        
    print(decrypted_message)
    end = time.time()

    print(end - start)


def run():
    initial_a = input("Hello, would you like to encrypt, decrypt, or exit?")
    initial_a = initial_a.lower()
    while initial_a!= "exit":
        if initial_a != "encrypt" and initial_a!= "decrypt" and initial_a!= "exit":
          initial_a = input("Hello, would you like to encrypt, decrypt, or exit?")
        else:
          if initial_a == "encrypt":
              try:
                e = int(input("What is your e value?"))
                n = int(input("What is your n value?"))            
                encrypt(e,n)
                initial_a = input("Hello, would you like to encrypt, decrypt, or exit?") 
              except:
                print("Invalid input. Please enter an integer. Let's start over")
             
          elif initial_a == "decrypt":
            try:
              d = int(input("What is your d value?"))
              n = int(input("What is your n value?"))           
              decrypt(d,n)
              initial_a = input("Hello, would you like to encrypt, decrypt, or exit?")
            except:
              print("Invalid input. Please enter an integer. Let's start over")
    print("Program Complete")
run()    