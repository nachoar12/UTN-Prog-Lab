import os

# EJERCICIOS FUNCIONES

# Ejercicio 01: Escribe una función que calcule el área de un círculo. La función debe recibir
# el radio como parámetro y devolver el área.

# Ejercicio 02: Crea una función que verifique si un número dado es par o impar. La función
# debe imprimir un mensaje indicando si el número es par o impar.

# Ejercicio 03: Diseña una función que tome una lista de números y devuelva la suma de
# todos los elementos.

# Ejercicio 04: Define una función que encuentre el máximo de tres números. La función
# debe aceptar tres argumentos y devolver el número más grande.

# Ejercicio 05: Escribe una función que tome una cadena como entrada y devuelva la
# cadena invertida.

# Ejercicio 06: Crea una función que reciba una lista de palabras y devuelva una nueva lista
# con las palabras ordenadas alfabéticamente.

# Ejercicio 07: Diseña una función que calcule la potencia de un número. La función debe
# recibir la base y el exponente como argumentos y devolver el resultado.

# Ejercicio 08: Define una función que reciba una lista de números y devuelva una nueva
# lista con solo los números pares.

# Ejercicio 09: Escribe una función que tome una lista de números y calcule el producto de
# todos los elementos.

# Ejercicio 10: Crea una función que determine si una cadena dada es un palíndromo (se lee
# igual de izquierda a derecha que de derecha a izquierda).

# Nota: Todas las funciones deben estar probadas y se podrá acceder a cada una de
# ellas mediante un menú de opciones.

### MENU DE OPCIONES ###

# funcion para limpiar la consola
def limpiar_consola():
    os.system('clear')

# funciones del programa

def validarNumeroIngresado():
    """
    Valida si el usuario ingresa un numero valido.

    Returns:
        float: Numero del usuario validado.
    """
    while True:
        try:
            numero_ingresado = input("Ingrese un numero: ")
            numero = float(numero_ingresado)
            return numero
        except:
            print("Numero ingresado invalido. Ingrese un numero valido.")

def validarRadioIngresado():
    """
    Valida si el usario ingresa un radio valido

    Returns:
        float: radio ingresado por el usuario valido
    """
    while True:
        radio_ingresado = validarNumeroIngresado()

        if radio_ingresado > 0 :
                limpiar_consola()
                break
        else:
            print("Ingrese un numero entero positivo")

    return radio_ingresado

def cargarListaDeNumeros():
    """
    Arma una lista de numeros ingresador por el usuario

    Returns:
        list: lista de numeros
    """
    lista_de_numeros = []

    while True:
        numero_ingresado = validarNumeroIngresado()
        lista_de_numeros.append(numero_ingresado)

        agregar_otro_numero = input("Desea agregar otro numero (s/n): ").lower()
        if agregar_otro_numero != 's':
            break

    return lista_de_numeros

def armarListaDeCaracteres(cadena):
    """
    Crea una lista a partir de una cadena

    Args:
        cadena (str): cadena de caracteres

    Returns:
        list: lista armada con la cadena de argumento
    """
    lista_de_caracteres = []
    for caracter in cadena:
        lista_de_caracteres.append(caracter)
    return lista_de_caracteres

def calcularAreaDeCirculo(radio):
    """
    Calcula el area de un circulo a partir de un raio ingresado por el usuario

    Args:
        radio (float): Numero ingresado por el usuario

    Returns:
        float: Area del circulo en base al radio ingresado como argumento
    """
    limpiar_consola()
    print("Calcular Area de círculo")

    area = radio ** 2 * 3.14 

    return area

def elNumeroEsPar(numero):
    """
    Valida si el numero ingresado es par o no

    Args:
        numero (float): Numero ingresado por el usario

    Returns:
        str: PAR si el numero ingresado como argumento es par o IMPAR si no lo es
    """
    limpiar_consola()
    print("Numero Par o Impar")
    if numero % 2 == 0:
        respuesta = "PAR"
    else:
        respuesta = "IMPAR"
    return respuesta

