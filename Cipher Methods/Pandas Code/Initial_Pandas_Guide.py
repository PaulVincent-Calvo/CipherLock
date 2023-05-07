import pandas as pd
import os


# Note: if naka-open yung csv file sa excel or wps ay close nyo muna bago i-debug/run yung code

# Note, create a csv file first in the same directory of your python file.
def csv(data_encode): # function for storing the values into a csv file 
    csv_data_encode = pd.DataFrame(data_encode)
    csv_data_encode.to_csv('RSA.csv', mode = 'a', index=False, header=False) # mode = 'a' --> append
# -----------------------------------------------------------------------------------------
    
    
    
    
def main_home():
  print("\n\nACTION:\n    1: ENCODE\n    2: DECODE\n    3: HISTORY")

  user_act = int(input("\n   Enter: "))

  if user_act == 1:
    encoding_word = input("Enter: ")
    encoded_char = 'abcd' # sample
    
    data_encode = {"Method": 'Encode', '|': '|', "Word/Values": [encoding_word],'Data': ':','Decoded/Encoded Words/Values': [encoded_char]}
    csv(data_encode) # calling the function
    
    go_home()
  
# -----------------------------------------------------------------------------------------

  if user_act == 2:
    decoding_word = input("Enter: ")
    decoded_char = 'dcba' # sample
    
    data_encode = {"Method": 'Decode', '|': '|', "Word/Values": [decoding_word],'Data': ':','Decoded/Encoded Words/Values': [decoded_char]}
    csv(data_encode) # calling the function
    
    go_home()

# -----------------------------------------------------------------------------------------
  if user_act == 3:
    os.system('cls')
    dataset = pd.read_csv('RSA.csv') # reads the csv file and its content
    print(dataset)
    go_home()
  
  

# -----------------------------------------------------------------------------------------
def go_home():
  main_home()
  
  
main_home()