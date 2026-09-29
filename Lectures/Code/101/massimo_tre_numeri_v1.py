# Inserimento dei tre numeri
a = int(input("Inserisci il primo numero: "))
b = int(input("Inserisci il secondo numero: "))
c = int(input("Inserisci il terzo numero: "))

# Ricerca del massimo
if a > b and a > c:
    massimo = a
elif b > a and b > c:
    massimo = b
else:
    massimo = c

# Stampa del risultato
print("Il numero massimo è:", massimo)