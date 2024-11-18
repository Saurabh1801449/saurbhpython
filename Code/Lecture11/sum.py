import tkinter as tk
from tkinter import messagebox

def calculate_sum():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        result = num1 + num2
        entry_result.config(state="normal")
        entry_result.delete(0, tk.END)
        entry_result.insert(0, str(result))
        entry_result.config(state="readonly")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers.")

root = tk.Tk()
root.title("Sum Calculator")
root.geometry("400x300")

label_num1 = tk.Label(root, text="Enter first number:")
label_num1.pack(pady=5)
entry_num1 = tk.Entry(root)
entry_num1.pack(pady=5)

label_num2 = tk.Label(root, text="Enter second number:")
label_num2.pack(pady=5)
entry_num2 = tk.Entry(root)
entry_num2.pack(pady=5)

sum_button = tk.Button(root, text="Calculate Sum", command=calculate_sum)
sum_button.pack(pady=10)

label_result = tk.Label(root, text="Result:")
label_result.pack(pady=5)
entry_result = tk.Entry(root)
entry_result.pack(pady=5)
entry_result.config(state="readonly")

root.mainloop()
