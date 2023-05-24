import sys
import os
import msvcrt as m
import pandas as pd

# Clearing Terminal
def clear(): os.system('cls')
clear()

def csv(data_encode):
    csv_data_encode = pd.DataFrame(data_encode)
    csv_data_encode.to_csv('Base64.csv', mode = 'a', index = False, header = False)
    # ------------------------------------------------------------------------------

def main_home():
  print("\n\nACTION:\n    1: ENCODE\n    2: DECODE\n    3: HISTORY")

  user_act = int(input("\n   Enter: "))
  
  if user_act == 1:
    user_message = str(input("Please type the message you want to encrypt: "))
    base64_obj = base64_cipher(user_message)
    base64_obj.print_encryption(user_message)
    go_home()

  if user_act == 2:
    user_message = str(input("Please type the message you want to decrypt: "))
    if len(user_message) % 4 != 0:
            print("UH OH it appears that you have made a mistake, please try again.")
            go_home()
    else:
        base64_obj = base64_cipher(user_message)
        base64_obj.print_decryption(user_message)
        go_home()
    
  if user_act == 3:
    os.system('cls')
    dataset = pd.read_csv('Base64.csv') # reads the csv file and its content
    print(dataset)
    go_home()


class base64_cipher:
    def __init__ (self, user_message):
        self.user_message = user_message

    def base64_encryption (self, user_message):
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
        data_encode = {"Method": 'Encode', '|': '|', "Word/Values": [user_message],'Data': ':','Decoded/Encoded Words/Values': [encoded]}
        csv(data_encode)

        return encoded
       
    def base64_decryption (self, user_message):

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
        data_encode = {"Method": 'Encode', '|': '|', "Word/Values": [user_message],'Data': ':','Decoded/Encoded Words/Values': [decoded]}
        csv(data_encode) # calling the function

        return decoded
    
    def print_encryption (self, user_message):
        print ("The encrypted message is " + self.base64_encryption(user_message))

    def print_decryption (self, user_message): 
        print ("The decrypted message is " + self.base64_decryption(user_message))


def go_home():

    main_home()

main_home()

