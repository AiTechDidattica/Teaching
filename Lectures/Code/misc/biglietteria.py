
# Programma: Biglietteria automatica

while True:

    # Visualizzazione del tariffario
    print("\n========== BIGLIETTERIA ==========")
    print("1. Bambini  -  5 euro")
    print("2. Studenti -  7 euro")
    print("3. Adulti   - 12 euro")
    print("4. Anziani  -  8 euro")
    print("==================================")

    while True:

        try:
            codice = int(input("Seleziona una categoria (1-4): "))

        except ValueError:
            print("Errore: inserire un numero intero.\n")

        else:
            if codice < 1 or codice > 4:
                print("Errore: codice non valido.\n")
                continue
            break
        
    # Determinazione della categoria e del prezzo
    if codice == 1:
        categoria = "Bambini"
        prezzo = 5

    elif codice == 2:
        categoria = "Studenti"
        prezzo = 7

    elif codice == 3:
        categoria = "Adulti"
        prezzo = 12

    else:
        categoria = "Anziani"
        prezzo = 8

    # Visualizzazione del risultato
    print(f"\nCategoria selezionata: {categoria}")
    print(f"Prezzo del biglietto: {prezzo} euro")

    while True:

        risposta = input("\nVuoi effettuare un nuovo acquisto? (y/n): ")

        if risposta != "y" and risposta != "n":
            print("Errore: inserire esclusivamente y oppure n.")
            continue
        break

    # Terminazione del programma
    if risposta == "n":
        print("\nChiusura della biglietteria. Arrivederci!")
        break
        



