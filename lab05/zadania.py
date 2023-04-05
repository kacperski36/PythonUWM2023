import random
import math
from typing import Union, Tuple

# Zadanie 1

A = [1/x for x in range(1,11)]
B = [2**x for x in range(11)]
C = [x for x in B if x%4==0]

print(A)
print(B)
print(C)

# Zadanie 2
macierz = [[random.randint(0,100) for i in range(4)] for j in range(4)]
print(macierz)

lista = [macierz[i][i] for i in range(4)]
print(lista)

#Zadanie 3
zdanie = "Ala ma kota"
lista = zdanie.split(" ")

zad3 = [(slowo, [ord(litera) for litera in list(slowo)]) for slowo in lista]
print(zad3)

#Zadanie 4
Num = Union[int, float]

def row_kwadratowe(a: Num, b: Num, c: Num)-> Num :
    delta = b**2 - 4 * a * c
    if (delta < 0):
        # brak pierwiastków
        return -1
    elif (delta == 0):
        # jeden pierwiastek
        x = (-b) / (2 * a)
        return x
    else:
        # równanie ma dwa pierwiastki
        x1 = (- b - math.sqrt(delta)) / (2 * a)
        x2 = (- b + math.sqrt(delta)) / (2 * a)
        return x1, x2

print(row_kwadratowe(6,1,3))
print(row_kwadratowe(1,2,1))
print(row_kwadratowe(1,4,1))

# Zadanie 5
def kostka(n: int) -> list():
    kostka = dict.fromkeys([i for i in range(1, 7)], 0)
    for j in range(n):
        rzut = random.randint(1, 6)
        kostka[rzut] += 1
    return [(f'oczka: {k}', f'rzutów: {kostka[k]}') for k in range(6, 0, -1)]


print(kostka(5))
# zadanie 6

def ciag(* liczby):
    if len(liczby) == 0:
        return " "
    else:
        return sorted(liczby)

print(ciag())
print(ciag("Ala", "Kot","Andrzej", "Borysek", "Zebra", "Celina"))

#Zadanie 7
def punkty(**druzyny)->int:
    wyniki=0
    for druzyna in druzyny:
        wyniki += druzyny[druzyna]
    return wyniki 

print(punkty(arka=10, barca= 34, besiktas=5, anitech=45))