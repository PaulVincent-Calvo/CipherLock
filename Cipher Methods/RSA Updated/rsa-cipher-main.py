import math
import secrets
import os
from sympy import primerange
from sympy import mod_inverse

class Rsa():
  
  def prime_generator(self):
    os.system('cls')
    print("Choose Primes: \n    1: Manually \n    2: Automatically")
    prime_numbers = list(primerange(5, 700)) # generates a list of prime numbers from 5 to 700
    
    while True:
      generate_primes = int(input("\n   Enter Here:  ")) # using the function check_input
    
      if generate_primes == 1:
          # Prompt the user to enter the primes
          while True:
            self.prime1 = int(input("\n\tEnter the first prime: "))
            self.prime2 = int(input("\tEnter the second prime: "))
    
            if self.prime1 not in prime_numbers or self.prime2 not in prime_numbers:
                os.system('cls')
                print("Invalid Primes")
              
            else:
                break
    
          break # breaks the loop when once the condition is satisfied
            
      elif generate_primes == 2:
          self.prime1 = secrets.choice(prime_numbers)
          self.prime2 = secrets.choice(prime_numbers)
          break
        
      else:
        print("\n\tInvalid Input")

    # Important Values
    self.n_value = self.prime1 * self.prime2
    self.totient_value = (self.prime1 - 1) * (self.prime2 - 1)
      
      
  def public_key(self): # Public Key: Choose E: it must be coprime of T and N
    e_basis = range(2, self.totient_value)

    coprimes = []
    for e in e_basis:
      if math.gcd(e, self.totient_value) == 1 and math.gcd(e, self.n_value) == 1: # coprimes determinator
        coprimes.append(e)

    self.e_value = secrets.choice(coprimes) # randomly chooses a value in the list of of possible "e" values in "coprimes"
    
  def dipslay_pubkey(self):
    print(f"\n\tPublic Key: ({self.e_value}, {self.n_value})\n")
  
#----------------------------------------------------------------------------
   
  def private_key(self):  # Condition: (D * E) % T == 1
    self.d_value = mod_inverse(self.e_value, self.totient_value) # finds the modular inverse
  
  def dipslay_privkey(self):
    print(f"\tPrivate Key: ({self.d_value}, {self.n_value})\n")



#----------------------------------------------------------------------------
  def encrypt_process(self): # Formula: (plaintext ** e_value) % n_value
    os.system('cls')
    plaintext_letter= (input("Plaintext: "))
  
    strg_plaintext = [ord(letter) for letter in plaintext_letter] # `ord` function takes a single character from the plaintext and returns its Unicode code point as an integer
    self.strg_encrpt_val = [(value ** self.e_value) % self.n_value for value in strg_plaintext ] # performing the operation for encryption
    strg_encrpt_ltr = [chr(encrypt_val) for encrypt_val in self.strg_encrpt_val] # maps the corresponding character of a value in its Unicode point
    
    self.final_ciphtext = ''.join(map(str, strg_encrpt_ltr)) # joins the encrypted letters
  
  def dipslay_ciphertext(self):
    print(f"\nCiphertext: {self.final_ciphtext}")

#------------------------------------------------------------------------------------------
  def decrypt_process(self):  # DECRYPTION: (ciphertext ** d_value) % n_value
    
    print("KEYS:")
    user_privatekey_d = int(input("   Private Key 1 (d): "))
    user_privatekey_n = int(input("   Private Key 2 (n): "))
    print(f"\n   Private Keys: ({user_privatekey_d}, {user_privatekey_n})\n")
    
    ciphertext = input("Ciphertext: ")
    storage_ciphtext = [ord(text) for text in ciphertext] # takes the each character in ciphertext and finds its corresponding value in Unicode point

    strg_dcrpt_val = [(ciphval ** user_privatekey_d) % user_privatekey_n for ciphval in storage_ciphtext]
    self.strg_dcrpt_ltr = [chr(decrypt_val) for decrypt_val in strg_dcrpt_val]
  
  def dipslay_plaintext(self):
    print(f"\nPlaintext: {self.strg_dcrpt_ltr}")
 
  
  
def Encrypt_user(): # function for encryption
  encryption_object = Rsa()
  encryption_object.prime_generator()
  encryption_object.public_key()
  encryption_object.private_key()
  encryption_object.dipslay_pubkey()
  encryption_object.dipslay_privkey()
  encryption_object.encrypt_process()
  encryption_object.dipslay_ciphertext()


def Decrypt_user():  # function for decryption
  decryption_object = Rsa()
  decryption_object.decrypt_process()
  decryption_object.dipslay_plaintext()


def rsa_home(): # main home
  print("Choose Action: \n    1: ENCRYPT\n    2: DECRYPT")
  user_action = int(input("\n    Enter Here: "))

  if user_action == 1:
    Encrypt_user()
    go_home()

  elif user_action == 2:
    os.system('cls')
    Decrypt_user()
    go_home()
    
  else:
    os.system("cls")
    print("Invalid Option")
    go_home()
    
    
def go_home(): # function for going back to home
  while True:
    print("\n\n1: Home")
    user_home = int(input("    Enter 1: "))
    
    if user_home == 1:
      os.system('cls')
      rsa_home()
      break
    
    else:
      print("Enter Again")

rsa_home()
