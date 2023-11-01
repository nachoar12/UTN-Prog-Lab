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
lista = [4, 9, 2, 8, 5]
print(f"Lista desordenada: {lista}")

# es mejor guardar la longitud en una variable ya que no se modificara en el ordenamiento, es mas eficiente
tam_de_lista = len(lista)
# print(f"Tam de lista: {tam_de_lista}\n")

for i in range(tam_de_lista - 1):
    # print(f"Nro de barrida = {i + 1}")

    for j in range(i+1, tam_de_lista):
        # print(f"I:{i} - J:{j}")
        if lista[i] > lista[j]:  # criterio de ordenamiento
            aux = lista[i]
            lista[i] = lista[j]
            lista[j] = aux

    # print("---------")
print(f"Lista ordenada: {lista}")

lista_de_numeros = [74, 43, 22, 61, 38, 12, 36, 79,
                    96, 87, 27, 84, 7, 17, 97, 75, 59, 18, 77, 20]
print(f"Lista Num desordenada: {lista_de_numeros}")


def ordenar_lista_enteros(lista_de_numeros: list, orden: str):
    """Ordena una lista de numeros segun el orden recibido

    Args:
        lista_de_numeros (lista): lista de numeros a ordenar\n
        orden (str): + : creciente o - : decreciente

    Returns:
        list: la lista ordenada segun el orden recibido como argumente
    """
    lista = lista_de_numeros
    tam_de_lista = len(lista)
    for i in range(tam_de_lista - 1):
        if orden == "+":
            for j in range(i+1, tam_de_lista):
                if lista[i] > lista[j]:  # criterio de ordenamiento creciente
                    aux = lista[i]
                    lista[i] = lista[j]
                    lista[j] = aux
        elif orden == "-":
            for j in range(i+1, tam_de_lista):
                if lista[i] < lista[j]:  # criterio de ordenamiento decreciente
                    aux = lista[i]
                    lista[i] = lista[j]
                    lista[j] = aux
    return lista


print(f"Lista Num ordenada: {ordenar_lista_enteros(lista_de_numeros,'+')}")
