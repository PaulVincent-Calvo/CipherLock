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



def shift_cipher_clicked():
    print("Shift Cipher clicked!")
    # making the window for when the shift cipher button is clicked by the user
    shift_cipher_window = tk.Tk()
    shift_cipher_window.title("CipherLock - Shift Cipher")
    shift_cipher_window.geometry("600x400")
    
    # making the functions that will be used for the encryption and decryption of texts
    def encrypt_message():
        message = user_message_entry_field.get()  # Get the message from the entry field
        key = int(cipher_key_entry_field.get())  # Get the cipher key from the entry field

        # Create an instance of the shift_cipher class
        cipher = shift_cipher(message, key)

        # Call the encryption method and get the encrypted message
        encrypted_message = cipher.shift_cipher_encryption(message)

        # Display the encrypted message
        messagebox.showinfo("Encrypted Message:", encrypted_message)

    def decrypt_message():
        message = user_message_entry_field.get()  # Get the message from the entry field
        key = int(cipher_key_entry_field.get())  # Get the cipher key from the entry field

        # Create an instance of the shift_cipher class
        cipher = shift_cipher(message, key)

        # Call the encryption method and get the encrypted message
        decrypted_message = cipher.shift_cipher_decryption(message)

        # Display the encrypted message
        messagebox.showinfo("Decrypted Message:", decrypted_message)

    # creating the entry fields for the message and cipher key
    user_message_label = tk.Label(shift_cipher_window, text="Message", font=("Arial",18))
    user_message_entry_field = tk.Entry(shift_cipher_window, width=30)
    cipher_key_label = tk.Label(shift_cipher_window, text="Cipher Key", font=("Arial",18))
    cipher_key_entry_field = tk.Entry(shift_cipher_window, width=30)

    # creating the buttons for the Shift Cipher window
    shift_cipher_back_button = tk.Button(shift_cipher_window, text="Back", command=shift_cipher_window.destroy, font=("Arial", 14))
    shift_cipher_encrypt_button = tk.Button(shift_cipher_window, text="Encrypt", command=encrypt_message, font=("Arial", 14))
    shift_cipher_decrypt_button = tk.Button(shift_cipher_window, text="Decrypt", command=decrypt_message, font=("Arial", 14))

    # layout of the buttons and entry field
    shift_cipher_back_button.place(relx=0, rely=0)
    user_message_label.place(relx=0.185, rely=0.3)
    user_message_entry_field.place(relx=0.12, rely=0.4)
    cipher_key_label.place(relx=0.55, rely=0.3)
    cipher_key_entry_field.place(relx=0.5, rely=0.4)
    shift_cipher_encrypt_button.place(relx=0.4, rely=0.8,anchor= "center")
    shift_cipher_decrypt_button.place(relx=0.55, rely=0.8, anchor= "center")

def caesar_cipher_clicked():
    print("Caesar Cipher clicked!")

def vigenere_cipher_clicked():
    print("Vigenere Cipher clicked!")

def hill_cipher_clicked():
    print("Hill clicked!")

def matrix_inverse_cipher_clicked():
    print("Matrix Inverse Cipher clicked!")

def rsa_cipher_clicked():
    print("RSA Cipher clicked!")

def base64_cipher_clicked():
    print("Base64 Cipher clicked!")

def main():
    # creating the main CipherLock window
    cipherlock_window = tk.Tk()
    cipherlock_window.title("CipherLock")
    cipherlock_window.geometry("600x400")       

    # creating the buttons a
    shift_cipher_button = tk.Button(cipherlock_window, text="Shift Cipher", command=cipherlock_window.destroy and shift_cipher_clicked, font=("Arial", 14))
    caesar_cipher_button = tk.Button(cipherlock_window, text="Caesar Cipher", command=caesar_cipher_clicked, font=("Arial", 14))
    vigenere_cipher_button = tk.Button(cipherlock_window, text="Vigenere Cipher", command=vigenere_cipher_clicked, font=("Arial", 14))
    hill_cipher_button = tk.Button(cipherlock_window, text="Hill Cipher", command=hill_cipher_clicked, font=("Arial", 14))
    matrix_inverse_cipher_button = tk.Button(cipherlock_window, text="Matrix Inverse", command=matrix_inverse_cipher_clicked, font=("Arial", 14))
    rsa_cipher_button = tk.Button(cipherlock_window, text="RSA Cipher", command=rsa_cipher_clicked, font=("Arial", 14))
    base64_cipher_button = tk.Button(cipherlock_window, text="Base64 Cipher", command=base64_cipher_clicked, font=("Arial", 14))

    shift_cipher_button.grid(row=0, column=0, sticky="nsew")
    caesar_cipher_button.grid(row=0, column=1, sticky="nsew")
    vigenere_cipher_button.grid(row=0, column=2, sticky="nsew")
    hill_cipher_button.grid(row=1, column=0, sticky="nsew")
    matrix_inverse_cipher_button.grid(row=1, column=1, sticky="nsew")
    rsa_cipher_button.grid(row=1, column=2, sticky="nsew")
    base64_cipher_button.grid(row=2, column=1, sticky="nsew")

    # this will allow the window to be stretched while still maintaining the buttons at the center 
    cipherlock_window.columnconfigure((0, 1, 2), weight=1)
    cipherlock_window.rowconfigure((0, 1, 2), weight=1)

    # Run the main cipherlock_window's event loop
    cipherlock_window.mainloop()

main()