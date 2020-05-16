"""
Escribir un programa que almacene la cadena de caracateres contraseña en una variable, pregunte
al usuario por la contraseña e imprima por pantalla si la contraseña introducida por el usuario
coincide con la guardada en la variable sin tener en cuenta mayuscula y minusculas
"""
password = "contraseña"
password_u = input("Introduce la contraseña: ")
password_u = password_u.lower()

if password == password_u:
    print("La contraseña es correcto")
else:
    print("La contraseña no es correcta")