
# Esempi di Funzioni in Python

## 1. Calcolo della Somma di Due Numeri
Questa funzione prende due numeri come input e restituisce la loro somma.

```python
def somma(a, b):
    return a + b

# Esempio d'uso
risultato = somma(10, 5)
print("La somma è:", risultato)
```

## 2. Fattoriale di un Numero
Questa funzione calcola il fattoriale di un numero intero positivo usando la ricorsione.

```python
def fattoriale(n):
    if n == 0:
        return 1
    else:
        return n * fattoriale(n - 1)

# Esempio d'uso
risultato = fattoriale(5)
print("Il fattoriale è:", risultato)
```

## 3. Verifica se un Numero è Primo
Questa funzione controlla se un numero è primo restituendo `True` se lo è e `False` altrimenti.

```python
def is_primo(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# Esempio d'uso
risultato = is_primo(7)
print("Il numero è primo:", risultato)
```

## 4. Convertitore di Temperatura da Celsius a Fahrenheit
Questa funzione converte una temperatura da gradi Celsius a gradi Fahrenheit.

```python
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Esempio d'uso
risultato = celsius_to_fahrenheit(25)
print("Temperatura in Fahrenheit:", risultato)
```

## 5. Contare le Parole in una Frase
Questa funzione conta il numero di parole in una stringa data.

```python
def conta_parole(frase):
    parole = frase.split()
    return len(parole)

# Esempio d'uso
risultato = conta_parole("Questa è una frase di esempio.")
print("Numero di parole:", risultato)
```

## 6. Verifica se un Numero è Pari o Dispari
Questa funzione prende un numero come input e restituisce una stringa che indica se il numero è pari o dispari.

```python
def pari_o_dispari(numero):
    if numero % 2 == 0:
        return "Pari"
    else:
        return "Dispari"

# Esempio d'uso
numero = 7
risultato = pari_o_dispari(numero)
print(f"Il numero {{numero}} è:", risultato)
```
