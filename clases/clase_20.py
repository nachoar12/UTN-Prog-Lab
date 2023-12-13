# PROG CLASE 20

numero = 8
pi = 3.14
cadena = "Juan"
running = True
lista = []

# def sumar(a, b):
#   return a + b

# sumar = lambda a, b : a + b  ---> tiene sentido para pasar a funciones mas grandes


def sumar(a, b):
    return a + b


pepe = sumar

print(pepe)

print(pepe(3, 6))


def calcular(a, b, operacion):
    print(operacion(a, b))


calcular(5, 10, sumar)
# ---> tambien se puede utilizar como literal de funcion
calcular(3, 7, lambda a, b: a + b)
# ---> aqui se coloca la funcion lambda en un contenedor al colocarla entre parentesis y luego los parametros en otros parentesis
# ---> inmediatrly invoke function / funcion autoinvocada
print((lambda a, b: a + b)(3, 4))


def restar(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    resultado = a / b
    return int(resultado) if resultado % 2 == 0 else resultado


calcular(5, 2, multiplicar)
calcular(18, 3, dividir)

# una funcion se comporta como como cualquier otra variable. "Ciudadano de primera clase"
