from tkinter import *
from tkinter import messagebox
from ListItems import db

database = db("lista.db")

def frissit():
    toDo_list.delete(0, END)
    for row in database.fetch():
        toDo_list.insert(END, row)

def hozzaad():
    if tipus_szoveg.get() == "" or tevekenyseg_szoveg.get() == "" or mikor_szoveg.get() == "":
        messagebox.showerror("HIBA", "Töltsd ki az összes mezőt!")
        return
    database.insert(tipus_szoveg.get(), tevekenyseg_szoveg.get(), mikor_szoveg.get())
    toDo_list.delete(0, END)
    toDo_list.insert(END, (tipus_szoveg.get(), tevekenyseg_szoveg.get(), mikor_szoveg.get()))
    ujra()
    frissit()

def kivalaszt(event):
    try:
        global kivalasztott
        index = toDo_list.curselection()[0]
        kivalasztott = toDo_list.get(index)
        tipus_be.delete(0, END)
        tipus_be.insert(END, kivalasztott[1])
        tevekenyseg_be.delete(0, END)
        tevekenyseg_be.insert(END, kivalasztott[2])
        mikor_be.delete(0, END)
        mikor_be.insert(END, kivalasztott[3])
    except IndexError:
        pass

def torles():
    database.remove(kivalasztott[0])
    ujra()
    frissit()

def modositas():
    database.update(kivalasztott[0], tipus_szoveg.get(), tevekenyseg_szoveg.get(), mikor_szoveg.get())
    frissit()

def ujra():
    tipus_be.delete(0, END)
    tevekenyseg_be.delete(0, END)
    mikor_be.delete(0, END)



# Létrehoz egy ablakot
app = Tk()

"""Típus"""

tipus_szoveg = StringVar()
tipus_cim = Label(app, text="Határidő", font=("bold", 12), pady=20)
tipus_cim.grid(row=0, column=0, sticky=W)
#input
tipus_be = Entry(app, textvariable=tipus_szoveg)
tipus_be.grid(row=0, column=1)

"""Mi"""

tevekenyseg_szoveg = StringVar()
tevekenyseg_cim = Label(app, text="Típus", font=("bold", 12), pady=20)
tevekenyseg_cim.grid(row=1, column=0, sticky=W)
#input
tevekenyseg_be = Entry(app, textvariable=tevekenyseg_szoveg)
tevekenyseg_be.grid(row=1, column=1)

"""Mikorra"""

mikor_szoveg = StringVar()
mikor_cim = Label(app, text="Tevékenység", font=("bold", 12), pady=20)
mikor_cim.grid(row=2, column=0, sticky=W)
#input
mikor_be = Entry(app, textvariable=mikor_szoveg)
mikor_be.grid(row=2, column=1)

"""Lista"""

toDo_list = Listbox(app, font=("bold", 14), height=20, width=70)
toDo_list.grid(row=5, column=0, columnspan=4, rowspan=3)

#kivalaszt
toDo_list.bind("<<ListboxSelect>>", kivalaszt)

"""Gombok"""

gomb_hozzaad = Button(app, text="Hozzáadás", width=12, command=hozzaad)
gomb_hozzaad.grid(row=3, column=0)

gomb_torles = Button(app, text="Törlés", width=12, command=torles)
gomb_torles.grid(row=3, column=1)

gomb_modosit = Button(app, text="Módosítás", width=12, command=modositas)
gomb_modosit.grid(row=3, column=2)

gomb_ujra = Button(app, text="Újraírás", width=12, command=ujra)
gomb_ujra.grid(row=3, column=3)

"""Görgő"""

scrollbar = Scrollbar(app)
scrollbar.grid(row=5, column=5)

#scroll -> lista

toDo_list.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=toDo_list.yview)

"""POP"""
frissit()


#Ablak
app.title("ToDoList")
app.geometry("725x600") 

# Programindítás
app.mainloop()
