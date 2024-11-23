# Somma degli elementi di una lista

numeri = [1, 2, 3, 4, 5]

somma = 0

print(numeri)

for i in range(len(numeri)):
    print(numeri[i])

for numero in numeri:
    somma += numero

print(f"La somma degli elementi è: {somma}")
