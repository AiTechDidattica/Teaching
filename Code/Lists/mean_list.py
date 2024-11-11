# Media degli elementi di una lista

numeri = [1, 2, 3, 4, 5]

somma = 0

for numero in numeri:
    somma += numero

media = somma / len(numeri)

print(f"La media degli elementi è: {media:.2f}")
