from string import ascii_lowercase, digits
# zadanie 1
lista = [1,2,3,4,5,6,7,8,9,10]
lista2=lista[5:]
lista=lista[:5]

print(lista)
print(lista2)

# zadanie 2

zad2_lista = lista + lista2
zad2_lista.insert(0,0)

print(zad2_lista)

#zadanie 3
txt=input("Wpisz tekst ")
txt = list(dict.fromkeys(list(txt.casefold().replace(' ', ''))))
print(txt)
txt.sort()
print(txt)
# zadanie 4

miesiace = {
    1: "styczeń",
    2: "luty",
    3: "marzec",
    4: "kwiecień",
    5: "maj",
    6: "czerwiec",
    7: "lipiec",
    8: "sierpień",
    9: "wrzesień",
    10: "piździernik",
    11: "listopad",
    12: "grudzień"
}

# zadanie 5
months = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December"
}

dictMonths = {
    "pl": miesiace,
    "en": months
}

print(dictMonths['pl'][4])
print(dictMonths['en'][4])

# Zadanie 6
ciag = "Marianna"
zad6 = dict.fromkeys(tuple(ciag), 1)
print(zad6)

# zadanie 7
znak_lower=0
znak_digits=0
txt2 = input('Podaj tekst: ')
znaki = dict.fromkeys(list(ciag.casefold()))

for znak in znaki:
    if(znak in ascii_lowercase):
        znak_lower+=1
    elif(znak in digits):
        znak_digits+=1

znak_lower=znak_lower/len(ascii_lowercase)*100
znak_digits=znak_digits/len(digits)*100

print("W tekście jest ",znak_lower," /% ascii_lowercase oraz ",znak_digits,"/% digits ")
