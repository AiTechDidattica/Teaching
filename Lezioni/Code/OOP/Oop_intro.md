
# Introduzione alla Programmazione Orientata agli Oggetti (OOP) in Python

La programmazione orientata agli oggetti (OOP) è un paradigma di programmazione basato sul concetto di **oggetti**, che rappresentano entità del mondo reale o concetti astratti. Ogni oggetto è un'istanza di una **classe**, che definisce un "prototipo" o una "struttura" da cui gli oggetti vengono creati.

## Concetti fondamentali dell'OOP

### 1. Classe e Oggetto
- **Classe**: È un modello o una struttura che descrive le proprietà (attributi) e i comportamenti (metodi) di un oggetto.
- **Oggetto**: È un'istanza di una classe.

```python
# Definizione di una classe
class Persona:
    def __init__(self, nome, eta):
        self.nome = nome
        self.eta = eta

    def saluta(self):
        print(f"Ciao, mi chiamo {self.nome} e ho {self.eta} anni.")

# Creazione di un oggetto
persona1 = Persona("Luca", 30)
persona1.saluta()  # Output: Ciao, mi chiamo Luca e ho 30 anni.
```

### 2. Incapsulamento
L'incapsulamento si riferisce alla capacità di nascondere i dettagli interni di un oggetto e di esporre solo ciò che è necessario. In Python, gli attributi privati si indicano con un underscore (`_`) o un doppio underscore (`__`).

```python
class ContoBancario:
    def __init__(self, saldo):
        self.__saldo = saldo  # Attributo privato

    def deposita(self, importo):
        self.__saldo += importo

    def visualizza_saldo(self):
        print(f"Saldo attuale: {self.__saldo}")

conto = ContoBancario(1000)
conto.deposita(500)
conto.visualizza_saldo()  # Output: Saldo attuale: 1500
```

### 3. Ereditarietà
L'ereditarietà permette a una classe (classe derivata) di ereditare attributi e metodi da un'altra classe (classe base).

```python
class Veicolo:
    def __init__(self, marca):
        self.marca = marca

    def guida(self):
        print(f"Sto guidando un veicolo della marca {self.marca}.")

class Auto(Veicolo):
    def __init__(self, marca, modello):
        super().__init__(marca)
        self.modello = modello

    def guida(self):
        print(f"Sto guidando un'auto {self.marca} {self.modello}.")

auto1 = Auto("Fiat", "Panda")
auto1.guida()  # Output: Sto guidando un'auto Fiat Panda.
```

### 4. Polimorfismo
Il polimorfismo consente di utilizzare un'interfaccia comune per oggetti di classi diverse.

```python
class Animale:
    def parla(self):
        pass

class Cane(Animale):
    def parla(self):
        print("Bau!")

class Gatto(Animale):
    def parla(self):
        print("Miao!")

def fai_parlare(animale):
    animale.parla()

cane = Cane()
gatto = Gatto()

fai_parlare(cane)  # Output: Bau!
fai_parlare(gatto)  # Output: Miao!
```

### 5. Astrazione
L'astrazione nasconde i dettagli complessi e mostra solo le funzionalità essenziali.

```python
from abc import ABC, abstractmethod

class Forma(ABC):
    @abstractmethod
    def area(self):
        pass

class Rettangolo(Forma):
    def __init__(self, larghezza, altezza):
        self.larghezza = larghezza
        self.altezza = altezza

    def area(self):
        return self.larghezza * self.altezza

rettangolo = Rettangolo(10, 5)
print(f"L'area del rettangolo è: {rettangolo.area()}")  # Output: L'area del rettangolo è: 50
```

### Esempio: Oggetti Collegati (Studente ed Esami)

In questo esempio, creeremo due classi: **Studente** ed **Esame**. Ogni studente può avere un numero variabile di esami superati.

```python
class Esame:
    def __init__(self, nome, voto):
        self.nome = nome
        self.voto = voto

    def __str__(self):
        return f"Esame: {self.nome}, Voto: {self.voto}"

class Studente:
    def __init__(self, nome):
        self.nome = nome
        self.esami_superati = []

    def aggiungi_esame(self, esame):
        self.esami_superati.append(esame)

    def visualizza_esami(self):
        if self.esami_superati:
            print(f"Esami superati da {self.nome}:")
            for esame in self.esami_superati:
                print(f" - {esame}")
        else:
            print(f"{self.nome} non ha ancora superato alcun esame.")

# Creazione di uno studente
studente1 = Studente("Mario Rossi")

# Creazione di alcuni esami
esame1 = Esame("Matematica", 28)
esame2 = Esame("Fisica", 30)

# Aggiunta degli esami allo studente
studente1.aggiungi_esame(esame1)
studente1.aggiungi_esame(esame2)

# Visualizzazione degli esami dello studente
studente1.visualizza_esami()
# Output:
# Esami superati da Mario Rossi:
#  - Esame: Matematica, Voto: 28
#  - Esame: Fisica, Voto: 30
```
Questo esempio mostra come gli oggetti possono essere collegati tra loro per rappresentare relazioni complesse. Qui, ogni **Studente** ha una lista di oggetti **Esame** che rappresentano gli esami superati.

## Perché utilizzare l'OOP?
- **Modularità**: Il codice è più organizzato e facile da mantenere.
- **Riutilizzo del codice**: Grazie all'ereditarietà.
- **Facilità di debug**: Il codice è strutturato in blocchi (classi e oggetti) isolati.

L'OOP è particolarmente utile per progetti di grandi dimensioni, in cui la gestione e l'organizzazione del codice sono fondamentali.

## Conclusione
La programmazione orientata agli oggetti è un potente paradigma che consente di scrivere codice più strutturato, modulare e riutilizzabile. Python, con la sua sintassi semplice e leggibile, è uno strumento ideale per apprendere e utilizzare l'OOP.
