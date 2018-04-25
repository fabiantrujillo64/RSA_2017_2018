def encrypt(e,n):
    message = ''
    encrypted_message = ''
    message = input('Please type your message:')
    for i in message:
        numerize = ord(i)
        encrypt = pow(numerize, e, n)
        denumerize = chr(encrypt)
        encrypted_message += denumerize

    print(encrypted_message)
    

def decrypt(d,n):
    decrypted_message = ''    
    encrypted_message= input("Hello, please type in the encrypted message:")
    for t in encrypted_message:
        print(t)
        numerize = ord(t)
        decrypt = pow(numerize,d,n)
        denumerize = chr(decrypt)
        decrypted_message += denumerize
        
    print(decrypted_message)


def run():
    initial_a = input("Hello, would you like to encrypt, decrypt, or exit?") 
    while initial_a!= "exit" and initial_a!= "Exit":
        if initial_a != "encrypt" and initial_a!= "decrypt" and initial_a!= "exit":
          initial_a = input("Hello, would you like to encrypt, decrypt, or exit?")
        else:
          if initial_a == "encrypt":
              e = int(input("What is your e value?"))
              n = int(input("What is your n value?"))            
              encrypt(e,n)
              initial_a = input("Hello, would you like to encrypt, decrypt, or exit?") 
          
          elif initial_a == "decrypt":
              d = int(input("What is your d value?"))
              n = int(input("What is your n value?"))           
              decrypt(d,n)
              initial_a = input("Hello, would you like to encrypt, decrypt, or exit?")
    print("Program Complete")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    