from tkinter import *
from tkinter import font
import pygame 
from tkinter import filedialog
import os

langas = Tk()
virsus = Frame(langas)
apacia = Frame(langas)
apacia2 = Frame(langas)
langas.geometry("550x800")

pygame.init()

# Screenas/Listas
scrollbaras = Scrollbar(virsus)
screenas = Listbox(virsus, yscrollcommand=scrollbaras.set, width=43, height=4, bg='grey', fg='orange')
scrollbaras.config(command=screenas.yview)
bolded = font.Font(weight='bold') 
screenas.config(font=bolded)

# Garsu listas
scrollbaras2 = Scrollbar(apacia)
listas_instrument = Listbox(apacia, yscrollcommand=scrollbaras2.set, width=20, height=5)
scrollbaras2.config(command=listas_instrument.yview)

sarasas = ['gitara', 'AfroDrum', 'D', 'bass1', "kick2", 'guiro']
listas_instrument.insert(END, *sarasas)

# Garsu listas 2
scrollbaras3 = Scrollbar(apacia)
listas2 = Listbox(apacia, yscrollcommand=scrollbaras.set, width=20, height=5)
scrollbaras3.config(command=listas2.yview)

paspaustas=None
kas_groja = []
seka = []

# screen tekstas
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
    seka.append(paspaustas[-2])
    screenas.insert(END, *kas_groja)
    kas_groja.pop()
    print(paspaustas)

def playC(event):
    global paspaustas
    paspaustas='Garsas "C"'
    kas_groja.append(paspaustas)
    seka.append(paspaustas[-2])
    screenas.insert(END, *kas_groja)
    kas_groja.pop()
    print(paspaustas)

def playD(event):
    global paspaustas
    paspaustas='Garsas "D"'
    kas_groja.append(paspaustas)
    seka.append(paspaustas[-2])
    screenas.insert(END, *kas_groja)
    kas_groja.pop()
    print(paspaustas)

def playE(event):
    global paspaustas
    paspaustas='Garsas "E"'
    kas_groja.append(paspaustas)
    seka.append(paspaustas[-2])
    screenas.insert(END, *kas_groja)
    kas_groja.pop()
    print(paspaustas)

def playF(event):
    global paspaustas
    paspaustas='Garsas "F"'
    kas_groja.append(paspaustas)
    seka.append(paspaustas[-2])
    screenas.insert(END, *kas_groja)
    kas_groja.pop()
    print(paspaustas)

# seka
def paspaustas_list(event):
    seka_baras['text'] = seka
    print(seka)

# sekos istrynimas
def paspausto_listo_clear(event):
    seka.clear()
    seka_baras['text'] = seka
    seka_baras['text'] = ''

def pauze(event):
    pygame.mixer.stop()

# pagr garsai
def hihat(event):
    hihatas = 'Hihat:'
    kas_groja.append(hihatas)
    screenas.insert(END, *kas_groja)
    kas_groja.pop()
    sound = pygame.mixer.Sound("audio/hi hat.WAV")
    sound.play()
    playA(event)

def clap(event):
    kickas = 'Clap:'
    kas_groja.append(kickas)
    screenas.insert(END, *kas_groja)
    kas_groja.pop()
    sound = pygame.mixer.Sound("audio/clap.WAV")
    sound.play()
    playB(event)

def crash(event):
    crashas = 'Crash:'
    kas_groja.append(crashas)
    screenas.insert(END, *kas_groja)
    kas_groja.pop()
    sound = pygame.mixer.Sound(("audio/crash2.wav"))
    sound.play()
    playC(event)

def bass(event):
    bass = 'Bass:'
    kas_groja.append(bass)
    screenas.insert(END, *kas_groja)
    kas_groja.pop()
    sound = pygame.mixer.Sound(("audio/bass.WAV"))
    sound.play()
    playD(event)

def kick(event):
    kickas = 'Kick:'
    kas_groja.append(kickas)
    screenas.insert(END, *kas_groja)
    kas_groja.pop()
    sound = pygame.mixer.Sound(("audio/kick.wav"))
    sound.play()
    playE(event)

def tom(event):
    tomas = 'Tom:'
    kas_groja.append(tomas)
    screenas.insert(END, *kas_groja)
    kas_groja.pop()
    sound = pygame.mixer.Sound(("audio/tom.wav"))
    sound.play()
    playF(event)

# papildomi garsai liste
def gitara1(event):
    klavisas = 'Gitara: (D)'
    kas_groja.append(klavisas)
    seka.append(klavisas[-2])
    screenas.insert(END, *kas_groja)
    kas_groja.pop()
    sound = pygame.mixer.Sound("audio/gitara.wav")
    sound.play()

