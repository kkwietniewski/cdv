
#programowanie = [listy] (tuple) {słownik}

#listy
programowanie = ['PHP', 'Java', 'Python']
programowanie.append('C#')
programowanie.append('PHP')
print(programowanie)
ile = programowanie.count('PHP')
print(f'PHP występuje {ile} razy')

#tuple
imiona = ('Julia', 'Anna', 'Tomek')
print(type(imiona)) #Type tuple(nie da się dodawać elementów)
print(imiona)
firstName = imiona[0]
print(f'First name: {firstName}')

#słownik
osoba = {
    'imie':'Janusz',
    'nazwisko':'Nowak',
    'miasto':'Poznan',
    'wiek':20,
    'umowaOprace':True
}

print(osoba)
print(type(osoba)) #Type dict
print(osoba['miasto'])
print(osoba.get('xyz','Brak klucza'))
print(osoba.get('imie','Brak klucza'))
print(osoba.keys())
#dict_keys(['imie','nazwisko','miasto','wiek','umowaOprace'])
