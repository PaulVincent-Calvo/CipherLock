
import tkinter as tk
import numpy as np

class Matrix_inverse():
  
    def __init__(self):

        first_char = np.array(['$']) # filler/placeholder character
        alphabet = np.array(['a','b','c','d','e','f','g','h','i','j',
                                    'k','l','m','n','o','p','q','r','s','t',
                                    'u','v','w','x','y','z','_'])

        self.alphabet = np.concatenate((first_char, np.tile(alphabet, 10))) # used to join the first character array with 10 copies of the alphabet array. This results in an array of 260 characters (26 letters + 1 underscore) repeated 10 times, with $ as the first character.
    
    
    def select_size(self, matrix_size):
        if matrix_size == 2:
            self.matrix_basis = np.array([[12,34],[3,4]]) # fetched from Matrix Generators
    
        elif matrix_size == 3:
            self.matrix_basis = np.array([[1,9,8],[20,40,2],[5,21,11]])
            
        elif matrix_size == 4:
            self.matrix_basis = np.array([[10, 87, 3, 23],[1, 100, 34, 65],[66, 69, 5, 8],[90, 2, 45, 11]])
        
        elif matrix_size == 5:
            self.matrix_basis = np.array([[66, 7, 78, 21, 43],[1, 99, 56, 34, 32],[7, 76, 23, 32, 98],[9, 66, 88, 12, 43], [6, 54, 76, 89, 13]])
        
        elif matrix_size == 6:
            self.matrix_basis = np.array([[99, 81, 2, 36, 17, 13],[1, 90, 65, 22, 34, 79],[3, 56, 87, 92, 13, 29],[46, 33, 72, 4, 6, 1], [23, 99, 12, 8, 28, 67],[88, 66, 9, 11, 83, 5]])

        elif matrix_size == 7:
            self.matrix_basis = np.array([[80, 12, 45, 23, 88, 6, 90],[1, 33, 78, 99, 34 , 56, 21],[9, 59, 32, 53 , 67, 75, 23],[6, 73, 84, 23, 12, 65, 87], [87, 34, 88, 43, 34, 11, 43],[82, 2, 56, 64, 75, 32, 4],[87, 43, 88, 99, 23, 54, 8]])
        
        
        print(self.matrix_basis)
    
    def process_encode(self): # ENCODING PROCESS
      os.system('cls')
      print(f"NOTE:\n    The number of characters/value must be equal to the number of elements of the array size that you chose.\n\tEx. {self.matrix_size} x {self.matrix_size} ({self.matrix_size ** 2} LETTERS characters only)")
      print(f"\n    Matrix Size: {self.matrix_size} x {self.matrix_size}\n")
      
      while True:
          encode_word = input("\nEncoding Word: ")

          if len(encode_word) != self.matrix_size ** 2 or encode_word.isalpha == False:
            print("\nERROR:\n    It must be a letter from ENGLISH alphabet and must have the same character length as the dimension of the matrix size you chose.\n ")
            print(f"    Character Length of Encoded Word: {len(encode_word)}\n")
          else:
              break
       
      encode_chars = np.array(list(encode_word.replace(' ','_').lower())) # Separates the encoded word by characters in lowercase and replaces whitespace with a specific character
      copy_encode_chars = encode_chars.copy()
      orig_indices = self.alphabet.argsort() # Returns the indices that would sort the alphabet array
      basis_matrix = orig_indices[np.searchsorted(self.alphabet[orig_indices], copy_encode_chars)] # Makes the array 1D : used to find the indices where elements in copy_encode_chars should be inserted into the sorted array

  
      # Reshaping the Basis 1D Matrix:
      basis_matrix1d = basis_matrix.reshape((self.matrix_size, self.matrix_size)) # Reshapes the matrix into a specified dimension depending on the indicated size of the user.
      transposed_mtrx = basis_matrix1d.T  # TRANSPOSE
        
      # Performing Dot Product
      encoding_mtrx = self.matrix_basis # Fetched from the MATRIX GENERATORS 
      resulting_mtrx = np.dot(encoding_mtrx ,transposed_mtrx) # Finds the dot product of the encoding matrix and basis matrix.
        
      # Converts the Resulting Matrix into 1D:
      self.linear_form = np.reshape(resulting_mtrx, -1, order='F') # Reads 2D array column by column and create 1D array from it
      
      
    def print_encodedword(self):
      print(f"Encoded Message in Linear Form:\n{self.linear_form}")

    

      
