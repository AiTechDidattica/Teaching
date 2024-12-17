# Esercizio: Sistema di Gestione delle Informazioni di Studenti

Crea un programma che gestisca le informazioni di diversi studenti usando un dizionario. Il programma deve permettere di:

- Aggiungere uno studente con il suo nome e una lista di voti.
- Calcolare e restituire la media dei voti di uno studente.
- Mostrare tutti gli studenti con le loro informazioni.
- Cancellare uno studente dal sistema.

## Richieste aggiuntive:

- Il codice deve essere strutturato in funzioni.
- Deve essere fornito un opportuno dataset per il testing, dimostrando al contempo la robustezza del codice sviluppato.

## Suggerimento:

Usa un dizionario principale per memorizzare tutti gli studenti, dove ogni studente è identificato dal nome. Le funzioni dovrebbero avere questo schema:

## Struttura programma:

```python

def aggiungi_studente(studenti, nome, voti):
    # Aggiunge uno studente con nome e lista di voti

def calcola_media_voti(studenti, nome):
    # Calcola e restituisce la media dei voti dello studente con il nome fornito

def mostra_studenti(studenti):
    # Stampa tutte le informazioni di ciascuno studente

def cancella_studente(studenti, nome):
    # Rimuove uno studente con il nome specificato dal dizionario

# Esempio di utilizzo
aggiungi_studente(studenti, "Luigi", [7, 8, 9])
aggiungi_studente(studenti, "Anna", [8, 6, 9])

mostra_studenti(studenti)
media = calcola_media_voti(studenti, "Luigi")
print("Media voti di Luigi:", media)

cancella_studente(studenti, "Anna")
mostra_studenti(studenti)
