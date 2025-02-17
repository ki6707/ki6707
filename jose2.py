#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
import tkinter as tk
 
window = tk.Tk()
window.title('My Window')
window.geometry('500x300')
 
var = tk.StringVar()
l = tk.Label(window, bg='white', width=40, text='select your course: ')
l.pack()
 
def print_selection():
    l.config(text='you have selected ' + var.get())
 
r1 = tk.Radiobutton(window, text='PYTHON', variable=var, value='PYTHON', command=print_selection)
r1.pack()
r2 = tk.Radiobutton(window, text='JAVA', variable=var, value='JAVA', command=print_selection)
r2.pack()
r3 = tk.Radiobutton(window, text='C & C++', variable=var, value='C & C++', command=print_selection)
r3.pack()
r4=tk.Radiobutton(window,text="DCA-P",value='DCA-P',variable=var,command=print_selection)
r3.pack()
r5=tk.Radiobutton(window,text="DCA-TALLY",value='DCA-TALLY',variable=var,command=print_selection)
r5.pack()
 
window.mainloop()