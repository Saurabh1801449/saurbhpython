import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Prime Number Checker")
root.geometry("300x200")

def is_prime():
    try:
        number = int(entry.get())
        if number < 2:
            result_label.config(text="Not a prime number")
            return
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                result_label.config(text="Not a prime number")
                return
        result_label.config(text="Prime number")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid integer.")

entry_label = tk.Label(root, text="Enter a number:")
entry_label.pack(pady=10)
entry = tk.Entry(root)
entry.pack(pady=10)

check_button = tk.Button(root, text="Check Prime", command=is_prime)
check_button.pack(pady=10)

result_label = tk.Label(root, text="Result")
result_label.pack(pady=10)

root.mainloop()
