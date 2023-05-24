# RSA with list comprehension
import math
import secrets
import os
import string
from sympy import primerange
from sympy import mod_inverse

class Rsa():
  
  def __init__(self):
        self.prime_numbers = list(primerange(5, 700))

  def values(self, generate_primes, prime1, prime2):
    
      if generate_primes == 1:
        
          if prime1 not in self.prime_numbers or prime2 not in self.prime_numbers:
              os.system('cls')
              print("Invalid Primes")
              Rsa()
            
      elif generate_primes == 2:
          prime1 = secrets.choice(self.prime_numbers)
          prime2 = secrets.choice(self.prime_numbers)
          
      else:
        raise ValueError("Invalid Input")

      self.n_value = prime1 * prime2
      self.totient_value = (prime1 - 1) * (prime2 - 1)
      print(self.n_value, self.totient_value)
      
#------------------------------------------------------------------------------------------
  def public_key(self):
    # Public Key: Choose E: it must be coprime of T and N
    e_basis = range(2, self.totient_value)

    coprimes = []
    for e in e_basis:
      if math.gcd(e, self.totient_value) == 1 and math.gcd(e, self.n_value) == 1: # coprimes determinator
        coprimes.append(e)

    self.e_value = secrets.choice(coprimes) # randomly chooses a value in the list of of possible "e" values in "coprimes"
    self.copy_n_value = self.n_value # to avoid calling this value from various classes
    
    print(f"N: {self.n_value}")
    print(f"T: {self.totient_value}")
    print(f"E value: {self.e_value}")
    print(f"Public Key: ({self.e_value}, {self.n_value})\n")
    
#------------------------------------------------------------------------------------------
  def private_key(self):
    # Private Key: (D * E) % T == 1
    self.d_value = mod_inverse(self.e_value, self.totient_value) # finds the modular inverse
    print(f"D Value: {self.d_value}")
    print(f"Private Key: ({self.d_value}, {self.n_value})\n")

#------------------------------------------------------------------------------------------
  def encrypt_process(self): # ENCRYPTION: (plaintext ** e_value) % n_value
    plaintext_letter= (input("Original: "))
  
    strg_plaintext = [ord(letter) for letter in plaintext_letter] # `ord` function takes a single character from the plaintext and returns its Unicode code point as an integer
    self.strg_encrpt_val = [(value ** self.e_value) % self.n_value for value in strg_plaintext ] # performing the operation for encryption
    strg_encrpt_ltr = [chr(encrypt_val) for encrypt_val in self.strg_encrpt_val] # maps the corresponding character of a value in its Unicode point
    
    final_ciphtext = ''.join(map(str, strg_encrpt_ltr)) # joins the encrypted letters
    
    print(f"\nCipher Values: {self.strg_encrpt_val}")
    print(f"\nCiphertext List: {strg_encrpt_ltr}")
    print(f"\nCiphertext: {final_ciphtext}")

#------------------------------------------------------------------------------------------
  def decrypt_process(self):  # DECRYPTION: (ciphertext ** d_value) % n_value
    
    print("KEYS:")
    user_privatekey_d= int(input("   Private Key 1 (d): "))
    user_privatekey_n = int(input("  Private Key 2 (n): "))
    print(f"\n   Private Keys: ({user_privatekey_d}, {user_privatekey_n})\n")
    
    ciphertext = input("Ciphertext: ")
    storage_ciphtext = [ord(text) for text in ciphertext] # takes the each character in ciphertext and finds its corresponding value in Unicode point

    strg_dcrpt_val = [(ciphval ** user_privatekey_d) % user_privatekey_n for ciphval in storage_ciphtext]
    strg_dcrpt_ltr = [chr(decrypt_val) for decrypt_val in strg_dcrpt_val]
  
    print(f"\nPlainValues: {strg_dcrpt_val}")
    print(f"Plaintext: {strg_dcrpt_ltr}")
    
# EXCEPTION HANDLING-------------------------------------------------------------------------
def check_input(value): # checks whether the input is an integer or not
    
    try:
      user_input = int(input(value))
      
    except ValueError:
      os.system
      print("Invalid Input. INTEGERS only.")
    
    return user_input
  
# -------------------------------------------------------------------------------
def Encrypt_user(): # function for encryption
  print("Choose Primes: \n    1: Manually \n    2: Automatically")
  generate_primes = check_input("\n   Enter Here:  ")
  
  if generate_primes == 1:
      # Prompt the user to enter the primes
      prime1 = check_input("Enter the first prime: ")
      prime2 = check_input("Enter the second prime: ")
  else:
      prime1 = None
      prime2 = None
      
  encryption_object = Rsa()
  encryption_object.values(generate_primes, prime1, prime2)
  encryption_object.public_key()
  encryption_object.private_key()
  encryption_object.encrypt_process()

#----------------------------------------------------------------------------------
def  Decrypt_user():  # function for decryption
  decryption_object = Rsa()
  decryption_object.decrypt_process()

# -------------------------------------------------------------------------------
def rsa_home():
  print("Choose Action: \n    1: ENCODE\n    2: DECODE")
  user_action = int(input("\n    Enter Here: "))

  if user_action == 1:
    Encrypt_user()
    go_home()

  elif user_action == 2:
    Decrypt_user()
    go_home()
    
  else:
    os.system("cls")
    print("Invalid Option")
    go_home()
    
# -------------------------------------------------------------------------------
def go_home():
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