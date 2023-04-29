import tkinter as tk
import pyperclip

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', " ", ".", ",", "?", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', " ", ".", ",", "?", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

def encrypt():
    text = text_input.get().lower()
    shift = int(shift_input.get())
    cipher_text = ""
    for letter in text:
        position = alphabet.index(letter)
        new_position = position + shift
        new_letter = alphabet[new_position]
        cipher_text += new_letter
    output_label.config(text=f"The encrypted text is: {cipher_text}")
    pyperclip.copy(cipher_text)

def decrypt():
    text = text_input.get().lower()
    shift = int(shift_input.get())
    plain_text = ""
    for letter in text:
        position = alphabet.index(letter)
        new_position = position - shift
        new_letter = alphabet[new_position]
        plain_text += new_letter
    output_label.config(text=f"The decrypted text is: {plain_text}")
    pyperclip.copy(plain_text)

# Create GUI window
window = tk.Tk()
window.title("Caesar Cipher")

# Create widgets
text_label = tk.Label(window, text="Enter the text to encrypt/decrypt:")
text_input = tk.Entry(window)
shift_label = tk.Label(window, text="Enter the shift number:")
shift_input = tk.Entry(window)
encrypt_button = tk.Button(window, text="Encrypt", command=encrypt)
decrypt_button = tk.Button(window, text="Decrypt", command=decrypt)
output_label = tk.Label(window, text="")

# Add widgets to window
text_label.pack()
text_input.pack()
shift_label.pack()
shift_input.pack()
encrypt_button.pack()
decrypt_button.pack()
output_label.pack()

# Run the GUI loop
window.mainloop()
