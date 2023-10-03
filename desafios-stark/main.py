import os
from data_stark import lista_personajes


def limpiar_pantalla():
    """
    Limpia la pantalla de la consola.
    """
    os.system('clear')

def mostrar_menu():
    """
    Muestra el menú de opciones para el programa.
    """
    print("╔═════════════════════════════ MENU ══════════════════════════════╗")
    print("║  1. Mostrar nombres de los superheroes.                         ║")
    print("║  2. Mostrar nombre y altura de los superheroes.                 ║")
    print("║  3. El superheroe mas alto.                                     ║")
    print("║  4. El superheroe mas bajo.                                     ║")
    print("║  5. Altura promedio de los superheroes.                         ║")
    print("║  6. Nombre del superheroe mas alto y mas bajo.                  ║")
    print("║  7. Superheroe mas y menos pesado.                              ║")
    print("║  0. Salir                                                       ║")
    print("╚═════════════════════════════════════════════════════════════════╝")


def validar_opcion_usuario():
    """
    Valida y obtiene la opción ingresada por el usuario.
    """
    while True:
        try:
            opcion = int(input("Ingrese su opción y presione Enter: "))
            if opcion >= 0 and opcion <= 7:
                return opcion
            else:
                print("Opción inválida. Por favor, ingrese una opción válida (0-9).")
        except:
            print("Entrada no válida. Por favor, ingrese un número válido (0-9).")

def mostrar_nombres_super_heroes():
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
        print(f"Heroe Nº {num_heroe} - {heroe['nombre']} | Altura: {reducir_num(heroe['altura'])} KG")


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

def opcion_invalida():
    """
    Maneja una opción inválida seleccionada por el usuario.
    """
    # Implementación para manejar una opción inválida
    print("Opción inválida seleccionada.")

def elegir_opcion(opcion_usuario):
    """
    Llama a la función correspondiente según la opción del usuario.
    """
    if opcion_usuario == 1:
        mostrar_nombres_super_heroes()
    elif opcion_usuario == 2:
        mostrar_nombres_y_altura()
    elif opcion_usuario == 3:
        mostrar_super_mas_alto()
    elif opcion_usuario == 4:
        mostrar_super_mas_bajo()
    elif opcion_usuario == 5:
        promedio_altura()
    elif opcion_usuario == 6:
        mostrar_mas_alto_y_mas_bajo()
    elif opcion_usuario == 7:
        mostrar_mas_y_menos_pesados()
    else:
        opcion_invalida()


while True:
    limpiar_pantalla()
    mostrar_menu()
    opcion_usuario = validar_opcion_usuario()

    if opcion_usuario == 0:
        print("Saliendo del programa...")
        break
    else:
        limpiar_pantalla()   
        print(f"Ha elegido la opción {opcion_usuario}\n")
        elegir_opcion(opcion_usuario)
        input("\nPresione Enter para volver al menú.")
    
