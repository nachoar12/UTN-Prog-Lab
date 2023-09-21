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

# Function to clear the console
def limpiar_consola():
    os.system('clear')

# Define functions for each option
def view_profile():
    limpiar_consola()
    print("Viewing Profile")

def update_settings():
    limpiar_consola()
    print("Updating Settings")

# Define functions for other options similarly

def salir_del_programa():
    limpiar_consola()
    print("Exiting Program")
    exit()

# Function to clear the console
def limpiar_consola():
    os.system('clear')

# menu
while True:
    print("========== Console Option Menu ==========")
    print("1. View Profile")
    print("2. Update Settings")
    print("3. Send Message")
    print("4. View Messages")
    print("5. Create New Post")
    print("6. View Posts")
    print("7. Search")
    print("8. View Notifications")
    print("9. Logout")
    print("10. blabla")
    print("0. Salir")
    print("=========================================")

    while True:
        choice = input("Please enter the number corresponding to your choice: ")

        if choice.isdigit():
            choice = int(choice)
            if choice >= 0 and choice <= 10:
                limpiar_consola()
                break
            else:
                print("Invalid choice. Please enter a number between 0 and 10.")
        else:
            print("Invalid input. Please enter a valid number.")

    # Match user's choice and print a message for each case
    match choice:
        case 0:
            print("Saliendo del programa...")
            exit()
        case 1:
            print("View Profile")
        case 2:
            print("Update Settings")
        case 3:
            print("Send Message")
        case 4:
            print("View Messages")
        case 5:
            print("Create New Post")
        case 6:
            print("View Posts")
        case 7:
            print("Search")
        case 8:
            print("View Notifications")
        case 9:
            print("Logout")
        case 10:
            print("bla bla")
        case _:
            print("Invalid choice. Please try again.")
