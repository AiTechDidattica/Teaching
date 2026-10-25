# Lezione di Informatica – I cicli `for` in Python

## 1. Introduzione: le strutture iterative

Nella programmazione, una **struttura iterativa** permette di eseguire ripetutamente un blocco di istruzioni, evitando di doverle riscrivere più volte.

In Python, le due principali strutture iterative sono:

- **`while`**: che ripete un blocco di istruzioni finché una determinata condizione risulta vera.
- **`for`**: permette di scorrere gli elementi di una sequenza o più in generale di un oggetto iterabile, eseguendo un blocco di istruzioni per ciascun ciclo.

La differenza fondamentale riguarda il modo in cui viene controllata la ripetizione: 
- Nel caso del costrutto **`while`** la gestione è di tipo manuale
- Nel caso del costrutto **`for`** la gestione è di tipo automatico

Consideriamo un programma che deve visualizzare i numeri da 1 a 5.

**Con `while`:**

```python
numero = 1

while numero <= 5:
    print(numero)
    numero += 1
```

**Con `for`:**

```python
for numero in range(1, 6):
    print(numero)
```

Entrambi i programmi producono:

```text
1
2
3
4
5
```

Nel primo caso dobbiamo inizializzare una variabile, controllare una condizione e aggiornare esplicitamente il contatore. Nel secondo caso è il ciclo `for` a gestire automaticamente l'avanzamento attraverso i valori prodotti dalla funzione `range()`.

## 2. Definizione e sintassi del ciclo `for`

Il ciclo `for` è un'istruzione che consente di **eseguire un blocco di codice una volta per ogni elemento di un iterabile**.

La sintassi generale è:

```python
for variabile in iterabile:
    istruzione_1
    istruzione_2
    # Altre istruzioni

# Prima istruzione esterna al ciclo
```

Dove:

- `for` è la parola chiave che introduce il ciclo.
- `variabile` assume, a ogni iterazione, il valore dell'elemento corrente.
- `in` introduce l'oggetto da attraversare.
- `iterabile` è una sequenza o un altro oggetto che può essere percorso.

Un'**iterazione** è una singola esecuzione del corpo del ciclo.

### Esempio 1 – Ripetizione di un messaggio

```python
for i in range(3):
    print("Benvenuto alla lezione di Python!")
```

Output:

```text
Benvenuto alla lezione di Python!
Benvenuto alla lezione di Python!
Benvenuto alla lezione di Python!
```

Il blocco viene eseguito tre volte. La variabile `i` (indice) assume successivamente i valori `0`, `1` e `2`, anche se in questo programma non viene utilizzata.

Quando non si necessità di utilizzare valore della variabile `i`, per convenzione si può scrivere:

```python
for _ in range(3):
    print("Benvenuto alla lezione di Python!")
```

Il carattere `_` (placeholder) indica che non abbiamo intenzione di utilizzare il valore corrente dell'indice.


### 2.1 Gli oggetti iterabili in Python

Un **oggetto iterabile** (*iterable*) è un oggetto che permette di attraversare progressivamente i propri elementi, uno alla volta, attraverso un processo chiamato **iterazione**.

Il ciclo `for` utilizza questo meccanismo per eseguire un blocco di istruzioni per ciascun elemento dell'oggetto iterabile, terminando automaticamente quando tutti gli elementi sono stati attraversati.

In Python, i principali oggetti iterabili sono:

| Oggetto | Esempio | Elementi attraversati |
|---|---|---|
| Stringa (`str`) | `"Python"` | Singoli caratteri |
| Lista (`list`) | `[10, 20, 30]` | Elementi della lista |
| Tupla (`tuple`) | `(4, 8, 12)` | Elementi della tupla |
| Dizionario (`dict`) | `{"a": 1, "b": 2}` | Chiavi del dizionario |
| Insieme (`set`) | `{3, 6, 9}` | Elementi, senza ordine garantito |
| Range (`range`) | `range(5)` | Numeri interi da 0 a 4 |

**Esempio – Iterazione su una lista**

```python
numeri = [10, 20, 30]

for numero in numeri:
    print(numero)
```

**Output:**

```text
10
20
30
```

In questo esempio:
- `numeri` è l'**oggetto iterabile**;
- `numero` è la **variabile di iterazione**, che assume progressivamente il valore di ciascun elemento;
- il corpo del ciclo viene eseguito **tre volte**, una per ogni elemento della lista.

