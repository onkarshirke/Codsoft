import math
import tkinter as tk
from tkinter.constants import END

class CustomButton(tk.Button):
    def __init__(self, master, **kwargs):
        super().__init__(master=master, **kwargs)
        self.default_background = self["background"]
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)

    def on_enter(self, e):
        self['background'] = self['activebackground']

    def on_leave(self, e):
        self['background'] = self.default_background

def lab(val):
    label = tk.Label(ui, text=str(val), width=5, borderwidth=3, bg="#e0f7fa")
    label.grid(row=0, column=4, pady=8, columnspan=2)

def view(val):
    tk.Label(ui, borderwidth=3, relief="sunken", text=str(val), width=34, bg="#f0e68c", fg="#000000").grid(row=2, column=0, columnspan=5, pady=5)

def insrt(number):
    global flag
    if flag == 1:
        e.delete(0, END)
        view("Calculations here")
        lab(": )")
        flag = 0
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def set_operation(op):
    global stat, num
    stat = op
    num = e.get()
    e.delete(0, END)

def calculate():
    global stat
    num2 = e.get()
    e.delete(0, END)
    
    try:
        if stat == "+":
            ans = float(num) + float(num2)
        elif stat == "-":
            ans = float(num) - float(num2)
        elif stat == "x":
            ans = float(num) * float(num2)
        elif stat == "/":
            ans = float(num) / float(num2)
        else:
            ans = "Error"
        
        e.insert(0, str(ans))
        global flag
        flag = 1
        view(f"{num} {stat} {num2} = {ans}")
    except ValueError:
        e.insert(0, "Error")

def clear():
    lab(": |")
    view("Calculations here")
    global flag
    flag = 1
    e.delete(0, END)

ui = tk.Tk()
ui.title("Codcalc")
ui.geometry("320x400")  
ui.configure(bg="#f0f8ff")
ui.attributes('-topmost', True)

e = tk.Entry(ui, font=("Arial", 14), bd=5, width=20, justify='right')
e.grid(row=0, rowspan=2, column=0, columnspan=4, padx=5, pady=5)

lab(": )")
view("Calculations here")

global flag
flag = 0

# Buttons
buttons = [
    ("7", 4, 0), ("8", 4, 1), ("9", 4, 2), ("/", 4, 3),
    ("4", 5, 0), ("5", 5, 1), ("6", 5, 2), ("x", 5, 3),
    ("1", 6, 0), ("2", 6, 1), ("3", 6, 2), ("-", 6, 3),
    ("0", 7, 0), (".", 7, 1), ("+", 7, 2), ("=", 7, 3),
    ("cls", 3, 0)
]

for (text, row, col) in buttons:
    if text == "cls":
        btn = CustomButton(ui, text=text, padx=15, pady=15, bg="#ff7f7f", activebackground='#ffcccc', command=clear)
    else:
        btn = CustomButton(ui, text=text, padx=20, pady=15, bg="#add8e6", activebackground='#b0e0e6',
                           command=lambda t=text: insrt(t) if t not in "=+-x/" else set_operation(t) if t != "=" else calculate())
    btn.grid(row=row, column=col, sticky="nsew")

made_by_label = tk.Label(ui, text="Made by Onkar", bg="#f0f8ff", font=("Arial", 10, "italic"))
made_by_label.grid(row=8, column=0, columnspan=4, pady=10)

for i in range(8):
    ui.grid_rowconfigure(i, weight=1)
for j in range(4):
    ui.grid_columnconfigure(j, weight=1)

ui.mainloop()
