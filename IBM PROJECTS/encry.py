import cv2 
import os
import numpy as np 

def encrypt_image(image, output_path="encryImage.png"): 
    img = cv2.imread(image_path) 
    if img is None:
        print("Error: Image not found!")
        return 

    msg = input("Enter secret message: ")
    password = input("Enter a passcode: ")

    #Converting msg into ASCII values
    ascii_values = [ord(char) for char in msg]

    m, n, z = 0, 0, 0

    for value in ascii_values:
        img[n, m, z] = np.uint8(value)  # Storing the exact ASCII values
        n += 1
        m += 1
        z = (z + 1) % 3

    cv2.imwrite(output_path, img, [cv2.IMWRITE_PNG_COMPRESSION, 0])
    print("Encryption Successful.")

    #Saving passcode and message length 
    with open("encry_data.txt", "w") as file:
        file.write(f"{password}\n{len(msg)}")

if __name__ == "__main__":
    image_path = "image.png"
    encrypt_image(image_path)