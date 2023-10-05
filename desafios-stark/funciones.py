import os
from data_stark import lista_personajes

def limpiar_pantalla():
    """
    Limpia la pantalla de la consola.
    """
    os.system('clear')


def validar_opcion_usuario():
    """
    Valida y obtiene la opción ingresada por el usuario.
    """
    while True:
        try:
            opcion = int(input("Ingrese su opción y presione Enter: "))
            if opcion >= 0 and opcion <= 22:
                return opcion
            else:
                print("Opción inválida. Por favor, ingrese una opción válida (0-22).")
        except:
            print("Entrada no válida. Por favor, ingrese un número válido (0-22).")


def opcion_invalida():
    """
    Maneja una opción inválida seleccionada por el usuario.
    """
    # Implementación para manejar una opción inválida
    print("Opción inválida seleccionada.")

def mostrar_nombres_superheroes():
    """
    Muestra los nombres de los superhéroes.
    """
    # Implementación para la opción 1
    print("Mostrar nombres de los superheroes: \n")
    num_heroe = 0
    for heroe in lista_personajes:
        num_heroe += 1
        print(f"Heroe Nº {num_heroe} - {heroe['nombre']}")


def reducir_num(num):
    """
    Convierte una cadena en un número flotante.
    Args:
        num (string): cadena de un numero

    Returns:
        float: el argumento num convertido a float
    """
    peso = float(num)
    return peso

def mostrar_nombres_y_altura():
    """
    Muestra el nombre y altura de los superhéroes.
    """
    # Implementación para la opción 2
    print("Mostrar nombre y altura de los superheroes: \n")
    num_heroe = 0
    for heroe in lista_personajes:
        num_heroe += 1
        print(f"Heroe Nº {num_heroe} - {heroe['nombre']} | Altura: {reducir_num(heroe['altura'])} CM")


def mostrar_super_mas_alto():
    """
    Muestra el superhéroe más alto y su altura.
    """
    # Implementación para la opción 3
    print("El superheroe mas alto.\n")
    altura_max = None
    nombre_mas_alto = ""
    for heroe in lista_personajes:
        altura = reducir_num(heroe["altura"])
        if altura_max == None or altura_max <= altura:
            altura_max = altura
            nombre_mas_alto = heroe["nombre"]
    
    print(f"El superheroe mas alto es {nombre_mas_alto} con un altura de {altura_max} CM")
            
def mostrar_super_mas_bajo():
    """
    Muestra el superhéroe más bajo y su altura.
    """
    # Implementación para la opción 4
    print("El superheroe mas bajo.\n")
    altura_min = None
    nombre_mas_bajo = ""
    for heroe in lista_personajes:
        altura = reducir_num(heroe["altura"])
        if altura_min == None or altura_min >= altura:
            altura_min = altura
            nombre_mas_bajo = heroe["nombre"]
    
    print(f"El superheroe mas alto es {nombre_mas_bajo} con un altura de {altura_min} CM")

def promedio_altura():
    """
    Calcula y muestra la altura promedio de los superhéroes.
    """
    # Implementación para la opción 5
    print("Altura promedio de los superheroes.\n")
    suma_de_alturas = 0
    contador_de_alturas = 0
    for heroe in lista_personajes:
        suma_de_alturas += reducir_num(heroe["altura"])
        contador_de_alturas += 1
        
    altura_promedio = suma_de_alturas // contador_de_alturas
    print(f"La altura promedio de los superheroes es = {altura_promedio} CM")

def mostrar_mas_alto_y_mas_bajo():
    """
    Muestra el superhéroe más alto y el más bajo.
    """
    # Implementación para la opción 6
    print("Nombre del superheroe mas alto y mas bajo.\n")
    mostrar_super_mas_alto()
    print("")
    mostrar_super_mas_bajo()

def mostrar_mas_y_menos_pesados():
    """
    Muestra el superhéroe más pesado y el menos pesado.
    """
    # Implementación para la opción 7
    print("Superheroe mas y menos pesado.\n")
    maximo_peso = None
    minimo_peso = None
    super_mas_pesado = ""
    super_menos_pesado = ""
    for heroe in lista_personajes:
        peso = reducir_num(heroe["peso"])
        if maximo_peso == None or maximo_peso <= peso:
            maximo_peso = peso
            super_mas_pesado = heroe["nombre"]
        elif minimo_peso == None or minimo_peso >= peso:
            minimo_peso = peso
            super_menos_pesado = heroe["nombre"]

    print(f"El super mas pesado es {super_mas_pesado} con un peso de: {maximo_peso} KG\n")
    print(f"El super menos pesado es {super_menos_pesado} con un peso de: {minimo_peso} KG")

def mostrar_super_masculinos():
    """
    Muestra a los superheroes de genero masculino.
    """
    # Implementación para la opción 8
    print("Mostrar superheroes masculinos: \n")
    num_heroe = 0
    for heroe in lista_personajes:
        num_heroe += 1
        if heroe["genero"] == "M":
            print(f"Heroe Nº {num_heroe} - {heroe['nombre']}")

def mostrar_super_femeninos():
    """
    Muestra a los superheroes de genero femenino.
    """
    # Implementación para la opción 9
    print("Mostrar superheroes femeninos: \n")
    num_heroe = 0
    for heroe in lista_personajes:
        num_heroe += 1
        if heroe["genero"] == "F":
            print(f"Heroe Nº {num_heroe} - {heroe['nombre']}")

