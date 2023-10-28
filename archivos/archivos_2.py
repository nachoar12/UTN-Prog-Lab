# modos de apertura
# r lectura texto
# rb lectura binaria
# w escritura texto
# wb escritura binaria
# a (append) agregar texto
# x

with open("archivos/scores.txt", "w") as file:

    file.write("Ahora no te saludo")

with open("archivos/scores.txt", "r") as file:
    x = file.read()
    print(x)
