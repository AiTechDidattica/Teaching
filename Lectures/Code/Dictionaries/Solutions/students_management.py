# Dizionario principale per memorizzare gli studenti
studenti = {}

def aggiungi_studente(studenti, nome, voti):
    """Aggiunge uno studente con il nome e una lista di voti."""
    studenti[nome] = voti

def calcola_media_voti(studenti, nome):
    """Calcola e restituisce la media dei voti dello studente con il nome fornito."""
    if nome in studenti:
        voti = studenti[nome]
        media = sum(voti) / len(voti) if voti else 0
        return media
    else:
        print("Studente non trovato.")
        return None

def mostra_studenti(studenti):
    """Stampa tutte le informazioni di ciascuno studente."""
    for nome, voti in studenti.items():
        print(f"Nome: {nome}, Voti: {voti}")

def cancella_studente(studenti, nome):
    """Rimuove uno studente con il nome specificato dal dizionario."""
    if nome in studenti:
        del studenti[nome]
        print(f"Studente {nome} rimosso.")
    else:
        print("Studente non trovato.")

def main():
    aggiungi_studente(studenti, "Luigi", [7, 8, 9])
    aggiungi_studente(studenti, "Anna", [8, 6, 9])

    mostra_studenti(studenti)
    media = calcola_media_voti(studenti, "Luigi")
    if media is not None:
        print("Media voti di Luigi:", media)

    cancella_studente(studenti, "Anna")
    mostra_studenti(studenti)

if __name__ == '__main__':
    main()
