import random
from tkinter import *
import string
from tkinter import messagebox, ttk
root = Tk()
var = IntVar()
var1 = IntVar()

def low():
    entry.delete(0 ,END)
    length = var1.get()
    pwd = ""
    if var.get() == 1:
        lower = string.ascii_lowercase
        for i in range(length):
            pwd = pwd + random.choice(lower)
        return pwd
    elif var.get() == 0:
        letter = string.ascii_letters
        for i in range(length):
            pwd = pwd + random.choice(letter)
        return pwd
    elif var.get() == 3:
        choices = string.ascii_letters + '' + '0123456789' + '!@#$%^&*()_-+/\{}[].~><?:;'
        for i in range(length):
            pwd = pwd + random.choice(choices)
        return pwd
    else:
        messagebox.showwarning("Select Options")
        
def copytoclip():
    pwd = entry.get()
    root.clipboard_clear()
    root.clipboard_append(pwd)

def generate():
    pwd = low()
    entry.insert(10, pwd)

root.title("Password Generator")
password = Label(root, text = "Password")
password.grid(row = 0)
entry = Entry(root)
entry.grid(row = 0, column = 1)

length = Label(root, text = "Length")
length.grid(row = 1)

copy_btn = Button(root, text = "Copy", command = copytoclip)
copy_btn.grid(row = 0, column = 2)
generate_btn = Button(root, text = "Generate", command = generate)
generate_btn.grid(row = 0, column = 3)
exit_btn = Button(root, text = "Exit", command = root.quit)
exit_btn.grid(row = 0, column = 4)

radio_low = Radiobutton(root, text = "Low", variable = var, value = 1)
radio_low.grid(row = 1, column = 2, sticky = "E")
radio_middle = Radiobutton(root, text = "Middle", variable = var, value = 0)
radio_middle.grid(row = 1, column = 3, sticky = "E")
radio_high = Radiobutton(root, text = "Strong", variable = var, value = 3)
radio_high.grid(row = 1, column = 4, sticky = "E")

combo = ttk.Combobox(root, width = 27, textvariable = var1)
combo['values'] = (8,9,10,11,12,13,14,15,16,17,18,19,20)
combo.current()
combo.bind('<<ComboBoxSelected>>')
combo.grid(column=1,row=1)
root.mainloop()