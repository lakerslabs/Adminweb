# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 13:00:41 2020

@author: eduardo.berga
"""
import tkinter as tk

root= tk.Tk()

canvas1 = tk.Canvas(root, width = 400, height = 300,  relief = 'raised')
canvas1.pack()

label1 = tk.Label(root, text='Calcular la raíz cuadrada')
label1.config(font=('helvetica', 14))
canvas1.create_window(200, 25, window=label1)

label2 = tk.Label(root, text='Escriba un número:')
label2.config(font=('helvetica', 10))
canvas1.create_window(200, 100, window=label2)

entry1 = tk.Entry (root, text='Escriba un número:') 
canvas1.create_window(200, 140, window=entry1)

def getSquareRoot ():
    
    x1 = entry1.get()
    
    label3 = tk.Label(root, text= 'La raíz cuadrada de ' + x1 + ' is:',font=('helvetica', 10))
    canvas1.create_window(200, 210, window=label3)
    
    label4 = tk.Label(root, text= float(x1)**0.5,font=('helvetica', 10, 'bold'))
    canvas1.create_window(200, 230, window=label4)
    
button1 = tk.Button(text='Obtenga la raíz cuadrada', command=getSquareRoot, bg='brown', fg='white', font=('helvetica', 9, 'bold'))
canvas1.create_window(200, 180, window=button1)

root.mainloop()