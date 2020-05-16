'''
Almacenar contraseña en una variable y comprobar si es igual
a la que tenemos almacenada en memoria, sin tener en cuanta mayúsculas
y minúsculas
'''
password = 'contraseña'
user_password = input('Introduzca la contraseña: ')
user_password = user_password.lower()

if password == user_password:
    print('Password correcto')
else:
    print('Password incorrecto')

