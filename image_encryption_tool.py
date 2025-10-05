import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import numpy as np

# --- Encryption ---
def encrypt_image(image_path, key, output_path):
    image = Image.open(image_path).convert('RGB')
    pixels = np.array(image, dtype=np.int32)  # int32 to prevent overflow

    # --- Pixel Shuffling ---
    flat_pixels = pixels.reshape(-1, 3)
    np.random.seed(key)
    indices = np.arange(flat_pixels.shape[0])
    np.random.shuffle(indices)
    shuffled_pixels = flat_pixels[indices]

    # --- Pixel Value Encryption ---
    encrypted_pixels = (shuffled_pixels + key) % 256
    encrypted_image = Image.fromarray(encrypted_pixels.astype(np.uint8).reshape(pixels.shape), 'RGB')
    encrypted_image.save(output_path)
    messagebox.showinfo("Success", f"Image encrypted and saved as {output_path}")

# --- Decryption ---
def decrypt_image(image_path, key, output_path):
    image = Image.open(image_path).convert('RGB')
    pixels = np.array(image, dtype=np.int32)

    # --- Reverse Pixel Value Encryption ---
    decrypted_pixels = (pixels - key) % 256
    flat_pixels = decrypted_pixels.reshape(-1, 3)

    # --- Reverse Pixel Shuffling ---
    np.random.seed(key)
    indices = np.arange(flat_pixels.shape[0])
    np.random.shuffle(indices)

    # Compute inverse permutation
    inverse_indices = np.zeros_like(indices)
    inverse_indices[indices] = np.arange(len(indices))

    original_flat = flat_pixels[inverse_indices]
    original_image = original_flat.reshape(pixels.shape)

    decrypted_image = Image.fromarray(original_image.astype(np.uint8), 'RGB')
    decrypted_image.save(output_path)
    messagebox.showinfo("Success", f"Image decrypted and saved as {output_path}")

# --- GUI ---
def select_file():
    path = filedialog.askopenfilename(filetypes=[("Image Files", ".png;.jpg;.jpeg;.bmp")])
    if path:
        entry_file.delete(0, tk.END)
        entry_file.insert(0, path)
        img = Image.open(path).convert('RGB')
        img.thumbnail((200, 200))
        img_tk = ImageTk.PhotoImage(img)
        lbl_preview.img = img_tk
        lbl_preview.config(image=lbl_preview.img)

def perform_encrypt():
    path = entry_file.get()
    if not path:
        messagebox.showerror("Error", "Please select an image")
        return
    try:
        key = int(entry_key.get())
    except:
        messagebox.showerror("Error", "Key must be an integer")
        return
    output_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG","*.png")])
    if output_path:
        encrypt_image(path, key, output_path)

def perform_decrypt():
    path = entry_file.get()
    if not path:
        messagebox.showerror("Error", "Please select an encrypted image")
        return
    try:
        key = int(entry_key.get())
    except:
        messagebox.showerror("Error", "Key must be an integer")
        return
    output_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG","*.png")])
    if output_path:
        decrypt_image(path, key, output_path)

# --- GUI Layout ---
root = tk.Tk()
root.title("RGB-Safe Image Encryption Tool")
root.geometry("400x550")

tk.Label(root, text="Select Image:").pack(pady=5)
entry_file = tk.Entry(root, width=40)
entry_file.pack(pady=5)
tk.Button(root, text="Browse", command=select_file).pack(pady=5)

tk.Label(root, text="Enter Key (integer):").pack(pady=5)
entry_key = tk.Entry(root, width=20)
entry_key.pack(pady=5)

tk.Button(root, text="Encrypt", width=15, command=perform_encrypt).pack(pady=10)
tk.Button(root, text="Decrypt", width=15, command=perform_decrypt).pack(pady=5)

lbl_preview = tk.Label(root)
lbl_preview.pack(pady=10)

root.mainloop()
