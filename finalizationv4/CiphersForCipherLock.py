import string
import re
import numpy as np
import sys

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

