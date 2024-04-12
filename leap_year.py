def leap_year():
    leap=int(input("Ingrese un año: "))
    if leap%4==0 or leap%400==0:
        bisiesto="es bisiesto"
    else:  
        bisiesto="no es bisiesto"
    print(f'El año {leap} {bisiesto}')
