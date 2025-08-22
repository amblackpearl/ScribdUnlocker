import os
from dotenv import load_dotenv
import re
import tkinter as tk
from tkinter import messagebox
import webbrowser  # to open the link

def extract_doc_number(url):
    # Define regex patterns for Scribd URLs
    patterns = (
        r"scribd\.com/doc/(\d+)",
        r"scribd\.com/document/(\d+)",
        r"scribd\.com/presentation/(\d+)"
    )

    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match.group(1)
    return None

def unlock_url():
    url = entry.get()
    doc_number = extract_doc_number(url)
    load_dotenv()
    base_url = os.getenv("BASE_URL")

    if doc_number:
        embed_url = base_url.format(nomor=doc_number)
        result_var.set(embed_url)
        # Automatically open in browser
        webbrowser.open(embed_url)
        entry.delete(0, tk.END)
        result_var.delete(0, tk.END)
    else:
        messagebox.showerror("Invalid URL", "Please enter a valid Scribd URL.")
        entry.delete(0, tk.END)

# --- GUI Setup ---
root = tk.Tk()
root.title("Scribd Unlocker")
root.geometry("600x200")
root.configure(bg="#1e1e2e")  # dark background

# set icon
try:
    root.iconbitmap("unlocker.ico")
except Exception as e:
    print("Icon not found or invalid:", e)

title_label = tk.Label(root, text="🔓 Scribd Unlocker", font=("Segoe UI", 16, "bold"), fg="white", bg="#1e1e2e")
title_label.pack(pady=10)

entry = tk.Entry(root, width=60, font=("Segoe UI", 11))
entry.pack(pady=5)

unlock_button = tk.Button(root, text="Unlock", command=unlock_url, font=("Segoe UI", 12), bg="#4CAF50", fg="white", relief="raised")
unlock_button.pack(pady=10)


result_var = tk.StringVar()
result_label = tk.Label(root, textvariable=result_var, wraplength=500, fg="#00ffcc", bg="#1e1e2e", font=("Segoe UI", 10))
result_label.pack(pady=10)

root.mainloop()
