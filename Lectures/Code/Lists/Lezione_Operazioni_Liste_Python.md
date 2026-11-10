# Operazioni con le liste in Python

## Obiettivi della lezione

Al termine della lezione sarai in grado di creare una lista, accedere ai suoi elementi, modificarli, aggiungerli e rimuoverli, estrarre porzioni di una lista, ordinare i dati e scorrere gli elementi con un ciclo `for`.

> **Come usare gli esempi:** ogni esempio è **autonomo**, quindi può essere copiato ed eseguito indipendentemente dagli altri. La lista `fruits` viene ricreata all'inizio dei vari esempi per evitare che le modifiche precedenti alterino i risultati.

## 0. Che cos'è una lista?

Una **lista** è una struttura dati che raccoglie più valori in un'unica variabile, mantenendone l'ordine. In Python si rappresenta con le parentesi quadre `[]` e i valori sono separati da virgole.

```python
fruits = ["apple", "banana", "cherry"]
```

Una lista:

- è **ordinata**: ogni elemento occupa una posizione;
- è **modificabile** (*mutable*): gli elementi possono essere aggiunti, sostituiti o rimossi;
- può contenere **duplicati**;
- può contenere valori di tipi differenti, anche se spesso è più semplice lavorare con dati dello stesso tipo.

### Indici: da 0, non da 1

| Indice positivo | `0` | `1` | `2` |
|:---|:---|:---|:---|
| Elemento | `"apple"` | `"banana"` | `"cherry"` |
| Indice negativo | `-3` | `-2` | `-1` |

Gli indici positivi partono da `0`, quelli negativi contano dalla fine. Per una lista di tre elementi gli indici positivi validi sono `0`, `1`, `2`.

---

## 1. Creare una lista

**Sintassi:** `nome_lista = [elemento1, elemento2, ...]`

```python
fruits = ["apple", "banana", "cherry"]
print(fruits)

empty_list = []
print(empty_list)
```

**Output:**

```text
['apple', 'banana', 'cherry']
[]
```

**Spiegazione:** i tre elementi vengono memorizzati nell'ordine in cui sono scritti. `[]` crea invece una lista vuota.

## 2. Aggiungere un elemento alla fine: `append()`

**Sintassi:** `lista.append(elemento)`

```python
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
print(fruits)
```

**Output:**

```text
['apple', 'banana', 'cherry', 'orange']
```

**Spiegazione:** `append()` modifica la lista esistente e aggiunge **un solo elemento** in fondo. Non restituisce la nuova lista: il suo valore di ritorno è `None`.

**Da ricordare:** `fruits.append("orange")` è corretto; `fruits = fruits.append("orange")` no, perché in quest'ultimo caso `fruits` diventa `None`.

## 3. Inserire un elemento in una posizione specifica: `insert()`

**Sintassi:** `lista.insert(indice, elemento)`

```python
fruits = ["apple", "banana", "cherry"]
fruits.insert(1, "kiwi")
print(fruits)
```

**Output:**

```text
['apple', 'kiwi', 'banana', 'cherry']
```

**Spiegazione:** `"kiwi"` viene inserito all'indice `1`, cioè nella **seconda posizione**. `"banana"` e `"cherry"` si spostano di una posizione verso destra; non vengono eliminati.

## 4. Rimuovere un elemento conoscendone il valore: `remove()`

**Sintassi:** `lista.remove(valore)`

```python
fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")
print(fruits)
```

**Output:**

```text
['apple', 'cherry']
```

**Spiegazione:** `remove()` cerca il valore specificato ed elimina **la prima occorrenza**.

```python
fruits = ["apple", "banana", "banana", "cherry"]
fruits.remove("banana")
print(fruits)
```

**Output:**

```text
['apple', 'banana', 'cherry']
```

**Attenzione:** se l'elemento non è presente, Python genera `ValueError`. Prima di rimuoverlo è possibile controllare `if "banana" in fruits:`.

