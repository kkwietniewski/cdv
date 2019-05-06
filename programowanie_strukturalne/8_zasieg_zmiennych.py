#zasięg zmiennych, zmienne lokalne i globalne

#precyzja liczby(zaokrąglenie do 3 liczb po przecinku)
'''
x = "{0:.3f}".format(5)
print(x)
def	plnToChf(value):			#Franki(Chf) na złotówki
	kursChf = 3.7536
	iloscChf = value / kursChf			#liczy ile dostaniemy franków z x zł
	iloscChf = "{0:.0f}".format(iloscChf)		#obcina miejsca po przecinku
	print(f'Ilość CHF: {iloscChf}')
plnToChf(100)
#	Utwórz funkcję zwracającą ilość EURO
#	Jaką klient może kupić za PLN
#	Użytkownik podaje dane z klawiatury
def plnToEuro(value):
	kursEuro = 4.2867
	iloscEuro = value / kursEuro
	iloscEuro = "{0:.1f}".format(iloscEuro)				#Zostawia 1 miejsce po ,
	print(f'Ilość Euro: {iloscEuro}')
pln = (input('Podaj ilość złotówek: '))
plnToEuro(float(pln))
#zmienna globalna
kursUSD = 3.8281
print(f'Kurs dolara: {kursUSD}')
def plnToUSD(value):
	kursUSD = 5.4
	print(f'\nId dolara wewnątrz funkcji: {id(kursUSD)}')
	print(f'Kurs dolara wewnątrz funkcji: {kursUSD}')
	iloscUSD = value / kursUSD
	iloscUSD = "{0:.0f}".format(iloscUSD)
	return iloscUSD
print(f'\nId dolara: {id(kursUSD)}')
print(f'\nKurs dolara: {kursUSD}')
pln = input('Podaj kwotę PLN jaką chcesz wymienić na USD: ')
usd = plnToUSD(float(pln))
print(f'Ilość {pln}PLN = {usd}USD')
print(f'\nKurs dolara: {kursUSD}')
'''

####################################################################

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
