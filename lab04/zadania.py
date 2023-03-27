#Zadanie 1
import random
import sys
import this


liczba = int(input("Podaj liczbę: "))

print(bin(liczba))
print(oct(liczba))
print(hex(liczba))

#Zadanie 2

liczba2 = input("Podaj liczbę: ")

try:
    int(liczba2)
    print(f"{liczba2} może być rzutowane na typ int")
except ValueError:
    print(f"{liczba2} nie może być rzutowane na typ int")

try:
    float(liczba2)
    print(f"{liczba2} może być rzutowane na typ float")
except ValueError:
    print(f"{liczba2} nie może być rzutowane na typ float")


#Zadanie 3
print("Podaj liczbe do podzielenia: ")
liczba3 = int(sys.stdin.readline())
mnozniki=[]
potegi=[]

txt="Podaną liczbe można zapisać jako:"
for i in range(len(str(liczba3))):
    mnozniki.append(str(liczba3%(10**(i+1)))[0])
    potegi.append(str(10**(i)))


for j in range(len(potegi)-1, -1, -1):
    txt= txt + " " + potegi[j] + "*" + mnozniki[j]
    if(j!=0):
        txt+=" + "


print(txt)


#Zadanie 4

zad4_zdanie = input("Podaj zdanie: ")

zakodowane_zdanie = ""

for litera in zad4_zdanie:
    if litera in this.d:
        zakodowane_zdanie += this.d[litera]
    else:
        zakodowane_zdanie += litera

print(zakodowane_zdanie)


#Zadanie 5

zad5_zdanie = input("Podaj zdanie: ")
slowa= zad5_zdanie.split()
slowa = sorted(slowa, key=len)
print(slowa)

#Zadanie 6

wyrazenia1 = [
    'Koleżanki i koledzy',
    'Z drugiej strony',
    'Podobnie',
    'Nie zapominajmy jednak, że',
    'W ten oto sposób',
    'Praktyka dnia codziennego dowodzi, że',
    'Wagi i znaczenia tych problemów nie trzeba szerzej uzasadniać, ponieważ',
    'Różnorakie i bogate doświadczenia',
    'Troska organizacji, a szczególnie',
    'Wyższe założenia ideowe, a także'
]
wyrazenia2 = [
    'realizacja nakreślonych zadań programowych',
    'zakres i miejsce szkolenia kadr',
    'stały wzrost ilości i zakres naszej aktywności',
    'aktualna struktura organizacji',
    'nowy model działalności organizacyjnej',
    'stałe zabezpieczenie informacyjno programowe naszej działalności',
    'wzmacnianie i rozwijanie struktur',
    'konsultacja z szerokim aktywem',
    'rozpoczęcie powszechnej akcji kształtowania postaw'
]
wyrazenia3 = [
    'zmusza nas do przeanalizowania',
    'spełnia istotną rolę w kształtowaniu',
    'wymaga sprecyzowania i określenia',
    'pomaga w przygotowaniu i realizacji',
    'zabezpiecza udział szerokiej grupie w kształtowaniu',
    'spełnia ważne zadania w wypracowaniu',
    'umożliwia w większym stopniu tworzenie',
    'powoduje docenianie wagi',
    'przedstawia intersującą próbę sprawdzenia',
    'pociąga za sobą proces wdrażania i unowocześniania'
]
wyrazenia4 = [
    'istniejących warunków administracyjno-finansowych.',
    'dalszych kierunków rozwoju.',
    'systemu powszechnego uczestnictwa.',
    'postaw uczestników wobec zadań stawianych przez organizację.',
    'nowych propozycji.',
    'kierunków postępowego wychowania.',
    'systemu szkolenia kadry odpowiadającego potrzebom.',
    'odpowiednich waruknków aktywizacji.',
    'modelu rozwoju.',
    'form oddziaływania.'
]

liczba_zdan = int(input("Podaj liczbe w celu stworzenia zdan: "))

for i in range(liczba_zdan):
    print(f'{random.choice(wyrazenia1)} {random.choice(wyrazenia2)} {random.choice(wyrazenia3)} {random.choice(wyrazenia4)}')
