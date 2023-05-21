import sys
import numpy as np


def hillciph_enc():
    msg = input("Enter the message that you would like to encrypt:\n").upper()
    msg = msg.replace(" ", "")

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
    

    key = input("\nEnter the 4-letter Key String:\n").upper()
    key = key.replace(" ", "")

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
 

    enc_txt = ""
    itr_count = int(len(msg)/2)
    if len_chk == 0:
        for i in range(itr_count):
            temp1 = msg2d[0][i] * key2d[0][0] + msg2d[1][i] * key2d[0][1]
            enc_txt += chr((temp1 % 26) + 65)
            temp2 = msg2d[0][i] * key2d[1][0] + msg2d[1][i] * key2d[1][1]
            enc_txt += chr((temp2 % 26) + 65)
   
    else:
        for i in range(itr_count-1):
            temp1 = msg2d[0][i] * key2d[0][0] + msg2d[1][i] * key2d[0][1]
            enc_txt += chr((temp1 % 26) + 65)
            temp2 = msg2d[0][i] * key2d[1][0] + msg2d[1][i] * key2d[1][1]
            enc_txt += chr((temp2 % 26) + 65)
   
    print("\nHere is your encrypted text:\n{}".format(enc_txt))


def hillciph_dec():
    msg = input("Enter the message that you would like to decrypt:\n").upper()
    msg = msg.replace(" ", "")

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

    key = input("\nEnter the 4-letter Key String:\n").upper()
    key = key.replace(" ", "")

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
    dec_txt = ""
    itr_count = int(len(msg) / 2)
    if len_chk == 0:
        for i in range(itr_count):
            temp1 = msg2d[0][i] * key2d[0][0] + msg2d[1][i] * key2d[0][1]
            dec_txt += chr((temp1 % 26) + 65)
            temp2 = msg2d[0][i] * key2d[1][0] + msg2d[1][i] * key2d[1][1]
            dec_txt += chr((temp2 % 26) + 65)
            # for
    else:
        for i in range(itr_count - 1):
            temp1 = msg2d[0][i] * key2d[0][0] + msg2d[1][i] * key2d[0][1]
            dec_txt += chr((temp1 % 26) + 65)
            temp2 = msg2d[0][i] * key2d[1][0] + msg2d[1][i] * key2d[1][1]
            dec_txt += chr((temp2 % 26) + 65)

    print("\nHere is your decrypted text:\n{}".format(dec_txt))


def main():
    choice = int(input("Hallo, fella! This is Dr. Hill. How may I help you?\n1. I would like to encrypt a message.\n2. I would like to decrypt a message.\nChoose(1,2): "))
    if choice == 1:
        print("\n--------------------------Encryption--------------------------\n")
        hillciph_enc()
    elif choice == 2:
        print("\n--------------------------Decryption--------------------------\n")
        hillciph_dec()
    else:
        print("Oh, boy. It looks like your choice is invalid. Please, try again.")

if __name__ == "__main__":
    main()