# Media con numeri random e lista
import random

lista = []
somma = 0

n = int(input("Numero elementi: "))

for _ in range(n):
    lista.append(random.randint(1, 10))
    
print(f"Eccoti una lista di {n} elementi random")
print(lista)

for i in range(len(lista)):
    somma += lista[i]
    
print(f"La media è: {somma / n:.2f}")
