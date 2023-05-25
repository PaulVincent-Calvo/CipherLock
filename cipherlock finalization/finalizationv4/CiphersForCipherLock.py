import string
import re
import numpy as np
import sys
import math
import secrets
import os
from sympy import primerange
from sympy import mod_inverse

class shift_cipher():

    def __init__ (self, user_message, cipher_key):
        self.cipher_key = cipher_key
        self.user_message = user_message        

    def shift_cipher_encryption (self, user_message):
        characters = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation + " "
        encrypted_message = ""

        # replaces multiple spaces to a single space
        user_message = re.sub(" +", " ", user_message)

        # makes a translation table using the maketrans function from string library
        # first parameter is the list of characters to be changed and the second parameter is the list of characters sliced based on the key 
        translation_table = str.maketrans(characters, characters[self.cipher_key:]+characters[:self.cipher_key])
        
        # encrypts (translates) the message using the translation table created earlier
        encrypted_message = user_message.translate(translation_table)

        #print(user_message)
        return encrypted_message
    
    def shift_cipher_decryption (self, user_message):
        characters = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation + " "
        decrypted_message = "" 

        n = int(len(characters))

        shift_cipher_decryption_key = n - self.cipher_key

        # multiple spaces not replaced to a single space because it may be intentional as spaces are part of the translation table

        translation_table = str.maketrans(characters, characters[shift_cipher_decryption_key:]+characters[:shift_cipher_decryption_key])
        
        # translated message
        decrypted_message = user_message.translate(translation_table)

        #print(user_message)
        return decrypted_message

# caesar cipher inherits from shift cipher because it is just a shift cipher that has a fixed shift key of 3
class caesar_cipher (shift_cipher):

    def __init__ (self, user_message):
        self.cipher_key = 3
        self.user_message = user_message

# vigenere cipher inherits from shift cipher because it is a modified shift cipher wherein every letter in a text is encrypted/decrypted using a different key depending on how many keys the user wanted to use
class vigenere_cipher (shift_cipher):
    
    def __init__(self, user_message, cipher_key = None):
        super().__init__(user_message, cipher_key)

    def vigenere_cipher_encryption (self, user_message):
        encrypted_message = "" 

        # validate the number of keys input
        while True:
            try:
                no_of_keys = int(input("How many keys do you want to use: "))
                if no_of_keys > 0 and no_of_keys <= len(user_message):
                    break
                else:
                    print("Number of keys should be greater than 0 and less than or equal to the length of the message you want to encrypt")
            except ValueError:
                print("Invalid input. Please enter an integer.")

        list_of_keys = []
        for i in range (no_of_keys):
            # validate the keys input
            while True:
                try:
                    key = int(input(f"Key [{i+1}]: "))
                    list_of_keys.append(key)
                    break
                except ValueError:
                    print("Invalid input. Please enter an integer.")

        for i, char in enumerate(user_message):
            self.cipher_key = int(list_of_keys[i % len(list_of_keys)]) 
            user_message_for_enc = str(char)
            encrypted_message += super().shift_cipher_encryption (user_message_for_enc)

        return encrypted_message
    
    def vigenere_cipher_decryption (self, user_message):
        decrypted_message = "" 

        while True:
            try:
                no_of_keys = int(input("How many keys do you want to use: "))
                if no_of_keys > 0 and no_of_keys <= len(user_message):
                    break
                else:
                    print("Number of keys should be greater than 0 and less than or equal to the length of the message you want to decrypt")
            except ValueError:
                print("Invalid input. Please enter an integer.")

        list_of_keys = []
        for i in range (no_of_keys):
            # validate the keys input
            while True:
                try:
                    key = int(input(f"Key [{i+1}]: "))
                    list_of_keys.append(key)
                    break
                except ValueError:
                    print("Invalid input. Please enter an integer.")

        for i, char in enumerate(user_message):
            self.cipher_key = int(list_of_keys[i % len(list_of_keys)]) 
            user_message_for_enc = str(char)
            decrypted_message += super().shift_cipher_decryption (user_message_for_enc)

        return decrypted_message
    
