# decryption.py
import cv2

# Load encrypted image
img = cv2.imread("encryptedImage.jpg")

# Get passcode
password = input("Enter passcode for decryption: ")
original_password = input("Re-enter original passcode for verification: ")

d = {}
c = {}

for i in range(255):
    d[chr(i)] = i
    c[i] = chr(i)

message = ""
n, m, z = 0, 0, 0

if password == original_password:
    while True:
        try:
            message += c[img[n, m, z]]
            n += 1
            m += 1
            z = (z + 1) % 3
        except KeyError:
            break
    print("Decryption message:", message)
else:
    print("Authentication failed! Decryption not possible.")