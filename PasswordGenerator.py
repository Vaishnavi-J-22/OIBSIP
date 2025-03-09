import random
import string
import tkinter as tk
from tkinter import messagebox
import pyperclip


def GeneratePassword():
    try:
        length = int(length_entry.get())
        if length < 4:
            messagebox.showwarning("Warning..!", "Password should be atleast 4 characters long.")
            return
        
        characters = ""
        if letters_var.get():
            characters += string.ascii_letters
        if numbers_var.get():
            characters += string.digits
        if symbols_var.get():
            characters += string.punctuation
        
        if not characters:
            messagebox.showwarning("Warning..!", "Please select atleast 1 character set.")
            return
        
        password = ''.join(random.choice(characters) for _ in range(length))
        password_entry.delete(0, tk.END)
        password_entry.insert(0, password)
    except ValueError:
        messagebox.showerror("Input Error..!", "Please Enter a valid number for length.")

def copy_to_clipboard():
    pyperclip.copy(password_entry.get())

root = tk.Tk()
root.title("Password Generator")

tk.Label(root, text="Password-Length:").grid(row=0, column=0)
length_entry = tk.Entry(root)
length_entry.grid(row=0, column=1)

letters_var = tk.BooleanVar(value=True)
numbers_var = tk.BooleanVar(value=True)
symbols_var = tk.BooleanVar(value=True)

tk.Checkbutton(root, text="Letters", variable=letters_var).grid(row=1, column=0, sticky="w")
tk.Checkbutton(root, text="Numbers", variable=numbers_var).grid(row=2, column=0, sticky="w")
tk.Checkbutton(root, text="Symbols", variable=symbols_var).grid(row=3, column=0, sticky="w")

tk.Button(root, text="Generate Password", command=GeneratePassword).grid(row=4, column=0, columnspan=2)
password_entry = tk.Entry(root, width=30)
password_entry.grid(row=5, column=0, columnspan=2)
tk.Button(root, text="Copy", command=copy_to_clipboard).grid(row=6, column=0, columnspan=2)
root.mainloop()

