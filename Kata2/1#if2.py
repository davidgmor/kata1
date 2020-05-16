'''
Calculo de precio de entradas dependiendo de la edad
'''

user_age = int(input('Introduce tu edad: '))

if user_age < 4:
    print('El precio es 0€')
elif 4 <= user_age < 18:
    print('El precio es 5€')
else:
    print('El precio es 10€')