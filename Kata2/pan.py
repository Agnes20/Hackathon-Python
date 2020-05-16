"""
Una panadería vende barras de pan de 3.49€ cada una. El pan no es el día
tiene un descuento del 60%.
Escribe un programa que comience leyendo el número de barras vendidas que no
son del día. Despues tu programa debe mostrar el precio habitual de una barra
de pan, el descuento que se le hace por no ser fresca y el final total.
"""
precio = 3.49
descuento = 1 - 0.6
precio_con_descuento = precio * descuento
pan = input("Cuantas barras de pan has vendido: ")
pan = int(pan)
print("Precio Normal: " + str(precio))
print("Precio con Descuento: " + str(descuento))
print("He vendido "+ str(pan) + " barras de Pan " + "El Precio final: " + str(precio_con_descuento * pan))