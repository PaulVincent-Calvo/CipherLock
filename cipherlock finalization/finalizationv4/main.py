import os
import CiphersForCipherLock
from CiphersForCipherLock import Rsa
from CiphersForCipherLock import Matrix_inverse

class CipherLock_main():
    def __init__(self):
        pass
    
    def print_choices(self):
        choices = ["Encrypt", "Decrypt", "Return to Main Menu"]

        for index, choice in enumerate(choices):
            print (f"[{index + 1}] {choice}")
        
    def shift_chosen(self):
        os.system("cls")
        print ("="*80 + "\n" + " "*33 + "Shift Cipher" + "\n" + "="*80)
        self.print_choices()
        
        shift_choice = input("Please input the number beside the action that you'd like to do: ")
        
        while shift_choice not in ['1', '2', '3']:
            print("Invalid input. Please try again.")
            shift_choice = input("Please input the number beside the action that you'd like to do: ")
        
        shift_choice = int(shift_choice)
        
        # declared outside the if-else loop to make the code shorter
        choices2 = ["Return to the Shift Cipher Menu", "Return to Main Menu", "Exit the Program"]

        if shift_choice == 1:
            os.system("cls")
            print ("="*80 + "\n" + " "*33 + "Shift Cipher" + "\n" + "="*80)
            user_message = input("\nPlease enter the message that you want to encrypt: ")

            while True:
                cipher_key = input("Please enter the key you'd like to use: ")
                try:
                    cipher_key = int(cipher_key)
                    # the cipher key must be positive and lower than 95 because if the value is above or equal to the length of the list of characters then it won't shift
                    if cipher_key > 0 and cipher_key < 95:
                        break
                    else:
                        print("Invalid input. Please enter a positive integer between 1 and 94.")
                except ValueError:
                    print("Invalid input. Please enter a positive integer.")

            cipher_obj = CiphersForCipherLock.shift_cipher(user_message, cipher_key)
            encrypted_message = cipher_obj.shift_cipher_encryption(user_message)

            print (f"\nEncrypted Message: {encrypted_message}")

            # after encrypting, asks if the user wants to encrypt/decrypt again, go back to the main menu to choose a different cipher, or terminate the program
            print ("\nWhat would you like to do?")
            for index, choice in enumerate(choices2):
                print (f"[{index + 1}] {choice}")

            shift_choice2 = input("Please input the number beside the action that you'd like to do: ")
            while shift_choice2 not in ['1', '2', '3']:
                print("Invalid input. Please try again.")
                shift_choice2 = input("Please input the number beside the action that you'd like to do: ")
            
            shift_choice2 = int(shift_choice2)

            if shift_choice2 == 1:
                self.shift_chosen()
            
            elif shift_choice2 == 2:
                self.main()

            else:
                self.terminate()

        elif shift_choice == 2:
            os.system("cls")
            print ("="*80 + "\n" + " "*33 + "Shift Cipher" + "\n" + "="*80)
            user_message = input("\nPlease enter the message that you want to decrypt: ")

            while True:
                cipher_key = input("Please enter the key you'd like to use: ")
                try:
                    cipher_key = int(cipher_key)
                    # the cipher key must be positive and lower than 95 because if the value is above or equal to the length of the list of characters then it won't shift
                    if cipher_key > 0 and cipher_key < 95:
                        break
                    else:
                        print("Invalid input. Please enter a positive integer between 1 and 93.")
                except ValueError:
                    print("Invalid input. Please enter a positive integer.")

            cipher_obj = CiphersForCipherLock.shift_cipher(user_message, cipher_key)
            decrypted_message = cipher_obj.shift_cipher_decryption(user_message)

            print (f"\nDecrypted Message: {decrypted_message}")

            # after decrypting, asks if the user wants to encrypt/decrypt again, go back to the main menu to choose a different cipher, or terminate the program
            print ("\nWhat would you like to do?")
            for index, choice in enumerate(choices2):
                print (f"[{index + 1}] {choice}")

            shift_choice2 = input("Please input the number beside the action that you'd like to do: ")
            while shift_choice2 not in ['1', '2', '3']:
                print("Invalid input. Please try again.")
                shift_choice2 = input("Please input the number beside the action that you'd like to do: ")
            
            shift_choice2 = int(shift_choice2)

            if shift_choice2 == 1:
                self.shift_chosen()
            
            elif shift_choice2 == 2:
                self.main()

            else:
                self.terminate()
        else:
            self.main()

    def caesar_chosen(self):
        os.system("cls")
        print ("="*80 + "\n" + " "*37 + "Caesar Cipher" "\n" + "="*80)
        self.print_choices()
        
        caesar_choice = input("Please input the number beside the action that you'd like to do: ")
        
        while caesar_choice not in ['1', '2', '3']:
            print("Invalid input. Please try again.")
            caesar_choice = input("Please input the number beside the action that you'd like to do: ")
        
        caesar_choice = int(caesar_choice)

        # declared outside the if-else loop to make the code shorter
        choices2 = ["Return to the Caesar Cipher Menu", "Return to Main Menu", "Exit the Program"]

        if caesar_choice == 1:
            os.system("cls")
            print ("="*80 + "\n" + " "*37 + "Caesar Cipher" "\n" + "="*80)

            user_message = input("\nPlease enter the message that you'd like to encrypt: ")
            
            cipher_obj = CiphersForCipherLock.caesar_cipher(user_message)
            encrypted_message = cipher_obj.shift_cipher_encryption(user_message)

            print (f"Encrypted Message: {encrypted_message}")

            # after encrypting, asks if the user wants to encrypt/decrypt again, go back to the main menu to choose a different cipher, or terminate the program
            print ("\nWhat would you like to do?")
            for index, choice in enumerate(choices2):
                print (f"[{index + 1}] {choice}")

            caesar_choice2 = input("Please input the number beside the action that you'd like to do: ")
            while caesar_choice2 not in ['1', '2', '3']:
                print("Invalid input. Please try again.")
                caesar_choice2 = input("Please input the number beside the action that you'd like to do: ")
            
            caesar_choice2 = int(caesar_choice2)

            if caesar_choice2 == 1:
                self.caesar_chosen()
            
            elif caesar_choice2 == 2:
                self.main()

            else:
                self.terminate()

        elif caesar_choice == 2:
            os.system("cls")
            print ("="*80 + "\n" + " "*37 + "Caesar Cipher" "\n" + "="*80)

            user_message = input("\nPlease enter the message that you'd like to decrypt: ")
            
            cipher_obj = CiphersForCipherLock.caesar_cipher(user_message)
            decrypted_message = cipher_obj.shift_cipher_decryption(user_message)

            print (f"Decrypted Message: {decrypted_message}")

            # after decrypting, asks if the user wants to encrypt/decrypt again, go back to the main menu to choose a different cipher, or terminate the program
            print ("\nWhat would you like to do?")
            for index, choice in enumerate(choices2):
                print (f"[{index + 1}] {choice}")

            caesar_choice2 = input("Please input the number beside the action that you'd like to do: ")
            while caesar_choice2 not in ['1', '2', '3']:
                print("Invalid input. Please try again.")
                caesar_choice2 = input("Please input the number beside the action that you'd like to do: ")
            
            caesar_choice2 = int(caesar_choice2)

            if caesar_choice2 == 1:
                self.caesar_chosen()
            
            elif caesar_choice2 == 2:
                self.main()

            else:
                self.terminate()

        else:
            self.main()

    def vigenere_chosen(self):
        os.system("cls")
        print ("="*80 + "\n" + " "*33 + "Vigenere Cipher" "\n" + "="*80)
        self.print_choices()

        vigenere_choice = input("Please input the number beside the action that you'd like to do: ")
        
        while vigenere_choice not in ['1', '2', '3']:
            print("Invalid input. Please try again.")
            vigenere_choice = input("Please input the number beside the action that you'd like to do: ")
        
        vigenere_choice = int(vigenere_choice)

        # declared outside the if-else loop to make the code shorter
        choices2 = ["Return to the Vigenere Cipher Menu", "Return to Main Menu", "Exit the Program"]       

        if vigenere_choice == 1:
            os.system("cls")
            print ("="*80 + "\n" + " "*33 + "Vigenere Cipher" "\n" + "="*80)

            user_message = input("\nPlease enter the message that you'd like to Encrypt: ")
            cipher_obj = CiphersForCipherLock.vigenere_cipher(user_message)

            encrypted_message = cipher_obj.vigenere_cipher_encryption(user_message)

            print (f"Encrypted Message: {encrypted_message}")

            # after encrypting, asks if the user wants to encrypt/decrypt again, go back to the main menu to choose a different cipher, or terminate the program
            print ("\nWhat would you like to do?")
            for index, choice in enumerate(choices2):
                print (f"[{index + 1}] {choice}")

            vigenere_choice2 = input("Please input the number beside the action that you'd like to do: ")
            while vigenere_choice2 not in ['1', '2', '3']:
                print("Invalid input. Please try again.")
                vigenere_choice2 = input("Please input the number beside the action that you'd like to do: ")
            
            vigenere_choice2 = int(vigenere_choice2)

            if vigenere_choice2 == 1:
                self.vigenere_chosen()
            
            elif vigenere_choice2 == 2:
                self.main()

            else:
                self.terminate()

        elif vigenere_choice == 2:
            os.system("cls")
            print ("="*80 + "\n" + " "*33 + "Vigenere Cipher" "\n" + "="*80)

            user_message = input("\nPlease enter the message that you'd like to decrypt: ")
            cipher_obj = CiphersForCipherLock.vigenere_cipher(user_message)

            decrypted_message = cipher_obj.vigenere_cipher_decryption(user_message)

            print (f"Decrypted Message: {decrypted_message}")

            # after decrypting, asks if the user wants to encrypt/decrypt again, go back to the main menu to choose a different cipher, or terminate the program
            print ("\nWhat would you like to do?")
            for index, choice in enumerate(choices2):
                print (f"[{index + 1}] {choice}")

            vigenere_choice2 = input("Please input the number beside the action that you'd like to do: ")
            while vigenere_choice2 not in ['1', '2', '3']:
                print("Invalid input. Please try again.")
                vigenere_choice2 = input("Please input the number beside the action that you'd like to do: ")
            
            vigenere_choice2 = int(vigenere_choice2)

            if vigenere_choice2 == 1:
                self.vigenere_chosen()
            
            elif vigenere_choice2 == 2:
                self.main()

            else:
                self.terminate()
        
        else:
            self.terminate()

    def hill_chosen(self):
        os.system("cls")
        print ("="*80 + "\n" + " "*38 + "Hill Cipher" "\n" + "="*80)
        self.print_choices()

        hill_choice = input("Please input the number beside the action that you'd like to do: ")

        while hill_choice not in ['1', '2', '3']:
            print("Invalid input. Please try again.")
            hill_choice = input("Please input the number beside the action that you'd like to do: ")

        hill_choice = int(hill_choice)

        # declared outside the if-else loop to make the code shorter
        choices2 = ["Return to the Hill Cipher Menu", "Return to Main Menu", "Exit the Program"]
        
        if hill_choice == 1:
            os.system("cls")
            print ("="*80 + "\n" + " "*33 + "Hill Cipher" + "\n" + "="*80)
            user_message = input("\nPlease enter the message that you want to encrypt: ")

            while True:
                cipher_key = input("Please enter the key you'd like to use: ")
                try:
                    cipher_key = str(cipher_key)
                    # the cipher key must be positive and lower than 95 because if the value is above or equal to the length of the list of characters then it won't shift
                    if len(cipher_key) == 4:
                        break
                    else:
                        print("Invalid input. Please enter a key that's only 4 letters long.")
                except ValueError:
                    print("Invalid input.")

            cipher_obj = CiphersForCipherLock.hill_cipher(user_message, cipher_key)
            encrypted_message = cipher_obj.hill_cipher_encryption(user_message, cipher_key)

            print (f"\nEncrypted Message: {encrypted_message}")

            # after encrypting, asks if the user wants to encrypt/decrypt again, go back to the main menu to choose a different cipher, or terminate the program
            print ("\nWhat would you like to do?")
            for index, choice in enumerate(choices2):
                print (f"[{index + 1}] {choice}")

            hill_choice = input("Please input the number beside the action that you'd like to do: ")
            while hill_choice not in ['1', '2', '3']:
                print("Invalid input. Please try again.")
                hill_choice = input("Please input the number beside the action that you'd like to do: ")

            hill_choice = int(hill_choice)

            if hill_choice == 1:
                self.hill_chosen()
            
            elif hill_choice == 2:
                self.main()

            else:
                self.terminate()  

        elif hill_choice == 2:
            os.system("cls")
            print ("="*80 + "\n" + " "*33 + "Hill Cipher" "\n" + "="*80)

            user_message = input("\nPlease enter the message that you'd like to decrypt: ")
            while True:
                cipher_key = input("Please enter the key you'd like to use: ")
                try:
                    cipher_key = str(cipher_key)
                    # the cipher key must be positive and lower than 95 because if the value is above or equal to the length of the list of characters then it won't shift
                    if len(cipher_key) == 4:
                        break
                    else:
                        print("Invalid input. Please enter a key that's only 4 letters long.")
                except ValueError:
                    print("Invalid input.")

            cipher_obj = CiphersForCipherLock.hill_cipher(user_message, cipher_key)
            decrypted_message = cipher_obj.hill_cipher_decryption(user_message, cipher_key)

            print (f"Decrypted Message: {decrypted_message}")

            # after decrypting, asks if the user wants to encrypt/decrypt again, go back to the main menu to choose a different cipher, or terminate the program
            print ("\nWhat would you like to do?")
            for index, choice in enumerate(choices2):
                print (f"[{index + 1}] {choice}")

            hill_choice2 = input("Please input the number beside the action that you'd like to do: ")
            while hill_choice2 not in ['1', '2', '3']:
                print("Invalid input. Please try again.")
                hill_choice2 = input("Please input the number beside the action that you'd like to do: ")
            
            hill_choice2 = int(hill_choice2)

            if hill_choice2 == 1:
                self.hill_chosen()
            
            elif hill_choice2 == 2:
                self.main()

            else:
                self.terminate()
        
        else:
            self.terminate()      
    
    def matrix_inverse_chosen(self):
        os.system("cls")
        print ("="*80 + "\n" + " "*30 + "Matrix Inverse Cipher" "\n" + "="*80)
        self.print_choices()

        matrix_inverse_choice = input("Please input the number beside the action that you'd like to do: ")
       
        while matrix_inverse_choice not in ['1', '2', '3']:
            print("Invalid input. Please try again.")
            matrix_inverse_choice = input("Please input the number beside the action that you'd like to do: ")
        
        matrix_inverse_choice = int(matrix_inverse_choice)
        
      # declared outside the if-else loop to make the code shorter
        choices2 = ["Return to the RSA Cipher Menu", "Return to Main Menu", "Exit the Program"]       
        
        if matrix_inverse_choice == 1:
          os.system("cls")
          print ("="*80 + "\n" + " "*37 + "Matrix-Inverse Cipher" "\n" + "="*80)
          matrix_inv_obj = Matrix_inverse()
          matrix_inv_obj.select_size()
          matrix_inv_obj.matrix_inverse_encryption()
          matrix_inv_obj.print_encrypted_message()
        
        elif matrix_inverse_choice == 2:
          os.system("cls")
          print ("="*80 + "\n" + " "*37 + "Matrix-Inverse Cipher" "\n" + "="*80)
          matrix_inv_obj2 = Matrix_inverse()
          matrix_inv_obj2.select_size()
          matrix_inv_obj2.matrix_inverse_encryption()
          matrix_inv_obj2.print_decrypted_message()
        
        else:
            self.terminate()
            
            
    def rsa_chosen(self):
      
      os.system("cls")
      print ("="*80 + "\n" + " "*35 + "RSA Cipher" "\n" + "="*80)
      self.print_choices()

      rsa_choice = input("Please input the number beside the action that you'd like to do: ")
      
      while rsa_choice not in ['1', '2', '3']:
          print("Invalid input. Please try again.")
          rsa_choice = input("Please input the number beside the action that you'd like to do: ")
      
      rsa_choice = int(rsa_choice)

      # declared outside the if-else loop to make the code shorter
      choices2 = ["Return to the RSA Cipher Menu", "Return to Main Menu", "Exit the Program"]       

      if rsa_choice == 1:
        os.system("cls")
        print ("="*80 + "\n" + " "*37 + "RSA Algorithm" "\n" + "="*80)
        rsa_obj = Rsa()
        rsa_obj.prime_generator()
        rsa_obj.public_key()
        rsa_obj.dipslay_pubkey()
        rsa_obj.private_key()
        rsa_obj.dipslay_privkey()
        rsa_obj.rsa_encryption()
        rsa_obj.dipslay_ciphertext()
        
      elif rsa_choice == 2:
        os.system("cls")
        print ("="*80 + "\n" + " "*37 + "RSA Algorithm" "\n" + "="*80)
        rsa_obj2 = Rsa()
        rsa_obj2.rsa_decryption()
        rsa_obj2.dipslay_plaintext()
      
      else:
            self.terminate()
            
    def base64_chosen(self):
        os.system("cls")
        print ("="*80 + "\n" + " "*37 + "Base64 Cipher" "\n" + "="*80)
        self.print_choices()
        
        base64_choice = input("Please input the number beside the action that you'd like to do: ")
        
        while base64_choice not in ['1', '2', '3']:
            print("Invalid input. Please try again.")
            base64_choice = input("Please input the number beside the action that you'd like to do: ")
        
        base64_choice = int(base64_choice)

        # declared outside the if-else loop to make the code shorter
        choices2 = ["Return to the Base64 Cipher Menu", "Return to Main Menu", "Exit the Program"]
        
        if base64_choice == 1:
            os.system("cls")
            print ("="*80 + "\n" + " "*37 + "Base64 Cipher" "\n" + "="*80)
            user_message = input("\nPlease enter the message that you'd like to encrypt: ")

            cipher_obj = CiphersForCipherLock.base64_cipher(user_message)
            encrypted_message = cipher_obj.base64_cipher_encryption(user_message)

            print (f"Encrypted Message: {encrypted_message}")

            # after encrypting, asks if the user wants to encrypt/decrypt again, go back to the main menu to choose a different cipher, or terminate the program
            print ("\nWhat would you like to do?")
            for index, choice in enumerate(choices2):
                print (f"[{index + 1}] {choice}")

            base64_choice2 = input("Please input the number beside the action that you'd like to do: ")
            while base64_choice2 not in ['1', '2', '3']:
                print("Invalid input. Please try again.")
                base64_choice2 = input("Please input the number beside the action that you'd like to do: ")
            
            base64_choice2 = int(base64_choice2)

            if base64_choice2 == 1:
                self.base64_chosen()
            
            elif base64_choice2 == 2:
                self.main()

        elif base64_choice == 2:
            os.system("cls")
            print ("="*80 + "\n" + " "*37 + "Base64 Cipher" "\n" + "="*80)
            user_message = input("\nPlease enter the message that you'd like to decrypt: ")

            while len(user_message) % 4 != 0:
                print("Invalid input. Make sure that the length of your message is divisible by 4")
                user_message = input("\nPlease enter the message that you'd like to decrypt: ")

            cipher_obj = CiphersForCipherLock.base64_cipher(user_message)
            decrypted_message = cipher_obj.base64_cipher_decryption(user_message)

            print (f"Decrypted Message: {decrypted_message}")

            # after decrypting, asks if the user wants to encrypt/decrypt again, go back to the main menu to choose a different cipher, or terminate the program
            print ("\nWhat would you like to do?")
            for index, choice in enumerate(choices2):
                print (f"[{index + 1}] {choice}")

            base64_choice2 = input("Please input the number beside the action that you'd like to do: ")
            while base64_choice2 not in ['1', '2', '3']:
                print("Invalid input. Please try again.")
                base64_choice2 = input("Please input the number beside the action that you'd like to do: ")
            
            base64_choice2 = int(base64_choice2)

            if base64_choice2 == 1:
                self.base64_chosen()
            
            elif base64_choice2 == 2:
                self.main()

            else:
                self.terminate()

        else:
                self.terminate()

        
    def terminate (self):
        os.system("cls")
        print ("="*80 + "\n" + " "*35 + "CipherLock" + "\n" + "="*80)
        print ("Thank you for using our program!")

    def main(self):
        os.system("cls")
        print ("="*80 + "\n" + " "*35 + "CipherLock" + "\n" + "-"*80 + "\n" + " "*36 + "Main Menu" + "\n" + "="*80)
        print ("Please choose a Cipher.")
        options = ["Shift", "Caesar", "Vigenere", "Hill", "Matrix Inverse", "RSA", "Base64", "Exit"]
        
        for index, option in enumerate (options):
            if index < len(options) - 1:
                print (f"[{index + 1}] {option} Cipher")
            else:
                print (f"[{index + 1}] {option}")
        
        user_choice = input("\nPlease input the number beside the Cipher that you want to use: ")

        while user_choice not in ['1', '2', '3', '4', '5', '6', '7', '8']:
            print("Invalid input. Please try again.")
            user_choice = input("Please input the number beside the Cipher that you want to use: ")

        user_choice = int(user_choice)

        if user_choice == 1:
            self.shift_chosen()

        elif user_choice == 2:
            self.caesar_chosen()

        elif user_choice == 3:
            self.vigenere_chosen()

        elif user_choice == 4:
            self.hill_chosen()

        elif user_choice == 5:
            self.matrix_inverse_chosen()

        elif user_choice == 6:
            self.rsa_chosen()

        elif user_choice == 7:
            self.base64_chosen()

        else:
            self.terminate()

obj1 = CipherLock_main()
obj1.main()
