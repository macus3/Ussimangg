from tkinter import * 
import random

raskustase = str.lower(input("Vali mangu raskustase; lihtne(L), keskmine(K), raske(R), voimatu(V): "))

if raskustase == "lihtne" or raskustase == 'l':

    MANGULAIUS = 700
    MANGUKORGUS = 700
    KIIRUS = 200
    SUURUS = 70
    USSIKEHA = 5

elif raskustase == 'keskmine' or raskustase == 'k':

    MANGULAIUS = 700
    MANGUKORGUS = 700
    KIIRUS = 100
    SUURUS = 50
    USSIKEHA = 3

elif raskustase == 'raske' or raskustase == 'r':

    MANGULAIUS = 700
    MANGUKORGUS = 700
    KIIRUS = 50
    SUURUS = 25
    USSIKEHA = 3

elif raskustase == 'voimatu' or raskustase == 'v': 

    MANGULAIUS = 700
    MANGUKORGUS = 700
    KIIRUS = 25
    SUURUS = 25
    USSIKEHA = 1  

else:
    print("Proovi uuesti!!!")

USSIVARV = '#0000FF' #sinine
OUNAVARV = '#FF0000' #punane
TAUSTAVARV = '#00FF00' #roheline
 
class Uss:
    def __init__(self):
        self.kehaSuurus = USSIKEHA
        self.coordinates = []
        self.ruudud = []

        for i in range (0, USSIKEHA):
            self.coordinates.append([0,0])

        for x, y in self.coordinates:
            ruut = aluspind.create_rectangle(x, y, x + SUURUS, y + SUURUS, fill=USSIVARV, tag='uss')
            self.ruudud.append(ruut)

class Oun:
    
    def __init__(self):
        x = random.randint(0, (MANGULAIUS/SUURUS)-1) * SUURUS
        y = random.randint(0, (MANGUKORGUS/SUURUS)-1) * SUURUS

        self.coordinates = [x, y]

        aluspind.create_oval(x, y, x + SUURUS, y + SUURUS, fill=OUNAVARV, tag= 'oun')

def jargmineLiigutus(uss, oun):
    
    x, y = uss.coordinates[0]

    if suund == "ules":
        y -= SUURUS
    elif suund == "alla":
        y += SUURUS
    elif suund == "vasakule":
        x -= SUURUS
    elif suund == "paremale":
        x += SUURUS

    uss.coordinates.insert(0, (x, y))

    ruut = aluspind.create_rectangle(x, y, x + SUURUS, y + SUURUS, fill=USSIVARV)

    uss.ruudud.insert(0, ruut)

    if x == oun.coordinates[0] and y == oun.coordinates[-1]:

        global skoor

        skoor += 1

        kiri.config(text="Skoor on {}".format(skoor))

        aluspind.delete("oun")

        oun = Oun()

    else: 
        del uss.coordinates[-1]

        aluspind.delete(uss.ruudud[-1])

        del uss.ruudud[-1]

    if kokkuporked(uss):
        manglabi()
    
    else:
        aken.after(KIIRUS, jargmineLiigutus, uss, oun)

def suunamuutus(uusSuund):
    global suund 

    if uusSuund == 'vasakule':
        if suund != 'paremale':
            suund = uusSuund
    elif uusSuund == 'paremale':
        if suund != 'vasakule':
            suund = uusSuund
    elif uusSuund == 'alla':
        if suund != 'ules':
            suund = uusSuund
    elif uusSuund == 'ules':
        if suund != 'alla':
            suund = uusSuund

def kokkuporked(uss):
    
    x, y = uss.coordinates[0]

    if x < 0 or x >= MANGULAIUS:
        return True
        
    if y < 0 or y >= MANGUKORGUS:
        return True

    for kehaosa in uss.coordinates[1:]:
        if x == kehaosa[0] and y == kehaosa[1]:
            return True
        
    return False

def restart_game(even=None):
    global uss, oun, skoor, suund
    aluspind.delete(ALL)
    uss = Uss()
    oun = Oun()
    skoor = 0
    suund = 'alla'
    kiri.config(text="Skoor on {}".format(skoor), font=('comic sans', 40))
    jargmineLiigutus(uss, oun)

def manglabi():
    aluspind.delete(ALL)
    aluspind.create_text(aluspind.winfo_width()/2, aluspind.winfo_height()/2, font=('comic sans', 70), fill='black',text="MANG LABI LOL", tag="manglabi")
    aluspind.create_text(aluspind.winfo_width()/2, aluspind.winfo_height()/3, font=('comic sans', 40),fill='black', text="Vajuta klahvi R, et uuesti proovida", tag="restart")

aken = Tk()
aken.title("Ussimang")
aken.resizable(False, False)


skoor = 0
suund = 'alla'

kiri = Label(aken, text="Skoor on {}".format(skoor), font=('comic sans', 40))
kiri.pack()

aluspind = Canvas(aken, bg = TAUSTAVARV, height = MANGUKORGUS, width = MANGULAIUS)
aluspind.pack()

aken.update()

aken.bind('<Left>', lambda event: suunamuutus('vasakule'))
aken.bind('<Right>', lambda event: suunamuutus('paremale'))
aken.bind('<Up>', lambda event: suunamuutus('ules'))
aken.bind('<Down>', lambda event: suunamuutus('alla'))
aken.bind('a', lambda event: suunamuutus('vasakule'))
aken.bind('d', lambda event: suunamuutus('paremale'))
aken.bind('w', lambda event: suunamuutus('ules'))
aken.bind('s', lambda event: suunamuutus('alla'))
aken.bind('r', restart_game)
aken.bind('<Escape>', exit)

uss = Uss()
oun = Oun()

jargmineLiigutus(uss, oun)

aken.mainloop()