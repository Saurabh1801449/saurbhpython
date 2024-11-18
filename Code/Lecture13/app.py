import tkinter as tk
from tkinter import filedialog, messagebox
import qrcode
import pandas as pd
from PIL import Image, ImageTk
import os

class QRCodeApp:
    def __init__(self, root): 
        self.root = root
        self.root.title("CSV QR Code Generator")
        self.root.geometry("450x500")
        self.root.config(bg="#f0f0f5")

        self.csv_file_path = ""
        self.qr_code = None

        self.title_label = tk.Label(root, text="CSV QR Code Generator", font=("Arial", 18, "bold"), fg="#4b4b8a", bg="#f0f0f5")
        self.title_label.pack(pady=15)

       
        self.desc_label = tk.Label(root, text="Generate a single QR code containing all data from a CSV file.", font=("Arial", 10), fg="#4b4b8a", bg="#f0f0f5")
        self.desc_label.pack(pady=5)

        
        self.select_btn = tk.Button(root, text="Select CSV File", command=self.select_file, bg="#4b4b8a", fg="white", font=("Arial", 12, "bold"), padx=20, pady=10)
        self.select_btn.pack(pady=10)

        self.generate_btn = tk.Button(root, text="Generate QR Code", command=self.generate_qr_code, state="disabled", bg="#6a0dad", fg="white", font=("Arial", 12, "bold"), padx=20, pady=10)
        self.generate_btn.pack(pady=10)

        
        self.save_btn = tk.Button(root, text="Save QR Code", command=self.save_qr_code, state="disabled", bg="#007acc", fg="white", font=("Arial", 12, "bold"), padx=20, pady=10)
        self.save_btn.pack(pady=10)

        self.canvas = tk.Canvas(root, width=300, height=300, bg="#e6e6fa")
        self.canvas.pack(pady=20)

    def select_file(self):
        self.csv_file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
        if self.csv_file_path:
            self.generate_btn.config(state="normal")
            messagebox.showinfo("File Selected", f"Selected file: {self.csv_file_path}")

    def generate_qr_code(self):
        if not self.csv_file_path:
            messagebox.showwarning("No File", "Please select a CSV file first.")
            return
        
        try:
            data = pd.read_csv(self.csv_file_path)
            data_str = data.to_string(index=False)
            
            self.qr_code = qrcode.make(data_str)
            self.display_qr_code(self.qr_code)
            self.save_btn.config(state="normal")
            messagebox.showinfo("QR Code Generated", "QR code for the CSV data has been generated successfully.")

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    def display_qr_code(self, qr_code):
        qr_image = qr_code.resize((300, 300))
        self.img = ImageTk.PhotoImage(qr_image)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.img)

    def save_qr_code(self):
        if not self.qr_code:
            messagebox.showwarning("No QR Code", "No QR code to save. Generate it first.")
            return

        save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG Files", "*.png")])
        if save_path:
            self.qr_code.save(save_path)
            messagebox.showinfo("Saved", "QR code has been saved successfully.")

root = tk.Tk()
app = QRCodeApp(root)
root.mainloop()
