import tkinter as tk

def create_layout():
    root = tk.Tk()
    root.title("Layout Example")

    button_north = tk.Button(root, text="North", bg="red")
    button_south = tk.Button(root, text="South", bg="blue")
    button_east = tk.Button(root, text="East", bg="green")
    button_west = tk.Button(root, text="West", bg="yellow")

    button_north.pack(side=tk.TOP, fill=tk.X)
    button_south.pack(side=tk.BOTTOM, fill=tk.X)
    button_east.pack(side=tk.RIGHT, fill=tk.Y)
    button_west.pack(side=tk.LEFT, fill=tk.Y)

    root.mainloop()

create_layout()