def bass1(event):
    klavisas = 'Bass1: (D)'
    kas_groja.append(klavisas)
    seka.append(klavisas[-2])
    screenas.insert(END, *kas_groja)
    kas_groja.pop()
    sound = pygame.mixer.Sound("audio/bass.wav")
    sound.play()

def afrodrum(event):
    klavisas = 'Afrodrum: (D)'
    kas_groja.append(klavisas)
    seka.append(klavisas[-2])
    screenas.insert(END, *kas_groja)
    kas_groja.pop()
    sound = pygame.mixer.Sound("audio/afrodrum.wav")
    sound.play()

def kick2(event):
    klavisas = 'Kick2: (D)'
    kas_groja.append(klavisas)
    seka.append(klavisas[-2])
    screenas.insert(END, *kas_groja)
    kas_groja.pop()
    sound = pygame.mixer.Sound("audio/kick2.wav")
    sound.play()
    
def guiro(event):
    klavisas = 'Guiro: (D)'
    kas_groja.append(klavisas)
    seka.append(klavisas[-2])
    screenas.insert(END, *kas_groja)
    kas_groja.pop()
    sound = pygame.mixer.Sound("audio/guiro.wav")
    sound.play()

# loopai
def radiob_loop_on_a():
    looping_on = None
    sound1 = pygame.mixer.Sound(("audio/hi hat.WAV"))
    if a.get() == 1:
        looping_on = 1000
    else:
        looping_on = 0
        pygame.mixer.stop()
    sound1.play(loops=looping_on)

def radiob_loop_on_b():
    looping_on = None
    sound2 = pygame.mixer.Sound(("audio/clap.WAV"))
    if b.get() == 1:
        looping_on = 1000
    else:
        looping_on = 0
        pygame.mixer.stop()
    sound2.play(loops=looping_on)

def radiob_loop_on_f():
    looping_on = None
    sound3 = pygame.mixer.Sound(("audio/tom.wav"))
    if f.get() == 1:
        looping_on = 1000
    else:
        looping_on = 0
        pygame.mixer.stop()
    sound3.play(loops=looping_on)

# metronomui

def metronomas():
    kartai = None
    sound_met= pygame.mixer.Sound("audio/metronomas.wav")
    sound_met.set_volume(0.75)
    if m.get() == 1:
        kartai = 1000
    else:
        kartai = 0
        pygame.mixer.stop()
    sound_met.play(loops=kartai)

d_myg_text = StringVar()

# garsu idejimas i D mygtuka
def spausdinti(pasirinkta):
    pasirinkta = sarasas[listas_instrument.curselection()[0]]
    d_myg_text.set(str(pasirinkta)+'\nNum 1')
    if pasirinkta == 'gitara':
        d_mygtukas.bind("<Button-1>", gitara1)
        langas.bind("<KP_1>", gitara1)
    elif pasirinkta == "AfroDrum":
        d_mygtukas.bind("<Button-1>", afrodrum)
        langas.bind("<KP_1>", afrodrum)
    elif pasirinkta == 'D':
        d_mygtukas.bind("<Button-1>", bass)
        langas.bind("<KP_1>", bass)
    elif pasirinkta == 'bass1':
        d_mygtukas.bind("<Button-1>", bass1)
        langas.bind("<KP_1>", bass1)
    elif pasirinkta == 'kick2':
        d_mygtukas.bind("<Button-1>", kick2)
        langas.bind("<KP_1>", kick2)
    elif pasirinkta == 'guiro':
        d_mygtukas.bind("<Button-1>", guiro)
        langas.bind("<KP_1>", guiro)
    print(pasirinkta)

# Checkbox'am
k = IntVar()
a = IntVar()
b = IntVar()
f = IntVar()
m = IntVar()

audio_pav = ''

def open_file(event):
    global audio_pav
    audio_pav = filedialog.askopenfilename(filetypes=(("Audio Files", ".wav .ogg"),   ("All Files", "*.*")))

def grojimas(event):
   if audio_pav:
        garso_failas = pygame.mixer.Sound(audio_pav)
        garso_failas.play(loops=100)
        filename = os.path.basename(audio_pav)
        grojimo_baras['text'] = 'Groja:  ' + filename

# Objektai / Mygtukai
a_mygtukas = Button(apacia, text="A\nNum 4", fg='black', bg='#FF6600', height=5, width=9)
a_mygtukas.bind("<Button-1>", hihat)
langas.bind("<KP_4>", hihat)

b_mygtukas = Button(apacia, text="B\nNum 5", fg='black', bg='#FF781f', height=5, width=9)
b_mygtukas.bind("<Button-1>", clap)
langas.bind("<KP_5>", clap)

c_mygtukas = Button(apacia, text='C\nNum 6', fg='black', bg='#FFA501', height=5, width=9)
c_mygtukas.bind("<Button-1>", crash)
langas.bind("<KP_6>", crash)