**Osservazione:** non tutti gli oggetti Python sono iterabili. Ad esempio, un singolo numero intero (`int`) non può essere attraversato direttamente attraverso un ciclo `for`.

Il ciclo `for` non serve quindi esclusivamente a ripetere istruzioni un numero prestabilito di volte, ma più in generale ad **attraversare gli elementi di un oggetto iterabile**.


## 3. La funzione `range()`

La funzione `range()` genera un oggetto che rappresenta una sequenza di numeri interi. È particolarmente utile quando vogliamo eseguire un'operazione un numero prestabilito di volte oppure utilizzare valori numerici progressivi.

Esistono tre forme principali.

### Le tre sintassi di `range()`

| Sintassi | Significato |
|---|---|
| `range(stop)` | Da `0` fino a `stop` escluso |
| `range(start, stop)` | Da `start` fino a `stop` escluso |
| `range(start, stop, step)` | Come sopra, ma con incremento o decremento `step` |

**Nota:** il valore finale `stop` non viene mai incluso. Lo `step` predefinito è 1 e non può essere 0.

### 3.1 `range(stop)`

```python
for i in range(5):
    print(i)
```

**Visualizzazione delle iterazioni:**

| Iterazione | 1 | 2 | 3 | 4 | 5 |
|---|---:|---:|---:|---:|---:|
| Valore di `i` | 0 | 1 | 2 | 3 | 4 |

Il ciclo compie cinque iterazioni, partendo da zero.

### 3.2 `range(start, stop)`

```python
for i in range(2, 7):
    print(i)
```

Output: `2, 3, 4, 5, 6`.

**Osservazione:** per includere il numero 7, occorre utilizzare `range(2, 8)`.

### 3.3 `range(start, stop, step)`

```python
for i in range(0, 11, 2):
    print(i)
```

Output: `0, 2, 4, 6, 8, 10`.

Lo `step` determina la distanza tra due valori consecutivi.

Lo stesso meccanismo permette di realizzare cicli decrescenti.

```python
for i in range(10, 0, -2):
    print(i)
```

Output: `10, 8, 6, 4, 2`.

Il passo negativo determina un decremento della variabile a ogni iterazione.

I parametri **Start**, **Stop** e **Step** possono essere modificati tramite controlli ed i valori generati vengono visualizzati insieme al numero di iterazioni. 

**Impostazione iniziale della simulazione:** `start = 1`, `stop = 11`, `step = 2`.

```python
start = 1
stop = 11
step = 2

valori = list(range(start, stop, step))
print(valori)
print(f"{len(valori)} iterazioni")
```

Risultato:

```text
[1, 3, 5, 7, 9]
5 iterazioni
```

**Prove da effettuare:**

| Start | Stop | Step | Valori prodotti | Iterazioni |
|---:|---:|---:|---|---:|
| 1 | 11 | 2 | 1, 3, 5, 7, 9 | 5 |
| 0 | 5 | 1 | 0, 1, 2, 3, 4 | 5 |
| 10 | 0 | -2 | 10, 8, 6, 4, 2 | 5 |
| 5 | 0 | 1 | Nessuno: sequenza vuota | 0 |

È importante comprendere che `range()` non è un elenco di numeri già memorizzati in una lista: rappresenta una sequenza calcolabile, attraverso la quale Python può iterare.

### Esempio 2 – Calcolo della somma dei primi N numeri naturali

```python
n = int(input("Inserisci N: "))

somma = 0

for i in range(1, n + 1):
    somma += i

print(f"La somma è {somma}")
```

Per `n = 5`, le operazioni sono:

| Iterazione | `i` | `somma` dopo l'aggiornamento |
|---|---:|---:|
| Iniziale | — | 0 |
| 1 | 1 | 1 |
| 2 | 2 | 3 |
| 3 | 3 | 6 |
| 4 | 4 | 10 |
| 5 | 5 | 15 |

In questo esempio, `somma` è una **variabile accumulatrice**, perché conserva e aggiorna progressivamente un risultato.

## 4. Il ciclo `for` come ciclo `for each`

In Python il `for` è, per sua natura, un ciclo di tipo *for each*: permette di attraversare direttamente gli elementi di un iterabile.

