def line():
    import math
    print("TO DO")
    a=float(input("Ingrese el coeficiente A: "))
    b=float(input("Ingrese el coeficiente B: "))
    x1=float(input("Ingrese el coeficiente X1: "))
    x2=float(input("Ingrese el coeficiente X2: "))
    print(f'El coeficiente A de su ecuación de la recta es: {a}')
    print(f'El coeficiente B de su ecuación de la recta es: {b}')
    print(f'El coeficiente X1 de su ecuación de la recta es: {x1}')
    print(f'El coeficiente X2 de su ecuación de la recta es: {x2}')
    y1=(a*x1+b)
    y2=(a*x2+b)
    print(f"""
    Para la siguiente ecuación:
            Y = {a}X + {b}

    Dados los siguientes puntos:
            P1 ({x1},{y1})
            P2 ({x2},{y2})""")
    cuenta= ((x2-x1)**2)+((y2-y1)**2)
    distancia = math.sqrt(cuenta)
    print(f'\nLa distancia entre ellos es: {distancia}')
