
# Programma: Menù interattivo

while True:

    # Visualizzazione del menù principale
    print("\n========== MENÙ PRINCIPALE ==========")
    print("1. Saluto")
    print("2. Informazioni")
    print("3. Istruzioni")
    print("4. Crediti")
    print("=====================================")

    # Inserimento e validazione della scelta
    while True:

        try:
            scelta = int(input("Seleziona un'opzione (1-4): "))

        except ValueError:
            print("Errore: inserire un valore numerico.\n")
            continue

        else:
            if scelta < 1 or scelta > 4:
                print("Errore: selezionare un'opzione tra 1 e 4.\n")
                continue

            break

    # Esecuzione dell'opzione selezionata
    if scelta == 1:
        print("\nBenvenuto nel programma!")

    elif scelta == 2:
        print("\nQuesto programma presenta un menù interattivo.")

    elif scelta == 3:
        print("\nSeleziona un'opzione inserendo un numero da 1 a 4.")

    else:
        print("\nProgramma realizzato per un'esercitazione di Python.")

    # Richiesta di una nuova selezione
    while True:

        risposta = input("\nVuoi effettuare un'altra selezione? (y/n): ")

        if risposta != "y" and risposta != "n":
            print("Errore: rispondere esclusivamente con y oppure n.")
            continue
        break

    # Controllo della richiesta di uscita
    if risposta == "n":
        print("\nChiusura del programma. Arrivederci!")
        break