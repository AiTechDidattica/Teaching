# Gestione di un Dizionario di Persone

## Descrizione del Programma:

Il programma consente di raccogliere informazioni su un numero specificato di persone, salvandole in una lista di dizionari. Ogni dizionario contiene tre campi: nome, età e lavoro.

## Funzionalità:

1. Richiesta del numero di persone da aggiungere, con validazione dell'input.
2. Raccolta di nome, età e lavoro per ogni persona.
3. Archiviazione dei dati in una lista di dizionari.
4. Visualizzazione dei dati raccolti.

## Richieste aggiuntive:

- Il codice deve essere strutturato in funzioni.
- Deve essere fornito un opportuno dataset per il testing, dimostrando al contempo la robustezza del codice sviluppato.

Esempio di output:

```plaintext
Quante persone vuoi aggiungere: 2

Inserimento dati per la persona 1:
Nome: Mario
Età: 30
Lavoro: Ingegnere

Inserimento dati per la persona 2:
Nome: Lucia
Età: 25
Lavoro: Medico

Dati inseriti:
[{'nome': 'Mario', 'età': 30, 'lavoro': 'Ingegnere'}, {'nome': 'Lucia', 'età': 25, 'lavoro': 'Medico'}]
```


## Variante JSON :

Fornire una variante del programma in modo da fornire in output la rappresentazione JSON dei dati gestiti, utilizzando l'omonima libreria.

### Esempio di rappresentazione JSON dell'output:

```json
[
  {
    "nome": "Mario",
    "età": 30,
    "lavoro": "Ingegnere"
  },
  {
    "nome": "Lucia",
    "età": 25,
    "lavoro": "Medico"
  }
]

