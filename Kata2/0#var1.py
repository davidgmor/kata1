'''
Calcula precio de barras de pan dadas con un descuento
'''

precio = 3.49
descuento = 1 - 0.6
precio_con_descuento = precio * descuento

numero_de_barras = input('Introduce el número de barras vendidas = ')
numero_de_barras = int(numero_de_barras)

print('Precio habitual ' + str(precio))
print('Descuento ' + str(precio_con_descuento))
print('Coste final ' + str(numero_de_barras * precio_con_descuento))

