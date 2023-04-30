# Cipher Project w/ Object Oriented Programming Prototype 2
import string
import re

class shift_cipher():

    def __init__ (self, user_message, cipher_key):
        self.cipher_key = cipher_key
        self.user_message = user_message        

    def shift_cipher_encryption (self, user_message):
        characters = string.ascii_lowercase + string.ascii_uppercase + string.digits + " "+ string.punctuation
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
        characters = string.ascii_lowercase + string.ascii_uppercase + string.digits + " "+ string.punctuation
        decrypted_message = "" 

        n = int(len(characters))

        shift_cipher_decryption_key = n - self.cipher_key

        # multiple spaces not replaced to a single space because it may be intentional as spaces are part of the translation table

        translation_table = str.maketrans(characters, characters[shift_cipher_decryption_key:]+characters[:shift_cipher_decryption_key])
        
        # translated message
        decrypted_message = user_message.translate(translation_table)

        #print(user_message)
        return decrypted_message
    
    def tester_shift_cipher_encryption (self):
        print ("Shift Key = " + str(self.cipher_key))
        print ("Encrypted Message = " + self.shift_cipher_encryption(user_message))

    def tester_shift_cipher_decryption (self):
        print ("Shift Key = " + str(self.cipher_key))
        print ("Decrypted Message = " + self.shift_cipher_decryption(user_message))

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

        no_of_keys = int(input("How many keys do you want to use: "))

        list_of_keys = []
        for i in range (no_of_keys):
            list_of_keys.append (int(input("Key [" + str((i + 1)) + "]: " )))

        for i, char in enumerate(user_message):
            self.cipher_key = int(list_of_keys[i % len(list_of_keys)]) 
            user_message_for_enc = str(char)
            encrypted_message += super().shift_cipher_encryption (user_message_for_enc)

        print ("Encrypted Message: " + encrypted_message)
    
    def vigenere_cipher_decryption (self, user_message):
        decrypted_message = "" 

        no_of_keys = int(input("How many keys do you want to use: "))

        list_of_keys = []
        for i in range (no_of_keys):
            list_of_keys.append (int(input("Key [" + str((i + 1)) + "]: " )))

        for i, char in enumerate(user_message):
            self.cipher_key = int(list_of_keys[i % len(list_of_keys)]) 
            user_message_for_enc = str(char)
            decrypted_message += super().shift_cipher_decryption (user_message_for_enc)

        print ("Decrypted Message: " + decrypted_message)

user_message = str(input("Test message: "))
cipherobj = vigenere_cipher (user_message)
cipherobj.vigenere_cipher_encryption(user_message)

user_message = str(input("Test message: "))
cipherobj.vigenere_cipher_decryption(user_message)
#encrypted_message = cipherobj.vigenere_cipher_encryption(user_message)
#print("Encrypted Message:", encrypted_message)

