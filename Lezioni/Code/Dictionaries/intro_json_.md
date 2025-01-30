
# Introduzione a JSON

JSON (*JavaScript Object Notation*) è un formato leggero per lo scambio di dati. È facile da leggere e scrivere per gli esseri umani e semplice da analizzare e generare per le macchine.

JSON è costituito da due strutture principali:
1. Una raccolta di coppie chiave/valore (un oggetto).
2. Un elenco ordinato di valori (un array).

## Caratteristiche principali
- Le chiavi sono sempre stringhe racchiuse tra doppi apici.
- I valori possono essere di tipo: stringa, numero, oggetto, array, booleano o `null`.

---

## Sintassi di Base

### Esempio di un oggetto JSON:
```json
{
  "nome": "Mario",
  "eta": 30,
  "lavoro": "Sviluppatore",
  "lingue": ["Italiano", "Inglese"],
  "attivo": true
}
```

### Esempio di un array JSON:
```json
[
  {
    "nome": "Anna",
    "eta": 25
  },
  {
    "nome": "Luca",
    "eta": 28
  }
]
```

### Tipi di dati supportati:
| Tipo         | Esempio                       |
|--------------|-------------------------------|
| Stringa      | `"testo"`                     |
| Numero       | `42`, `3.14`                  |
| Booleano     | `true`, `false`               |
| Array        | `[1, 2, 3]`                   |
| Oggetto      | `{"chiave": "valore"}`        |
| Null         | `null`                        |

### Oggetto JSON annidato:
```json
{
  "utente": {
    "id": 1,
    "dati": {
      "nome": "Giulia",
      "cognome": "Rossi"
    }
  }
}
```

---

## Vantaggi di JSON
1. **Compatibilità**: JSON è indipendente dalla piattaforma ed è supportato da molteplici linguaggi di programmazione.
2. **Leggibilità**: È facile da leggere per gli esseri umani.
3. **Efficienza**: È più leggero rispetto ad altri formati come XML.

---

## Utilizzo di JSON nei linguaggi di programmazione

### In JavaScript:
```javascript
const dati = {
  nome: "Paolo",
  eta: 32
};

console.log(dati.nome); // Output: Paolo
```

### In Python:
```python
import json

dati = '{"nome": "Paolo", "eta": 32}'
dati_dict = json.loads(dati)
print(dati_dict["nome"])  # Output: Paolo
```

---

JSON è diventato uno standard di fatto per lo scambio di dati grazie alla sua semplicità ed efficienza.


---

### Esempio di creazione (dump) di JSON

#### In Python:
```python
import json

# Dizionario Python
dati = {
    "nome": "Marco",
    "eta": 40,
    "lingue": ["Italiano", "Francese"]
}

# Convertire in JSON
json_dati = json.dumps(dati, indent=4)
print(json_dati)
```

**Output:**
```json
{
    "nome": "Marco",
    "eta": 40,
    "lingue": [
        "Italiano",
        "Francese"
    ]
}
```
