import string
import re
import tkinter as tk
from tkinter import messagebox

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
    
    # used a printer function for the shift cipher since the encryption and decryption methods will be inherited by caesar cipher and vigenere cipher
    def printer_shift_cipher_encryption (self):
        print ("Shift Key = " + str(self.cipher_key))
        print ("Encrypted Message = " + self.shift_cipher_encryption(user_message))

    def printer_shift_cipher_decryption (self):
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

        # validate the number of keys input
        while True:
            try:
                no_of_keys = int(input("How many keys do you want to use: "))
                if no_of_keys < 1:
                    print("Number of keys should be greater than 0.")
                    continue
                break
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

        print ("Encrypted Message: " + encrypted_message)
    
    def vigenere_cipher_decryption (self, user_message):
        decrypted_message = "" 

        while True:
            try:
                no_of_keys = int(input("How many keys do you want to use: "))
                if no_of_keys < 1:
                    print("Number of keys should be greater than 0.")
                    continue
                break
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

        print ("Decrypted Message: " + decrypted_message)

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

    def print_encryption (self, user_message):
        print ("The encrypted message is " + self.base64_encryption(user_message))

    def print_decryption (self, user_message): 
        print ("The decrypted message is " + self.base64_decryption(user_message))

class CipherLockGUI():
    def __init__(self):
        self.cipherlock_window = tk.Tk()
        self.cipherlock_window.title("CipherLock")
        self.cipherlock_window.geometry("600x400")       

    def shift_cipher_clicked(self):
        # making the window for when the shift cipher button is clicked by the user
        self.shift_cipher_window = tk.Tk()
        self.shift_cipher_window.title("CipherLock - Shift Cipher")
        self.shift_cipher_window.geometry("600x400")
        
        # making the functions that will be used for the encryption and decryption of texts
        def shift_encrypt_message():
            message = self.user_message_entry_field.get()  # Get the message from the entry field
            key = int(self.cipher_key_entry_field.get())  # Get the cipher key from the entry field

            # Create an instance of the shift_cipher class
            shift_cipher_obj = shift_cipher(message, key)

            # Call the encryption method and get the encrypted message
            encrypted_message = shift_cipher_obj.shift_cipher_encryption(message)

            # Display the encrypted message
            messagebox.showinfo("Encrypted Message:", encrypted_message)

        def shift_decrypt_message():
            message = self.user_message_entry_field.get()  # Get the message from the entry field
            key = int(self.cipher_key_entry_field.get())  # Get the cipher key from the entry field

            # Create an instance of the shift_cipher class
            shift_cipher_obj = shift_cipher(message, key)

            # Call the decryption method and get the decrypted message
            decrypted_message = shift_cipher_obj.shift_cipher_decryption(message)

            # Display the decrypted message
            messagebox.showinfo("Decrypted Message:", decrypted_message)

        # creating the entry fields and labels for the message and cipher key
        self.user_message_label = tk.Label(self.shift_cipher_window, text="Message", font=("Arial",18))
        self.user_message_entry_field = tk.Entry(self.shift_cipher_window, width=30)
        self.cipher_key_label = tk.Label(self.shift_cipher_window, text="Cipher Key", font=("Arial",18))
        self.cipher_key_entry_field = tk.Entry(self.shift_cipher_window, width=30)

        # creating the buttons for the Shift Cipher window
        self.shift_cipher_back_button = tk.Button(self.shift_cipher_window, text="Back", command=self.shift_cipher_window.destroy, font=("Arial", 14))
        self.shift_cipher_encrypt_button = tk.Button(self.shift_cipher_window, text="Encrypt", command=shift_encrypt_message, font=("Arial", 14))
        self.shift_cipher_decrypt_button = tk.Button(self.shift_cipher_window, text="Decrypt", command=shift_decrypt_message, font=("Arial", 14))

        # layout of the buttons, labels, and entry fields
        self.shift_cipher_back_button.place(relx=0, rely=0)
        self.user_message_label.place(relx=0.185, rely=0.3)
        self.user_message_entry_field.place(relx=0.12, rely=0.4)
        self.cipher_key_label.place(relx=0.55, rely=0.3)
        self.cipher_key_entry_field.place(relx=0.5, rely=0.4)
        self.shift_cipher_encrypt_button.place(relx=0.4, rely=0.8,anchor= "center")
        self.shift_cipher_decrypt_button.place(relx=0.55, rely=0.8, anchor= "center")

    def caesar_cipher_clicked(self):
        # making the window for when the caesar cipher button is clicked by the user
        self.caesar_cipher_window = tk.Tk()
        self.caesar_cipher_window.title("CipherLock - Caesar Cipher")
        self.caesar_cipher_window.geometry("600x400")
        
        # making the functions that will be used for the encryption and decryption of text
        def caesar_encrypt_message():
            message = self.user_message_entry_field.get()

            # create instance of the caesar_cipher class
            caesar_cipher_obj = caesar_cipher(message)

            # encrypting the message
            encrypted_message = caesar_cipher_obj.shift_cipher_encryption(message)

            # printing the encrypted message
            messagebox.showinfo("Encrypted Message:", encrypted_message)

        def caesar_decrypt_message():
            message = self.user_message_entry_field.get()

            # create instance of the caesar_cipher class
            caesar_cipher_obj = caesar_cipher(message)

            # encrypting the message
            decrypted_message = caesar_cipher_obj.shift_cipher_decryption(message)

            # printing the encrypted message
            messagebox.showinfo("Decrypted Message:", decrypted_message)

        # creating the entry field for the message; note: no key needed since caesar cipher has fixed shift key of 3
        self.user_message_label = tk.Label(self.caesar_cipher_window, text="Message", font=("Arial",18))
        self.user_message_entry_field = tk.Entry(self.caesar_cipher_window, width=50)

        # creating the buttons for the Caesar Cipher Window
        self.caesar_cipher_back_button = tk.Button(self.caesar_cipher_window, text="Back", command=self.caesar_cipher_window.destroy, font=("Arial", 14))
        self.caesar_cipher_encrypt_button = tk.Button(self.caesar_cipher_window, text="Encrypt", command=caesar_encrypt_message, font=("Arial", 14))
        self.caesar_cipher_decrypt_button = tk.Button(self.caesar_cipher_window, text="Decrypt", command=caesar_decrypt_message, font=("Arial", 14))

        # layout of the buttons, label, and entry field
        self.caesar_cipher_back_button.place(relx=0, rely=0)
        self.user_message_label.place(relx=0.4, rely=0.3)
        self.user_message_entry_field.place(relx=0.229, rely=0.4)
        self.caesar_cipher_encrypt_button.place(relx=0.4, rely=0.8,anchor= "center")
        self.caesar_cipher_decrypt_button.place(relx=0.55, rely=0.8, anchor= "center")
    
    def vigenere_cipher_clicked(self):
        print("Vigenere Cipher clicked!")
        
    def hill_cipher_clicked(self):
        print("Hill clicked!")

    def matrix_inverse_cipher_clicked(self):
        print("Matrix Inverse Cipher clicked!")

    def rsa_cipher_clicked(self):
        print("RSA Cipher clicked!")

    def base64_cipher_clicked(self):
        # making the window for when the Base64 cipher button is clicked by the user
        self.base64_cipher_window = tk.Tk()
        self.base64_cipher_window.title("CipherLock - Base64 Cipher")
        self.base64_cipher_window.geometry("600x400")
        
        # making the functions that will be used for the encryption and decryption of text
        def base64_encrypt_message():
            message = self.user_message_entry_field.get()

            # create instance of the caesar_cipher class
            base64_cipher_obj = base64_cipher(message)

            # encrypting the message
            encrypted_message = base64_cipher_obj.base64_cipher_encryption(message)

            # printing the encrypted message
            messagebox.showinfo("Encrypted Message:", encrypted_message)

        def base64_decrypt_message():
            message = self.user_message_entry_field.get()

            # create instance of the caesar_cipher class
            base64_cipher_obj = base64_cipher(message)

            # encrypting the message
            decrypted_message = base64_cipher_obj.base64_cipher_decryption(message)

            # printing the encrypted message
            messagebox.showinfo("Decrypted Message:", decrypted_message)

        # creating the entry field for the message; note: no key needed 
        self.user_message_label = tk.Label(self.base64_cipher_window, text="Message", font=("Arial",18))
        self.user_message_entry_field = tk.Entry(self.base64_cipher_window, width=50)

        # creating the buttons for the Caesar Cipher Window
        self.base64_cipher_back_button = tk.Button(self.base64_cipher_window, text="Back", command=self.base64_cipher_window.destroy, font=("Arial", 14))
        self.base64_cipher_encrypt_button = tk.Button(self.base64_cipher_window, text="Encrypt", command=base64_encrypt_message, font=("Arial", 14))
        self.base64_cipher_decrypt_button = tk.Button(self.base64_cipher_window, text="Decrypt", command=base64_decrypt_message, font=("Arial", 14))

        # layout of the buttons, label, and entry field
        self.base64_cipher_back_button.place(relx=0, rely=0)
        self.user_message_label.place(relx=0.4, rely=0.3)
        self.user_message_entry_field.place(relx=0.229, rely=0.4)
        self.base64_cipher_encrypt_button.place(relx=0.4, rely=0.8,anchor= "center")
        self.base64_cipher_decrypt_button.place(relx=0.55, rely=0.8, anchor= "center")
    
    def main(self):
        # creating the main CipherLock window

        # creating the buttons a
        shift_cipher_button = tk.Button(self.cipherlock_window, text="Shift Cipher", command=self.shift_cipher_clicked, font=("Arial", 14))
        caesar_cipher_button = tk.Button(self.cipherlock_window, text="Caesar Cipher", command=self.caesar_cipher_clicked, font=("Arial", 14))
        vigenere_cipher_button = tk.Button(self.cipherlock_window, text="Vigenere Cipher", command=vigenere_cipher_clicked, font=("Arial", 14))
        hill_cipher_button = tk.Button(self.cipherlock_window, text="Hill Cipher", command=hill_cipher_clicked, font=("Arial", 14))
        matrix_inverse_cipher_button = tk.Button(self.cipherlock_window, text="Matrix Inverse", command=matrix_inverse_cipher_clicked, font=("Arial", 14))
        rsa_cipher_button = tk.Button(self.cipherlock_window, text="RSA Cipher", command=rsa_cipher_clicked, font=("Arial", 14))
        base64_cipher_button = tk.Button(self.cipherlock_window, text="Base64 Cipher", command=self.base64_cipher_clicked, font=("Arial", 14))

        shift_cipher_button.grid(row=0, column=0, sticky="nsew")
        caesar_cipher_button.grid(row=0, column=1, sticky="nsew")
        vigenere_cipher_button.grid(row=0, column=2, sticky="nsew")
        hill_cipher_button.grid(row=1, column=0, sticky="nsew")
        matrix_inverse_cipher_button.grid(row=1, column=1, sticky="nsew")
        rsa_cipher_button.grid(row=1, column=2, sticky="nsew")
        base64_cipher_button.grid(row=2, column=1, sticky="nsew")

        # this will allow the window to be stretched while still maintaining the buttons at the center 
        self.cipherlock_window.columnconfigure((0, 1, 2), weight=1)
        self.cipherlock_window.rowconfigure((0, 1, 2), weight=1)

        # Run the main cipherlock_window's event loop
        self.cipherlock_window.mainloop()

def vigenere_cipher_clicked():
    print("Vigenere Cipher clicked!")
    
def hill_cipher_clicked():
    print("Hill clicked!")

def matrix_inverse_cipher_clicked():
    print("Matrix Inverse Cipher clicked!")

def rsa_cipher_clicked():
    print("RSA Cipher clicked!")


obj1 = CipherLockGUI()
obj1.main()
