# Image Steganography

A simple Python-based steganography project that hides a secret message and passcode in an image using Least-Significant-Bit (LSB) encoding, and later retrieves the message securely.

## Overview

This project uses robust LSB steganography to embed a secret message along with a passcode into an image. .

## Features

- **Encryption:**  
  Embeds a secret message and passcode into `mypic.jpg` and saves the result as `encrypted.png`.

- **Decryption:**  
  Retrieves the hidden message from `encrypted.png` when the correct passcode is provided.

## Requirements

- Python 3.x  
- OpenCV  

## Installation

Ensure you have Python 3 installed, then install OpenCV:

     pip install opencv-python
