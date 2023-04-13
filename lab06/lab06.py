import pandas as pd
from datetime import datetime
# zadanie 1 


df = pd.read_csv("lab06/pliki_wyjscia/zamowienia.csv", delimiter=";")

df["Utarg"] = df["Utarg"].str.replace(",", ".")
df["Utarg"] = df["Utarg"].str.replace(" ", "")

df["Data zamowienia"] = df["Data zamowienia"].apply(lambda x: datetime.strptime(x, "%d-%m-%Y").strftime("%Y-%m-%d"))

df_polska = df[df["Kraj"] == "Polska"]
df_niemcy = df[df["Kraj"] == "Niemcy"]

df_polska.to_csv("lab06/pliki_wejscia/zamowienia_polska.csv", sep=";", index=False)
df_niemcy.to_csv("lab06/pliki_wejscia/zamowienia_niemcy.csv", sep=";", index=False)

# zadanie 2 

def scalaniePlikow(nowy_plik, *pliki):
    with open("lab06/pliki_wyjscia/"+nowy_plik, "w") as nowy:
        for plik in pliki:
            with open("lab06/pliki_wejscia/"+plik, "r") as stary:
                nowy.write(stary.read())

# scalaniePlikow("wynik_zad1.txt", "1.txt", "2.txt")

# Zadanie 3
def zad3(lista,n):
    for element in lista:
        if not isinstance(element, (int, float)):
            return False
    rodzaj = input("Podaj cyfrę: czy lista ma byc rosnąco- 1 czy malejąco- 2: ")
    rodzaj = int(rodzaj)
    if rodzaj==1:
        lista.sort()
    elif rodzaj==2:
        lista.sort(reverse=True)
    else:
        print("Podałeś złą liczbę")
        return False
    print(lista[:n])

# zad3([1,2,3,10,12,3,12,3,5,12,78],2)


#Zadanie 4
def grupuj(lista):
    slownik={}
    for element in lista:
        rodzaj = type(element).__name__
        if rodzaj not in slownik:
            slownik[rodzaj]=[]
        slownik[rodzaj].append(element)
    print(slownik)

# grupuj([1, 2.3, 'Zbyszek', 5, 'Marian', 3.0])

#Zadanie 5

def imionaDoPlikow(lista):
    a_m = []
    n_z = []
    for imie in lista:
        if imie[0].lower() in 'abcdefghijklm':
            a_m.append(imie)
        else:
            n_z.append(imie)

    with open('lab06/pliki_wyjscia/A-M_nazwiska.txt', 'w') as plik:
        for imie in a_m:
            plik.write(imie + '\n')

    with open('lab06/pliki_wyjscia/N-Ż_nazwiska.txt', 'w') as plik:
        for imie in n_z:
            plik.write(imie + '\n')

# imionaDoPlikow(['Kowalski', 'Nowak', 'Smith', 'Johnson', 'Gonzalez', 'Zorro'])

# Zadanie6 

def odworoconeSlowa(text):
    words = text.split()
    reversed_words = [word[::-1] for word in words]
    print (' '.join(reversed_words))

# odworoconeSlowa("Ala ma kota")

# Zadanie 7

import random

def karty():
    kolor = ['pik', 'kier', 'karo', 'trefl']
    rodzaj = ['As', 'Król', 'Dama', 'Walet', '10', '9', '8', '7', '6', '5', '4', '3', '2']
    talia = [f'{rank} {suit}' for suit in kolor for rank in rodzaj]

    random.shuffle(talia)

    gracze = ['Ala', 'Piotras', 'Kacper', 'Marcel']
    rece = {}
    for gracz in gracze:
        reka = []
        for i in range(5):
            card = talia.pop()
            reka.append(card)
        rece[gracz] = reka

    for gracz, reka in rece.items():
        print(f'{gracz}: {reka}')

# karty()

# Zadanie 8

def emaile(domena):
    with open("lab06/pliki_wejscia/zad8.txt", 'r') as f:
        imiona = [line.strip() for line in f]

    wyniki = []
    for imie in imiona:
        imie = imie.lower().replace(' ', '.')
        imie = imie.translate(str.maketrans('ąćęłńóśźż', 'acelnoszz'))
        email = f'{imie}@{domena}'
        wyniki.append(email)


    with open('lab06/pliki_wyjscia/adresy_email.txt', 'w') as f:
        for i, imie in enumerate(imiona):
            f.write(f'{imie}, {wyniki[i]}\n')

# emaile('student.uwm.edu.pl')
# Zadanie 9