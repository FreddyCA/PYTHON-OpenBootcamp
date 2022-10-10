##Escribe una función que pueda decirte si un año (número entero) es bisiesto o no.
def bisiesto(year):
    if year % 400 == 0:
        print(year, " SI es un año bisiesto")
    elif year % 100 != 0 and year % 4 == 0:
        print(year, " SI es un año bisiesto")
    else:
        print(year, " NO es un año bisiesto")

bisiesto(2020)
bisiesto(1999)
bisiesto(2000)