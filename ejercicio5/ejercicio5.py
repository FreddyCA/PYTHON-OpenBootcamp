##Escribe una función que pueda decirte si un año (número entero) es bisiesto o no.
def bisiesto(year):
    if year % 4 == 0:
        print("es divisible entre 4")
        if year % 100 == 0:
            print("es divisible entre 100")
            if year % 400 == 0:
                print("es divisible entre 400")

bisiesto(2008)