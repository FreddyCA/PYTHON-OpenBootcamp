import time

print("Hor-Min-Seg actual:", time.strftime("%I-%M-%S"))

horaActual = int(time.strftime("%I"))
minutoActual = int(time.strftime("%M"))
segundoActual = int(time.strftime("%S"))

if horaActual > 7:
    print("Es hora de ir a casa")
else:
    print("Siga trabajando, le quedan",
          6 - horaActual, "horas ",
          60 - minutoActual, "minutos ",
          60 - segundoActual, "segundos")

