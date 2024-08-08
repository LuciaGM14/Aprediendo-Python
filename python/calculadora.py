def suma(n1, n2):
    return n1 + n2

def resta(n1, n2):
    return n1 - n2

def multiplicacion(n1, n2):
    return n1 * n2

def division(n1, n2):
    if n2 == 0:
        print("No se puede dividir un numero entre 0")
    return n1 / n2

def calculadora():
    print("Introduce la elección que deseas realizar:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")

    eleccion = input("Introduce el número de la elección que vas a realizar (1/2/3/4):")

   
    numero1 = float(input("Escribe un número: "))
    numero2 = float(input("Escribe el otro número: "))

    
    if eleccion == '1':
        print(f"La suma de {numero1} y {numero2} es: {suma(numero1, numero2)}")

    elif eleccion == '2':
        print(f"La resta de {numero1} y {numero2} es: {resta(numero1, numero2)}")

    elif eleccion == '3':
        print(f"La multiplicación de {numero1} y {numero2} es: {multiplicacion(numero1, numero2)}")

    elif eleccion == '4':
        print(f"La división de {numero1} y {numero2} es: {division(numero1, numero2)}")

    else:
        print("No es válido")

calculadora()

