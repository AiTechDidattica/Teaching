# Indovina il numero segreto - 5 tentativi

import random

min_limit = 1
max_limit = 100
numero_tentativi = 5

numero_segreto = random.randint(min_limit, max_limit)

# Sentinella per controllare la fine della partita
fine_partita = False

print(f"Indovina il numero segreto compreso tra {min_limit} e {max_limit} "
      f"in {numero_tentativi} tentativi!")


while not fine_partita:

    # Sentinella per controllare la validità dell'inserimento
    dati_non_validi = True

    while dati_non_validi:

        try:
            numero_giocatore = int(
                input(f"Tentativi rimasti {numero_tentativi} - Prova: ")
            )

        except ValueError:
            print("Il valore inserito deve essere un numero intero!")

        else:
            if numero_giocatore > min_limit - 1 and numero_giocatore <= max_limit:
                dati_non_validi = False
            else:
                print(f"Range consentito [{min_limit}, {max_limit}]")

    # Controllo del numero inserito
    if numero_giocatore > numero_segreto:
        print(f"\nIl numero segreto è minore di {numero_giocatore}")

    elif numero_giocatore < numero_segreto:
        print(f"\nIl numero segreto è maggiore di {numero_giocatore}")

    else:
        print(f"\nBravo, hai indovinato! Il numero segreto era {numero_segreto}")
        fine_partita = True

    # il numero di tentativi rimasti decrementato dopo un inserimento valido
    numero_tentativi -= 1

    # Se non ci sono più tentativi, la partita termina
    if numero_tentativi == 0:
        fine_partita = True


if numero_giocatore != numero_segreto:
    print(f"\nTentativi terminati!\nHai perso, il numero segreto era {numero_segreto}")