class Gui():
  
    '''def __init__(self):
          self.cipherlock_window = tk.Tk()
          self.cipherlock_window.title("CipherLock")
          self.cipherlock_window.geometry("600x400")'''
          
    def matrix_inv_enrcyption():
        pass
    def  matrix_inv_decryption():
        pass
      
    def matrix_clicked(self):
      self.cipherlock_window = tk.Tk()
      self.cipherlock_window.title("CipherLock")
      self.cipherlock_window.geometry("600x400")
          
    def matrix_size(self):
      label_size = tk.Label(self.cipherlock_window, text='Choose Matrix Size', font=('Arial', 18))
      label_size.pack(padx=20, pady=20)
      
      # Object for Matrix_inverse: 
      self.matrix_inv = Matrix_inverse()
      
      framebutton = tk.Frame(self.cipherlock_window)
      framebutton.columnconfigure(0, weight=1)
      framebutton.columnconfigure(1, weight=1)
      framebutton.columnconfigure(2, weight=1)

      button_2by2 = tk.Button(framebutton, text='2 x 2', font=('Arial', 12), command=lambda: [self.choose_action(), self.matrix_inv.select_size(2)])
      button_2by2.grid(row=0, column=0, sticky=tk.W+tk.E)

      button_3by3 = tk.Button(framebutton, text='3 x 3', font=('Arial', 12), command=lambda: [self.choose_action(), self.matrix_inv.select_size(3)])
      button_3by3.grid(row=0, column=1, sticky=tk.W+tk.E)

      button_4by4 = tk.Button(framebutton, text='4 x 4', font=('Arial', 12), command=lambda: [self.choose_action(), self.matrix_inv.select_size(4)])
      button_4by4.grid(row=0, column=2, sticky=tk.W+tk.E)

      button_5by5 = tk.Button(framebutton, text='5 x 5', font=('Arial', 12), command=lambda: [self.choose_action(), self.matrix_inv.select_size(5)])
      button_5by5.grid(row=1, column=0, sticky=tk.W+tk.E)

      button_6by6 = tk.Button(framebutton, text='6 x 6', font=('Arial', 12), command=lambda: [self.choose_action(), self.matrix_inv.select_size(6)])
      button_6by6.grid(row=1, column=1, sticky=tk.W+tk.E)

      button_7by7 = tk.Button(framebutton, text='7 x 7', font=('Arial', 12), command=lambda: [self.choose_action(), self.matrix_inv.select_size(7)])
      button_7by7.grid(row=1, column=2, sticky=tk.W+tk.E)

      framebutton.pack(fill='x', padx=20, pady=20)
      self.cipherlock_window.mainloop()
  

    def encrypt_window(self):
      self.cipherlock_window = tk.Tk()
      self.cipherlock_window.title("CipherLock")
      self.cipherlock_window.geometry("600x400")
      
      encrypt_label = tk.Label(self.cipherlock_window, text='Enter the Encrypting Word', font=('Arial', 15))
      encrypt_label.pack(padx=20, pady=20)
      
      user_message_entry_field = tk.Entry(self.cipherlock_window)
      user_message_entry_field.pack(padx=20, pady=20)
      
      submit_button = tk.Button(self.cipherlock_window, text='Submit', font=('Arial', 12) )
      submit_button.pack(padx=20, pady=20)
      
      self.cipherlock_window.mainloop()  
    
    def decrypt_window(self):
      self.cipherlock_window = tk.Tk()
      self.cipherlock_window.title("CipherLock")
      self.cipherlock_window.geometry("600x400")
      
      decrypt_label = tk.Label(self.cipherlock_window, text='Enter the Dercypting Word', font=('Arial', 15))
      decrypt_label.pack(padx=20, pady=20)
      
      user_message_entry_field = tk.Entry(self.cipherlock_window)
      user_message_entry_field.pack(padx=20, pady=20)
      
      submit_button = tk.Button(self.cipherlock_window, text='Submit', font=('Arial', 12) )
      submit_button.pack(padx=20, pady=20)
      
      self.cipherlock_window.mainloop()   
    
    def choose_action(self): 
      self.cipherlock_window = tk.Tk()
      self.cipherlock_window.title("CipherLock")
      self.cipherlock_window.geometry("600x400")
      
      buttonframe = tk.Frame(self.cipherlock_window)
      buttonframe.columnconfigure(0, weight=1)
      buttonframe.columnconfigure(1, weight=1)
      
      encrypt_button = tk.Button(buttonframe, command = self.encrypt_window,  text='Encrypt', font=('Arial', 12) )
      encrypt_button.grid(row=0, column=0, sticky=tk.W+tk.E)
      
      decrypt_button = tk.Button(buttonframe, command = self.decrypt_window, text='Decrypt', font=('Arial', 12) )
      decrypt_button.grid(row=1, column=0, sticky=tk.W+tk.E)
      
      buttonframe.pack(fill='x', padx=20, pady=20)
      
      self.cipherlock_window.mainloop()

        
      

gui_obj = Gui()
gui_obj.matrix_clicked()
gui_obj.matrix_size()


