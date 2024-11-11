# Ricerca elemento in una lista
# Lista di elementi
frutti = ['mela', 'banana', 'arancia', 'kiwi']
print(frutti)

# Elemento da cercare
frutto_da_cercare = input("Frutto da cercare: ")

# Controllo se l'elemento è nella lista
if frutto_da_cercare in frutti:
    print(f"{frutto_da_cercare} è presente nella lista.")
else:
    print(f"{frutto_da_cercare} non è presente nella lista.")
