import tkinter as tk
from tkinter import Entry
from tkinter import StringVar
from tkinter import PhotoImage
from tkinter import messagebox
from tkinter import  Toplevel
#root
root = tk.Tk()
root.title("SigmaClicker")
root.iconbitmap(r"assets\icon.ico")
root.geometry("800x600+50+200")
root.maxsize(800,600)
root.minsize(800,600)

#zdjecia
IkonaSklep = PhotoImage(file=r"assets\shopicon.png")
#zmienne
click = 0
ItemkiSklep = ["Multiplier"]
ile_razy_kupiono_mult = 1
cena = 10
#wyswietlane zmienne
cena_wyswietl = StringVar()
cena_wyswietl.set("Koszt: 10 klikniec")

ile_razy_kupiono_mult_wyswietl = StringVar()
ile_razy_kupiono_mult_wyswietl.set("Jeszcze nic nie kupiono!")

wyswietl = StringVar()
wyswietl.set("nacisnij przycisk aby zaczac!")

#funckje
def akcja_guzik():
    global click
    global ile_razy_kupiono_mult
    click += 1*ile_razy_kupiono_mult
    wyswietl.set(f"{click:.0f}")

def ile_kupiono():
    global ile_razy_kupiono_mult
    global ile_razy_kupiono_mult_wyswietl
    global click
    global cena
    global cena_wyswietl
    if click >= cena:
        ile_razy_kupiono_mult += 1
        ile_razy_kupiono_mult_wyswietl.set("tyle razy kupiono: "+str(ile_razy_kupiono_mult-1))
        click -= cena
        cena += cena*0.2
        wyswietl.set(f"{click:.0f}")
        cena_wyswietl.set(f"Koszt: {cena:.0f} klikniec")
    elif click < cena:
        messagebox.showinfo("Sklep","Nie masz wystarczajaco klikniec")


def sklep_interface(nazwaokna):
    global ItemkiSklep
    global ile_razy_kupiono_mult_wyswietl
    global ile_razy_kupiono_mult
    global cena
    napis_multiplier = tk.Label(
        nazwaokna,
        text = ItemkiSklep[0],
        font=("gothic",30)
    )
    podnapis_multiplier = tk.Label(
        nazwaokna,
        textvariable = cena_wyswietl,
        font=("gothic", 16)
    )
    ile_multiplier = tk.Label(
        nazwaokna,
        textvariable = ile_razy_kupiono_mult_wyswietl,
        font=("gothic", 20)
    )
    guzik_kup_multiplier = tk.Button(
        nazwaokna,
        text = "Kup",
        width = 12,
        height = 3,
        relief = "ridge",
        command = ile_kupiono
    )
    napis_multiplier.place(x = 50, y = 100)
    podnapis_multiplier.place(x = 150, y = 150)
    guzik_kup_multiplier.place(x = 300, y = 100)
    ile_multiplier.place(x = 400, y = 100)
#otwiera pop-upa
def guzik_sklep():
    oknosklep = Toplevel(root)
    oknosklep.geometry("800x600+1050+200")
    oknosklep.maxsize(800,600)
    oknosklep.minsize(800,600)
    oknosklep.title("Sigma Clicker - Sklep")
    oknosklep.iconbitmap(r"assets\icon.ico")
    sklep_interface(oknosklep)

#label odpowiedzialny za wyswietlanie ilosci klikniec
liczbaKlikniec = tk.Label(
    root,
    textvariable=wyswietl,
    bd = 0,
    font=("gothic", 40)
)
#guziki
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
#guzik do sklepu
guzikSklep = tk.Button(
    root,
    image = IkonaSklep,
    command=guzik_sklep
)
#komendy do ulozenia danych rzeczy (place, mainloop itd)
guzik.place(x = 50, y = 300)
guzikSklep.place(x = 730, y = 20)
liczbaKlikniec.place(x=395, y=150, anchor = tk.CENTER)
root.mainloop()