# Utilizzo di continue e break per controllare la ripetizione dell'inserimento
min_limit = 1
max_limit = 10

while True:
    try:
        val = int(input(f"Inserisci un valore intero compreso tra {min_limit} e {max_limit}: "))

    except ValueError as ve:
        print("input non conforme")
        continue

    else:
        if val > min_limit - 1 and val <= max_limit:
            print(f"\nHai inserito il valore {val} ottimo lavoro!")
            break

        print(f"Range consentito [{min_limit}, {max_limit}]")