#Przekazywanie argumentów przez referencję
#'''
def show(name):
    print(f'Przed modyfikacją: {name}')
    name[0] = 'Beata'
    name[1] = 'Barbara'
    name[2] = 'Bogdan'
    print(f'Po modyfikacji: {name}')
    print(f'id po modyfikacji: {id(name)}')

data = ['Anna', 'Agnieszka', 'Andrzej']

print(f'Przed wywołaniem funkcji show: {data}')
print(f'id obiektu show: {id(data)}')

show(data)
print(f'Po wywołaniu funkcji show: {data}')

########################################
#Słownik
########################################

data1 = {
	'Imie':'Andrzej',
	'Nazwisko':'Nowak',
}

print(f'\nId przed modyfikacją: {id(data1)}')
show(data1)

########################################
#Przekazywanie argumentów przez wartość
########################################

print('\n\n')

def show1(city):
    print(f'Przed modyfikacją: {city}')
    city[0] = 'Beata'
    city[1] = 'Barbara'
    #city[2] = 'Bogdan'
    print(f'Po modyfikacji: {city}')
    print(f'id po modyfikacji: {id(city)}')

miasto = ['Poznań','Gniezno']		#lista

print(f'Przed wywołaniem funkcji show1: {miasto}')
print(f'\Id Przed modyfikacją: {id(miasto)}')
show1(list(miasto))
print(f'Po wywołaniu funkcji: {miasto}')

print('\n\n')
#'''
def show2(city):
    print(f'Przed modyfikacją: {city}')
    city[0] = 'Berlin'
    city[1] = 'Londyn'
    #city[2] = 'Bogdan'
    print(f'Po modyfikacji: {city}')
    print(f'id po modyfikacji: {id(city)}')

miasto1 ={						#Słownik
	0:'Gniezno',
	1:'Poznan'
}

print(f'Przed wywołaniem funkcji show1: {miasto1}')
print(f'\Id Przed modyfikacją: {id(miasto1)}')
show2(list(miasto1))
print(f'Po wywołaniu funkcji: {miasto1}')
