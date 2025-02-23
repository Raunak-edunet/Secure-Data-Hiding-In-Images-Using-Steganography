# encryption.py
import cv2
import os

# Load image
img = cv2.imread("image.jpg")  # Use provided image

# Get message and password
msg = input("Enter secret message: ")
password = input("Enter a passcode: ")

d = {}
c = {}

for i in range(255):
    d[chr(i)] = i
    c[i] = chr(i)

m, n, z = 0, 0, 0

# Hide message in image
for i in range(len(msg)):
    img[n, m, z] = d[msg[i]]
    n = n + 1
    m = m + 1
    z = (z + 1) % 3

cv2.imwrite("encryptedImage.jpg", img)
os.system("start encryptedImage.jpg")  # Open the encrypted image

print("Encryption completed! Saved as 'encryptedImage.jpg'")