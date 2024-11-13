
# Media, Moda e Mediana di 10 Numeri Casuali

In questo esempio, vedremo come calcolare la **media**, la **moda** e la **mediana** di una lista di 10 numeri casuali generati da Python.

## Dati di partenza
Abbiamo una lista di 10 numeri generati casualmente, ad esempio:\
(Si consiglia di usare questa lista di partenza per il testing)

```python
numbers = [34, 67, 12, 45, 78, 23, 45, 56, 12, 89]
```

## Media
La **media** di una lista di numeri è semplicemente la somma di tutti gli elementi divisa per il numero totale di elementi. La formula è:

```
Media = (somma degli elementi) / (numero degli elementi)
```

Ad esempio, se abbiamo i numeri:

```python
numbers = [34, 67, 12, 45, 78, 23, 45, 56, 12, 89]
```

La somma degli elementi è: `34 + 67 + 12 + 45 + 78 + 23 + 45 + 56 + 12 + 89 = 511`

La media sarà: `511 / 10 = 51.1`

Quindi la **media** è `51.1`.

## Moda
La **moda** è il numero che appare con maggiore frequenza nella lista. Se ci sono più numeri con la stessa frequenza, la lista ha più di una moda (è bimodale o multimodale). Se nessun numero si ripete, non c'è una moda. Nel nostro esempio:

```python
numbers = [34, 67, 12, 45, 78, 23, 45, 56, 12, 89]
```

La moda è `12` e `45`, poiché entrambi appaiono due volte.

Se non ci fossero numeri ripetuti, la moda sarebbe "Nessuna moda".

## Mediana
La **mediana** è il numero che si trova al centro della lista quando gli elementi sono ordinati in ordine crescente (o decrescente). Se la lista ha un numero dispari di elementi, la mediana è il numero al centro. Se la lista ha un numero pari di elementi, la mediana è la media dei due numeri centrali.

Per ordinare la lista:

```python
numbers = [34, 67, 12, 45, 78, 23, 45, 56, 12, 89]
numbers.sort()
```

La lista ordinata è:

```python
[12, 12, 23, 34, 45, 45, 56, 67, 78, 89]
```

Poiché la lista ha un numero pari di elementi, la mediana è la media dei due numeri centrali: `45` e `45`. Quindi la mediana è `45`.

### Riassunto:
- **Media**: 51.1
- **Moda**: 12 e 45 (entrambi appaiono due volte)
- **Mediana**: 45