La struttura è:

```python
for elemento in sequenza:
    # Istruzioni che utilizzano elemento
```

In questo caso non stiamo lavorando con un contatore numerico, ma direttamente con il contenuto della sequenza.

### Esempio 3 – Scorrimento di una lista

```python
frutti = ["Mela", "Pera", "Banana", "Arancia"]

for frutto in frutti:
    print(f"Frutto: {frutto}")
```

A ogni iterazione, `frutto` assume il valore dell'elemento corrente.

| Iterazione | Valore di `frutto` |
|---|---|
| 1 | `"Mela"` |
| 2 | `"Pera"` |
| 3 | `"Banana"` |
| 4 | `"Arancia"` |

Non è necessario conoscere anticipatamente il numero degli elementi della lista.

### Esempio 4 – Scorrimento di una stringa

Anche una stringa è iterabile: possiamo attraversarla un carattere alla volta.

```python
parola = "PYTHON"

for carattere in parola:
    print(carattere)
```

L'output conterrà le lettere `P`, `Y`, `T`, `H`, `O`, `N`, ciascuna su una riga.

### Esempio 5 – Conteggio dei numeri pari in una lista

```python
numeri = [4, 7, 12, 19, 22, 31]

contatore = 0

for numero in numeri:
    if numero % 2 == 0:
        contatore += 1

print(f"Numeri pari: {contatore}")
```

**Distinzione importante:** un contatore aumenta di una quantità prefissata, tipicamente 1, ogni volta che si verifica un evento; un accumulatore raccoglie invece risultati progressivi, come una somma.

## 5. Iterazione mediante indice: `range()` e `len()`

Talvolta non è sufficiente conoscere il valore di un elemento. Potrebbe essere necessario conoscere anche la sua **posizione all'interno della sequenza**.

Nelle liste Python, la posizione di un elemento è identificata da un indice che parte da zero.

Prendiamo la lista:

```python
voti = [7, 8, 6, 9]
```

**Rappresentazione della lista:**

| Indice | 0 | 1 | 2 | 3 |
|---|---:|---:|---:|---:|
| Valore | 7 | 8 | 6 | 9 |

La funzione `len()` restituisce il numero degli elementi presenti in una sequenza.

```python
voti = [7, 8, 6, 9]

for i in range(len(voti)):
    print(f"Indice {i}: voto {voti[i]}")
```

In questo programma:

- `len(voti)` restituisce `4`;
- `range(4)` produce gli indici `0, 1, 2, 3`;
- `voti[i]` consente di accedere all'elemento nella posizione corrente.

### Esempio 6 – Modificare gli elementi di una lista

Un utilizzo particolarmente interessante dell'iterazione per indice consiste nella possibilità di modificare direttamente il contenuto di una lista.

```python
numeri = [2, 4, 6, 8]

for i in range(len(numeri)):
    numeri[i] = numeri[i] * 2

print(numeri)
```

Output:

```text
[4, 8, 12, 16]
```

Qui l'utilizzo dell'indice è necessario per assegnare i nuovi valori alle posizioni originali della lista.

Attenzione: scrivere semplicemente `numero = numero * 2` all'interno di un `for numero in numeri` non modificherebbe gli elementi della lista, ma soltanto la variabile locale `numero`.

## 6. La funzione `enumerate()`: ottenere indice e valore

Il comando che cercavi è proprio **`enumerate()`**.

Questa funzione consente di attraversare un iterabile ottenendo contemporaneamente due informazioni:

1. L'indice progressivo dell'elemento.
2. Il valore dell'elemento stesso.

La sintassi più comune è:

```python
for indice, elemento in enumerate(sequenza):
    # Istruzioni
```

### Esempio 7 – Elenco numerato degli studenti

```python
studenti = ["Marco", "Anna", "Luca", "Sara"]

for indice, studente in enumerate(studenti):
    print(f"{indice}: {studente}")
```

Output:

```text
0: Marco
1: Anna
2: Luca
3: Sara
```

Se vogliamo cominciare la numerazione da 1, possiamo utilizzare il parametro `start`.

```python
for indice, studente in enumerate(studenti, start=1):
    print(f"{indice}: {studente}")
```

Output:

```text
1: Marco
2: Anna
3: Luca
4: Sara
```

### Come funziona `enumerate()` (trasposizione della simulazione interattiva)