## 5. Rimuovere un elemento conoscendone l'indice: `del`

**Sintassi:** `del lista[indice]`

```python
fruits = ["apple", "banana", "cherry"]
del fruits[0]
print(fruits)
```

**Output:**

```text
['banana', 'cherry']
```

**Spiegazione:** `del fruits[0]` elimina il primo elemento. Gli elementi successivi scalano verso sinistra. Un indice inesistente genera `IndexError`.

**Nota:** `del` è un'istruzione del linguaggio Python, non un metodo della lista.

## 6. Rimuovere e ottenere un elemento: `pop()`

**Sintassi:** `lista.pop()` oppure `lista.pop(indice)`

```python
fruits = ["apple", "banana", "cherry"]
last_fruit = fruits.pop()
print("Last fruit removed:", last_fruit)
print("Fruits after pop:", fruits)
```

**Output:**

```text
Last fruit removed: cherry
Fruits after pop: ['apple', 'banana']
```

**Spiegazione:** senza argomenti `pop()` elimina e **restituisce l'ultimo elemento**. Con un indice elimina e restituisce quello nella posizione indicata.

```python
fruits = ["apple", "banana", "cherry"]
removed_fruit = fruits.pop(1)
print("Removed fruit:", removed_fruit)
print(fruits)
```

**Output:**

```text
Removed fruit: banana
['apple', 'cherry']
```

**Attenzione:** `pop()` su una lista vuota genera `IndexError`.

## 7. Ottenere il numero di elementi: `len()`

**Sintassi:** `len(lista)`

```python
fruits = ["apple", "banana", "cherry"]
length = len(fruits)
print("Length of the list:", length)
```

**Output:**

```text
Length of the list: 3
```

**Spiegazione:** `len()` restituisce la quantità di elementi, **non** l'indice dell'ultimo elemento. Con una lista non vuota l'ultimo indice positivo è `len(fruits) - 1`.

## 8. Accedere a un elemento tramite indice

**Sintassi:** `lista[indice]`

```python
fruits = ["apple", "banana", "cherry"]
first_fruit = fruits[0]
last_fruit = fruits[-1]
print("First fruit:", first_fruit)
print("Last fruit:", last_fruit)
```

**Output:**

```text
First fruit: apple
Last fruit: cherry
```

**Spiegazione:** `[0]` legge il primo elemento e `[-1]` legge l'ultimo. Il contenuto della lista non viene modificato. L'accesso a un indice inesistente, ad esempio `fruits[3]`, genera `IndexError`.

## 9. Estrarre una porzione della lista: *slicing*

**Sintassi generale:** `lista[inizio:fine:passo]`. `inizio` è incluso, mentre **`fine` è escluso**. Il passo è facoltativo.

```python
fruits = ["apple", "banana", "cherry", "orange", "kiwi"]

print("From second to third:", fruits[1:3])
print("First two fruits:", fruits[:2])
print("From second onward:", fruits[1:])
print("Last two fruits:", fruits[-2:])
print("One every two:", fruits[::2])
print("In reverse order:", fruits[::-1])
```

**Output:**

```text
From second to third: ['banana', 'cherry']
First two fruits: ['apple', 'banana']
From second onward: ['banana', 'cherry', 'orange', 'kiwi']
Last two fruits: ['orange', 'kiwi']
One every two: ['apple', 'cherry', 'kiwi']
In reverse order: ['kiwi', 'orange', 'cherry', 'banana', 'apple']
```

**Spiegazione dei casi:**

- `[1:3]`: prende gli elementi agli indici `1` e `2`, **non** quello all'indice `3`;
- `[:2]`: parte dall'inizio e si ferma prima dell'indice `2`;
- `[1:]`: parte dall'indice `1` e continua fino alla fine;
- `[-2:]`: seleziona gli ultimi due elementi;
- `[::2]`: seleziona un elemento ogni due;
- `[::-1]`: genera una nuova lista con l'ordine invertito, **senza modificare l'originale**.

