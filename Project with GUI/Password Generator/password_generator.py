# importing libraries
from tkinter import *
import random, string
import pyperclip


#gui window

window = Tk() # initializing window
window.geometry("400x400") #setting the height and width of window
window.resizable(0,0) #setting the fixed window size
window.title("Password Generator by Kapeed ") #title of the window
Label(window, text = 'Password Generator' , font =' Helvetica 16 bold').pack() #label is used to display text within the window

#user selects password length

pass_head = Label(window, text= 'Enter Password Length', font= 'Helvetica 12 bold').pack()
pass_len = IntVar() #integer type variable to store the length of password
length = Spinbox(window, from_=8, to_ = 36, textvariable= pass_len, width=15).pack() #select from a fixed number of values

#password generation

pass_value = StringVar()
def Generation():
    password = ''

    for x in range (0,4):
        password = random.choice(string.ascii_uppercase) + random.choice(string.ascii_lowercase) + random.choice(string.digits) + random.choice(string.punctuation)
    for y in range (pass_len.get()-4):
        password = password + random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation)
        pass_value.set(password)

Button(window, text = "Generate Password" , command = Generation ).pack(pady= 5)
Entry(window , textvariable = pass_value).pack()

#function to allow user to copy the password

def PassCopy():
    pyperclip.copy(pass_value.get())
Button(window, text = 'Copy', command = PassCopy).pack(pady=5)

window.mainloop()
