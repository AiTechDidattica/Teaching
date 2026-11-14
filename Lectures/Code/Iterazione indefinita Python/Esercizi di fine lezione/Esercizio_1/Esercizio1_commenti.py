# Es 1
N = int(input("Inserisci un numero positivo intero"))
while True:
    if N > 0:
        for i in range(1, N + 1):
            print(i)
        break
    else:
        # Questo errore di ripetere l'istruzione di inserimento nel while anche dopo averla usata per il primo inserimento
        # fuori dal while è una "bad practice"; un while viene appositamente impiegato per non dover ripetere le istruzioni
        N = int(input("Inserisci un altro nuovo int positivo")) 
        continue

# E'un controsenso qui andare ad impiegare un while true che incarna una iterazione definita solo per racchiudere una
# iterazione definita rappresentata dal for.
while True:
    for i in range(N, 0, -1):
        print(i)
    break
