'''
def witaj():
    print('Witaj', end=' ')
    print('Janusz')
witaj()
def wyswietlWiek(wiek):
    print(f'Twój wiek: {wiek}')
wyswietlWiek(20)
'''



'''
    Utwórz funkcję zwracającą iloczyn dwóch liczba, uzytkownik podaje dane z klawiatury
'''



def iloczyn(a, b):
    return a*b


x=int(input('Podaj x: '))
y=int(input('Podja y: '))

print(f'Iloczyn a i b wynosi: {iloczyn(x,y)}')

def ilraz(a, b):
    return a/b

print('Iloraz wynosi:', iloraz(2,4))
print('Iloraz wynosi:', iloraz(b=2,a=4))
