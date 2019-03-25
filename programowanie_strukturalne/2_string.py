#tablica string
text = "Anna, paweł, JuLiA"

lista = text.split(", ")
print(text)
print(lista)
print(type(lista))

imie1 = lista[0]
print("Twoje imie to:",imie1)
'''
#zwiekszenie na drukowane
imieDuze = imie1.upper()#ANNA
print(imieDuze)

imieMale = imie1.lower()#anna
print(imieMale)

print(imie1)#Anna

#sprawdzanie zawartosci True/False
nazwisko = input("Podaj swoje nazwsko: ")
zawartosc = nazwisko.isalpha()
print(zawartosc)
#sprawdzic dlaczego przy liczbach jest False

nazwisko = ""
print(nazwisko.isalpha())
'''
text1 = "Julia\n"
text2 = "Nowak"
print(text + text2)

#czysci z prawej stony spacje taby itp
text1 = text1.rstrip()
print(text1 + text2)
print(text1 + " " + text2)

#wyswietalnie lancucha znakow

#wszystkie wersje Pythona
text = "%s, Java i %s" % ("PHP", "Python")
print(text)

#nowsze wersje Pythona >2.6
text = "{1}, Java i {0}".format("PHP", "Python")
print(text)

#help(text.replace)

new = text.replace("PHP", "C#")
print(new)

#wypisanie danych
rok = 2019
msc = "marzec"
dzien = 25

print("Data: ", end="")
print(dzien, msc, rok)

print("Data: ", end="")
print(dzien, msc, rok, sep="-")