## 10. Ordinare gli elementi: `sort()`

**Sintassi:** `lista.sort()` oppure `lista.sort(reverse=True)`

```python
fruits = ["cherry", "apple", "banana"]
fruits.sort()
print("Sorted fruits:", fruits)

fruits.sort(reverse=True)
print("Descending order:", fruits)
```

**Output:**

```text
Sorted fruits: ['apple', 'banana', 'cherry']
Descending order: ['cherry', 'banana', 'apple']
```

**Spiegazione:** `sort()` ordina la **lista originale**; per le stringhe usa l'ordinamento lessicografico. `reverse=True` richiede l'ordine decrescente. Il metodo restituisce `None`.

**Attenzione:** `sort()` richiede elementi confrontabili fra loro. Per creare invece una nuova lista ordinata senza alterare l'originale si può usare `sorted(fruits)`.

## 11. Unire due liste con `+`

**Sintassi:** `lista1 + lista2`

```python
fruits = ["apple", "banana", "cherry"]
more_fruits = ["grape", "pear"]
combined_fruits = fruits + more_fruits

print("Combined fruits:", combined_fruits)
print("Original fruits:", fruits)
```

**Output:**

```text
Combined fruits: ['apple', 'banana', 'cherry', 'grape', 'pear']
Original fruits: ['apple', 'banana', 'cherry']
```

**Spiegazione:** `+` crea una **nuova lista** con tutti gli elementi della prima seguiti da quelli della seconda. Le due liste di partenza non vengono modificate.

## 12. Contare le occorrenze di un elemento: `count()`

**Sintassi:** `lista.count(valore)`

```python
fruits = ["apple", "kiwi", "banana", "kiwi", "cherry"]
count_kiwi = fruits.count("kiwi")
print("Number of kiwis:", count_kiwi)
print("Number of pears:", fruits.count("pear"))
```

**Output:**

```text
Number of kiwis: 2
Number of pears: 0
```

**Spiegazione:** `count()` conta quante volte un valore appare nella lista. Se non è presente restituisce `0` e **non genera un errore**.

## 13. Invertire l'ordine: `reverse()`

**Sintassi:** `lista.reverse()`

```python
fruits = ["apple", "banana", "cherry"]
fruits.reverse()
print("Reversed fruits:", fruits)
```

**Output:**

```text
Reversed fruits: ['cherry', 'banana', 'apple']
```

**Spiegazione:** `reverse()` modifica direttamente la lista, invertendo l'ordine in cui si trovano gli elementi. **Non è un ordinamento alfabetico decrescente**: inverte semplicemente la sequenza corrente. Restituisce `None`.

## 14. Copiare una lista: `copy()`

**Sintassi:** `nuova_lista = lista.copy()`

```python
fruits = ["apple", "banana", "cherry"]
fruits_copy = fruits.copy()
fruits_copy[0] = "kiwi"

print("Original fruits:", fruits)
print("Copied fruits:", fruits_copy)
```

**Output:**

```text
Original fruits: ['apple', 'banana', 'cherry']
Copied fruits: ['kiwi', 'banana', 'cherry']
```

**Spiegazione:** `copy()` produce una **nuova lista**. Modificare uno degli elementi mostrati nella copia non altera la lista originale.

**Distinzione importante:** `fruits_copy = fruits` **non copia** la lista: crea un secondo nome che fa riferimento alla stessa lista. Inoltre `copy()` è una *copia superficiale*: se la lista contiene altre liste, quelle interne rimangono condivise.

## 15. Trovare la posizione di un elemento: `index()`

**Sintassi:** `lista.index(valore)`

```python
fruits = ["apple", "kiwi", "banana", "kiwi"]
kiwi_index = fruits.index("kiwi")
print("Index of kiwi:", kiwi_index)
```

**Output:**

```text
Index of kiwi: 1
```

