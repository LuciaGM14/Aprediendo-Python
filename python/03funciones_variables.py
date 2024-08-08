variable_1 = 9
 
 # STR() es para hacer que cualquier tipo de variable se convierta en una cadena de texto y no dé problemas
funcion_str = str(variable_1)
print(funcion_str)
print(type(funcion_str))

# ABS() para saber el valor absoluto de un numero.
variable_2 = 3
variable_3 = 5

media_numeros = (abs(variable_2) + abs(variable_3))
print(media_numeros)

#SORTED() para ordenar
orden_numeros = sorted ([variable_1, variable_2, variable_3])
print (orden_numeros)

cadena1 = "vesugo"
cadena2 = "amor"
cadena3 = "coco"

orden_cadenas = sorted([cadena1, cadena2, cadena3])
print(orden_cadenas)

#MAP() para crear una funcion en cada uno de los datos
#LIST() para que salga en lista uno por uno con la funcion.
def cuadrado(n):
    return n * n

numeros = [1,2,3,4,5,6,7,8,9,10]
cuadrados_numeros = map (cuadrado, numeros)
print(list(cuadrados_numeros))

# LEN() contar la longitud de la palabra (abreviatura de lenght)
variable_larga = "Esternocleidomastoideo"
print(len(variable_larga))
