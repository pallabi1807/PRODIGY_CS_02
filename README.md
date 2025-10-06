# PRODIGY_CS_02
Pixel Manipulation for Image Encryption
---------
🎯 Aim

Develop a simple image encryption tool using pixel manipulation. You can perform operations like swapping pixel values or applying a basic mathematical operation to each pixel. Allow users to encrypt and decrypt images.
--------
🧠 Objective

Implement image encryption and decryption using Python and GUI (Tkinter).

Use pixel value modification and pixel shuffling to scramble images.

Please make sure encrypted images appear scrambled/noisy, while decryption restores the original image perfectly.

Support color (RGB) and grayscale images.
--------

🏢 Internship Task

This project is part of the Prodigy InfoTech Internship Program (CS Domain).
It was developed as Internship Task 02 (CS) to implement an image encryption and decryption tool using Python GUI.
-------
⚙️ Working

1. User selects an image file (PNG, JPG, JPEG, BMP) via the GUI.

2. User enters an integer key.

3. Encryption:

Pixel values are modified using the key.

Pixels may be shuffled based on the key for stronger encryption.

Encrypted image is saved and displayed in the GUI.

4. Decryption:

Reverse pixel modifications using the same key.

Reverse pixel shuffling (if applied).

The original image is restored perfectly and displayed in the GUI.
-------
💻 Steps to Run

1. Install Python 3 and required libraries:

pip install Pillow numpy

2. Open image_encryption_tool.py in VS Code or any Python IDE.

3. Run the program:

python image_encryption_tool.py

4. Use the GUI to:

Select an image,

Enter a key,

Click Encrypt or Decrypt.

5. Save the output image when prompted.

-----
🧩 Example Workflow

1. Original Image → Encrypt → Encrypted Image (Scrambled & Noisy)

2. Encrypted Image → Decrypt (with same key) → Original Image (Restored in full color)
-----
👩‍💻 Author

*Pallabi Poria*  
MCA Student | Cybersecurity Enthusiast  
Task completed under *Prodigy InfoTech Internship*

