import calculadora

a = 7
b = 8
print("Sean los numeros: ", a, "y", b)


def operaciones():
    resSuma = calculadora.suma(a, b)
    print("La SUMA", a, "+", b, " es: ", resSuma)
    resResta = calculadora.resta(a, b)
    print("La RESTA", a, "-", b, " es: ", resResta)
    resMult = calculadora.multiplicacion(a, b)
    print("La MULTIPLICACION", a, "*", b, " es: ", resMult)
    resDiv = round(calculadora.division(a, b), 2)
    print("La DIVISION", a, "/", b, " es: ", resDiv)


if __name__ == '__main__':
    operaciones()