**Spiegazione:** `index()` restituisce l'indice della **prima occorrenza** del valore. Se la voce cercata non compare nella lista viene generato `ValueError`.

```python
fruits = ["apple", "banana", "cherry"]
if "kiwi" in fruits:
    print(fruits.index("kiwi"))
else:
    print("Kiwi non presente")
```

**Output:**

```text
Kiwi non presente
```

---

# Altre operazioni utili

Queste operazioni integrano quelle del materiale di partenza e aiutano a scrivere programmi che elaborano le liste.

## 16. Modificare direttamente un elemento

**Sintassi:** `lista[indice] = nuovo_valore`

```python
fruits = ["apple", "banana", "cherry"]
fruits[1] = "kiwi"
print(fruits)
```

**Output:**

```text
['apple', 'kiwi', 'cherry']
```

**Spiegazione:** il valore all'indice `1` viene **sostituito**. A differenza di `insert()`, la lunghezza non cambia.

## 17. Aggiungere più elementi: `extend()`

**Sintassi:** `lista.extend(altra_lista)`

```python
fruits = ["apple", "banana"]
fruits.extend(["kiwi", "orange"])
print(fruits)
```

**Output:**

```text
['apple', 'banana', 'kiwi', 'orange']
```

**Spiegazione:** `extend()` aggiunge gli elementi della seconda lista **uno per uno** alla fine della prima. È diverso da `append(["kiwi", "orange"])`, che aggiungerebbe **una lista come singolo elemento**.

## 18. Verificare se un elemento è presente: `in` e `not in`

```python
fruits = ["apple", "banana", "cherry"]

print("banana" in fruits)
print("kiwi" not in fruits)
```

**Output:**

```text
True
True
```

**Spiegazione:** `in` verifica la presenza di un elemento; `not in` verifica la sua assenza. Entrambi producono un valore booleano.

## 19. Scorrere una lista con `for`

### 19.1 Leggere direttamente gli elementi

```python
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)
```

**Output:**

```text
apple
banana
cherry
```

### 19.2 Utilizzare gli indici con `range()` e `len()`

```python
fruits = ["apple", "banana", "cherry"]

for i in range(len(fruits)):
    print(i, fruits[i])
```

**Output:**

```text
0 apple
1 banana
2 cherry
```

### 19.3 Ottenere insieme indice ed elemento con `enumerate()`

```python
fruits = ["apple", "banana", "cherry"]

for i, fruit in enumerate(fruits):
    print(i, fruit)
```

**Output:**

```text
0 apple
1 banana
2 cherry
```

**Spiegazione:** il primo ciclo lavora sui valori, il secondo sulle posizioni, il terzo mette a disposizione entrambi. Sono tutti cicli `for` tradizionali, senza *list comprehension*.

## 20. Svuotare una lista: `clear()`

```python
fruits = ["apple", "banana", "cherry"]
fruits.clear()
print(fruits)
print(len(fruits))
```

**Output:**

```text
[]
0
```

**Spiegazione:** `clear()` rimuove tutti gli elementi dalla lista esistente, che rimane disponibile ma vuota.

## 21. Funzioni utili per le liste numeriche

```python
numbers = [4, 7, 2, 9]
print("Somma:", sum(numbers))
print("Minimo:", min(numbers))
print("Massimo:", max(numbers))
print("Elementi:", len(numbers))
```

**Output:**

```text
Somma: 22
Minimo: 2
Massimo: 9
Elementi: 4
```

**Spiegazione:** `sum()` somma i numeri; `min()` e `max()` identificano rispettivamente il valore minimo e massimo; `len()` conta gli elementi. `min()` e `max()` su una lista vuota, senza un valore predefinito, generano `ValueError`.

---

# Tabella di riepilogo

