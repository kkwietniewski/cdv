x = 6
if x==5:
    print('x = 5')
    x = str(x)
    print('x wynosi' + x)
else :
    print('x != 5')
    print('x wynosi:',x)
    print(f'x wynosi: {x}')

###############################

y = True

if y:
    print('Prawda')
else:
    print('Falsz')

##############################

z = 5>6

if z:
    print('Prawda')
else:
    print('Falsz')

##############################

#j = '1' #prawda
#j = '0' #prawda
#j = '' #falsz
j = False #falsz

if bool(j):
    print('Prawda')
else:
    print('Falsz')

##############################
'''
k = input()
k = float(k)
if bool(k):
    print('Prawda k')
else:
    print('Falsz k')
                    '''
##############################

if True:
    print('true')
else:
    print('false')
