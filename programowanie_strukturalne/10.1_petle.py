#pętle zadania

'''

Podaj wartosc poczatkowa i koncowa, ktora bedzie
wypiasana w porzadku malejacym

'''

'''
x = int(input("Podaj x: "))
y = int(input("Podaj y: "))

if y > x: #zamiana na wieksza

	pom = x
	x = y
	y = pom


for i in range(x,y-1,-1): #wyswietlanie od najwiekszej do najmniejszej
	print(i,end=" ")
'''

'''

*
**
***
****
*****

'''
'''
x = int(input("Podaj wielkosc: ")) + 1

for i in range(x):
	for j in range(i):
			print('*', end="")
	print("")


i = 1
ilosc = int(input('Ilosc wierszy: '))
znak = input('Znak: ')

for i in range(1,ilosc+1):
	print(znak * i)
	i=i+1

'''

#zadanie 1
'''
a = float(input('Podaj a:'))
b = float(input('Podaj b:'))

wynik=(a*a+b)
wynik1=((a+b)*(a+b))
if wynik1==0:
	print("Nie dziel przez 0")
else:
	suma=wynik/wynik1
	print(wynik)


for letter in 'CDV Poznan':
	if letter == 'V':
		continue
	print(f'Litera: {letter}',end=' ')

x=10
while x>0:
	x=x-1
	if x==6:
		continue
	print(f'{x} ',end=' ')
print('Koniec programu')

'''

'''
Uzytkownik podaje haslo z klawiatury, jesli poda haslo 'okon'
wyswietalmy mu na ekranie 'poprawne haslo'
Uzytkownik ma na podanie 3 proby, jesli przekroczy ilosc prob to wyswietli mu sie na ekranie 'przekroczono limit podania hasla'

'''

haslo = 'okon'
phaslo = input('Podaj haslo (limit 3): ')
i=1
while phaslo!='1yu':
	if(i==3 and phaslo!='okon'):
		print('Przekroczono limit podania hasla')
		phaslo='1yu'
	else:
		if(phaslo==haslo):
			print(f'Podane haslo {phaslo} jest rowne {haslo}')
			print(f'Haslo odgadnieto za {i} proba')
			phaslo='1yu'
		else:
			print('Podaj poprawne haslo')
			phaslo = input('Podaj haslo: ')
			i=i+1
			continue