def sumaDeNumeros(listaDeNumeros):
    """
    Calcula la suma total de una lista de numeros

    Parameters:
        listaDeNumeros (lista): Una lista de numeros.

    Returns:
        int o float: La suma total de los numeros de la lista.
    """
    limpiar_consola()
    print("Suma de numeros")
    suma = 0

    for numero in listaDeNumeros:
        suma += numero

    return suma

def calcularNumeroMaximo(listaDeNumeros):
    """
    Encuentra el numero maximo en la lista de numeros

    Parameters:
        listaDeNumeros (list): una lista de numeros

    Returns:
        float: el numero mas alto de la lista de numeros
    """

    numero_maximo = listaDeNumeros[0]

    for numero in listaDeNumeros:
        if numero >= numero_maximo:
            numero_maximo = numero

    return numero_maximo

def invertirCadena(lista):
    """
    Invierte el orden de una lista de caracteres

    Args:
        lista (list): una lista de caracteres

    Returns:
        list: la lista con la cadena de caracteres invertida
    """
    lista_invertida = []
    for i in range(len(lista)-1,-1,-1):
        lista_invertida.append(lista[i])
    return lista_invertida

# funcion para salir del programa

def salir_del_programa():
    limpiar_consola()
    print("Saliendo del programa...")
    exit()


# menu
while True:
    print("============ Menu de opciones ===========")
    print("1. Calcular el area de un cirlculo")
    print("2. Numero Par o Impar")
    print("3. Suma de numeros")
    print("4. Maximo entre 3 numeros")
    print("5. Invertir cadena")
    print("6. Palabras por orden alfabetico")
    print("7. Potencia de un numero")
    print("8. Lista de numeros pares")
    print("9. Producto de numeros")
    print("10. Palindromo")
    print("0. Salir")
    print("=========================================")

    while True:
        opcion_ingresada = input("Por favor ingrese el numero correspondiente a la opcion: ")

        if opcion_ingresada.isdigit():
            opcion_ingresada = int(opcion_ingresada)
            if opcion_ingresada >= 0 and opcion_ingresada <= 10:
                limpiar_consola()
                break
            else:
                print("Opcion invalida. Ingrese un numero entre 0 y 10.")
        else:
            print("Opcion invalida. Ingrese un numero valido.")

    # OPCIONES INGRESADAS POR EL USUARIO
    match opcion_ingresada:

        case 0: # SALIR DEL PROGRAMA

            salir_del_programa()

        case 1: # AREA DEL CIRCULO

            radio_ingresado = validarRadioIngresado() 
            area = calcularAreaDeCirculo(radio_ingresado)
            print(f"Area del circulo de radio {radio_ingresado} = {area}")
            print("")

        case 2: # NUMERO PAR OR IMPAR

            numero_ingresado = validarNumeroIngresado()
            respuesta = elNumeroEsPar(numero_ingresado)
            print(f"El numero {numero_ingresado} es = {respuesta}")
            print("")

        case 3: # SUMA DE NUMEROS DE UNA LISTA

            lista_ingresada = cargarListaDeNumeros()
            suma_total = sumaDeNumeros(lista_ingresada)
            print(lista_ingresada)
            print(f"\nLa suma total de los numeros ingreados es = {suma_total}")
            print("")

        case 4: # MAXIMO DE 3 NUMEROS

            lista_ingresada = []

            for i in range(3):
                lista_ingresada.append(validarNumeroIngresado())

            numero_maximo = calcularNumeroMaximo(lista_ingresada)
            print(lista_ingresada)
            print(f"\nEl numero maximo de la lista es = {numero_maximo}")
            print("")

        case 5: # INVERTIR CADENA

            cadena_ingresada = input("Ingrese una cadena de caracteres: ")
            lista_cadena = armarListaDeCaracteres(cadena_ingresada)
            print("Cadena orignal: \n")
            print(lista_cadena)
            lista_cadena_invertida = invertirCadena(lista_cadena)
            print("")
            print("Cadena invertida: \n")
            print(lista_cadena_invertida)
            print("")

        case 6: # 
            pass
        case 7: #
            pass
        case 8: #
            pass
        case 9: #
           pass
        case 10: #
            pass
        case _:
            print("Opcion invalida. Vuelva a ingresa una opcion.")
