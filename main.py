from tkinter import *
from tkinter import font

langas = Tk()
virsus = Frame(langas)
apacia = Frame(langas)
apacia2 = Frame(langas)


class Pagrindinis:
    def __init__(self, master):
        self.master = master

# Screenas/Listas
scrollbaras = Scrollbar(virsus)
screenas = Listbox(virsus, yscrollcommand=scrollbaras.set, width=43, height=4, bg='grey', fg='orange')
scrollbaras.config(command=screenas.yview)
bolded = font.Font(weight='bold') 
screenas.config(font=bolded)

# Garsu listas
scrollbaras2 = Scrollbar(apacia)
listas = Listbox(apacia, yscrollcommand=scrollbaras.set, width=20, height=5)
scrollbaras2.config(command=listas.yview)

# Garsu listas 2
scrollbaras3 = Scrollbar(apacia)
listas2 = Listbox(apacia, yscrollcommand=scrollbaras.set, width=20, height=5)
scrollbaras3.config(command=listas2.yview)

paspaustas=None
kas_groja = []
seka = []


# Klavisu f-jos
def playA(event):
    global paspaustas
    paspaustas='Garsas "A"'
    kas_groja.append(paspaustas)
    seka.append(paspaustas[-2])
    screenas.insert(END, *kas_groja)
    kas_groja.pop()
    print(paspaustas)

def playB(event):
    global paspaustas
    paspaustas='Garsas "B"'
    kas_groja.append(paspaustas)
    seka.append(paspaustas[-1])
    screenas.insert(END, *kas_groja)
    kas_groja.pop()
    print(paspaustas)

def playC(event):
    global paspaustas
    paspaustas='Garsas "C"'
    kas_groja.append(paspaustas)
    seka.append(paspaustas[-2])
    screenas.insert(END, *kas_groja)
    print(paspaustas)

def playD(event):
    global paspaustas
    paspaustas='Garsas "D"'
    kas_groja.append(paspaustas)
    seka.append(paspaustas[-2])
    screenas.insert(END, *kas_groja)
    print(paspaustas)

def playE(event):
    global paspaustas
    paspaustas='Garsas "E"'
    kas_groja.append(paspaustas)
    seka.append(paspaustas[-2])
    screenas.insert(END, *kas_groja)
    print(paspaustas)

def playF(event):
    global paspaustas
    paspaustas='Garsas "F"'
    kas_groja.append(paspaustas)
    seka.append(paspaustas[-2])
    screenas.insert(END, *kas_groja)
    print(paspaustas)

def paspaustas_list(event):
    seka_baras['text'] = seka
    print(seka)

def paspausto_listo_clear(event):
    seka.clear()
    seka_baras['text'] = seka
    seka_baras['text'] = ''

# Objektai / Mygtukai
a_mygt = Button(apacia, text="A", height=5, width=9)
a_mygt.bind("<Button-1>", playA)
langas.bind("<KP_4>", playA)

b_mygt = Button(apacia, text="B", height=5, width=9)
b_mygt.bind("<Button-1>", playB)
langas.bind("<KP_5>", playB)

c_mygt = Button(apacia, text="C", height=5, width=9)
c_mygt.bind("<Button-1>", playC)
langas.bind("<KP_6>", playC)

d_mygt = Button(apacia, text="D", height=5, width=9)
d_mygt.bind("<Button-1>", playD)
langas.bind("<KP_1>", playD)

e_mygt = Button(apacia, text="E", height=5, width=9)
e_mygt.bind("<Button-1>", playE)
langas.bind("<KP_2>", playE)

f_mygt = Button(apacia, text="F", height=5, width=9)
f_mygt.bind("<Button-1>", playF)
langas.bind("<KP_3>", playF)

langas.bind('<KP_9>', paspaustas_list)
langas.bind('<KP_Divide>', paspausto_listo_clear )

# Objektai / Tekstas
label_seka = Label(apacia, text="Klavisu seka:")
seka_baras = Label(apacia, text='Seka tuscia', bd=5, relief=SUNKEN, wraplength=150)
klavisu_reiksmes1 = Label(apacia, text='Spausti "9" sekos rodymui')
klavisu_reiksmes2 = Label(apacia, text='Spausti "/" sekos istrynimui')

langas.geometry("550x400")

# isdestymas
virsus.pack()
apacia.pack()

screenas.grid(row=0, column=0)
listas.grid(row=0, column=0)
listas2.grid(row=1,column=0)
scrollbaras.grid(row=0, column=1,sticky=N+S)

# mytgukai A,B,C,D,E,F
a_mygt.grid(row=0,column=1)
b_mygt.grid(row=0,column=2)
c_mygt.grid(row=0,column=3)
d_mygt.grid(row=1,column=1)
e_mygt.grid(row=1,column=2)
f_mygt.grid(row=1,column=3)

# text
label_seka.grid(row=2, column=0)
seka_baras.grid(row=3, column=0)
klavisu_reiksmes1.grid(row=4, column=0)
klavisu_reiksmes2.grid(row=5, column=0)


langas.mainloop()