#Pętla for

colors = ['red', 'green', 'blue', 'magenta']
print(colors)
print(type(colors))

for i in colors:
	print(f'{i}',end=' ')

print('\n\n')

#wypisz tekst
string = 'CDV - uczelnia ludzi ciekawych'

for letter in string:
	print(letter, end=' ')

print('\n\n')

###########################
#Wypisz liczby od 1 do 10 za pomocą for
###########################

for i in range(1,11):
	print(i,end=' ')