class base64_cipher():
    def __init__ (self, user_message):  
        self.user_message = user_message

    def base64_cipher_encryption (self, user_message):
        base64chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
        ending = ''
        encoded = ''

        # Convert the Phrase "user_message" into 8-bit binary
        chunks_8bit = ''
        if type(user_message) is str:
            for c in user_message:
                chunks_8bit += '{:08b}'.format(ord(c))

        elif type(user_message) is bytes:
            for c in user_message:
                chunks_8bit += '{:08b}'.format(c)

        # Adding zero bits at the end if needed
        if len(user_message) % 3 == 1:
            chunks_8bit += '0000'
            ending += '=='

        if len(user_message) % 3 == 2:
            chunks_8bit += '00'
            ending += '='

        # Extracting the 8-bits into 6-bit chunks and converting it to a number
        # using the 'base64chars' index to fully encode
        for i in range(0, len(chunks_8bit), 6):
            index = int(chunks_8bit[i:i+6], 2)
            encoded += base64chars[index]

        encoded += ending
        return encoded

    def base64_cipher_decryption (self, user_message):

        s = user_message
        i = 0
        base64 = decoded = ''
        base64chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'


        # Replace padding with "A" characters so the decoder can process the string, and save the padding length for later
        if user_message[-2:] == '==':
            s = user_message[0:-2] + "AA"
            padd = 2
        elif user_message[-1:] == '=':
            s = user_message[0:-1] + "A"
            padd = 1
        else:
            padd = 0

        # Take 4 characters at a time 
        while i < len(s):
            d = 0
            for j in range(0,4,1):
                d += base64chars.index( s[i] ) << (18 - j * 6)
                i += 1

            # Convert the 4 chars back to ASCII
            decoded += chr( (d >> 16 ) & 255 )
            decoded += chr( (d >> 8 ) & 255 )
            decoded += chr( d & 255 )

        # Remove padding
        decoded = decoded[0:len( decoded ) - padd]
        return decoded

