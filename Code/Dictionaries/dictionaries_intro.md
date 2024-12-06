
# Introduzione ai Dizionari in Python

I dizionari sono una struttura dati fondamentale in Python che permette di memorizzare coppie di chiavi e valori. Ogni elemento del dizionario ha una **chiave unica** associata a un **valore**. I dizionari sono estremamente utili per rappresentare dati strutturati.

## Creazione di un Dizionario

Un dizionario può essere creato utilizzando parentesi graffe `{}` e specificando le coppie di chiavi e valori:

```python
# Esempio di un dizionario
studente = {
    "nome": "Luca",
    "età": 20,
    "città": "Roma"
}
```

In questo esempio, `nome`, `età` e `città` sono chiavi, mentre `"Luca"`, `20` e `"Roma"` sono i valori associati.

## Accesso ai Valori

Per accedere a un valore, basta usare la chiave corrispondente tra parentesi quadre:

```python
print(studente["nome"])  # Output: Luca
```

Un altro metodo per accedere ai valori è il metodo `.get()`, che restituisce `None` se la chiave non esiste:

```python
print(studente.get("età"))     # Output: 20
print(studente.get("indirizzo"))  # Output: None
```

## Principali Operazioni sui Dizionari

Ecco alcune delle operazioni e dei metodi più comuni sui dizionari.

### Aggiungere o Modificare Elementi

Per aggiungere una nuova coppia chiave-valore o modificare una esistente:

```python
studente["corso"] = "Informatica"  # Aggiunge un nuovo elemento
studente["età"] = 21               # Modifica il valore di un elemento esistente
```

### Rimuovere Elementi

Per rimuovere una coppia chiave-valore si può usare `del`, `.pop()` o `.popitem()`:

```python
del studente["città"]        # Rimuove l'elemento con chiave "città"
corso = studente.pop("corso") # Rimuove "corso" e restituisce il valore
studente.popitem()            # Rimuove e restituisce l'ultimo elemento
```

### Iterare su Chiavi e Valori

Python permette di iterare su chiavi, valori o entrambi utilizzando rispettivamente i metodi `.keys()`, `.values()`, e `.items()`:

```python
# Itera sulle chiavi
for chiave in studente.keys():
    print(chiave)

# Itera sui valori
for valore in studente.values():
    print(valore)

# Itera sulle coppie chiave-valore
for chiave, valore in studente.items():
    print(f"{chiave}: {valore}")
```

## Conversione di un Dizionario in JSON

JSON è uno standard per rappresentare dati in formato testo. È possibile convertire un dizionario in una stringa JSON utilizzando la libreria `json`:

```python
import json

studente_json = json.dumps(studente)  # Converte il dizionario in una stringa JSON
print(studente_json)
```

### Conversione da JSON a Dizionario

Per convertire una stringa JSON in un dizionario:

```python
nuovo_studente = json.loads(studente_json)
print(nuovo_studente)
```

## Principali Funzioni Applicabili ai Dizionari

Ecco alcune delle funzioni e metodi utili per lavorare con i dizionari in Python:

- `len(dizionario)`: Restituisce il numero di elementi (coppie chiave-valore).
- `dizionario.keys()`: Restituisce un oggetto `dict_keys` con tutte le chiavi.
- `dizionario.values()`: Restituisce un oggetto `dict_values` con tutti i valori.
- `dizionario.items()`: Restituisce un oggetto `dict_items` con tutte le coppie chiave-valore.
- `dizionario.clear()`: Rimuove tutti gli elementi dal dizionario.
- `dizionario.update(altro_dizionario)`: Aggiorna il dizionario aggiungendo le coppie chiave-valore di un altro dizionario.

## Esempio Completo

```python
import json

# Creazione del dizionario
studente = {
    "nome": "Luca",
    "età": 21,
    "città": "Roma"
}

# Aggiunta di una chiave-valore
studente["corso"] = "Informatica"

# Conversione in JSON
studente_json = json.dumps(studente, ensure_ascii=False)
print("Dizionario in formato JSON:", studente_json)

# Riconversione in dizionario
studente_originale = json.loads(studente_json)
print("Dizionario originale:", studente_originale)
```

## Conclusione

I dizionari in Python sono una struttura dati flessibile e potente, ideale per rappresentare dati strutturati. Saper lavorare con i dizionari è essenziale per manipolare e gestire i dati in Python in modo efficace.
