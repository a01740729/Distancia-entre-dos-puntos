import math
def main():
    #escribe tu código abajo de esta línea
    pass

    x1 = float(input('Dame el punto de inicio en x: '))
    y1 = float(input('Dame el punto de inicio en y: '))
    x2 = float(input('Dame el punto de fin en x: '))
    y2 = float(input('Dame el punto de fin en y: '))

    d = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    print('La distancia es: '+str(round(d,2)))


if __name__=='__main__':
    main()
