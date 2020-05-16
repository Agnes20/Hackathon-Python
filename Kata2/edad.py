"""
Escribir un programa para una empresa que tiene salas de juegos para todas las
edades y quieres calcular de foarm automatica el precio que debe cobrar a sus
clientes por entrar. El programa debe preguntar al usuario la edad del cliente
y mostrar el precio de la entrada. Si el cliente es menor de 4 años puede entrar gratis
, si tiene entre 4 y 18 años debe pagar 5€ y si es mayor de 18 años, 10€
"""
edad = input("Introduce tú edad: ")
edad = int(edad)

if edad < 4:
    print("La entrada en gratis")
elif edad >=4 and edad <= 18: #4 <= edad <= 18
    print("El Precio de la entrada es 5€")
else:
    print("El precio de la entrada es 10€")