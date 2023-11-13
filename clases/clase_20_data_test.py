from data.mock_data import empleados


def ordenar_empl_edad(e1, e2):
    return e1["edad"] > e2["edad"]


def ordenar_empl_nombre(e1, e2):
    return e1["nombre"] > e2["nombre"]


# empleados.sort(key=["edad"],)


def mostrar_lista(titulo, lista):
    print(titulo)
    for i in range(len(lista)):
        print(lista[i])


def ordenar_lista(lista, comparador):
    tam = len(lista)
    for i in range(tam - 1):
        for j in range(i + 1, tam):
            if comparador(lista[i], lista[j]):
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux


mostrar_lista("Original:", empleados)
ordenar_lista(empleados, lambda e1, e2: e1["edad"] < e2["edad"])
mostrar_lista("Ordebados por edad:", empleados)
ordenar_lista(empleados, ordenar_empl_nombre)
mostrar_lista("Ordenados por nombre:", empleados)
