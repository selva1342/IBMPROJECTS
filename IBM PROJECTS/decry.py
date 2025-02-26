import cv2 
import numpy as np 

def decrypt_image(image_path):
    try:
        with open("encry_data.txt", "r") as file:
            saved_password = file.readline().strip()
            message_length = int(file.readline().strip())

    except FileNotFoundError:
        print("Error: Encryption data file not found!")
        return

    img = cv2.imread(image_path)
    if img is None:
        print("Error: Encrypted image not found!")
        return

    entered_password = input("Enter passcode for Decryption: ")

    if entered_password == saved_password:
        message = ""
        n, m, z = 0, 0, 0

        for _ in range(message_length):
            ascii_value = int(img[n, m, z]) # Read and convert to integer
            message += chr(ascii_value) # Convert back to character
            n += 1
            m += 1
            z = (z + 1) % 3
            
        print("Decryption message:", message)
    else:
        print("YOU ARE NOT auth")

if __name__ == "__main__": 
    image_path = "encryImage.png" # Match encryption output filename
    decrypt_image(image_path)
