
# Operazioni con le Liste in Python

Ecco alcune operazioni comuni che puoi eseguire con le liste in Python.

## Creare una lista
```python
fruits = ["apple", "banana", "cherry"]
print(fruits)
```

## Aggiungere un elemento alla lista
```python
fruits.append("orange")
print(fruits)
```

## Inserire un elemento in una posizione specifica
```python
fruits.insert(1, "kiwi")
print(fruits)
```

## Rimuovere un elemento dalla lista
```python
fruits.remove("banana")
print(fruits)
```

## Rimuovere un elemento per indice
```python
del fruits[0]
print(fruits)
```

## Rimuovere e restituire l'ultimo elemento
```python
last_fruit = fruits.pop()
print("Last fruit removed:", last_fruit)
print("Fruits after pop:", fruits)
```

## Ottenere la lunghezza della lista
```python
length = len(fruits)
print("Length of the list:", length)
```

## Accedere a un elemento della lista
```python
first_fruit = fruits[0]
print("First fruit:", first_fruit)
```

## Slicing di una lista
```python
subset = fruits[1:3]  # Ottiene gli elementi dal secondo al terzo
print("Subset of fruits:", subset)

subset = fruits[:2]   # Ottiene i primi due elementi
print("First two fruits:", subset)

subset = fruits[1:]   # Ottiene tutti gli elementi dal secondo
print("Fruits from the second onward:", subset)

subset = fruits[-2:]  # Ottiene gli ultimi due elementi
print("Last two fruits:", subset)
```

## Ordinare la lista
```python
fruits.sort()
print("Sorted fruits:", fruits)
```

## Unire due liste
```python
more_fruits = ["grape", "pear"]
combined_fruits = fruits + more_fruits
print("Combined fruits:", combined_fruits)
```

## Contare le occorrenze di un elemento
```python
count_kiwi = fruits.count("kiwi")
print("Number of kiwis:", count_kiwi)
```

## Capovolgere la lista
```python
fruits.reverse()
print("Reversed fruits:", fruits)
```

## Copiare una lista
```python
fruits_copy = fruits.copy()
print("Copied fruits:", fruits_copy)
```

## Trovare l'indice di un elemento
```python
kiwi_index = fruits.index("kiwi")
print("Index of kiwi:", kiwi_index)
```