| Operazione | Sintassi | Effetto sulla lista originale | Risultato prodotto |
|---|---|---|---|
| Creare | `fruits = ["apple"]` | Crea una nuova lista | Lista |
| Aggiungere un elemento | `fruits.append("kiwi")` | La modifica | `None` |
| Inserire in una posizione | `fruits.insert(1, "kiwi")` | La modifica | `None` |
| Rimuovere per valore | `fruits.remove("kiwi")` | La modifica | `None` |
| Rimuovere per indice | `del fruits[0]` | La modifica | Nessun valore restituito dall'istruzione |
| Rimuovere e ottenere | `fruits.pop()` | La modifica | Elemento rimosso |
| Contare gli elementi | `len(fruits)` | Non la modifica | Numero intero |
| Accedere per indice | `fruits[0]` | Non la modifica | Elemento |
| Slicing | `fruits[1:3]` | Non la modifica | Nuova lista |
| Ordinare | `fruits.sort()` | La modifica | `None` |
| Unire | `fruits + more_fruits` | Non le modifica | Nuova lista |
| Contare occorrenze | `fruits.count("kiwi")` | Non la modifica | Numero intero |
| Invertire l'ordine | `fruits.reverse()` | La modifica | `None` |
| Copiare | `fruits.copy()` | Non la modifica | Nuova lista (copia superficiale) |
| Cercare un indice | `fruits.index("kiwi")` | Non la modifica | Numero intero |
| Sostituire | `fruits[0] = "kiwi"` | La modifica | Nessun valore restituito dall'assegnazione |
| Aggiungere più elementi | `fruits.extend(["kiwi", "pear"])` | La modifica | `None` |
| Controllare presenza | `"kiwi" in fruits` | Non la modifica | `True` oppure `False` |
| Svuotare | `fruits.clear()` | La modifica | `None` |

# Errori frequenti da evitare

1. **Confondere indice e posizione:** il primo elemento ha indice `0`, non `1`.
2. **Confondere `remove()` e `pop()`:** il primo riceve un *valore*, il secondo un *indice* (facoltativo).
3. **Credere che la fine dello slicing sia inclusa:** `fruits[1:3]` seleziona gli indici `1` e `2`.
4. **Assegnare il risultato di `append()`, `sort()` o `reverse()` alla lista:** tali metodi modificano la lista originale e restituiscono `None`.
5. **Usare `index()` o `remove()` senza controllare che il valore esista:** in caso contrario si ottiene `ValueError`.
6. **Accedere a posizioni inesistenti:** `fruits[len(fruits)]` genera `IndexError` su una lista; l'ultimo indice è `len(fruits) - 1`.
7. **Confondere copia e assegnazione:** `lista2 = lista1` non crea una lista indipendente.

# Esercizio riepilogativo svolto: contare i valori maggiori di 5

In questo esempio si costruisce una lista di numeri casuali e, con i **soli cicli `for` tradizionali**, si crea una seconda lista contenente `1` quando il numero corrispondente è maggiore di 5 e `0` negli altri casi.

```python
import random

numbers = []
for i in range(10):
    numbers.append(random.randint(1, 10))

print("Numeri:", numbers)

greater_numbers = []
for num in numbers:
    if num > 5:
        greater_numbers.append(1)
    else:
        greater_numbers.append(0)

print("Indicatori:", greater_numbers)
print("Numeri maggiori di 5:", sum(greater_numbers))
```

**Possibile output** (i numeri cambiano a ogni esecuzione):

```text
Numeri: [3, 8, 1, 6, 10, 5, 2, 9, 4, 7]
Indicatori: [0, 1, 0, 1, 1, 0, 0, 1, 0, 1]
Numeri maggiori di 5: 5
```

**Domande per verificare la comprensione:**

1. Qual è la differenza fra `append()` e `insert()`?
2. Che differenza c'è fra `remove("banana")` e `pop(1)`?
3. Perché `fruits[1:3]` non comprende l'elemento di indice `3`?
4. Quali operazioni modificano la lista originale e quali ne creano una nuova?
5. Come si può percorrere una lista utilizzando `for` e `range(len(lista))`?