class hill_cipher():
    def __init__ (self, user_message, cipher_key):
        self.cipher_key = cipher_key
        self.user_message = user_message

    def hill_cipher_encryption(self, user_message, cipher_key):
        msg = str(user_message)
        msg = msg.upper().replace(" ", "")

        # If the length of the message is odd, append 0 at the end
        len_chk = 0
        if len(msg) % 2 != 0:
            msg += "0"
            len_chk = 1

        # Putting the Message into Matrices
        row = 2
        col = int(len(msg)/2)
        msg2d = np.zeros((row, col), dtype=int)

        itr1 = 0
        itr2 = 0
        for i in range(len(msg)):
            if i % 2 == 0:
                msg2d[0][itr1] = int(ord(msg[i])-65)
                itr1 += 1
            else:
                msg2d[1][itr2] = int(ord(msg[i])-65)
                itr2 += 1
        
        key = str(cipher_key)
        key = key.upper().replace(" ", "")

        # Key
        key2d = np.zeros((2, 2), dtype=int)
        itr3 = 0
        for i in range(2):
            for j in range(2):
                key2d[i][j] = ord(key[itr3])-65
                itr3 += 1

        # Validity Check of the Key
        # Finding The Determinant
        deter = key2d[0][0] * key2d[1][1] - key2d[0][1] * key2d[1][0]
        deter = deter % 26

        # Finding The Multiplicative Inverse
        mul_inv = -1
        for i in range(26):
            temp_inv = deter * i
            if temp_inv % 26 == 1:
                mul_inv = i
                break
            else:
                continue

        if mul_inv == -1:
            print("Brother, I think you used the wrong key. Please, try again.")
            sys.exit()
    
        encrypted_message = ""
        itr_count = int(len(msg)/2)
        if len_chk == 0:
            for i in range(itr_count):
                temp1 = msg2d[0][i] * key2d[0][0] + msg2d[1][i] * key2d[0][1]
                encrypted_message += chr((temp1 % 26) + 65)
                temp2 = msg2d[0][i] * key2d[1][0] + msg2d[1][i] * key2d[1][1]
                encrypted_message += chr((temp2 % 26) + 65)
    
        else:
            for i in range(itr_count-1):
                temp1 = msg2d[0][i] * key2d[0][0] + msg2d[1][i] * key2d[0][1]
                encrypted_message += chr((temp1 % 26) + 65)
                temp2 = msg2d[0][i] * key2d[1][0] + msg2d[1][i] * key2d[1][1]
                encrypted_message += chr((temp2 % 26) + 65)
        return encrypted_message

    def hill_cipher_decryption(self, user_message, cipher_key):
        msg = str(user_message)
        msg = msg.replace(" ", "").upper()

        # If the length of the message is odd, append 0 at the end
        len_chk = 0
        if len(msg) % 2 != 0:
            msg += "0"
            len_chk = 1

        # Putting the Message Into Matrices
        row = 2
        col = int(len(msg) / 2)
        msg2d = np.zeros((row, col), dtype=int)

        itr1 = 0
        itr2 = 0
        for i in range(len(msg)):
            if i % 2 == 0:
                msg2d[0][itr1] = int(ord(msg[i]) - 65)
                itr1 += 1
            else:
                msg2d[1][itr2] = int(ord(msg[i]) - 65)
                itr2 += 1

        key = str(cipher_key)
        key = key.replace(" ", "").upper()

        # Key
        key2d = np.zeros((2, 2), dtype=int)
        itr3 = 0
        for i in range(2):
            for j in range(2):
                key2d[i][j] = ord(key[itr3]) - 65
                itr3 += 1

        # Finding The Determinant
        deter = key2d[0][0] * key2d[1][1] - key2d[0][1] * key2d[1][0]
        deter = deter % 26

        # Finding The Multiplicative Inverse
        mul_inv = -1
        for i in range(26):
            temp_inv = deter * i
            if temp_inv % 26 == 1:
                mul_inv = i
                break
            else:
                continue

        # Adjugate Matrix
        # Swapping
        key2d[0][0], key2d[1][1] = key2d[1][1], key2d[0][0]

        # Changing The Signs
        key2d[0][1] *= -1
        key2d[1][0] *= -1

        key2d[0][1] = key2d[0][1] % 26
        key2d[1][0] = key2d[1][0] % 26

        # Multiplying The Multiplicative Inverse with the Adjugate Matrix
        for i in range(2):
            for j in range(2):
                key2d[i][j] *= mul_inv

        # Modulo
        for i in range(2):
            for j in range(2):
                key2d[i][j] = key2d[i][j] % 26

        # Decrypting the Text
        decrypted_message = ""
        itr_count = int(len(msg) / 2)
        if len_chk == 0:
            for i in range(itr_count):
                temp1 = msg2d[0][i] * key2d[0][0] + msg2d[1][i] * key2d[0][1]
                decrypted_message += chr((temp1 % 26) + 65)
                temp2 = msg2d[0][i] * key2d[1][0] + msg2d[1][i] * key2d[1][1]
                decrypted_message += chr((temp2 % 26) + 65)
                # for
        else:
            for i in range(itr_count - 1):
                temp1 = msg2d[0][i] * key2d[0][0] + msg2d[1][i] * key2d[0][1]
                decrypted_message += chr((temp1 % 26) + 65)
                temp2 = msg2d[0][i] * key2d[1][0] + msg2d[1][i] * key2d[1][1]
                decrypted_message += chr((temp2 % 26) + 65)

        return decrypted_message
    
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
            self.prime1 = check_input("\n\tEnter the first prime: ")
            self.prime2 = check_input("\tEnter the second prime: ")
            
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
  
  def private_key(self):  # Condition: (D * E) % T == 1
    self.d_value = mod_inverse(self.e_value, self.totient_value) # finds the modular inverse
  
  def dipslay_privkey(self):
    print(f"\tPrivate Key: ({self.d_value}, {self.n_value})\n")

  def encrypt_process(self): # Formula: (plaintext ** e_value) % n_value
    #os.system('cls')
    plaintext_letter= (input("Plaintext: "))
  
    strg_plaintext = [ord(letter) for letter in plaintext_letter] # `ord` function takes a single character from the plaintext and returns its Unicode code point as an integer
    self.strg_encrpt_val = [(value ** self.e_value) % self.n_value for value in strg_plaintext ] # performing the operation for encryption
    strg_encrpt_ltr = [chr(encrypt_val) for encrypt_val in self.strg_encrpt_val] # maps the corresponding character of a value in its Unicode point
    
    self.final_ciphtext = ''.join(map(str, strg_encrpt_ltr)) # joins the encrypted letters
  
  def dipslay_ciphertext(self):
    print(f"\nCiphertext: {self.final_ciphtext}")

  def decrypt_process(self):  # DECRYPTION: (ciphertext ** d_value) % n_value
    
    print("KEYS:")
    user_privatekey_d = int(input("   Private Key 1 (d): "))
    user_privatekey_n = int(input("   Private Key 2 (n): "))
    print(f"\n   Private Keys: ({user_privatekey_d}, {user_privatekey_n})\n")
    
    ciphertext = input("Ciphertext: ")
    storage_ciphtext = [ord(text) for text in ciphertext] # takes the each character in ciphertext and finds its corresponding value in Unicode point

    strg_dcrpt_val = [(ciphval ** user_privatekey_d) % user_privatekey_n for ciphval in storage_ciphtext] # performing the operation for decryption
    self.strg_dcrpt_ltr = [chr(decrypt_val) for decrypt_val in strg_dcrpt_val]  # maps the corresponding character of a value in its Unicode point
      
  def dipslay_plaintext(self):
    print(f"\nPlaintext: {self.strg_dcrpt_ltr}")

