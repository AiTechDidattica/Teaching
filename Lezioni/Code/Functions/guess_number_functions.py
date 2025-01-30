import random

# Genera un numero segreto casuale tra 1 e 100.
def genera_numero_segreto():
    return random.randint(1, 100)


# Chiede all'utente di inserire un numero e gestisce eventuali errori di input
def chiedi_tentativo(numero_tentativi):
    while True:
        try:
            numero_giocatore = int(input(f"Tentativi rimasti {numero_tentativi}: "))
        except ValueError:
            print("Il valore inserito deve essere un numero intero!")
            continue
        else:
            if numero_giocatore <= 0 or numero_giocatore > 100:
                print("Range Consentito [1,100]")
                continue
            return numero_giocatore


# Controlla se il tentativo dell'utente è giusto o meno
def controlla_tentativo(numero_giocatore, numero_segreto):
    if numero_giocatore > numero_segreto:
        print(f"Il numero segreto è minore di {numero_giocatore}")
        return False
    elif numero_giocatore < numero_segreto:
        print(f"Il numero segreto è maggiore di {numero_giocatore}")
        return False
    else:
        print(f"Bravo hai indovinato, il numero segreto era {numero_segreto}")
        return True


# Funzione principale per gestire il gioco.
def gioca():
    numero_segreto = genera_numero_segreto()
    numero_tentativi = 3

    print("Indovina il numero segreto compreso tra 1 e 100 in 3 tentativi!")

    while numero_tentativi > 0:
        numero_giocatore = chiedi_tentativo(numero_tentativi)

        if controlla_tentativo(numero_giocatore, numero_segreto):
            break

        numero_tentativi -= 1

    if numero_tentativi == 0:
        print(f"Tentativi Terminati!\nHai perso, il numero segreto era {numero_segreto}")


# Avvia il gioco
if __name__ == "__main__":
    gioca()
