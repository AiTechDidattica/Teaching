# Esercizi sui cicli `for` in Python — Tracce, listati e output

Questa raccolta contiene cinque esercizi con **traccia originale**, **soluzione completa in Python** ed **esempio di esecuzione**. Gli esempi utilizzano cicli `for` tradizionali, senza *list comprehension*.

---

## 1. Sequenza numerica — Base

Scrivere un programma che acquisisca un numero intero positivo N e visualizzi tutti i numeri compresi tra 1 e N, prima in ordine crescente e poi in ordine decrescente.

**Concetti:** `range()`.

### Listato Python

```python
n = int(input("Inserisci un numero intero positivo N: "))

if n > 0:
    print("Ordine crescente:")
    for i in range(1, n + 1):
        print(i, end=" ")

    print()
    print("Ordine decrescente:")
    for i in range(n, 0, -1):
        print(i, end=" ")

    print()
else:
    print("Errore: N deve essere maggiore di zero.")
```

### Esempio di esecuzione

```text
Inserisci un numero intero positivo N: 5
Ordine crescente:
1 2 3 4 5
Ordine decrescente:
5 4 3 2 1
```

---

## 2. Numeri pari e dispari — Base

Acquisire due numeri interi A e B, con A minore di B. Visualizzare separatamente tutti i numeri pari e tutti i numeri dispari compresi nell'intervallo [A, B].

**Concetti:** `range()` e condizioni.

### Listato Python

```python
a = int(input("Inserisci A: "))
b = int(input("Inserisci B (maggiore di A): "))

if a < b:
    print("Numeri pari:")
    for i in range(a, b + 1):
        if i % 2 == 0:
            print(i, end=" ")

    print()
    print("Numeri dispari:")
    for i in range(a, b + 1):
        if i % 2 != 0:
            print(i, end=" ")

    print()
else:
    print("Errore: A deve essere minore di B.")
```

### Esempio di esecuzione

```text
Inserisci A: 3
Inserisci B (maggiore di A): 10
Numeri pari:
4 6 8 10
Numeri dispari:
3 5 7 9
```

---

## 3. La tabellina personalizzata — Base

Acquisire un numero intero e visualizzarne la tabellina da 1 a 10, riportando ogni moltiplicazione e il relativo risultato.

**Concetti:** contatore e formattazione.

### Listato Python

```python
numero = int(input("Inserisci un numero intero: "))

print("Tabellina del", numero)
for i in range(1, 11):
    risultato = numero * i
    print(f"{numero} x {i} = {risultato}")
```

### Esempio di esecuzione

```text
Inserisci un numero intero: 7
Tabellina del 7
7 x 1 = 7
7 x 2 = 14
7 x 3 = 21
7 x 4 = 28
7 x 5 = 35
7 x 6 = 42
7 x 7 = 49
7 x 8 = 56
7 x 9 = 63
7 x 10 = 70
```

---

## 4. Somma e media di N numeri — Intermedio

Chiedere quanti numeri si desidera inserire, acquisirli uno alla volta e calcolarne la somma e la media aritmetica. Assicurarsi che la quantità richiesta sia maggiore di zero.

**Concetti:** `for` e accumulatore.

### Listato Python

```python
n = int(input("Quanti numeri vuoi inserire? "))

while n <= 0:
    print("Errore: la quantità deve essere maggiore di zero.")
    n = int(input("Quanti numeri vuoi inserire? "))

somma = 0

for i in range(n):
    numero = float(input(f"Inserisci il numero {i + 1}: "))
    somma += numero

media = somma / n

print("Somma:", somma)
print("Media:", media)
```

### Esempio di esecuzione

```text
Quanti numeri vuoi inserire? 4
Inserisci il numero 1: 5
Inserisci il numero 2: 7
Inserisci il numero 3: 8
Inserisci il numero 4: 10
Somma: 30.0
Media: 7.5
```

---

## 5. Ricerca di un carattere — Intermedio

Acquisire una parola e un carattere. Utilizzando un ciclo `for`, determinare quante volte il carattere compare nella parola, senza utilizzare il metodo `count()`.

**Concetti:** `for each`.

### Listato Python

```python
parola = input("Inserisci una parola: ")
carattere = input("Inserisci un carattere: ")

while len(carattere) != 1:
    print("Errore: inserisci un solo carattere.")
    carattere = input("Inserisci un carattere: ")

occorrenze = 0

for lettera in parola:
    if lettera == carattere:
        occorrenze += 1

print(f"Il carattere '{carattere}' compare {occorrenze} volte nella parola '{parola}'.")
```

### Esempio di esecuzione

```text
Inserisci una parola: banana
Inserisci un carattere: a
Il carattere 'a' compare 3 volte nella parola 'banana'.
```

**Nota:** il confronto è sensibile alle maiuscole e alle minuscole: `A` e `a` sono considerati caratteri diversi.
