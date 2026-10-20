# Indovina numero segreto - 3 tentativi

import random 

numero_segreto = random.randint(1, 100)

numero_tentativi = 3

print("Indovina il numero segreto compreso tra 1 e 100 in 3 tentativi!")

while True:

    if numero_tentativi > 0:

        try:
            numero_giocatore = int(input(f"Tentativi rimasti {numero_tentativi}: "))
        except ValueError:
            print("Il valore inserito deve essere un numero intero!")
            continue
        else:
            if numero_giocatore <= 0 or numero_giocatore > 100:
                print("Range Consentito [1,100]")
                continue
            
        if numero_giocatore > numero_segreto: 
            print(f"Il numero segreto è minore di {numero_giocatore}")
        elif numero_giocatore < numero_segreto: 
            print(f"Il numero segreto è maggiore di {numero_giocatore}")
        else:
            print(f"Bravo hai indovinato, il numero segreto era {numero_segreto}")
            break
           
        numero_tentativi -= 1
        continue
  
    else:
        print(f"Tentativi Terminati!\nHai perso, il numero segreto era {numero_segreto}")
        break
