# Sentinella per controllare la ripetizione dell'inserimento
min_limit = 1
max_limit = 10
dati_non_validi = True

while dati_non_validi:
    try:
        val = int(input(f"Inserisci un valore intero compreso tra {min_limit} e {max_limit}: "))

    except ValueError:
        print("Input non conforme")

    else:
        if val > min_limit - 1 and val <= max_limit:
            print(f"\nHai inserito il valore {val}, ottimo lavoro!")
            dati_non_validi = False
        else:
            print(f"Range consentito [{min_limit}, {max_limit}]")