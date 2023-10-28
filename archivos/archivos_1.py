# abro el archivo "r"
file = open(
    "/home/nacho/Desktop/github-utn-prog-lab/archivos/scores.txt", "r")

print(file)

x = file.read()  # leo todo el archivo con el metodo read()
x = file.readline()  # con el metodo readline() leo una linea

print("")
print(x)

# cierro el archivo
file.close()

# se arma un contexto donde el archivo solo esta abierto dentro del mismo y se cierra automaticamente
with open(
        "/home/nacho/Desktop/github-utn-prog-lab/archivos/scores.txt", "r") as file:
    if not file.closed:
        print("file abierto")  # file abierto

if file.closed:
    print("file cerrado")  # file cerrado

a = "holanda"
b = "afuera"

print(a, b)

print(a, end=" ")
print(b)
