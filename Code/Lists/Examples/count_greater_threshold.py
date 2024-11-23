import random

# Numero di elementi da generare
n = 10

# Genera una lista di n numeri casuali tra 1 e 100
numbers = [random.randint(1, 100) for _ in range(n)]

# Chiedi all'utente di fornire il numero soglia
threshold = int(input("Inserisci il numero soglia: "))

# Inizializza il contatore
counter = 0

# Ciclo per contare quanti numeri sono maggiori della soglia
for num in numbers:
    if num > threshold:
        counter += 1

# Stampa la lista e il conteggio
print("Lista di numeri casuali:", numbers)
print(f"Numero di elementi maggiori di {threshold}: {counter}")
