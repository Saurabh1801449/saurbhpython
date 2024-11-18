import tkinter as tk

root = tk.Tk()
root.title("Simple Calculator")

display = tk.Entry(root, width=16, font=("Arial", 20), borderwidth=2, relief="solid")
display.grid(row=0, column=0, columnspan=4)

def button_click(value):
    display.insert(tk.END, value)


def calculate():
    try:
        result = eval(display.get())
        display.delete(0, tk.END)
        display.insert(tk.END, str(result))
    except:
        display.delete(0, tk.END)
        display.insert(tk.END, "Error")

def clear_display():
    display.delete(0, tk.END)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', 'C', '=', '+'
]

for i, text in enumerate(buttons):
    action = calculate if text == '=' else (clear_display if text == 'C' else lambda x=text: button_click(x))
    tk.Button(root, text=text, width=5, height=2, command=action).grid(row=1 + i // 4, column=i % 4, padx=5, pady=5)

root.mainloop()
