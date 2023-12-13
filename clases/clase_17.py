from data import data_personas
from data.mock_data import empleados
import os
import json

# import json

# for i in range(5):
#     print(f"i: {i}")
#     for j in range(3):
#         print(f"j: {j}")
#     print("----------")


x = 5
y = 10

# print(f"x:{x} - y:{y}")

# swap / intercambio

aux = x
x = y
y = aux

aux = y
y = x
x = aux

# ---------------------------------------------------------------------------------------------------- #
# ALGORITMO DE LA BURBUJA #
lista_de_numeros = [4, 9, 2, 8, 5]
# print(f"Lista desordenada: {lista_de_numeros}")

# es mejor guardar la longitud en una variable ya que no se modificara en el ordenamiento, es mas eficiente
tam_de_lista_de_numeros = len(lista_de_numeros)
# print(f"Tam de lista_de_numeros: {tam_de_lista_de_numeros}\n")

for i in range(tam_de_lista_de_numeros - 1):
    # print(f"Nro de barrida = {i + 1}")

    for j in range(i+1, tam_de_lista_de_numeros):
        # print(f"I:{i} - J:{j}")
        if lista_de_numeros[i] > lista_de_numeros[j]:  # criterio de ordenamiento
            aux = lista_de_numeros[i]
            lista_de_numeros[i] = lista_de_numeros[j]
            lista_de_numeros[j] = aux

    # print("---------")
# print(f"Lista ordenada: {lista_de_numeros}")

# ---------------------------------------------------------------------------------------------------- #

# lista_de_numeros = [74, 43, 22, 61, 38, 12, 36, 79,
#                     96, 87, 27, 84, 7, 17, 97, 75, 59, 18, 77, 20]
# print(f"Lista Num desordenada: {lista_de_numeros}")


# def ordenar_lista_de_numeros_enteros(lista_de_numeros: list, orden: str):
#     """Ordena una lista_de_numeros de numeros segun el orden recibido

#     Args:
#         lista_de_numeros_de_numeros (lista_de_numeros): lista_de_numeros de numeros a ordenar\n
#         orden (str): '+' : creciente o '-' : decreciente

#     """
#     tam_de_lista = len(lista_de_numeros)
#     for i in range(tam_de_lista - 1):
#         if orden == "+":
#             for j in range(i+1, tam_de_lista):
#                 # criterio de ordenamiento creciente
#                 if lista_de_numeros[i] > lista_de_numeros[j]:
#                     aux = lista_de_numeros[i]
#                     lista_de_numeros[i] = lista_de_numeros[j]
#                     lista_de_numeros[j] = aux
#         elif orden == "-":
#             for j in range(i+1, tam_de_lista):
#                 # criterio de ordenamiento decreciente
#                 if lista_de_numeros[i] < lista_de_numeros[j]:
#                     aux = lista_de_numeros[i]
#                     lista_de_numeros[i] = lista_de_numeros[j]
#                     lista_de_numeros[j] = aux

def ordenar_lista_de_numeros_enteros(lista_de_numeros: list, ascendente: bool = True):
    """Ordena una lista_de_numeros de numeros segun el orden recibido

    Args:
        lista_de_numeros_de_numeros (lista_de_numeros): lista_de_numeros de numeros a ordenar\n
        orden (str): '+' : creciente o '-' : decreciente

    """
    tam_de_lista = len(lista_de_numeros)
    for i in range(tam_de_lista - 1):
        for j in range(i+1, tam_de_lista):
            # criterio de ordenamiento creciente                              # criterio de ordenamiento decreciente
            if (ascendente and lista_de_numeros[i] > lista_de_numeros[j]) or (not ascendente and lista_de_numeros[i] < lista_de_numeros[j]):
                aux = lista_de_numeros[i]
                lista_de_numeros[i] = lista_de_numeros[j]
                lista_de_numeros[j] = aux


# ordenar_lista_de_numeros_enteros(lista_de_numeros)
# print(f"Lista Num ordenada: {lista_de_numeros}")
# ordenar_lista_de_numeros_enteros(lista_de_numeros, False)
# print(f"Lista Num ordenada: {lista_de_numeros}")
# ---------------------------------------------------------------------------------------------------- #

# from data import lista

# x = open("data/mock_data.json")
# data = json.load(x)
lista_de_personas = data_personas.lista


def mostar_personas(lista: list):
    print("")
    print("                      Lista de Personas                       ")
    print("--------------------------------------------------------------")
    print(" id |    Nombre   | Edad | Genero |          Sector          |")
    print("--------------------------------------------------------------")

    for persona in lista:
        print(
            f" {str(persona['id']).ljust(3)}| {persona['nombre'].ljust(11)} | {str(persona['edad']).center(4)} | {persona['gender'].center(7)}| {persona['sector'].ljust(25)}|")

        print("--------------------------------------------------------------")


# mostar_personas(lista_de_personas)


def filtrar_lista(lista: list[dict]):
    tam = len(lista)
    for i in range(tam - 1):
        for j in range(i + 1, tam):
            # ordeno primero por sector
            if lista[i]["sector"] > lista[j]["sector"]:
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux


filtrar_lista(lista_de_personas)

# mostar_personas(lista_de_personas)

# ---------------------------------------------------------------------------------------------------- #

# cwd -----> current working directory

# directorio_actual = os.getcwd()

# print(directorio_actual)
# with open("./archivo.txt, "w") as file:
#   file.write("Hola mundo")

# path = directorio_actual + "\mi_archivo.txt"
# print(path)
# with open(path, "w") as file:
#   file.write("Hola mundo")

# print(__file__)  # imprime el directorio actual con el nombre del archivo al final

# devuelve una tupla con el directorio raiz como primer elemento , y el nombre del archivo como 2do elemento
path, nombre_archivo = os.path.split(__file__)

print(path)

# path absoluto

directorio = os.getcwd()
path_completo = os.path.join(directorio, "mock_data.json")

print(path_completo)

with open(path_completo, "w") as file:
    json.dump(empleados, file, indent=4)

with open(path_completo, "r") as file:
    data = json.load(file)

print((data))

# Archivos CSV

with open(path, "r") as file:
    header = file.readline()
    data = file.readlines()

header = header.strip().split(",")

personas = []

for index, item in enumerate(data):
    data[index] = item.strip()

# data = [item.strip() for item in data]

for index, item in enumerate(data):
    data[index] = item.split(",")

for item in data:
    dict_persona = {}
    indice = 0
    for key in header:
        if item[indice].isdigit():
            item[] = int(item[indice])
        # dict_persona[key] = item[header.index(key)]
        dict_persona[key] = item[indice]
        indice += 1
    personas.append(dict_persona)

for persona in personas:
    print(persona)

with open(os.path.join(dir_acual, "personas2.csv"), "w") as file:

    header = ",".join(list(personas[0].keys())) + "\n"
    file.write(header)
    for persona in personas:
        values = []
        for value in persona.values():
            if isinstance(value,int):
                value = str(value)
            values.append(value)
        line = ",".join(values) + "\n"
        file.write(line)