def super_masculino_mas_alto():
    """
    Muestra y devuelve el superhéroe masculino más alto y su altura.
    """
    # Implementación para la opción 10
    print("El superheroe masculino mas alto.\n")
    altura_max = None
    masculino_mas_alto = ""
    for heroe in lista_personajes:
        if heroe["genero"] == "M":
            altura = reducir_num(heroe["altura"])
            if altura_max == None or altura_max <= altura:
                altura_max = altura
                masculino_mas_alto = heroe["nombre"]
    
    print(f"El superheroe masculino mas alto es {masculino_mas_alto} con un altura de {altura_max} CM")
    return masculino_mas_alto

def super_femenino_mas_alto():
    """
    Muestra el superhéroe femenino más alto y su altura.
    """
    # Implementación para la opción 11
    print("El superheroe femenino mas alto.\n")
    altura_max = None
    femenino_mas_alto = ""
    for heroe in lista_personajes:
        if heroe["genero"] == "F":
            altura = reducir_num(heroe["altura"])
            if altura_max == None or altura_max <= altura:
                altura_max = altura
                femenino_mas_alto = heroe["nombre"]
    
    print(f"El superheroe femenino mas alto es {femenino_mas_alto} con un altura de {altura_max} CM")
    

def super_masculino_mas_bajo():
    """
    Muestra el superhéroe masculino más bajo y su altura.
    """
    # Implementación para la opción 12
    print("El superheroe masculino mas bajo.\n")
    altura_min = None
    masculino_mas_bajo = ""
    for heroe in lista_personajes:
        if heroe["genero"] == "M":
            altura = reducir_num(heroe["altura"])
            if altura_min == None or altura_min >= altura:
                altura_min = altura
                masculino_mas_bajo = heroe["nombre"]
    
    print(f"El superheroe masculino mas bajo es {masculino_mas_bajo} con un altura de {altura_min} CM")

def super_femenino_mas_bajo():
    """
    Muestra y devuelve el superhéroe femenino más bajo y su altura.
    """
    # Implementación para la opción 13
    
    print("El superheroe femenino mas bajo.\n")
    altura_min = None
    femenino_mas_bajo = ""
    for heroe in lista_personajes:
        if heroe["genero"] == "F":
            altura = reducir_num(heroe["altura"])
            if altura_min == None or altura_min >= altura:
                altura_min = altura
                femenino_mas_bajo = heroe["nombre"]
    
    print(f"El superheroe femenino mas alto es {femenino_mas_bajo} con un altura de {altura_min} CM")
    return femenino_mas_bajo

def promedio_altura_masculinos():
    """
    Calcula y muestra la altura promedio de los superhéroes masculinos.
    """
    # Implementación para la opción 14
    print("Altura promedio de los superheroes masculinos.\n")
    suma_de_alturas = 0
    contador_de_alturas = 0
    for heroe in lista_personajes:
        if heroe["genero"] == "M":
            suma_de_alturas += reducir_num(heroe["altura"])
            contador_de_alturas += 1
        
    altura_promedio = suma_de_alturas // contador_de_alturas
    print(f"La altura promedio de los superheroes masculinos es = {altura_promedio} CM")

def promedio_altura_femeninos():
    """
    Calcula y muestra la altura promedio de los superhéroes femeninos.
    """
    # Implementación para la opción 15
    print("Altura promedio de los superheroes femeninos.\n")
    suma_de_alturas = 0
    contador_de_alturas = 0
    for heroe in lista_personajes:
        if heroe["genero"] == "F":
            suma_de_alturas += reducir_num(heroe["altura"])
            contador_de_alturas += 1
        
    altura_promedio = suma_de_alturas // contador_de_alturas
    print(f"La altura promedio de los superheroes femeninos es = {altura_promedio} CM")

def nombre_masc_mas_alto_y_fem_mas_bajo():
    """
    Muestra el nombre del superheroe masculino mas alto y el nombre del superheroe femenino mas bajo.
    """
    # Implementación para la opción 16
    print("El superheroe masculino mas alto y el femenino mas bajo .\n")
    super_masculino_mas_alto()
    print("")
    super_femenino_mas_bajo()

def mostrar_segun_color_de_ojos():
    """
    Muestra la cantidad de heroes que hay segun el color de ojos.
    """
    # Implementación para la opción 17
    print("Mostrar cuantos hay segun color de ojos.\n")
    for heroe in lista_personajes:
        pass


def listar_color_de_ojos():
    """
    Genera y devuelve una lista con los disintos colores de ojos de los superheroes.

    Returns:
        list: lista que contiene los disintos colores de ojos.
    """
    # Implementación para la opción 18

    lista_de_ojos = []
    for heroe in lista_personajes:
        lista_de_ojos = heroe["color_ojos"]
    
    return lista_de_ojos

def mostrar_segun_color_de_pelo():
    """
    Muestra el superhéroe femenimasculinono más bajo y su altura.
    """
    # Implementación para la opción 18
    print("El superheroe masculino mas bajo.\n")

def mostrar_segun_inteligencia():
    """
    Muestra el superhéroe femenimasculinono más bajo y su altura.
    """
    # Implementación para la opción 19
    print("El superheroe masculino mas bajo.\n")

def listar_segun_color_de_ojos():
    """
    Muestra el superhéroe femenimasculinono más bajo y su altura.
    """
    # Implementación para la opción 20
    print("El superheroe masculino mas bajo.\n")

def listar_segun_color_de_pelo():
    """
    Muestra el superhéroe femenimasculinono más bajo y su altura.
    """
    # Implementación para la opción 21
    print("El superheroe masculino mas bajo.\n")

def listar_segun_inteligencia():
    """
    Muestra el superhéroe femenimasculinono más bajo y su altura.
    """
    # Implementación para la opción 22

    print("El superheroe masculino mas bajo.\n")
