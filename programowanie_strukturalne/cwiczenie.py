'''
#potegaowanie
potega = 3**3
print(potega)
'''
'''
#podawanie zmiennej
zmienna = input("Podaj zmienna: ")

#wyswietlanie z mnozeniem stringa
print("Zmienna to " + 3*zmienna)

#wyswiatlanie dlugosci stringa konwersja na int
dl = len(zmienna)
print(dl)

#wyswietlanie typu danych
print(type(dl))
print(type(zmienna))

wiek = input("Podaj wiek: ")
print("\nTwój wiek to " + wiek + " lat")
'''
'''
#wyswietlanie znaku z tablicy srtingow
znaki = 'Mateusz'
znak = znaki[2]
print(znak)
'''
'''
#konwersja
x = "5.123"
print(type(x))
print(x)
x = float(x)
print(type(x))
print(x)
'''
'''
#wyswietalnie stringa z parametrami
naz  = 'Collegium Da Vinci'
print(naz[0:12])
print(naz[0:12:2])
print(naz[-5:] + naz[0:10])
'''
'''
#towrzenie listy ze stringa
zw = "Kot, pies, ryba"
print(type(zw))
print(zw)
lista = zw.split(", ")
print(type(lista))
print(lista)
#wybranie elementu listy
print(lista[1])
'''
'''
#wyswietlanie łańcucha znaków
wersja = "{0}, PHP, {1}".format("Java", "JS", "CSS")
print(wersja)
#podmiana tekstu
zamiana = wersja.replace("Java", "C++")
print(zamiana)
'''
'''
#funkcje matematyczne
#import biblioteki math
import math
pi = math.pi
pierw = math.sqrt(7)
print("Liczba pi:",pi)
print("Pierwiastek z 7 to:",pierw)
#import bibl random
import random
los = random.random()
print(los)
print(random.randint(0,100))
print(random.choice(["Ala", "Kot", "Ma"]))
'''
'''
import math
import random
x = input("podaj poczatek przedzialu: ")
s = input("podaj koniec przedzialu: ")
print(type(x))
print(type(s))
x = int(x)
s = int(s)
print(type(x))
print(type(s))
y = random.randint(x,s)
if x<0:
    print(x)
else:
    print(y)
'''
'''
import math
x = 9
y = math.pow(x,2)
print('->',y)
'''

'''
    Utwórz funkcję zwracającą iloczyn dwóch liczba, uzytkownik podaje dane z klawiatury
'''
'''
def iloczyn(liczba1,liczba2):
    il = liczba1*liczba2
    return il
liczbaPierwsza = int(input("Podaj pierwszy dzielnik: "))
liczbaDruga = int(input("Podaj drugi dzielnik: "))
#liczbaPierwsza = int(liczbaPierwsza)
#liczbaDruga = int(liczbaDruga)
#print(type(liczbaPierwsza))
#print(type(liczbaDruga))
print(f'Iloczyn 2 liczb to: {iloczyn(liczbaPierwsza,liczbaDruga)}')
'''

zaok = float(input('Podaj liczbe do zaokraglenia: '))
x = "{0:.3f}".format(zaok)
print(x)

zmiennaGlobalna = 10
print(f'\n\n Wartość zmiennaGlobalna: {zmiennaGlobalna}')
print(f'Id zmiennaGlobalna: {id(zmiennaGlobalna)}')

def spr():
	global zmiennaGlobalna					# global - przypisuje wartość globalnie, bez global po wyjściu z funkcji wartość wraca do poprzedniej
	zmiennaGlobalna = 20
	print(f'\n\n Wartość zmiennaGlobalna wewnątrz funkcji: {zmiennaGlobalna}')
	print(f'Id zmiennaGlobalna: {id(zmiennaGlobalna)}')


spr()

print(f'Wartośc zmiennaaGlobalna: {zmiennaGlobalna}')