d_mygtukas = Button(apacia, textvariable=d_myg_text, fg='black', bg='#ff8b3d',height=5, width=9)
d_myg_text.set("D\nNum 1")
d_mygtukas.bind("<Button-1>", bass)
langas.bind("<KP_1>", bass)

e_mygtukas = Button(apacia, text="E\nNum 2", fg='black', bg='#ff9d5c',height=5, width=9)
e_mygtukas.bind("<Button-1>", kick)
langas.bind("<KP_2>", kick)

f_mygtukas = Button(apacia, text="F\nNum 3", fg='black', bg='#cc5a2a',height=5, width=9)
f_mygtukas.bind("<Button-1>", tom)
langas.bind("<KP_3>", tom)

pasirinkti = Button(apacia, text="Pasirinkti", fg='black', bg='#cc5a2a',height=1, width=5)
pasirinkti.bind("<Button-1>", spausdinti)
langas.bind("<Return>", spausdinti)

pauze1 = Button(apacia, text="Stop", fg='black', bg='#cc5a2a',height=1, width=1)
pauze1.bind("<Button-1>", pauze)

atidaryti = Button(apacia, text="Atidaryti Faila", fg='black', bg='#cc5a2a',height=1, width=9)
atidaryti.bind("<Button-1>", open_file)

groti = Button(apacia, text="Groti Faila >", fg='black', bg='#cc5a2a',height=1, width=8)
groti.bind("<Button-1>", grojimas)

#remai
rem1 = Button(apacia, text="", fg='black', bg='#cc5a2a',height=1, width=9)
rem2 = Button(apacia, text="", fg='black', bg='#cc5a2a',height=1, width=20)
rem3 = Button(apacia, text="", fg='black', bg='#cc5a2a',height=1, width=20)

langas.bind('<KP_9>', paspaustas_list)
langas.bind('<KP_Divide>', paspausto_listo_clear )

# Objektai / Tekstas
label_seka = Label(apacia, text="Klavisu seka:")
seka_baras = Label(apacia, text='Seka tuscia', bd=5, relief=SUNKEN, wraplength=150)
grojimo_baras = Label(apacia, text='Failu Grojimas\nnevyksta', bd=5, relief=SUNKEN, wraplength=150, anchor=N)
klavisu_reiksmes1 = Label(apacia, text='Spausti "9" sekos rodymui')
klavisu_reiksmes2 = Label(apacia, text='Spausti "/" sekos trynimui')

# loopu checkoboxai
loopig_a = Checkbutton(apacia, text="A 1000x\nLoop", padx = 1, variable=a, onvalue=1, offvalue=0,command=radiob_loop_on_a, bg='#FF6600')
loopig_b = Checkbutton(apacia, text="B 1000x\nLoop", padx = 1, variable=b, onvalue=1, offvalue=0,command=radiob_loop_on_b, bg='#FF781f')
loopig_c = Checkbutton(apacia, text="F 1000X\nLoop", padx = 1, variable=f, onvalue=1, offvalue=0,command=radiob_loop_on_f, bg='#FFA501')

metronomas1 = Checkbutton(apacia, text="Metronomas", padx = 1, variable=m, onvalue=1, offvalue=0,command=metronomas, bg='#FFA501')

# isdestymas
virsus.pack()
apacia.pack()

screenas.grid(row=0, column=0)
listas_instrument.grid(row=0, column=0)
# listas2.grid(row=1,column=0) toj vietoj radio button
scrollbaras.grid(row=0, column=1,sticky=N+S)
scrollbaras2.grid(row=0, column=0,sticky=E+S)

# mytgukai A,B,C,D,E,F
a_mygtukas.grid(row=0,column=1)
b_mygtukas.grid(row=0,column=2)
c_mygtukas.grid(row=0,column=3)
d_mygtukas.grid(row=1,column=1)
e_mygtukas.grid(row=1,column=2)
f_mygtukas.grid(row=1,column=3)

# text / radio_b
label_seka.grid(row=2, column=0)
klavisu_reiksmes1.grid(row=3, column=0)
rem1.grid(row=2, column=0)
klavisu_reiksmes2.grid(row=4, column=0)
rem2.grid(row=3, column=0)
pasirinkti.grid(row=1, column=0)
rem3.grid(row=4, column=0)
loopig_a.grid(row=3, column=1)
loopig_b.grid(row=3, column=2)
loopig_c.grid(row=3, column=3)
pauze1.grid(row=4,column=1)
metronomas1.grid(row=4, column=2)
atidaryti.grid(row=5, column=1)
groti.grid(row=5, column=2)
grojimo_baras.grid(row=5, column=0)
seka_baras.grid(row=6, column=0)

langas.mainloop()