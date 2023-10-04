from menu import mostrar_menu
from funciones import *

def elegir_opcion(opcion_usuario):
    """
    Llama a la función correspondiente según la opción del usuario.
    """
    if opcion_usuario == 1:
        mostrar_nombres_superheroes()
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
    