Nella simulazione originale è possibile avanzare o retrocedere tra quattro iterazioni, visualizzando ogni volta i valori di `indice` e `studente` prodotti da `enumerate(studenti, start=1)`.

| Iterazione | `indice` | `studente` | Output |
|---:|---:|---|---|
| 1 | 1 | Marco | `1: Marco` |
| 2 | 2 | Anna | `2: Anna` |
| 3 | 3 | Luca | `3: Luca` |
| 4 | 4 | Sara | `4: Sara` |

### Quando utilizzare le diverse forme di iterazione?

| Modalità | Quando è utile |
|---|---|
| `for i in range(n)` | Quando occorre ripetere un'operazione `n` volte |
| `for elemento in lista` | Quando interessa soltanto il valore |
| `for i in range(len(lista))` | Quando serve accedere o modificare gli elementi tramite indice |
| `for i, elemento in enumerate(lista)` | Quando servono contemporaneamente posizione e valore |

È bene precisare che l'indice restituito da `enumerate()` rappresenta un conteggio progressivo: il suo valore iniziale può essere personalizzato e non necessariamente coincide con un indice valido della lista.

## 7. Cicli `for` annidati

Un **ciclo annidato** è un ciclo contenuto all'interno del corpo di un altro ciclo.

Questa struttura permette di ripetere un insieme di operazioni per ogni iterazione del ciclo esterno.

La sintassi generale è:

```python
for i in range(n):
    for j in range(m):
        # Istruzioni del ciclo interno
```

Per ogni valore assunto da `i`, il ciclo interno viene eseguito completamente, attraversando tutti i valori previsti per `j`.

Se il ciclo esterno compie 3 iterazioni e quello interno ne compie 4, il blocco più interno viene eseguito **12 volte**.

### Esempio 8 – Comprendere l'ordine delle iterazioni

```python
for i in range(1, 4):
    for j in range(1, 4):
        print(f"i = {i}, j = {j}")
```

Output:

```text
i = 1, j = 1
i = 1, j = 2
i = 1, j = 3
i = 2, j = 1
i = 2, j = 2
i = 2, j = 3
i = 3, j = 1
i = 3, j = 2
i = 3, j = 3
```

Si osserva che `i` rimane costante mentre `j` attraversa tutti i valori. Soltanto al completamento del ciclo interno viene aggiornata `i`.

### Visualizzazione dei cicli annidati (trasposizione della simulazione interattiva)

Nella simulazione originale si possono scegliere da 2 a 5 iterazioni esterne e da 2 a 6 iterazioni interne, quindi avanzare o retrocedere un passaggio alla volta. La cella corrente mostra i valori della coppia `(i, j)`, e le celle precedenti rappresentano le iterazioni già eseguite.

**Configurazione iniziale:** `outer = 3`, `inner = 4`.

```python
for i in range(1, 4):
    for j in range(1, 5):
        print(i, j)
```

**Griglia dei passaggi**, letta da sinistra a destra e dall'alto in basso:

| Ciclo esterno / interno | `j = 1` | `j = 2` | `j = 3` | `j = 4` |
|---|---|---|---|---|
| `i = 1` | (1, 1) | (1, 2) | (1, 3) | (1, 4) |
| `i = 2` | (2, 1) | (2, 2) | (2, 3) | (2, 4) |
| `i = 3` | (3, 1) | (3, 2) | (3, 3) | (3, 4) |

Numero complessivo di esecuzioni del corpo del ciclo interno: **3 × 4 = 12**.

Per effettuare una simulazione passo per passo anche a console:

```python
for i in range(1, 4):
    for j in range(1, 5):
        print(f"i = {i}, j = {j}")
        input("Premi INVIO per passare all'iterazione successiva...")
```

### Esempio 9 – La tabellina pitagorica

I cicli annidati sono particolarmente utili quando si devono rappresentare dati in forma tabellare.

```python
for riga in range(1, 6):
    for colonna in range(1, 6):
        print(f"{riga * colonna:4}", end="")

    print()
```

Output:

```text
   1   2   3   4   5
   2   4   6   8  10
   3   6   9  12  15
   4   8  12  16  20
   5  10  15  20  25
```

In questo esempio introduciamo due aspetti importanti:

