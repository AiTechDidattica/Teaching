# Sentinella per la ripetizione dell'inserimento dei dati
dati_non_validi = True

while dati_non_validi:

    # Inserimento dei dati
    lato1 = float(input("Inserisci la lunghezza del primo lato: "))
    lato2 = float(input("Inserisci la lunghezza del secondo lato: "))
    lato3 = float(input("Inserisci la lunghezza del terzo lato: "))

    # Controllo che i lati siano maggiori di zero
    if lato1 <= 0 or lato2 <= 0 or lato3 <= 0:
        print("Errore: le lunghezze dei lati devono essere maggiori di zero.\n")

    # Controllo della validità del triangolo
    elif lato1 >= lato2 + lato3 or lato2 >= lato1 + lato3 or lato3 >= lato1 + lato2:
        print("Errore: i lati inseriti non possono formare un triangolo.\n")

    # Se entrambi i controlli sono superati, i dati sono validi
    else:
        dati_non_validi = False
        print("I lati inseriti permettono di formare un triangolo.\n")


# Classificazione del triangolo
if lato1 == lato2 and lato2 == lato3:
    print("Il triangolo risulta equilatero.")

elif lato1 == lato2 or lato1 == lato3 or lato2 == lato3:
    print("Il triangolo risulta isoscele.")

else:
    print("Il triangolo risulta scaleno.")