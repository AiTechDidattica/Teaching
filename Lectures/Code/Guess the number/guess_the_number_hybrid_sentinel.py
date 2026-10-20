
# Indovina il numero segreto - 5 tentativi

import random

min_limit = 1
max_limit = 100
numero_tentativi = 5

numero_segreto = random.randint(min_limit, max_limit)

# Sentinella per indicare se il numero sia stato indovinato
indovinato = False

print(f"Indovina il numero segreto compreso tra {min_limit} e {max_limit} in {numero_tentativi} tentativi!")

while not indovinato and numero_tentativi > 0:

    try:
        numero_giocatore = int(input(f"Tentativi rimasti {numero_tentativi} - Prova: "))

    except ValueError:
        print("Il valore inserito deve essere un numero intero!")
        continue

    else:
        if numero_giocatore <= min_limit - 1 or numero_giocatore > max_limit:
            print(f"Range consentito [{min_limit}, {max_limit}]")
            continue

    if numero_giocatore > numero_segreto:
        print(f"\nIl numero segreto è minore di {numero_giocatore}")

    elif numero_giocatore < numero_segreto:
        print(f"\nIl numero segreto è maggiore di {numero_giocatore}")

    else:
        print(f"\nBravo, hai indovinato! Il numero segreto era {numero_segreto}")
        indovinato = True

    numero_tentativi -= 1

if not indovinato:
    print(f"\nTentativi terminati!\nHai perso, il numero segreto era {numero_segreto}")
