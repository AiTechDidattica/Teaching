import math

# Inserimento dei coefficienti
print("Risolutore equazioni secondo grado.\n")

a = int(input("Inserisci il coefficiente a: "))
b = int(input("Inserisci il coefficiente b: "))
c = int(input("Inserisci il coefficiente c: "))

# Calcolo del delta
delta = b**2 - 4*a*c

# Analisi del delta
if delta > 0:
    print("L'equazione ha due soluzioni reali distinte.")

    x1 = (-b + math.sqrt(delta)) / (2*a)
    x2 = (-b - math.sqrt(delta)) / (2*a)

    print("x1 =", x1)
    print("x2 =", x2)

elif delta == 0:
    print("L'equazione ha una soluzione reale doppia.")

    x = -b / (2*a)

    print("x1 = x2 =", x)

else:
    print("L'equazione ha soluzioni immaginarie.")