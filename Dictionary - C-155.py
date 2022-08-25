# -*- coding: utf-8 -*-
"""
Created on Thu Aug 25 17:13:53 2022

@author: PC_RC
"""

from tkinter import*

root = Tk()
root.title("Dictionary")
root.geometry("600x400")

label_of_mutable = Label(root)
label_of_immutable = Label(root)
label_of_tkinter = Label(root)


dictionary = {'Mutable': 'Values that can be changed. Just like a list',
              'Immutable': 'Values that cannot be changed. Just like a tuple',
              'Tkinter': 'It is the GUI library of Python'}

def mutable():
    label_of_mutable["text"] = dictionary['Mutable']
    
def immutable():
    label_of_immutable["text"] = dictionary['Immutable']
    
def tkinter():
    label_of_tkinter["text"] = dictionary['Tkinter']
    

button_mutable = Button(root, text="Meaning of Mutable", command = mutable)
button_mutable.place(relx = 0.5, rely = 0.2, anchor = CENTER)

label_of_mutable.place(relx = 0.5, rely = 0.3, anchor = CENTER)

button_immutable = Button(root, text="Meaning of Immutable", command = immutable)
button_immutable.place(relx = 0.5, rely = 0.4, anchor = CENTER)

label_of_immutable.place(relx = 0.5, rely = 0.5, anchor = CENTER)

button_tkinter = Button(root, text="Meaning of Mutable", command = tkinter)
button_tkinter.place(relx = 0.5, rely = 0.6, anchor = CENTER)

label_of_tkinter.place(relx = 0.5, rely = 0.7, anchor = CENTER)

root.mainloop()