- `end=""` impedisce a `print()` di andare a capo dopo ogni valore;
- `print()` senza argomenti permette di passare alla riga successiva al completamento del ciclo interno.

La formattazione `:4` riserva uno spazio minimo di quattro caratteri, allineando i numeri in colonne.

### Esempio 10 – Disegnare un triangolo con gli asterischi

```python
n = int(input("Inserisci l'altezza: "))

for i in range(1, n + 1):
    for j in range(i):
        print("*", end="")

    print()
```

Se `n = 5`, il risultato è:

```text
*
**
***
****
*****
```

Il ciclo esterno determina il numero della riga corrente. Il ciclo interno stampa un numero di asterischi pari al valore della riga.

La particolarità è che il numero di iterazioni del ciclo interno **dipende dalla variabile del ciclo esterno**.

### Esempio 11 – Scorrere una matrice

Una matrice può essere rappresentata tramite una lista di liste.

```python
matrice = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for riga in matrice:
    for elemento in riga:
        print(elemento, end=" ")

    print()
```

Output:

```text
1 2 3
4 5 6
7 8 9
```

Questo esempio combina due cicli *for each*, senza utilizzare indici numerici.

Se invece volessimo conoscere le coordinate di ciascun elemento, potremmo scrivere:

```python
for i, riga in enumerate(matrice):
    for j, valore in enumerate(riga):
        print(f"matrice[{i}][{j}] = {valore}")
```

Si tratta di un'applicazione che unisce i concetti di annidamento ed `enumerate()`.

## 8. Le istruzioni `break` e `continue` nei cicli `for`

Come già avviene nei cicli `while`, anche nei cicli `for` possiamo modificare il normale flusso di esecuzione attraverso `break` e `continue`.

**`break`** interrompe immediatamente il ciclo più interno che lo contiene.

```python
for numero in range(1, 11):
    if numero == 6:
        break

    print(numero)
```

Output: `1, 2, 3, 4, 5`.

**`continue`** interrompe soltanto l'iterazione corrente e passa alla successiva.

```python
for numero in range(1, 11):
    if numero % 2 == 0:
        continue

    print(numero)
```

Output: `1, 3, 5, 7, 9`.

Nei cicli annidati, un `break` collocato nel ciclo interno interrompe soltanto quel ciclo: il ciclo esterno può continuare normalmente.

---

# 9. Esercizi da assegnare a casa

Le seguenti tracce sono ordinate secondo una difficoltà crescente, per consolidare gradualmente i concetti affrontati.

**Scheda di esercitazione — 12 programmi.** Nell'interfaccia originale gli esercizi erano selezionabili mediante filtri (*Tutti*, *Base*, *Intermedi*, *Avanzati*) e contrassegnabili come completati; di seguito sono riportati **tutti e dodici, senza esclusioni**.

### 1. Sequenza numerica — Base

Scrivere un programma che acquisisca un numero intero positivo N e visualizzi tutti i numeri compresi tra 1 e N, prima in ordine crescente e poi in ordine decrescente.

**Concetti:** `range()`.

### 2. Numeri pari e dispari — Base

Acquisire due numeri interi A e B, con A minore di B. Visualizzare separatamente tutti i numeri pari e tutti i numeri dispari compresi nell'intervallo [A, B].

**Concetti:** `range()` e condizioni.

### 3. La tabellina personalizzata — Base

Acquisire un numero intero e visualizzarne la tabellina da 1 a 10, riportando ogni moltiplicazione e il relativo risultato.

**Concetti:** contatore e formattazione.

### 4. Somma e media di N numeri — Intermedio

Chiedere quanti numeri si desidera inserire, acquisirli uno alla volta e calcolarne la somma e la media aritmetica. Assicurarsi che la quantità richiesta sia maggiore di zero.

**Concetti:** `for` e accumulatore.

### 5. Ricerca di un carattere — Intermedio

Acquisire una parola e un carattere. Utilizzando un ciclo `for`, determinare quante volte il carattere compare nella parola, senza utilizzare il metodo `count()`.

**Concetti:** `for each`.

### 6. Analisi di una lista — Intermedio

Data la lista `[12, 5, 8, 21, 4, 17, 10]`, determinare quanti numeri sono pari, quanti dispari e la somma degli elementi maggiori di 10.

**Concetti:** `for each` e `if`.

### 7. Posizioni dei numeri negativi — Intermedio

