import tkinter as tk
from tkinter import Entry
from tkinter import StringVar
root = tk.Tk()
root.geometry("800x600")
root.maxsize(800,600)
root.minsize(800,600)

click = 0
wyswietl = StringVar()
wyswietl.set("nacisnij przycisk aby zaczac!")

def akcja_guzik():
    global click
    click+=1
    wyswietl.set(click)
    
liczbaKlikniec = tk.Label(
    root,
    textvariable=wyswietl,
    bd = 0,
    font=("gothic", 40)
)
guzik = tk.Button(
    root,
    text = "NACISNIJ MNIE",
    font = ("gothic", 50),
    width= 20,
    height=3,
    bd = 0,
    bg= "#b0b5b1",
    command = akcja_guzik
)

guzik.place(x = 50, y = 300) 
liczbaKlikniec.place(x=395, y=150, anchor = tk.CENTER)
root.mainloop()