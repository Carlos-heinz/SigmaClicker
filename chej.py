import tkinter as tk
from tkinter import StringVar
from tkinter import PhotoImage
from tkinter import messagebox
from tkinter import  Toplevel
#root
root = tk.Tk()
root.title("SigmaClicker")
root.iconbitmap(r"assets\icon.ico")
root.geometry("800x600+50+200")
root.resizable(False,False)

#zdjecia
IkonaSklep = PhotoImage(file=r"assets\shopicon.png")
IkonaZapisIWczytaj = PhotoImage(file=r"assets\save&load.png")
#zmienne
click = 0
ItemkiSklep = ["Multiplier","Autoclicker"]
ile_razy_kupiono_mult = 1
ile_razy_kupiono_autoclicker = 0
cenaMult = 10
cenaAuto = 200
#wyswietlane zmienne
cenaMult_wyswietl = StringVar()
cenaMult_wyswietl.set("Koszt: 10 klikniec")

ile_razy_kupiono_mult_wyswietl = StringVar()
ile_razy_kupiono_mult_wyswietl.set("Jeszcze nic nie kupiono!")

wyswietl = StringVar()
wyswietl.set("nacisnij przycisk aby zaczac!")

cenaAuto_wyswietl = StringVar()
cenaAuto_wyswietl.set(f"Koszt: {cenaAuto:.0f} klikniec")

ile_razy_kupiono_autoclicker_wyswietl = StringVar()
ile_razy_kupiono_autoclicker_wyswietl.set("Jeszcze nic nie kupiono!")

ile_na_sekunde_autoclicker = StringVar()
ile_na_sekunde_autoclicker.set(f"Klikniec na sekunde: {ile_razy_kupiono_autoclicker*4}")
#funckje
def zapisz_stan(nazwaokna):
    plik_zapisu = open("saves\\save.txt","w")
    plik_zapisu.write(f"{click}\n{ile_razy_kupiono_mult}\n{ile_razy_kupiono_autoclicker}\n{cenaMult}\n{cenaAuto}")
    label_zapisano = tk.Label(
        nazwaokna,
        text="Zapisano!",
        font=("gothic", 20)
    )
    label_zapisano.place(x=150, y=200)
    root.after(2000,label_zapisano.destroy)
    plik_zapisu.close()
def wczytaj_stan(nazwaokna):
    global click
    global ile_razy_kupiono_mult
    global ile_razy_kupiono_autoclicker
    global cenaMult
    global cenaAuto
    plik_zapisu = open("saves\save.txt","r")
    dane = plik_zapisu.readlines()
    click = float(dane[0])
    ile_razy_kupiono_mult = int(dane[1])
    ile_razy_kupiono_autoclicker = int(dane[2])
    cenaMult = float(dane[3])
    cenaAuto = float(dane[4])
    plik_zapisu.close()
    wyswietl.set(f"{click:.0f}")
    ile_razy_kupiono_mult_wyswietl.set("Kupiono: "+str(ile_razy_kupiono_mult))
    ile_razy_kupiono_autoclicker_wyswietl.set("Kupiono: "+str(ile_razy_kupiono_autoclicker))
    cenaMult_wyswietl.set(f"Koszt: {cenaMult:.0f} klikniec")
    cenaAuto_wyswietl.set(f"Koszt: {cenaAuto:.0f} klikniec")
    ile_na_sekunde_autoclicker.set(f"Klikniec na sekunde: {ile_razy_kupiono_autoclicker*4}")
    label_wczytano = tk.Label(
        nazwaokna,
        text="Wczytano!",
        font=("gothic", 20)
    )
    label_wczytano.place(x=150, y=200)
    root.after(2000,label_wczytano.destroy)
    if ile_razy_kupiono_autoclicker > 0:
        liczbaKlikniecSekunda.place(x=395, y=220, anchor = tk.CENTER)
        auto_clicker()


def auto_clicker():
    global click
    global ile_razy_kupiono_autoclicker
    if ile_razy_kupiono_autoclicker > 0:
        click += ile_razy_kupiono_autoclicker
        wyswietl.set(f"{click:.0f}")
    root.after(250, auto_clicker)   

def akcja_guzik():
    global click
    global ile_razy_kupiono_mult
    click += 1*ile_razy_kupiono_mult
    wyswietl.set(f"{click:.0f}")

