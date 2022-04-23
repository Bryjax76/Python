import os
import random
from turtle import clear

x = ["Katar","Ekwador","Niemcy","Holandia","Anglia","Iran","USA","Walia","Argentyna","Arabia Saudyjska","Meksyk","Polska","Francja","Australia","Dania","Tunezja"]
kraj = ["Katar","Ekwador","Niemcy","Holandia","Anglia","Iran","USA","Walia","Argentyna","Arabia Saudyjska","Meksyk","Polska","Francja","Australia","Dania","Tunezja"]

liczba = 4
grupaA = []
grupaB = []
grupaC = []
grupaD = []

def randGrupy():
    while (len(kraj) == 16):
        for i in range(liczba):
            rand = random.choice(kraj)
            grupaA.append(rand)
            kraj.remove(rand)
        for i in range(liczba):
            rand = random.choice(kraj)
            grupaB.append(rand)
            kraj.remove(rand)
        for i in range(liczba):
            rand = random.choice(kraj)
            grupaC.append(rand)
            kraj.remove(rand)
        for i in range(liczba):
            rand = random.choice(kraj)
            grupaD.append(rand)
            kraj.remove(rand)
        if (len(kraj) == 0):
            checkGrupy()
       
def checkGrupy():
    if 'Polska' in grupaA and 'Niemcy' in grupaA:
        print('Gr. 1: Niemcy i Polska są razem')
        reverseGrupy()
        randGrupy()      
    elif 'Polska' in grupaB and 'Niemcy' in grupaB:
        print('Gr. 2: Niemcy i Polska są razem')
        reverseGrupy()
        randGrupy()
    elif 'Polska' in grupaC and 'Niemcy' in grupaC:
        print('Gr. 3: Niemcy i Polska są razem')
        reverseGrupy()
        randGrupy()
    elif 'Polska' in grupaD and 'Niemcy' in grupaD:
        print('Gr. 4: Niemcy i Polska są razem')
        reverseGrupy()
        randGrupy()
    else:
        print("###########################")
        print(grupaA)
        print(grupaB)
        print(grupaC)
        print(grupaD)
        print("###########################")
        
sum = grupaA+grupaB+grupaC+grupaD

def reverseGrupy():
    print("!!!! ERROR !!!!")
    print(grupaA)
    print(grupaB)
    print(grupaC)
    print(grupaD)
    print("!!!! ERROR !!!!")
    grupaA.clear()
    grupaB.clear()
    grupaC.clear()
    grupaD.clear()
    kraj.clear()
    for each in x:
        kraj.append(each)

randGrupy()

