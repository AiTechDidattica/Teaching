# Conta le occorrenze degli elementi di una lista
import random 

dim = 10

lista = [random.randint(1, 5) for _ in range(dim)]
print(lista)

ricorrenze = []

for numero in lista:
    conteggio = 0 
    
    # Proporre altra versione for
    for i in range(len(lista)):
        if lista[i] == numero:
            conteggio +=1 
            
    ricorrenze.append(conteggio)

print(ricorrenze)