def check_input(value): # function that checks whether the input is an integer or not
    while True:
        try:
            user_input = int(input(value))
            break
          
        except ValueError:
            print("\nInvalid Input. INTEGERS only.")
    
    return user_input

class Matrix_inverse():

    def __init__(self):

        first_char = np.array(['$']) # filler/placeholder character
        alphabet = np.array(['a','b','c','d','e','f','g','h','i','j',
                                    'k','l','m','n','o','p','q','r','s','t',
                                    'u','v','w','x','y','z','_'])

        self.alphabet = np.concatenate((first_char, np.tile(alphabet, 50))) # used to join the first character array with 50 copies of the alphabet array. This results in an array of 1300 characters (26 letters + 1 underscore) repeated 50 times, with $ as the first character.
       
    def select_size(self):
        print("Choose Size of the Matrix:")
        print("\t2). 2 x 2\n\t3). 3 x 3\n\t4). 4 x 4\n\t5). 5 x 5\n\t6). 6 x 6\n\t7). 7 x 7\n\t8). 8 x 8\n\t9). 9 x 9\n")
        
        while True:

            try:
                self.matrix_size = int(input("\tEnter Here: "))

                if (self.matrix_size) == 2:
                    self.matrix_basis = np.array([[12,24],[3,4]])
                    break

                if (self.matrix_size) == 3:
                    self.matrix_basis = np.array([[1,9,8],[20,10,2],[5,1,11]])
                    break

                if (self.matrix_size) == 4:
                    self.matrix_basis = np.array([[10, 87, 3, 23],[1, 100, 34, 65],[66, 69, 5, 8],[90, 2, 45, 11]])
                    break

                if (self.matrix_size) == 5:
                    self.matrix_basis = np.array([[66, 7, 78, 21, 43],[1, 99, 56, 34, 32],[7, 76, 23, 32, 98],[9, 66, 88, 12, 43], [6, 54, 76, 89, 13]])
                    break

                if (self.matrix_size) == 6:
                    self.matrix_basis = np.array([[99, 81, 2, 36, 17, 13],[1, 90, 65, 22, 34, 79],[3, 56, 87, 92, 13, 29],[46, 33, 72, 4, 6, 1], [23, 99, 12, 8, 28, 67],[88, 66, 9, 11, 83, 5]])
                    break

                if (self.matrix_size) == 7:
                    self.matrix_basis = np.array([[80, 12, 45, 23, 88, 6, 90],[1, 33, 78, 99, 34 , 56, 21],[9, 59, 32, 53 , 67, 75, 23],[6, 73, 84, 23, 12, 65, 87], [87, 34, 88, 43, 34, 11, 43],[82, 2, 56, 64, 75, 32, 4],[87, 43, 88, 99, 23, 54, 8]])
                    break

                if (self.matrix_size) == 8:
                    self.matrix_basis = np.array([[8, 13, 3, 29, 10, 21, 18, 1],[7, 22, 29, 20, 15, 22, 27, 12],[12, 28, 2, 33, 19, 23, 13, 10],[1, 21, 15, 23, 16, 22, 37, 28], [19, 28, 37, 14, 19, 26, 6, 14],[12, 2, 16, 24, 15, 2, 4, 12],[15, 17, 23, 28, 19, 23, 24, 8],[11, 25, 12, 16, 22, 28, 15, 23]])
                    break

                if (self.matrix_size) == 9:
                    self.matrix_basis = np.array([[29, 29, 6, 15, 18, 28, 23, 5, 9], [28, 27, 28, 5, 7, 21, 28, 6, 26], [14, 3, 8, 7, 12, 21, 18, 5, 20], [28, 4, 14, 5, 7, 4, 29, 13, 12], [8, 5, 23, 25, 26, 5, 13, 15, 3], [9, 27, 29, 8, 27, 10, 10, 29, 23], [2, 20, 9, 10, 25, 11, 24, 16, 23], [16, 8, 22, 18, 24, 19, 19, 19, 21], [6, 29, 22, 12, 25, 11, 27, 27, 6]]) 
                    break

                else:
                    print("\nVALUE ERROR")
            
            except ValueError:
                print("\nInvalid Input\n")
     
    def process_encode(self): # ENCODING PROCESS
      os.system('cls')
      print(f"NOTE:\n    The number of characters/value must be equal to the number of elements of the array size that you chose.\n\tEx. {self.matrix_size} x {self.matrix_size} ({self.matrix_size ** 2} LETTERS characters only)")
      print(f"\n    Matrix Size: {self.matrix_size} x {self.matrix_size}\n")
      
      while True:
          encode_word = input("\nEncoding Word: ")

          if len(encode_word) != self.matrix_size ** 2 or not encode_word.isalpha():
            os.system('cls')
            print("\nERROR:\n    It must be a letter from ENGLISH alphabet and must have the same character length as the dimension of the matrix size you chose.\n ")
            print(f"    Character Length of Encoded Word: {len(encode_word)}\n")
          
          else:
              break
       
      self.encode_chars = np.array(list(encode_word.replace(' ','_').lower())) # Separates the encoded word by characters in lowercase and replaces whitespace with a specific character
      copy_encode_chars = self.encode_chars.copy()
      orig_indices = self.alphabet.argsort() # Returns the indices that would sort the alphabet array
      self.basis_matrix = orig_indices[np.searchsorted(self.alphabet[orig_indices], copy_encode_chars)] # Makes the array 1D : used to find the indices where elements in copy_encode_chars should be inserted into the sorted array
  
      # Reshaping the Basis  1`  1D Matrix:
      basis_matrix1d = self.basis_matrix.reshape((self.matrix_size, self.matrix_size)) # Reshapes the matrix into a specified dimension depending on the indicated size of the user.
      self.transposed_mtrx = basis_matrix1d.T  # TRANSPOSE
        
      # Performing Dot Product
      self.encoding_mtrx = self.matrix_basis # Fetched from the MATRIX GENERATORS 
      self.resulting_mtrx = np.dot(self.encoding_mtrx ,self.transposed_mtrx) # Finds the dot product of the encoding matrix and basis matrix.
        
      # Converts the Resulting Matrix into 1D:
      self.linear_form = np.reshape(self.resulting_mtrx, -1, order='F') # Reads 2D array column by column and create 1D array from it
           
    def print_encrypted_message(self):
      print(f"\n\tCharacters: {self.encode_chars}")
      print(f"\n\tBasis 1D Matrix: {self.basis_matrix}")
      print(f"\n\tEncoded Message in Linear Form:{self.linear_form}")

    def decode_process(self):
      os.system('cls')
      print(f"Enter Elements(Only Positive Integers) | Matrix Size: {self.matrix_size} x {self.matrix_size} | Required Number of Values: {self.matrix_size ** 2} \n")
      list_matrix = []  # Here we define an empty list.
    
      i = 0
    
      while len(list_matrix) < self.matrix_size ** 2:
        i += 1
        try:
            values = int(input(f'   Enter Value {i}: '))
            list_matrix.append(values)
            
        except ValueError:
            print("\n\nMust be an integer.")
            i -= 1
      
      orig_matrix = np.array(list_matrix) # turning the list into a numpy array so that it can be subscriptable
      self.mtrix_encoded= orig_matrix.reshape(self.matrix_size, self.matrix_size).T # Reshapes the current dimension depending on the size chosen by the user.
      
      self.decoding_mtrx = self.matrix_basis # Fetched from the MATRIX GENERATORS 
      self.inverse_decoding_mtrx = np.linalg.inv(self.decoding_mtrx) # Finds the inverse of the decoding matrix.

      self.resulting_mtrx = np.dot(self.inverse_decoding_mtrx, self.mtrix_encoded).T # It calculates the dot product of the encoding and decoding matrix.

      decoded_linearForm = np.array(self.resulting_mtrx.reshape(((int(self.resulting_mtrx.size/self.resulting_mtrx.size)), self.resulting_mtrx.size))) #reshapes the resulting_mtrx attribute of an object to a 2D array
      self.finalDecoded = (np.rint(decoded_linearForm)).astype(int) # CONVERTS FLOAT TYPE TO INTEGER
      self.decodedChar = self.alphabet[self.finalDecoded] # Each value loops through the alphabet list
      
    def print_decrypted_message(self):
      print (f"\n\tDecoded Characters: {self.decodedChar}")