Data la lista `[4, -2, 7, -5, 0, -1, 9]`, visualizzare il valore e l'indice di ciascun elemento negativo utilizzando `enumerate()`.

**Concetti:** `enumerate()`.

### 8. Aggiornamento dei prezzi — Intermedio

Data una lista di prezzi `[10.0, 25.0, 40.0, 15.0]`, aumentare ciascun prezzo del 10%, modificando direttamente gli elementi della lista. Visualizzare la lista aggiornata.

**Concetti:** `range(len())`.

### 9. Rettangolo di asterischi — Avanzato

Acquisire due numeri interi positivi, che rappresentano altezza e larghezza, e disegnare un rettangolo composto da asterischi. Utilizzare esclusivamente cicli `for` annidati per generare il disegno.

**Concetti:** `for` annidati.

### 10. Triangolo numerico — Avanzato

Acquisire un numero N positivo e stampare N righe. Nella prima riga visualizzare 1, nella seconda 1 2, nella terza 1 2 3 e così via, fino a N.

**Concetti:** annidamento variabile.

### 11. Tavola pitagorica N × N — Avanzato

Acquisire un numero intero N compreso tra 2 e 10 e visualizzare una tavola pitagorica di N righe e N colonne, allineando correttamente i risultati.

**Concetti:** `for` annidati e formattazione.

### 12. Analisi di una matrice — Avanzato

Data una matrice quadrata 3 × 3 di numeri interi, calcolare la somma complessiva degli elementi, la somma degli elementi della diagonale principale e individuare il valore massimo.

**Concetti:** `for` annidati ed `enumerate()`.

## 10. Indicazioni metodologiche per lo svolgimento

Per ciascun programma è opportuno chiedere agli studenti di:

1. Individuare i dati di input, le elaborazioni richieste e i risultati di output.
2. Scegliere la forma di iterazione più adatta, motivandola.
3. Implementare il programma in Python, utilizzando nomi di variabili significativi e commenti essenziali.
4. Eseguire almeno due prove con dati differenti, verificando la correttezza dei risultati.
5. Gestire, ove necessario, gli input non validi, ricorrendo agli strumenti già studiati.

## 11. Riepilogo finale

| Costrutto | Funzione |
|---|---|
| `for` | Esegue istruzioni per ciascun elemento di un iterabile |
| `range(n)` | Permette di iterare sui numeri da 0 a n−1 |
| `range(a, b, s)` | Permette di iterare da a verso b, escluso, con passo s |
| `for x in lista` | Accede direttamente agli elementi |
| `len(lista)` | Restituisce il numero degli elementi |
| `range(len(lista))` | Permette di attraversare gli indici della lista |
| `enumerate(lista)` | Restituisce indice progressivo ed elemento |
| `enumerate(lista, start=1)` | Permette di personalizzare l'indice iniziale |
| `for` annidati | Permettono di eseguire un ciclo all'interno di un altro |
| `break` | Interrompe il ciclo corrente |
| `continue` | Passa all'iterazione successiva |

---

### Proposta di organizzazione didattica

Considerando lezioni di due ore, suddividerei il materiale in **tre incontri**, per dare agli studenti il tempo di sperimentare concretamente i costrutti.

| Lezione | Contenuti | Attività pratica |
|---|---|---|
| 1ª – 2 ore | Introduzione al `for`, sintassi, `range()` e contatori/accumulatori | Sequenze numeriche, somme e tabelline |
| 2ª – 2 ore | `for each`, liste, indici, `len()` ed `enumerate()` | Elaborazione delle liste e ricerca di elementi |
| 3ª – 2 ore | Cicli annidati, matrici, `break` e `continue` | Disegni con asterischi e tavola pitagorica |

**Suggerimento didattico:** prima di eseguire ciascun programma, chiederei agli studenti di prevederne l'output, annotando come cambiano le variabili a ogni iterazione. Questo esercizio di *tracciamento del codice* è particolarmente utile per i cicli annidati, dove spesso nasce la difficoltà di comprendere quale variabile venga aggiornata e in quale momento.

La progressione proposta permette di passare dall'esecuzione ripetuta di istruzioni all'elaborazione di strutture dati, senza introdurre prematuramente concetti più avanzati come comprensioni di lista, generatori o iteratori personalizzati.
