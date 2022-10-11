class Vehiculo:
    Color = "rojo"
    Ruedas = 4
    Puertas = 5


class Coche(Vehiculo):
    Velocidad = 80
    Cilindrada = 1.197


coche = Coche()
print("La cilindrada es: ", coche.Cilindrada, "cc")
