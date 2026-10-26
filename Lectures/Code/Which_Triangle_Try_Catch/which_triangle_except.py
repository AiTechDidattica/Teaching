
# Flag per la validità dei singoli lati
lato1_valido = False
lato2_valido = False
lato3_valido = False

while True:

    # Inserimento del primo lato
    if not lato1_valido:
        try:
            lato1 = int(input("Inserisci il primo lato: "))
        except ValueError:
            print("Errore: inserire un valore numerico.\n")
            continue
        else:
            if lato1 <= 0:
                print("Errore: il lato deve essere maggiore di zero.\n")
                continue

            lato1_valido = True

    # Inserimento del secondo lato
    if not lato2_valido:
        try:
            lato2 = int(input("Inserisci il secondo lato: "))
        except ValueError:
            print("Errore: inserire un valore numerico.\n")
            continue
        else:
            if lato2 <= 0:
                print("Errore: il lato deve essere maggiore di zero.\n")
                continue

            lato2_valido = True

    # Inserimento del terzo lato
    if not lato3_valido:
        try:
            lato3 = int(input("Inserisci il terzo lato: "))
        except ValueError:
            print("Errore: inserire un valore numerico.\n")
            continue
        else:
            if lato3 <= 0:
                print("Errore: il lato deve essere maggiore di zero.\n")
                continue

            lato3_valido = True

    # Visualizzazione dei lati acquisiti
    print(f"\nLati inseriti: {lato1}, {lato2}, {lato3}")

    # Controllo della validità del triangolo
    if lato1 >= lato2 + lato3:
        print("Errore: i lati non formano un triangolo.")
        lato1_valido = False
        continue

    elif lato2 >= lato1 + lato3:
        print("Errore: i lati non formano un triangolo.")
        lato2_valido = False
        continue

    elif lato3 >= lato1 + lato2:
        print("Errore: i lati non formano un triangolo.")
        lato3_valido = False
        continue

    else:
        print("I lati inseriti permettono di formare un triangolo.\n")
        break


# Classificazione del triangolo
if lato1 == lato2 and lato2 == lato3:
    print("Il triangolo risulta equilatero.")

elif lato1 == lato2 or lato1 == lato3 or lato2 == lato3:
    print("Il triangolo risulta isoscele.")

else:
    print("Il triangolo risulta scaleno.")
