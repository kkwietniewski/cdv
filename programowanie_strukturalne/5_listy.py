#programowanie = [listy] (tuple) {słownik}

programowanie = ['Python', 'C#', 'JS', 'PHP', 'Java']
print(programowanie)
print(type(programowanie))

first = programowanie[0]
print(f'Pierwszy język programowanie w liście: {first}')

last = programowanie[-1]
print(f'Ostatni język programowanie w liście: {last}')

threeElements = programowanie[0:3]
print(f'Trzy języki programowania w liście: {threeElements}')

#Dodanie nowego elementu na końcu listy
programowanie.append('R')
print(programowanie)

#Zlicznie elementów w liście

programowanie.append('Python')
ile = programowanie.count('Python')
print(ile)

iloscElementow = len(programowanie)
print(f'Ilosc wszystkich elementow w liscie: ', end='')
print(iloscElementow)

#Połączenie list
print(programowanie)
inneJezyki = ['C', 'C++']
programowanie.extend(inneJezyki)
print(programowanie)

#Wyczyszczenie listy
nowa = programowanie
print(id(programowanie))
print(id(nowa))
print(nowa)
nowa.append('GO')
print(nowa)
print(programowanie)

nowa.clear()
print(nowa)
print(programowanie)
