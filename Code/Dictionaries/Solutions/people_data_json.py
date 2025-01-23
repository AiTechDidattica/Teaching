import json

# Chiede all'utente quante persone desidera aggiungere al dizionario.
def numero_persone():
    while True:
        try:
            numero = int(input("Quante persone vuoi aggiungere: "))
            if numero > 0:
                return numero
            else:
                print("Il numero deve essere maggiore di zero.")
        except ValueError:
            print("Per favore, inserisci un numero intero valido.")

# Raccoglie nome, età e lavoro per una singola persona.
def raccogli_dati():
    nome = input("Inserisci il nome: ")
    while True:
        try:
            età = int(input("Inserisci l'età: "))
            break
        except ValueError:
            print("Per favore, inserisci un numero intero valido per l'età.")
    lavoro = input("Inserisci il lavoro: ")
    return {"nome": nome, "età": età, "lavoro": lavoro}

# Aggiunge i dati raccolti in una lista di dizionari
def aggiungi_dati(numero_di_persone):
    persone = []
    for i in range(numero_di_persone):
        print(f"\nInserimento dati per la persona {i + 1}:")
        dati = raccogli_dati()
        persone.append(dati)
    return persone

# Funzione principale per gestire il programma.
def main():
    numero_di_persone = numero_persone()
    elenco_persone = aggiungi_dati(numero_di_persone)

    print("\nDati inseriti (lista di dizionari):")
    for i, persona in enumerate(elenco_persone, start=1):
        print(f"Persona {i}: {persona}")

    # Conversione della lista di dizionari in formato JSON
    dizionario_json = json.dumps(elenco_persone, indent=4)

    print("\nDati in formato JSON:")
    print(dizionario_json)

if __name__ == "__main__":
    main()
