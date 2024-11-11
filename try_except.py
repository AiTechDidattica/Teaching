while True:
    try:
        val = int(input("Inserisci valore compreso tra 1 e 10: "))
    except ValueError as ve:
        print("input non conforme")
        continue
    else:
        if val > 0 and val <=10:
            print(f"Hai inserito {val} ottimo lavoro!")
            break
        print("Range consentito [1, 10]")
