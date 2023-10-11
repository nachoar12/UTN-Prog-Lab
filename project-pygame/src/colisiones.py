from math import sqrt

def detectar_colision(rec_1, rec_2):
    for r1, r2 in [(rec_1, rec_2,),(rec_2, rec_1)]:
        return punto_en_rectangulo(r1.topleft, r2) or \
        punto_en_rectangulo(r1.topright, r2) or \
        punto_en_rectangulo(r1.bottomright, r2) or \
        punto_en_rectangulo(r1.bottomleft, r2)


def punto_en_rectangulo(punto, rect):
    x, y = punto
    return x >= rect.left and x <= rect.right and y >= rect.top and y <= rect.bottom

def detectar_colision_circ(rect_1, rect_2):
    distancia = distancia_centros_rect(rect_1, rect_2)
    radio_1 = calcular_radio_rectangulo(rect_1)
    radio_2 = calcular_radio_rectangulo(rect_2)
    return distancia <= (radio_1 + radio_2)

def distancia_entre_puntos(punto_1, punto_2):
    x1, y1 = punto_1
    x2, y2 = punto_2
    return sqrt((y1 - y2) ** 2 + (x1 - x2) ** 2)  

def calcular_radio_rectangulo(rect):
    return rect.width // 2

def distancia_centros_rect(rect_1, rect_2):
    return distancia_entre_puntos(rect_1.center, rect_2.center)