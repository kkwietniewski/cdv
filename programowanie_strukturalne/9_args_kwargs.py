
def wyswietl(num1, num2):
	print(f'Liczba 1: {num1}')
	print(f'Liczba 2: {num2}')
wyswietl(3, 4)
################################
# *args
################################
def wyswielArgs(num1, *args):
	print(f'Pierwszy element: {num1}')
	for i in args:						#Nie wiadomo ile bedzie wartosci
		print(f'Następna element: {i}')
wyswielArgs(3,5,1 ,1 ,1, 11, 6, 1, 1, 1, 1,)	#Można wpisać dow. ilość danych
imiona = ['Anna', 'Julia', 'Krzysztof', 'Jan']
wyswielArgs(imiona)				#Wyświetla wszystko jako I element
wyswielArgs(*imiona)			#Wyświtla wszystko jako kolejne elementy
################################
import os
#os.system('cls')

################################
#**kwargs
################################


def pracownik(**kwargs):
	for key, val in kwargs.items():
		#print(f'Klucz: {key}')
		print(f'Klusz: {key}, Wartość: {val}')

pracownik1 = {
	'imie':'Jan',			#Imie = key, Wartość = Jan
	'nazwisko':'Nowak',
	'wiek':21,
	'miasto':'Poznań',
	'umowaOPrace':True
}

pracownik(**pracownik1)