def ile_kupiono(numer):
    global ile_razy_kupiono_mult
    global ile_razy_kupiono_mult_wyswietl
    global click
    global cenaMult
    global cenaMult_wyswietl
    global cenaAuto
    global ile_razy_kupiono_autoclicker
    match numer:
        case 0:
            if click >= cenaMult:
                ile_razy_kupiono_mult += 1
                ile_razy_kupiono_mult_wyswietl.set("Kupiono: "+str(ile_razy_kupiono_mult))
                click -= cenaMult
                cenaMult += cenaMult*0.2
                wyswietl.set(f"{click:.0f}")
                cenaMult_wyswietl.set(f"Koszt: {cenaMult:.0f} klikniec")
            elif click < cenaMult:
                messagebox.showinfo("Sklep","Nie masz wystarczajaco klikniec")
        case 1:
            if click >= cenaAuto:
                ile_razy_kupiono_autoclicker += 1
                ile_razy_kupiono_autoclicker_wyswietl.set("Kupiono: "+str(ile_razy_kupiono_autoclicker))
                click -= cenaAuto
                cenaAuto += cenaAuto*0.2
                wyswietl.set(f"{click:.0f}")
                ile_na_sekunde_autoclicker.set(f"Klikniec na sekunde: {ile_razy_kupiono_autoclicker*4}")
                if ile_razy_kupiono_autoclicker == 1:
                    auto_clicker()
                if ile_razy_kupiono_autoclicker > 0:
                    liczbaKlikniecSekunda.place(x=395, y=220, anchor = tk.CENTER)
                cenaAuto_wyswietl.set(f"Koszt: {cenaAuto:.0f} klikniec")
            elif click < cenaAuto:
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
        textvariable = cenaMult_wyswietl,
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
        command =lambda: ile_kupiono(0)
    )
    napis_autoclicker = tk.Label(
        nazwaokna,
        text = ItemkiSklep[1],
        font=("gothic",30)
    )
    podnapis_autoclicker = tk.Label(
        nazwaokna,
        textvariable= cenaAuto_wyswietl,
        font=("gothic", 16)
    )
    guzik_kup_autoclicker = tk.Button(
        nazwaokna,
        text = "Kup",
        width = 12,
        height = 3,
        relief = "ridge",
        command=lambda: ile_kupiono(1)
    )
    ile_autoclicker = tk.Label(
        nazwaokna,
        textvariable = ile_razy_kupiono_autoclicker_wyswietl,
        font=("gothic", 20)
    )
    napis_multiplier.place(x = 50, y = 100)
    podnapis_multiplier.place(x = 150, y = 150)
    guzik_kup_multiplier.place(x = 300, y = 100)
    ile_multiplier.place(x = 400, y = 100)
    napis_autoclicker.place(x = 50, y = 300)
    podnapis_autoclicker.place(x = 150, y = 350)
    guzik_kup_autoclicker.place(x = 300, y = 300)
    ile_autoclicker.place(x = 400, y = 300)
#otwiera pop-upa
def guzik_sklep():
    oknosklep = Toplevel(root)
    oknosklep.geometry("800x600+1050+200")
    oknosklep.resizable(False,False)   
    oknosklep.title("Sigma Clicker - Sklep")
    oknosklep.iconbitmap(r"assets\icon.ico")
    sklep_interface(oknosklep)
#interfejs zapisu i wczytywania
def zapis_i_wczytaj_interface(nazwaokna):
    zapisztext = tk.Label(
        nazwaokna,
        text = "Zapisz stan gry",
        font = ("gothic", 30)
    )
    wczytajtext = tk.Label(
        nazwaokna,
        text = "Wczytaj stan gry",
        font = ("gothic", 30)
    )
    guzik_zapisz = tk.Button(
        nazwaokna,
        text = "Zapisz",
        width = 22,
        height = 3,
        relief = "ridge",
        command=lambda: zapisz_stan(nazwaokna)
    )
    guzik_wczytaj = tk.Button(
        nazwaokna,
        text = "Wczytaj",
        width = 22,
        height = 3,
        relief = "ridge",
        command =lambda :wczytaj_stan(nazwaokna)
    )
    guzik_zapisz.place(x=120, y=100)
    guzik_wczytaj.place(x=120, y=250)
    zapisztext.place(x=50, y=50)
    wczytajtext.place(x=50, y=200)
def guzik_zapis_i_wczytaj():
    okno_zapis_i_wczytaj = Toplevel(root)
    okno_zapis_i_wczytaj.geometry("400x350+550+300")
    okno_zapis_i_wczytaj.resizable(False,False)
    okno_zapis_i_wczytaj.title("Sigma Clicker - Zapis i Wczytaj")
    okno_zapis_i_wczytaj.iconbitmap(r"assets\save&load.ico")
    zapis_i_wczytaj_interface(okno_zapis_i_wczytaj)
    #WAZNE - funkcje zapisu i wczytywania nie sa jeszcze zaimplementowane
#label odpowiedzialny za wyswietlanie ilosci klikniec
liczbaKlikniec = tk.Label(
    root,
    textvariable=wyswietl,
    bd = 0,
    font=("gothic", 40)
)
liczbaKlikniecSekunda = tk.Label(
    root,
    textvariable = ile_na_sekunde_autoclicker,
    bd = 0,
    font=("gothic", 20)
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
guzikZapisIWczytaj = tk.Button(
    root,
    image = IkonaZapisIWczytaj,
    command = guzik_zapis_i_wczytaj
)
#autoclicker
#komendy do ulozenia danych rzeczy (place, mainloop itd)
#guzki sklepu
guzik.place(x = 50, y = 300)
guzikSklep.place(x = 750, y = 20)
#guziki zapisu stanu gry
guzikZapisIWczytaj.place(x = 680, y = 20)
liczbaKlikniec.place(x=395, y=150, anchor = tk.CENTER)
if ile_razy_kupiono_autoclicker > 0:
    ile_na_sekunde_autoclicker.place(x=395, y=220, anchor = tk.CENTER)
root.mainloop()