# zadanie 1
print("podaj tekst")
text = input()
print("podaj separator źródłowy")
sep_zrodlowy = input()
print("podaj separator docelowy")
sep_docelowy = input()

text2 = sep_docelowy.join(text.split(sep_zrodlowy))

print(text2)

# zadanie 2

zad2_text = "Lorem Ipsum jest tekstem stosowanym jako przykładowy wypełniacz w przemyśle poligraficznym. Został po raz pierwszy użyty w XV w. przez nieznanego drukarza do wypełnienia tekstem próbnej książki. Pięć wieków później zaczął być używany przemyśle elektronicznym, pozostając praktycznie niezmienionym. Spopularyzował się w latach 60. XX w. wraz z publikacją arkuszy Letrasetu, zawierających fragmenty Lorem Ipsum, a ostatnio z zawierającym różne wersje Lorem Ipsum oprogramowaniem przeznaczonym do realizacji druków na komputerach osobistych, jak Aldus PageMaker"

#zadanie 3
nazwisko = "Walczak"
litera1 = nazwisko[2]
# modyfikacja co do zadania 3 litera nazwiska i 3 litera imienia, w przeciwnym razie litera c występuje 2 razy
imie="Kacper"
litera2 = imie[2]

liczba_liter1 = zad2_text.count(litera1)
liczba_liter2 = zad2_text.count(litera2)
print("W tekście jest ",liczba_liter1," liter ",litera1," oraz ",liczba_liter2," liter ",litera2)