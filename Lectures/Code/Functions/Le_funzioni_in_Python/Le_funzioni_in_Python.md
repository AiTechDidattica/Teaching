# Le funzioni in Python

**Informatica – Classe 3AS – Liceo Scientifico Scienze Applicate**

Dispensa teorico-pratica

I listati completi possono essere eseguiti come script Python indipendenti. I frammenti illustrativi vanno letti nel contesto dell’esempio cui appartengono; gli esempi errati sono indicati esplicitamente.

## Indice

1. [Sottoprogrammi, funzioni e programmazione modulare](#1-sottoprogrammi-funzioni-e-programmazione-modulare)
2. [Definizione, chiamata e punto di ingresso del programma](#2-definizione-chiamata-e-punto-di-ingresso-del-programma)
3. [Le funzioni come black box: parametri e argomenti](#3-le-funzioni-come-black-box-parametri-e-argomenti)
4. [Il valore di ritorno: print() e return](#4-il-valore-di-ritorno-print-e-return)
5. [Le quattro tipologie fondamentali di funzioni](#5-le-quattro-tipologie-fondamentali-di-funzioni)
6. [Visibilità delle variabili: namespace e scope](#6-visibilità-delle-variabili-namespace-e-scope)
7. [Il passaggio dei parametri: oggetti mutabili e immutabili](#7-il-passaggio-dei-parametri-oggetti-mutabili-e-immutabili)
8. [Modalità di passaggio degli argomenti](#8-modalità-di-passaggio-degli-argomenti)
9. [Organizzazione di un programma mediante funzioni](#9-organizzazione-di-un-programma-mediante-funzioni)
10. [Cenni alle funzioni ricorsive](#10-cenni-alle-funzioni-ricorsive)

---

## 1. Sottoprogrammi, funzioni e programmazione modulare

### 1.1 I sottoprogrammi

Quando un problema da risolvere mediante un programma diventa particolarmente complesso, può risultare conveniente suddividerlo in problemi più piccoli e semplici da affrontare, detti **sottoproblemi**.

A ciascun sottoproblema può essere associata una specifica porzione di codice, chiamata **sottoprogramma**, alla quale viene affidato un compito ben definito.

In Python i sottoprogrammi vengono realizzati mediante le **funzioni**.

> **DEFINIZIONE – FUNZIONE**
>
> Una funzione è un blocco di istruzioni, identificato da un nome simbolico, progettato per svolgere uno specifico compito e che può essere richiamato una o più volte all'interno di un programma.

Una funzione può, ad esempio:

- acquisire e validare i dati inseriti dall'utente;
- eseguire un calcolo matematico;
- verificare il rispetto di una determinata condizione;
- elaborare gli elementi di una lista;
- visualizzare un menù di scelta;
- visualizzare o restituire il risultato di un'elaborazione.

Le funzioni risultano particolarmente utili quando, all'interno di un programma, è necessario eseguire più volte una stessa operazione: anziché riscrivere ogni volta le medesime istruzioni, è sufficiente definire una funzione e richiamarla ogni volta che se ne presenta la necessità.

### 1.2 La programmazione modulare

La **programmazione modulare** è un approccio alla progettazione e allo sviluppo del software che prevede la suddivisione di un programma in componenti più piccoli, ciascuno dei quali è responsabile dello svolgimento di uno specifico compito.

In Python le funzioni rappresentano uno degli strumenti fondamentali per applicare questo approccio.

![Figura 1.1 – Scomposizione di un problema in sottoproblemi e associazione delle relative funzioni.](images/01_programmazione_modulare.svg)

*Figura 1.1 – Scomposizione di un problema in sottoproblemi e associazione delle relative funzioni.*

La soluzione del problema complessivo si ottiene quindi attraverso l'esecuzione coordinata delle diverse funzioni.

#### Esempio: calcolo dell'area e del perimetro di un cerchio

Supponiamo di voler realizzare un programma che, acquisito il raggio di un cerchio, ne calcoli e visualizzi l'area e il perimetro.

Possiamo scomporre il problema in quattro sottoproblemi, associando a ciascuno di essi una funzione.

| Sottoproblema | Funzione associata |
|---|---|
| Acquisizione e validazione del raggio | `leggi_raggio()` |
| Calcolo del perimetro | `calcola_perimetro()` |
| Calcolo dell'area | `calcola_area()` |
| Visualizzazione dei risultati | `stampa_risultati()` |

![Figura 1.2 – Esempio di scomposizione funzionale: lo schema rappresenta l’organizzazione, non l’ordine di esecuzione.](images/02_scomposizione_cerchio.svg)

*Figura 1.2 – Esempio di scomposizione funzionale: lo schema rappresenta l’organizzazione, non l’ordine di esecuzione.*

Il programma principale avrà quindi il compito di coordinare l'esecuzione delle diverse funzioni necessarie alla risoluzione del problema complessivo.

> **BUONA PRATICA DI PROGRAMMAZIONE**
>
> Una funzione dovrebbe essere progettata per svolgere un compito specifico e ben definito. Il suo nome dovrebbe descrivere chiaramente l'operazione che essa esegue.

### 1.3 I vantaggi dell'utilizzo delle funzioni

| Vantaggio | Descrizione |
|---|---|
| **Modularità** | Permette di suddividere un programma complesso in componenti più piccoli e semplici da gestire. |
| **Riutilizzabilità** | Consente di scrivere un blocco di codice una sola volta e di utilizzarlo più volte, anche in programmi differenti. |
| **Leggibilità** | Rende il codice più ordinato, comprensibile e facilmente interpretabile. |
| **Manutenibilità** | Facilita la modifica, la correzione e il miglioramento del codice. |
| **Testing e debugging** | Permette di verificare il corretto funzionamento delle singole funzioni e di individuare più facilmente eventuali errori. |
| **Collaborazione** | Consente a più programmatori di occuparsi di differenti componenti dello stesso programma. |

L'utilizzo delle funzioni contribuisce inoltre a rispettare un importante principio della programmazione, denominato **DRY – Don't Repeat Yourself** (non ripeterti), secondo il quale è opportuno evitare inutili duplicazioni del codice.

![Figura 1.3 – Riutilizzo del codice mediante l’impiego delle funzioni.](images/03_riutilizzo_codice.svg)

*Figura 1.3 – Riutilizzo del codice mediante l’impiego delle funzioni.*

### 1.4 Le funzioni in Python

In Python possiamo distinguere due principali categorie di funzioni:

- **Funzioni predefinite (built-in functions):** funzioni già disponibili nel linguaggio Python.
- **Funzioni definite dall'utente (user-defined functions):** funzioni progettate e implementate direttamente dal programmatore.

#### 1.4.1 Funzioni predefinite (built-in functions)

Le funzioni built-in sono funzioni messe a disposizione direttamente dal linguaggio Python e utilizzabili senza doverne conoscere o implementare il funzionamento interno e senza dover importare moduli aggiuntivi.

Nel corso delle precedenti lezioni abbiamo già utilizzato numerose funzioni di questo tipo.

| Funzione | Descrizione | Esempio | Risultato |
|---|---|---|---|
| `print()` | Visualizza dati sullo schermo | `print("Ciao")` | Visualizza `Ciao` |
| `input()` | Acquisisce dati da tastiera | `input("Nome: ")` | Stringa inserita |
| `len()` | Restituisce il numero di elementi di una sequenza o collezione | `len("Python")` | `6` |
| `round()` | Arrotonda un numero | `round(3.14159, 2)` | `3.14` |
| `pow()` | Calcola una potenza | `pow(2, 3)` | `8` |
| `abs()` | Calcola il valore assoluto | `abs(-5)` | `5` |
| `max()` | Individua il valore massimo | `max(4, 8, 2)` | `8` |
| `min()` | Individua il valore minimo | `min(4, 8, 2)` | `2` |
| `sum()` | Calcola la somma degli elementi di una sequenza numerica | `sum([1, 2, 3])` | `6` |

Anche `int()`, `float()`, `str()` e `bool()`, già utilizzati per la conversione dei tipi di dato, sono strumenti predefiniti del linguaggio, sebbene tecnicamente siano tipi di dato richiamabili e non semplici funzioni.

Il vantaggio delle funzioni built-in consiste nella possibilità di eseguire operazioni di uso comune senza dover scrivere personalmente le istruzioni necessarie alla loro realizzazione.

#### 1.4.2 Funzioni definite dall'utente (user-defined functions)

Le funzioni definite dall'utente sono funzioni che il programmatore realizza per soddisfare le specifiche esigenze del proprio programma.

A differenza delle funzioni built-in, il programmatore deve definirne:

- il nome simbolico;
- gli eventuali dati in ingresso;
- le istruzioni da eseguire;
- l'eventuale valore da restituire.

Una volta definita, la funzione può essere richiamata ogni volta che risulta necessario eseguire il compito per il quale è stata progettata.

| Nome della funzione | Compito assegnato |
|---|---|
| `mostra_menu()` | Visualizzare un menù di scelta |
| `calcola_area()` | Calcolare l'area di una figura geometrica |
| `pari_o_dispari()` | Verificare se un numero è pari o dispari |
| `calcola_media()` | Calcolare la media di una serie di valori |
| `conta_parole()` | Contare le parole presenti in una frase |
| `valida_input()` | Verificare la validità di un dato inserito |

La sintassi necessaria per definire e richiamare queste funzioni verrà affrontata nella prossima sezione.

#### 1.4.3 Le funzioni disponibili nei moduli e nelle librerie

Oltre alle funzioni built-in e a quelle definite dall'utente nel programma corrente, Python mette a disposizione numerose funzioni organizzate all'interno di **moduli e librerie**, che possono essere importati all'interno dei propri programmi.

A differenza delle funzioni built-in, per utilizzare queste funzioni è necessario effettuare la relativa importazione.

```python
import math
import random

radice = math.sqrt(25)
numero_casuale = random.randint(1, 10)
```

In questo esempio:

- `math.sqrt()` calcola la radice quadrata di un numero;
- `random.randint()` genera un numero intero casuale compreso tra due estremi inclusi.

Entrambe le funzioni sono già implementate e possono essere utilizzate dal programmatore senza doverne riscrivere il codice.

### 1.5 Schema riepilogativo

![Figura 1.4 – Classificazione delle funzioni in base alla disponibilità nel programma corrente.](images/04_classificazione_funzioni.svg)

*Figura 1.4 – Classificazione delle funzioni in base alla disponibilità nel programma corrente.*

| Tipologia | Già implementata | Richiede importazione | Da implementare |
|---|:---:|:---:|:---:|
| Built-in | Sì | No | No |
| Funzioni di moduli e librerie | Sì | Sì | No |
| User-defined nel programma corrente | No | No | Sì |

La classificazione distingue la modalità di disponibilità delle funzioni nel programma corrente: una funzione definita dall'utente può a sua volta essere importata da un altro modulo.

---

## 2. Definizione, chiamata e punto di ingresso del programma

Per poter utilizzare una funzione definita dall'utente (*user-defined function*) in Python, è necessario distinguere due operazioni fondamentali:

- **Definizione della funzione:** consiste nello specificare il nome della funzione, gli eventuali dati in ingresso e le istruzioni che essa deve eseguire.
- **Chiamata della funzione (o invocazione):** consiste nel richiedere l'esecuzione delle istruzioni contenute nella funzione precedentemente definita.

Definire una funzione non significa eseguirla: le istruzioni contenute al suo interno vengono eseguite soltanto nel momento in cui essa viene chiamata.

### 2.1 Definizione di una funzione

In Python la definizione di una funzione avviene mediante la parola chiave riservata `def`, abbreviazione del termine inglese *define*.

#### Sintassi generale (schema)

```text
def nome_funzione(parametro_1, parametro_2, ...):
    istruzione_1
    istruzione_2
    ...
    return risultato
```

I puntini indicano eventuali ulteriori parametri o istruzioni: non costituiscono qui un listato eseguibile.

La definizione di una funzione è costituita da due parti fondamentali:

- **Intestazione della funzione (header):** identifica la funzione e specifica gli eventuali parametri in ingresso.
- **Corpo della funzione (body):** contiene il blocco di istruzioni da eseguire quando la funzione viene chiamata.

![Figura 2.1 – Anatomia della definizione di una funzione in Python.](images/05_anatomia_funzione.svg)

*Figura 2.1 – Anatomia della definizione di una funzione in Python.*

| Elemento | Descrizione |
|---|---|
| `def` | Parola chiave che indica la definizione di una nuova funzione. |
| `nome_funzione` | Nome simbolico attraverso il quale la funzione viene identificata e richiamata. |
| `()` | Parentesi obbligatorie che contengono gli eventuali parametri della funzione. |
| Parametri | Identificatori attraverso i quali la funzione può ricevere dati in ingresso. Possono anche essere assenti. |
| `:` | Simbolo obbligatorio che conclude l'intestazione della funzione. |
| Corpo della funzione | Blocco indentato contenente le istruzioni da eseguire. |
| `return` | Parola chiave che permette di terminare l'esecuzione della funzione e di restituire un eventuale valore al chiamante. Non è obbligatoria. |

#### Convenzioni per il nome delle funzioni

Il nome di una funzione deve rispettare le stesse regole sintattiche previste per gli identificatori delle variabili.

In particolare, adotteremo la convenzione **snake_case**, secondo la quale le parole che compongono il nome vengono scritte in minuscolo e separate mediante il carattere underscore (`_`). Utilizzeremo quattro spazi per ciascun livello di indentazione.

Il nome dovrebbe inoltre descrivere chiaramente l'operazione svolta dalla funzione, preferibilmente utilizzando un verbo.

| Nomi consigliati | Nomi poco significativi |
|---|---|
| `calcola_area()` | `funzione1()` |
| `leggi_numero()` | `f()` |
| `stampa_risultati()` | `abc()` |
| `valida_input()` | `operazione()` |
| `conta_elementi()` | `funzione2()` |

> **BUONA PRATICA DI PROGRAMMAZIONE**
>
> Il nome di una funzione dovrebbe permettere di comprendere quale compito essa svolge senza dover necessariamente leggere le istruzioni contenute al suo interno.

### 2.2 La chiamata di una funzione

Una volta definita, una funzione può essere eseguita mediante una **chiamata**, detta anche **invocazione**.

La chiamata avviene specificando il nome simbolico della funzione, seguito dalle parentesi tonde, all'interno delle quali vengono riportati gli eventuali dati da trasmettere alla funzione.

#### Sintassi generale

```python
# Chiamata di una funzione senza argomenti
nome_funzione()

# Chiamata di una funzione con argomenti
nome_funzione(valore_1, valore_2)

# Chiamata e acquisizione del valore restituito
risultato = nome_funzione(valore_1, valore_2)
```

#### Esempio: definizione e chiamata di una funzione senza parametri

```python
# Definizione della funzione
def saluta():
    print("Benvenuto nel programma!")


# Chiamata della funzione
saluta()
```

**Output:**

```text
Benvenuto nel programma!
```

Nell'esempio precedente, l'interprete Python incontra inizialmente la definizione della funzione `saluta()`, rendendola disponibile per un successivo utilizzo.

Le istruzioni contenute nel corpo della funzione non vengono però eseguite fino a quando l'interprete non incontra la chiamata `saluta()`.

#### Definizione e chiamata a confronto

![Figura 2.2 – Distinzione tra definizione e chiamata di una funzione.](images/06_definizione_chiamata.svg)

*Figura 2.2 – Distinzione tra definizione e chiamata di una funzione.*

### 2.3 Il programma chiamante e la funzione chiamata

Quando viene invocata una funzione, il normale flusso di esecuzione del programma viene temporaneamente sospeso per consentire l'esecuzione delle istruzioni contenute nella funzione stessa.

Possiamo quindi distinguere:

- **Programma chiamante (caller):** porzione di programma dalla quale viene effettuata la chiamata.
- **Funzione chiamata (callee):** funzione alla quale viene temporaneamente trasferito il controllo dell'esecuzione.

Il meccanismo della chiamata può essere suddiviso in cinque fasi:

1. Il programma chiamante esegue normalmente le proprie istruzioni.
2. Viene incontrata la chiamata di una funzione.
3. Il controllo dell'esecuzione viene trasferito alla funzione chiamata.
4. La funzione esegue le proprie istruzioni e termina, restituendo il controllo al chiamante.
5. Il programma chiamante riprende la propria esecuzione dal punto in cui era stato sospeso.

![Figura 2.3 – Trasferimento e restituzione del controllo di esecuzione tra chiamante e chiamato.](images/07_flusso_esecuzione.svg)

*Figura 2.3 – Trasferimento e restituzione del controllo di esecuzione tra chiamante e chiamato.*

#### Esempio: flusso di esecuzione di una funzione

```python
def saluta():
    print("Esecuzione della funzione saluta")


print("Inizio del programma")
saluta()
print("Fine del programma")
```

**Output:**

```text
Inizio del programma
Esecuzione della funzione saluta
Fine del programma
```

È possibile osservare come l'esecuzione del programma venga temporaneamente trasferita alla funzione `saluta()` per poi proseguire con le istruzioni successive alla chiamata.

La stessa funzione può essere richiamata più volte nel corso dell'esecuzione di un programma.

```python
def separatore():
    print("--------------------")


separatore()
print("PROGRAMMA DI CALCOLO")
separatore()
print("Elaborazione dei dati")
separatore()
```

**Output:**

```text
--------------------
PROGRAMMA DI CALCOLO
--------------------
Elaborazione dei dati
--------------------
```

La funzione `separatore()` è stata definita una sola volta, ma le istruzioni contenute al suo interno sono state eseguite tre volte.

Questo esempio evidenzia concretamente il principio della **riutilizzabilità del codice** introdotto nella sezione precedente.

### 2.4 L'ordine di definizione e chiamata delle funzioni

L'interprete Python esegue sequenzialmente le istruzioni presenti a livello principale del programma.

Quando incontra una definizione introdotta dalla parola chiave `def`, crea la funzione e associa ad essa il relativo nome simbolico, senza eseguirne immediatamente il corpo.

Quando invece incontra una chiamata, verifica che il nome della funzione sia già disponibile e, in caso affermativo, ne esegue le istruzioni.

> **ATTENZIONE**
>
> Una funzione deve essere già stata definita nel momento in cui viene eseguita la sua chiamata.

#### Esempio errato

```python
saluta()


def saluta():
    print("Ciao!")
```

**Errore:**

```text
NameError: name 'saluta' is not defined
```

L'interprete incontra la chiamata della funzione prima che sia stata eseguita la relativa definizione. Non conoscendo ancora l'identificatore `saluta`, genera un errore di tipo `NameError`.

#### Esempio corretto

```python
def saluta():
    print("Ciao!")


saluta()
```

**Output:**

```text
Ciao!
```

È quindi opportuno organizzare il codice riportando inizialmente le definizioni delle funzioni e successivamente le istruzioni che ne richiedono l'esecuzione.

Questa organizzazione del codice diventerà ancora più evidente introducendo la funzione principale del programma.

### 2.5 La funzione principale del programma: `main()`

Nella programmazione modulare, un programma è generalmente costituito da diverse funzioni, ciascuna responsabile dello svolgimento di uno specifico compito.

È buona pratica introdurre una **funzione principale**, denominata per convenzione `main()`, alla quale viene affidato il compito di coordinare l'esecuzione delle altre funzioni.

> **DEFINIZIONE – FUNZIONE PRINCIPALE**
>
> La funzione `main()` è la funzione principale del programma, all'interno della quale vengono organizzate e coordinate le operazioni necessarie alla risoluzione del problema complessivo.

A differenza di altri linguaggi di programmazione, come C e C++, in Python il nome `main` non è obbligatorio e non possiede un significato speciale per l'interprete.

Si tratta tuttavia di una convenzione ampiamente utilizzata nella progettazione dei programmi.

#### Esempio: organizzazione di un programma mediante la funzione `main()`

```python
# Definizione delle funzioni secondarie
def mostra_titolo():
    print("PROGRAMMA DI ESEMPIO")


def mostra_menu():
    print("1. Inserimento dati")
    print("2. Visualizzazione dati")
    print("3. Esci")


# Definizione della funzione principale
def main():
    mostra_titolo()
    mostra_menu()


# Punto di ingresso condizionale
if __name__ == "__main__":
    main()
```

**Output:**

```text
PROGRAMMA DI ESEMPIO
1. Inserimento dati
2. Visualizzazione dati
3. Esci
```

| Funzione | Compito |
|---|---|
| `mostra_titolo()` | Visualizzare il titolo del programma. |
| `mostra_menu()` | Visualizzare il menù di scelta. |
| `main()` | Coordinare l'esecuzione delle altre funzioni. |

![Figura 2.4 – Organizzazione gerarchica delle funzioni di un programma modulare.](images/08_organizzazione_main.svg)

*Figura 2.4 – Organizzazione gerarchica delle funzioni di un programma modulare.*

La funzione `main()` permette di ottenere una visione generale del funzionamento del programma senza dover necessariamente analizzare nel dettaglio l'implementazione delle singole funzioni.

### 2.6 Il punto di ingresso condizionale del programma

In Python è possibile utilizzare una particolare struttura condizionale per stabilire se avviare le operazioni del programma principale o renderne disponibili le funzioni quando il file viene importato come modulo.

Questa struttura prende il nome di **punto di ingresso condizionale**.

#### Sintassi

```python
if __name__ == "__main__":
    main()
```

**Attenzione:** sia `__name__` sia `__main__` presentano due caratteri underscore all'inizio e due alla fine.

L'interprete Python associa automaticamente a ciascun modulo una particolare variabile denominata `__name__`.

Il valore assunto da questa variabile dipende dalla modalità con cui viene utilizzato il file Python.

| Modalità di utilizzo del file | Valore di `__name__` | Condizione |
|---|---|---|
| Esecuzione diretta come programma principale | `"__main__"` | `True` |
| Importazione come modulo | Nome del modulo | `False` |

Di conseguenza:

- Se il file viene **eseguito direttamente**, la condizione risulta vera e viene chiamata la funzione `main()`.
- Se il file viene **importato come modulo**, la condizione risulta falsa e la chiamata alla funzione `main()` non viene eseguita.

In entrambi i casi le funzioni definite nel file diventano disponibili, ma soltanto nel primo caso viene eseguita automaticamente la funzione principale attraverso il punto di ingresso condizionale. Le eventuali altre istruzioni a livello di modulo vengono eseguite anche durante la prima importazione.

![Figura 2.5 – Funzionamento del punto di ingresso condizionale in Python.](images/09_punto_di_ingresso.svg)

*Figura 2.5 – Funzionamento del punto di ingresso condizionale in Python.*

#### Esempio pratico: esecuzione diretta e importazione

Supponiamo di avere un file Python denominato `messaggi.py`, contenente il seguente codice:

**File: `messaggi.py`**

```python
def saluta():
    print("Ciao!")


def main():
    print("Avvio del programma")
    saluta()


if __name__ == "__main__":
    main()
```

**Caso 1 — Esecuzione diretta del file `messaggi.py`**

```text
Avvio del programma
Ciao!
```

La variabile `__name__` assume il valore `"__main__"`, pertanto la condizione è vera e viene eseguita la funzione `main()`.

**Caso 2 — Importazione del file da un altro programma**

Realizziamo un secondo file Python, denominato `programma.py`, collocato nella stessa directory del precedente.

**File: `programma.py`**

```python
import messaggi


def main():
    messaggi.saluta()


if __name__ == "__main__":
    main()
```

**Output:**

```text
Ciao!
```

In questo secondo caso, durante l'importazione di `messaggi.py`, la variabile `__name__` di tale modulo assume il valore `"messaggi"`.

La funzione `main()` del modulo importato non viene quindi eseguita, mentre la funzione `saluta()` rimane disponibile e può essere richiamata dal nuovo programma.

Questo meccanismo consente di **riutilizzare le funzioni definite in altri file Python senza avviare automaticamente il relativo programma principale**.

> **BUONA PRATICA DI PROGRAMMAZIONE**
>
> Sebbene l'utilizzo del punto di ingresso condizionale non sia obbligatorio in Python, ne adotteremo sistematicamente l'impiego nei nostri programmi completi, in quanto favorisce la modularità, la riutilizzabilità e la manutenibilità del codice. I frammenti di codice utilizzati per illustrare singoli concetti potranno ometterlo.

### 2.7 La struttura generale di un programma modulare in Python

Alla luce dei concetti introdotti, possiamo individuare una struttura generale da utilizzare come riferimento per la stesura dei nostri programmi Python.

| Sezione | Contenuto |
|---|---|
| 1. Importazione dei moduli | Importazione degli eventuali moduli e librerie necessari. |
| 2. Definizione delle funzioni secondarie | Definizione delle funzioni responsabili dei singoli compiti. |
| 3. Definizione della funzione principale | Organizzazione e coordinamento delle operazioni attraverso `main()`. |
| 4. Punto di ingresso condizionale | Avvio della funzione principale in caso di esecuzione diretta del file. |

![Figura 2.6 – Struttura generale di un file Python organizzato secondo i principi della programmazione modulare.](images/10_struttura_programma.svg)

*Figura 2.6 – Struttura generale di un file Python organizzato secondo i principi della programmazione modulare.*

#### Modello generale di riferimento

```python
# 1. IMPORTAZIONE DEI MODULI
import math


# 2. DEFINIZIONE DELLE FUNZIONI SECONDARIE
def funzione_1():
    # Istruzioni della prima funzione
    ...


def funzione_2():
    # Istruzioni della seconda funzione
    ...


# 3. DEFINIZIONE DELLA FUNZIONE PRINCIPALE
def main():
    funzione_1()
    funzione_2()


# 4. PUNTO DI INGRESSO CONDIZIONALE
if __name__ == "__main__":
    main()
```

I simboli `...` rappresentano, in questo modello, le istruzioni che dovranno essere implementate dal programmatore.

Non tutte le sezioni sono strettamente obbligatorie: ad esempio, l'importazione dei moduli è necessaria soltanto quando il programma utilizza funzionalità che richiedono tali importazioni.

Adotteremo questa struttura come **modello di riferimento per la realizzazione dei programmi Python basati sull'utilizzo delle funzioni**.

### 2.8 Schema riepilogativo

| Concetto | Significato |
|---|---|
| `def` | Definisce una funzione. |
| Header | Intestazione della funzione. |
| Body | Corpo della funzione, costituito da istruzioni indentate. |
| Chiamata o invocazione | Richiesta di esecuzione della funzione. |
| Caller | Programma o funzione che effettua la chiamata. |
| Callee | Funzione alla quale viene trasferito il controllo. |
| `NameError` | Errore generato quando si tenta di utilizzare un identificatore non definito. |
| `main()` | Funzione principale che coordina le operazioni del programma. |
| `__name__` | Variabile speciale che identifica il modulo corrente. |
| `"__main__"` | Valore assunto da `__name__` quando il modulo viene eseguito come programma principale. |
| `if __name__ == "__main__":` | Punto di ingresso condizionale del programma. |

---

## 3. Le funzioni come black box: parametri e argomenti

### 3.1 Le funzioni come black box

Nella programmazione, una funzione può essere considerata come una **black box** (scatola nera), ovvero un componente del quale possiamo conoscere i dati necessari in ingresso e i risultati prodotti in uscita, senza dover necessariamente conoscere le istruzioni attraverso le quali viene effettuata l'elaborazione.

> **DEFINIZIONE – BLACK BOX**
>
> Una black box è un sistema o un componente del quale si conoscono i dati in ingresso (input) e i risultati in uscita (output), indipendentemente dal suo funzionamento interno.

Questo modello permette di distinguere due aspetti fondamentali di una funzione:

- **Interfaccia (interface):** definisce le modalità attraverso le quali è possibile utilizzare la funzione, specificando il suo nome, gli eventuali dati richiesti in ingresso e il risultato restituito.
- **Implementazione (implementation):** rappresenta l'insieme delle istruzioni contenute nel corpo della funzione, attraverso le quali viene svolta l'elaborazione.

![Figura 3.1 – Rappresentazione di una funzione secondo il modello black box.](images/11_modello_black_box.svg)

*Figura 3.1 – Rappresentazione di una funzione secondo il modello black box.*

Il modello black box risulta particolarmente utile quando utilizziamo funzioni built-in oppure funzioni appartenenti a moduli e librerie già implementati.

#### Esempio: la funzione built-in `pow()`

La funzione `pow()` permette di calcolare l'elevamento a potenza di un numero.

```python
risultato = pow(12, 2)
print(risultato)
```

**Output:**

```text
144
```

Per utilizzare correttamente questa funzione è sufficiente conoscere il nome `pow`, i dati richiesti in ingresso (base ed esponente), l'operazione svolta (elevamento a potenza) e il risultato restituito (il valore della potenza).

Non è invece necessario conoscere le istruzioni mediante le quali Python realizza internamente tale operazione.

![Figura 3.2 – Applicazione del modello black box alla funzione built-in pow().](images/12_black_box_pow.svg)

*Figura 3.2 – Applicazione del modello black box alla funzione built-in pow().*

Lo stesso principio può essere applicato alle funzioni definite dall'utente: una volta progettata, implementata e verificata una funzione, sarà possibile utilizzarla senza dover analizzare nuovamente il suo funzionamento interno.

Questa separazione tra interfaccia e implementazione prende il nome di **astrazione** e rappresenta un importante principio della programmazione.

### 3.2 La comunicazione tra chiamante e chiamato

Affinché una funzione possa eseguire un'elaborazione, può essere necessario fornirle i dati sui quali operare. Allo stesso modo, una volta terminata l'elaborazione, la funzione può dover comunicare il risultato ottenuto al programma chiamante.

| Elemento | Descrizione |
|---|---|
| **Parametri in ingresso (input)** | Consentono di trasmettere alla funzione i dati necessari all'elaborazione. |
| **Valore di ritorno (output)** | Rappresenta il risultato dell'elaborazione restituito dalla funzione al chiamante mediante `return`. |

![Figura 3.3 – Scambio di dati tra il programma chiamante e la funzione chiamata.](images/13_comunicazione_funzioni.svg)

*Figura 3.3 – Scambio di dati tra il programma chiamante e la funzione chiamata.*

È importante osservare che una funzione non deve necessariamente ricevere dati in ingresso o restituire un risultato significativo. L'utilizzo dei parametri e dell'istruzione `return` dipende dal compito per il quale la funzione è stata progettata.

> **OSSERVAZIONE**
>
> I dati in ingresso di una funzione non devono necessariamente essere acquisiti mediante `input()`, così come i risultati in uscita non devono necessariamente essere visualizzati mediante `print()`.
>
> I parametri e l'istruzione `return` permettono di scambiare dati direttamente tra le diverse funzioni di un programma.

### 3.3 Parametri formali e parametri attuali

> **DEFINIZIONE – PARAMETRI FORMALI (FORMAL PARAMETERS)**
>
> I parametri formali sono gli identificatori dichiarati nell'intestazione di una funzione, attraverso i quali la funzione riceve e utilizza i dati che le vengono trasmessi.

> **DEFINIZIONE – PARAMETRI ATTUALI (ACTUAL PARAMETERS)**
>
> I parametri attuali, comunemente denominati **argomenti**, sono i dati effettivamente trasmessi alla funzione nel momento in cui viene effettuata la sua chiamata.

#### Esempio: calcolo della somma di due numeri

Realizziamo una funzione che riceve in ingresso due numeri e restituisce il risultato della loro somma.

```python
def somma(a, b):
    return a + b


def main():
    risultato = somma(10, 5)
    print("La somma è:", risultato)


if __name__ == "__main__":
    main()
```

**Output:**

```text
La somma è: 15
```

In questo esempio:

- `a` e `b` sono i **parametri formali**, dichiarati nell'intestazione della funzione.
- `10` e `5` sono i **parametri attuali**, ossia gli argomenti trasmessi durante la chiamata.
- `a + b` rappresenta l'elaborazione effettuata dalla funzione.
- `15` è il valore restituito mediante l'istruzione `return`.
- `risultato` è la variabile del chiamante alla quale viene assegnato il valore restituito.

![Figura 3.4 – Associazione tra parametri attuali, parametri formali e valore restituito.](images/14_parametri_formali_attuali.svg)

*Figura 3.4 – Associazione tra parametri attuali, parametri formali e valore restituito.*

Al momento della chiamata, i parametri formali vengono associati ai corrispondenti oggetti forniti come argomenti. All'interno della funzione sarà quindi possibile utilizzare `a` e `b` come normali variabili.

#### Parametri e argomenti a confronto

| Caratteristica | Parametri formali | Parametri attuali |
|---|---|---|
| Dove vengono specificati? | Nella definizione della funzione | Nella chiamata della funzione |
| Che cosa rappresentano? | Gli identificatori utilizzati dalla funzione | I dati effettivamente trasmessi |
| Terminologia inglese | Formal parameters | Actual parameters / Arguments |
| Esempio | `def somma(a, b):` | `somma(10, 5)` |

> **DA RICORDARE**
>
> I parametri si trovano nella definizione della funzione, mentre gli argomenti si trovano nella sua chiamata.

### 3.4 L'utilizzo degli argomenti

Gli argomenti trasmessi a una funzione possono essere costituiti da valori letterali, variabili, espressioni o risultati restituiti da altre funzioni.

Consideriamo la seguente funzione:

```python
def somma(a, b):
    return a + b
```

#### 3.4.1 Passaggio di valori letterali

```python
risultato = somma(10, 5)
```

I valori `10` e `5` vengono trasmessi direttamente alla funzione.

#### 3.4.2 Passaggio di variabili

```python
numero_1 = 10
numero_2 = 5

risultato = somma(numero_1, numero_2)
```

Alla funzione vengono trasmessi gli oggetti associati alle variabili `numero_1` e `numero_2`. Non è necessario che i nomi delle variabili utilizzate dal chiamante coincidano con quelli dei parametri formali.

#### 3.4.3 Passaggio di espressioni

```python
risultato = somma(2 * 5, 3 + 2)
```

Le espressioni vengono valutate prima dell'esecuzione del corpo della funzione: `2 * 5` produce `10` e `3 + 2` produce `5`. La funzione riceverà quindi gli argomenti `10` e `5`.

#### 3.4.4 Passaggio dei risultati di altre funzioni

```python
risultato = somma(pow(2, 3), abs(-5))
```

Prima di eseguire la funzione `somma()`, Python valuta le chiamate delle funzioni utilizzate come argomenti: `pow(2, 3)` restituisce `8` e `abs(-5)` restituisce `5`. Successivamente viene eseguita la funzione `somma(8, 5)`, che restituisce `13`.

| Chiamata | Tipologia di argomenti | Risultato restituito |
|---|---|---:|
| `somma(10, 5)` | Valori letterali | 15 |
| `somma(numero_1, numero_2)` | Variabili con valori 10 e 5 | 15 |
| `somma(2 * 5, 3 + 2)` | Espressioni | 15 |
| `somma(pow(2, 3), abs(-5))` | Risultati di altre funzioni | 13 |

La stessa funzione può quindi essere utilizzata in contesti differenti, indipendentemente dalla provenienza dei dati che le vengono trasmessi.

### 3.5 Corrispondenza tra parametri formali e attuali

Nel caso più semplice, in cui tutti i parametri sono obbligatori e gli argomenti vengono trasmessi per posizione, dobbiamo considerare tre aspetti fondamentali:

| Aspetto | Descrizione |
|---|---|
| **Numero** | Il numero degli argomenti deve corrispondere al numero dei parametri richiesti. |
| **Posizione** | Gli argomenti vengono associati ai parametri formali secondo l'ordine in cui sono riportati. |
| **Compatibilità dei tipi** | I dati trasmessi devono essere compatibili con le operazioni svolte all'interno della funzione. |

#### 3.5.1 Corrispondenza in numero

```python
def somma(a, b):
    return a + b
```

| Chiamata | Esito |
|---|---|
| `somma(10, 5)` | Corretta |
| `somma(10)` | Errata – argomento mancante |
| `somma(10, 5, 3)` | Errata – argomento in eccesso |
| `somma()` | Errata – argomenti mancanti |

Una chiamata che non rispetta il numero di argomenti richiesti può generare un errore di tipo `TypeError`.

```python
risultato = somma(10)
```

**Errore:**

```text
TypeError: somma() missing 1 required positional argument: 'b'
```

#### 3.5.2 Corrispondenza in posizione

Gli argomenti vengono associati ai parametri formali secondo la posizione che occupano nella chiamata. Consideriamo una funzione che calcola la differenza tra due numeri.

```python
def differenza(a, b):
    return a - b


def main():
    print(differenza(10, 5))
    print(differenza(5, 10))


if __name__ == "__main__":
    main()
```

**Output:**

```text
5
-5
```

![Figura 3.5 – Effetti della variazione dell’ordine degli argomenti nella chiamata di una funzione.](images/15_argomenti_posizionali.svg)

*Figura 3.5 – Effetti della variazione dell’ordine degli argomenti nella chiamata di una funzione.*

> **ATTENZIONE**
>
> Modificare l'ordine degli argomenti può modificare il risultato dell'elaborazione, anche quando la chiamata è sintatticamente corretta.

Questa modalità di associazione prende il nome di **passaggio di argomenti posizionali** (*positional arguments*). Python prevede anche altre modalità di passaggio degli argomenti, che verranno approfondite successivamente.

#### 3.5.3 Compatibilità dei tipi di dato

Python è un linguaggio a **tipizzazione dinamica**: non è necessario specificare nella definizione di una funzione il tipo di dato associato a ciascun parametro.

```python
def somma(a, b):
    return a + b
```

Questa funzione può essere utilizzata con differenti tipi di dato, purché compatibili con l'operatore `+`.

| Chiamata | Tipo di argomenti | Risultato |
|---|---|---|
| `somma(10, 5)` | `int`, `int` | `15` |
| `somma(2.5, 3.5)` | `float`, `float` | `6.0` |
| `somma(10, 2.5)` | `int`, `float` | `12.5` |
| `somma("Buon", "giorno")` | `str`, `str` | `"Buongiorno"` |
| `somma([1, 2], [3, 4])` | `list`, `list` | `[1, 2, 3, 4]` |
| `somma(10, "Python")` | `int`, `str` | `TypeError` |

Nel caso delle stringhe e delle liste, l'operatore `+` non esegue una somma matematica, ma un'operazione di concatenazione.

```python
risultato = somma(10, "Python")
```

**Errore:**

```text
TypeError: unsupported operand type(s) for +: 'int' and 'str'
```

Python consente infatti di effettuare la chiamata, ma non può eseguire l'operazione prevista dalla funzione utilizzando due oggetti di tipo incompatibile con l'operatore `+`.

> **BUONA PRATICA DI PROGRAMMAZIONE**
>
> Quando si progetta o si utilizza una funzione, è importante stabilire quali dati essa deve ricevere in ingresso e assicurarsi che siano compatibili con le elaborazioni previste.

### 3.6 Esempio applicativo: conversione da Celsius a Fahrenheit

Realizziamo un programma che utilizza una funzione per convertire una temperatura espressa in gradi Celsius nella corrispondente temperatura espressa in gradi Fahrenheit.

La formula di conversione è: **F = C × 9/5 + 32**, dove C rappresenta la temperatura in gradi Celsius e F la temperatura in gradi Fahrenheit.

#### Progettazione della funzione

| Elemento | Descrizione |
|---|---|
| Nome della funzione | `celsius_to_fahrenheit()` |
| Parametro in ingresso | Temperatura in gradi Celsius |
| Elaborazione | Applicazione della formula di conversione |
| Valore restituito | Temperatura in gradi Fahrenheit |

![Figura 3.6 – Progettazione del convertitore di temperatura secondo il modello black box.](images/16_black_box_temperatura.svg)

*Figura 3.6 – Progettazione del convertitore di temperatura secondo il modello black box.*

#### Implementazione del programma

```python
def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


def main():
    risultato = celsius_to_fahrenheit(25)
    print("Temperatura in Fahrenheit:", risultato)


if __name__ == "__main__":
    main()
```

**Output:**

```text
Temperatura in Fahrenheit: 77.0
```

#### Versione con acquisizione e validazione del dato

Possiamo rendere il programma interattivo, consentendo all'utente di inserire la temperatura da convertire. Utilizziamo i concetti già affrontati nelle precedenti lezioni, in particolare il ciclo `while` e il blocco `try-except-else` per la validazione del dato in ingresso.

```python
def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


def main():
    dato_valido = False

    while not dato_valido:
        try:
            temperatura = float(input("Inserisci la temperatura in Celsius: "))
        except ValueError:
            print("Errore: inserire un valore numerico.")
        else:
            dato_valido = True

    risultato = celsius_to_fahrenheit(temperatura)

    print(f"Temperatura in Celsius: {temperatura} °C")
    print(f"Temperatura in Fahrenheit: {risultato} °F")


if __name__ == "__main__":
    main()
```

**Esempio di esecuzione:**

```text
Inserisci la temperatura in Celsius: abc
Errore: inserire un valore numerico.
Inserisci la temperatura in Celsius: 25
Temperatura in Celsius: 25.0 °C
Temperatura in Fahrenheit: 77.0 °F
```

La validazione di questo esempio verifica la convertibilità in `float`; non impone un intervallo fisico né esclude i valori speciali `NaN` e infinito.

È importante osservare che, nonostante siano state modificate le modalità di acquisizione e visualizzazione dei dati, la funzione `celsius_to_fahrenheit()` è rimasta invariata. Questo dimostra concretamente come la separazione tra acquisizione, elaborazione e visualizzazione favorisca la **riutilizzabilità del codice**.

### 3.7 Schema riepilogativo

| Concetto | Significato |
|---|---|
| **Black box** | Componente utilizzabile conoscendone l'interfaccia, senza dover conoscere il funzionamento interno. |
| **Interfaccia** | Modalità attraverso le quali è possibile utilizzare una funzione. |
| **Implementazione** | Insieme delle istruzioni che realizzano il compito della funzione. |
| **Astrazione** | Separazione degli aspetti necessari all'utilizzo di un componente dai dettagli della sua implementazione. |
| **Parametro formale** | Identificatore dichiarato nella definizione della funzione. |
| **Parametro attuale (argomento)** | Dato trasmesso alla funzione durante la chiamata. |
| **Valore di ritorno** | Risultato restituito dalla funzione al chiamante. |
| **Argomenti posizionali** | Argomenti associati ai parametri secondo la posizione che occupano nella chiamata. |
| **Tipizzazione dinamica** | Caratteristica di Python per cui non è obbligatorio dichiarare preventivamente il tipo dei parametri. |
| **`TypeError`** | Errore che può essere generato da una chiamata con un numero non valido di argomenti o da operazioni tra tipi incompatibili. |

![Figura 3.7 – Schema riepilogativo del passaggio degli argomenti, dell’elaborazione e della restituzione.](images/17_riepilogo_passaggio_parametri.svg)

*Figura 3.7 – Schema riepilogativo del passaggio degli argomenti, dell’elaborazione e della restituzione.*

---

## 4. Il valore di ritorno: `print()` e `return`

Una funzione, una volta eseguite le istruzioni contenute al suo interno, può visualizzare il risultato dell'elaborazione oppure restituirlo al programma chiamante, affinché quest'ultimo possa utilizzarlo per effettuare ulteriori operazioni.

In Python queste due modalità sono realizzate rispettivamente mediante la funzione built-in `print()` e la parola chiave `return`. Sebbene entrambe possano essere utilizzate in relazione al risultato di un'elaborazione, svolgono compiti profondamente differenti.

### 4.1 La visualizzazione di un risultato: `print()`

La funzione built-in `print()` permette di visualizzare dati sullo schermo, consentendo al programma di comunicare informazioni all'utente.

Quando viene utilizzata all'interno di una funzione, il risultato dell'elaborazione viene visualizzato, ma non viene restituito al programma chiamante come valore utilizzabile.

#### Esempio: funzione che visualizza il risultato di una somma

```python
def somma(a, b):
    risultato = a + b
    print("La somma è:", risultato)


def main():
    somma(10, 5)


if __name__ == "__main__":
    main()
```

**Output:**

```text
La somma è: 15
```

In questo esempio la funzione `somma()` riceve due argomenti, ne calcola la somma e visualizza direttamente il risultato. Il programma chiamante non riceve il valore `15` e non può quindi utilizzarlo direttamente per effettuare ulteriori elaborazioni.

### 4.2 La restituzione di un risultato: `return`

L'istruzione `return` permette a una funzione di terminare la propria esecuzione e di restituire un valore al programma chiamante.

> **DEFINIZIONE – VALORE DI RITORNO (RETURN VALUE)**
>
> Il valore di ritorno è il dato restituito da una funzione al programma chiamante al termine della propria esecuzione. Tale dato può essere utilizzato dal chiamante per effettuare ulteriori operazioni.

#### Sintassi generale

```python
return espressione
```

L'espressione riportata dopo la parola chiave `return` può essere costituita da un valore letterale, una variabile, un'espressione matematica o logica oppure dal risultato di un'altra funzione.

Esempi di istruzioni alternative da inserire nel corpo di una funzione:

```python
return 10
return risultato
return a + b
return numero > 0
return len(lista)
```

#### Esempio: funzione che restituisce il risultato di una somma

```python
def somma(a, b):
    risultato = a + b
    return risultato


def main():
    totale = somma(10, 5)
    print("La somma è:", totale)


if __name__ == "__main__":
    main()
```

**Output:**

```text
La somma è: 15
```

Nonostante il risultato visualizzato sia identico a quello dell'esempio precedente, il funzionamento del programma è differente.

1. La funzione `main()` chiama la funzione `somma()`, trasmettendole gli argomenti `10` e `5`.
2. La funzione `somma()` calcola il risultato dell'elaborazione.
3. L'istruzione `return` restituisce il valore `15` alla funzione chiamante.
4. Il valore restituito viene assegnato alla variabile `totale`.
5. La funzione `main()` visualizza il risultato mediante `print()`.

La funzione `somma()` si occupa esclusivamente dell'elaborazione dei dati, mentre la funzione `main()` decide come utilizzare il risultato ottenuto.

### 4.3 Differenza tra `print()` e `return`

![Figura 4.1 – Differenza tra visualizzazione mediante print() e restituzione mediante return.](images/18_print_vs_return.svg)

*Figura 4.1 – Differenza tra visualizzazione mediante print() e restituzione mediante return.*

| Caratteristica | `print()` | `return` |
|---|---|---|
| Tipologia | Funzione built-in | Parola chiave |
| Scopo | Visualizzare informazioni | Restituire il controllo e un eventuale valore |
| Destinatario del risultato | Utente | Programma chiamante |
| Visualizza automaticamente il risultato | Sì | No |
| Rende disponibile il risultato per ulteriori elaborazioni | No | Sì, se restituisce il risultato |
| Termina immediatamente la funzione che lo contiene | No | Sì (nei casi studiati) |
| Può essere utilizzato al di fuori di una funzione | Sì | No |

> **DA RICORDARE**
>
> `print()` comunica un risultato all'utente.
>
> `return` comunica un risultato al programma chiamante.

#### Quale dei due utilizzare?

| Compito della funzione | Istruzione consigliata |
|---|---|
| Visualizzare un menù | `print()` |
| Visualizzare un messaggio di benvenuto | `print()` |
| Visualizzare un messaggio di errore | `print()` |
| Calcolare un'area | `return` |
| Calcolare una media | `return` |
| Acquisire e validare un dato | `return` |
| Verificare una condizione | `return` |
| Contare gli elementi di una lista | `return` |
| Visualizzare i risultati finali | `print()` |

In generale, nelle funzioni dedicate all'elaborazione dei dati è preferibile utilizzare `return`, lasciando al programma chiamante la scelta di come utilizzare o visualizzare il risultato.

> **IL MANTRA DELLE FUNZIONI**
>
> **Una funzione dovrebbe generalmente terminare con un `print` o un `return`, altrimenti c'è qualcosa da rivedere nella stesura della funzione.**
>
> Quando progetti una funzione, chiediti sempre:
>
> - Qual è il compito che deve svolgere?
> - Deve visualizzare un risultato?
> - Deve restituire un risultato al programma chiamante?
> - Deve produrre un altro effetto utile?
>
> Se non riesci a individuare lo scopo della funzione, probabilmente è necessario rivederne la progettazione.

Questa regola rappresenta un riferimento pratico per la progettazione delle funzioni nei nostri esercizi, non un obbligo sintattico del linguaggio Python.

Esistono infatti funzioni che svolgono un compito utile senza utilizzare direttamente né `print()` né `return`, ad esempio modificando il contenuto di una lista oppure coordinando l'esecuzione di altre funzioni, come spesso accade nella funzione `main()`.

### 4.4 L'utilizzo del valore restituito da una funzione

Consideriamo la seguente funzione:

```python
def quadrato(numero):
    return numero ** 2
```

#### 4.4.1 Assegnazione a una variabile

Il valore restituito può essere assegnato a una variabile per essere utilizzato successivamente.

```python
risultato = quadrato(5)
print(risultato)
```

**Output:** `25`

#### 4.4.2 Utilizzo all'interno di un'espressione

```python
risultato = quadrato(5) + 10
print(risultato)
```

**Output:** `35`

#### 4.4.3 Utilizzo come argomento di un'altra funzione

```python
print(quadrato(5))
```

**Output:** `25`

In questo caso viene prima eseguita la funzione `quadrato()`, successivamente il suo valore di ritorno viene passato come argomento alla funzione `print()`.

#### 4.4.4 Utilizzo all'interno di una condizione

```python
if quadrato(5) > 20:
    print("Il risultato è maggiore di 20")
else:
    print("Il risultato non è maggiore di 20")
```

**Output:**

```text
Il risultato è maggiore di 20
```

![Figura 4.2 – Possibili modalità di utilizzo del valore restituito da una funzione.](images/19_utilizzo_valore_ritorno.svg)

*Figura 4.2 – Possibili modalità di utilizzo del valore restituito da una funzione.*

| Modalità di utilizzo | Esempio |
|---|---|
| Assegnazione a una variabile | `risultato = quadrato(5)` |
| Espressione matematica | `risultato = quadrato(5) + 10` |
| Argomento di un'altra funzione | `print(quadrato(5))` |
| Condizione logica | `if quadrato(5) > 20:` |

Questo rende le funzioni che restituiscono un risultato particolarmente flessibili e riutilizzabili.

### 4.5 La terminazione dell'esecuzione di una funzione

L'istruzione `return` svolge contemporaneamente due compiti fondamentali: restituisce un eventuale valore al programma chiamante e termina l'esecuzione della funzione.

Quando l'interprete Python incontra un'istruzione `return`, le eventuali istruzioni successive appartenenti allo stesso percorso di esecuzione non vengono eseguite (fatte salve particolari operazioni di chiusura, come i blocchi `finally`, non trattate in questa lezione).

```python
def esempio():
    print("Prima istruzione")
    return 10
    print("Seconda istruzione")


def main():
    risultato = esempio()
    print("Valore restituito:", risultato)


if __name__ == "__main__":
    main()
```

**Output:**

```text
Prima istruzione
Valore restituito: 10
```

L'istruzione `print("Seconda istruzione")` non viene mai eseguita, poiché preceduta da un'istruzione `return` incondizionata.

Una porzione di codice che non può mai essere raggiunta durante l'esecuzione del programma viene denominata **codice irraggiungibile (unreachable code)**.

![Figura 4.3 – Terminazione della funzione mediante return e codice irraggiungibile.](images/20_terminazione_funzione.svg)

*Figura 4.3 – Terminazione della funzione mediante return e codice irraggiungibile.*

> **ATTENZIONE**
>
> A differenza di `print()`, l'istruzione `return` termina l'esecuzione della funzione che la contiene, anche quando si trova all'interno di un blocco `if`, `while` o `for`.

### 4.6 Il valore di ritorno implicito: `None`

In Python ogni normale funzione che termina restituisce sempre un valore, anche quando al suo interno non è presente un'istruzione `return` esplicita.

In assenza di un valore di ritorno specificato dal programmatore, Python restituisce automaticamente il valore speciale `None`.

> **DEFINIZIONE – NONE**
>
> `None` è un valore speciale del linguaggio Python che rappresenta l'assenza di un valore significativo.

Il valore `None` non deve essere confuso con il numero `0`, una stringa vuota `""` o il valore booleano `False`.

#### Esempio: funzione senza `return`

```python
def saluta():
    print("Ciao!")


def main():
    risultato = saluta()
    print("Valore restituito:", risultato)


if __name__ == "__main__":
    main()
```

**Output:**

```text
Ciao!
Valore restituito: None
```

La funzione `saluta()` visualizza il messaggio `Ciao!`, ma non restituisce tale stringa al programma chiamante. Alla variabile `risultato` viene quindi assegnato il valore `None`.

#### L'istruzione `return` senza espressione

In Python è possibile utilizzare l'istruzione `return` anche senza specificare un valore da restituire. In questo caso la funzione termina e restituisce `None`.

Le seguenti tre funzioni, considerate come implementazioni alternative, risultano equivalenti dal punto di vista del valore restituito.

**Ritorno implicito**

```python
def esempio():
    print("Ciao")
```

**Return senza valore**

```python
def esempio():
    print("Ciao")
    return
```

**Return esplicito**

```python
def esempio():
    print("Ciao")
    return None
```

L'istruzione `return` senza espressione può risultare utile quando si desidera terminare anticipatamente l'esecuzione di una funzione senza restituire un risultato significativo.

#### Esempio: terminazione anticipata

```python
def mostra_radice(numero):
    if numero < 0:
        print("Errore: numero negativo.")
        return

    print("Radice quadrata:", numero ** 0.5)


def main():
    mostra_radice(-4)
    mostra_radice(25)


if __name__ == "__main__":
    main()
```

**Output:**

```text
Errore: numero negativo.
Radice quadrata: 5.0
```

Nella prima chiamata, l'istruzione `return` permette di terminare la funzione prima che venga effettuato il calcolo della radice quadrata. Nella seconda chiamata, invece, la funzione prosegue normalmente la propria esecuzione.

### 4.7 La presenza di più istruzioni `return`

Una funzione può contenere più istruzioni `return`, collocate in differenti punti del suo corpo. Questa soluzione risulta particolarmente utile quando il valore da restituire dipende dal verificarsi di determinate condizioni.

> **ATTENZIONE**
>
> Nei normali percorsi di esecuzione considerati nei nostri esercizi, una funzione può contenere più istruzioni `return`, ma durante una singola chiamata ne esegue al massimo una, poiché la prima istruzione `return` raggiunta determina la terminazione della funzione.

#### 4.7.1 Esempio: verifica se un numero sia pari o dispari

```python
def pari_o_dispari(numero):
    if numero % 2 == 0:
        return "Pari"
    else:
        return "Dispari"


def main():
    numero = 7
    risultato = pari_o_dispari(numero)

    print(f"Il numero {numero} è:", risultato)


if __name__ == "__main__":
    main()
```

**Output:**

```text
Il numero 7 è: Dispari
```

La funzione contiene due istruzioni `return`: `return "Pari"`, eseguita quando il numero è divisibile per 2, e `return "Dispari"`, eseguita quando il numero non è divisibile per 2.

![Figura 4.4 – Flow chart di una funzione contenente più istruzioni return.](images/21_return_multipli.svg)

*Figura 4.4 – Flow chart di una funzione contenente più istruzioni return.*

#### Versione alternativa senza `else`

```python
def pari_o_dispari(numero):
    if numero % 2 == 0:
        return "Pari"

    return "Dispari"
```

Le due versioni sono equivalenti. Infatti, se la condizione è vera, viene eseguito il primo `return` e la funzione termina. In caso contrario, l'esecuzione prosegue fino al secondo `return`.

### 4.8 Le funzioni che restituiscono valori booleani

Una funzione può essere progettata per verificare il rispetto di una determinata condizione e restituire un valore booleano: `True`, se la condizione risulta verificata, oppure `False`, se la condizione non risulta verificata.

Queste funzioni vengono anche denominate **funzioni predicato (predicate functions)**. Sono particolarmente utili nella validazione dei dati e nella costruzione di condizioni logiche.

#### Esempio: verifica se un numero sia positivo

```python
def is_positivo(numero):
    if numero > 0:
        return True
    else:
        return False
```

La funzione può essere utilizzata direttamente all'interno di una struttura di selezione.

```python
if is_positivo(10):
    print("Il numero è positivo.")
else:
    print("Il numero non è positivo.")
```

**Output:**

```text
Il numero è positivo.
```

Poiché l'espressione `numero > 0` produce già un valore booleano, la stessa funzione può essere scritta in forma più compatta:

```python
def is_positivo(numero):
    return numero > 0
```

> **BUONA PRATICA DI PROGRAMMAZIONE**
>
> Per le funzioni che restituiscono valori booleani è comune utilizzare nomi che iniziano con `is_` (è), `has_` (possiede) oppure utilizzare espressioni italiane come `numero_valido()` o `verifica_requisiti()`.

#### 4.8.1 Esempio applicativo: verifica se un numero sia primo

Un numero intero si definisce **primo** quando è maggiore di 1 e risulta divisibile esclusivamente per 1 e per sé stesso.

Realizziamo una funzione che riceve un numero intero e restituisce `True` se il numero è primo, `False` altrimenti.

```python
def is_primo(num):
    if num < 2:
        return False

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False

    return True


def main():
    risultato = is_primo(7)
    print("Il numero è primo:", risultato)


if __name__ == "__main__":
    main()
```

**Output:**

```text
Il numero è primo: True
```

#### Analisi del funzionamento

| Istruzione | Descrizione |
|---|---|
| `if num < 2:` | Verifica se il numero è minore di 2. |
| `return False` | Termina la funzione, poiché il numero non può essere primo. |
| `for i in range(...)` | Verifica la presenza di eventuali divisori, da 2 fino alla parte intera della radice quadrata del numero, inclusa. |
| `if num % i == 0:` | Verifica se il resto della divisione è uguale a zero. |
| `return False` | Termina immediatamente la funzione quando viene individuato un divisore. |
| `return True` | Viene eseguita soltanto quando il ciclo termina senza aver individuato alcun divisore. |

È sufficiente verificare la presenza di divisori fino alla radice quadrata del numero, poiché un eventuale divisore proprio maggiore della radice quadrata avrebbe necessariamente un divisore corrispondente minore della radice stessa. Il listato usa una radice in virgola mobile, adeguata ai piccoli interi degli esercizi; per interi molto grandi è preferibile `math.isqrt(num)`, che calcola la radice quadrata intera esatta.

![Figura 4.5 – Terminazione anticipata di una funzione durante l’esecuzione di un ciclo.](images/22_return_nel_ciclo.svg)

*Figura 4.5 – Terminazione anticipata di una funzione durante l’esecuzione di un ciclo.*

| Chiamata | Valore restituito | Motivazione |
|---|:---:|---|
| `is_primo(-5)` | `False` | Numero minore di 2 |
| `is_primo(1)` | `False` | Il numero 1 non è primo |
| `is_primo(2)` | `True` | Primo numero primo |
| `is_primo(7)` | `True` | Nessun divisore trovato |
| `is_primo(9)` | `False` | Divisibile per 3 |
| `is_primo(12)` | `False` | Divisibile per 2 |
| `is_primo(17)` | `True` | Nessun divisore trovato |

#### Differenza tra `break`, `continue` e `return`

| Istruzione | Comportamento |
|---|---|
| `break` | Termina il ciclo `while` o `for` più interno che la contiene. |
| `continue` | Interrompe l'iterazione corrente e passa alla successiva. |
| `return` | Termina l'intera funzione e restituisce il controllo al chiamante. |

Se un'istruzione `return` viene eseguita all'interno di un ciclo, vengono interrotte sia l'esecuzione del ciclo sia quella della funzione.

### 4.9 La restituzione di più valori

In Python una funzione può restituire più valori attraverso una singola istruzione `return`, separando i valori mediante una virgola.

```python
return valore_1, valore_2, valore_3
```

Dal punto di vista tecnico, Python restituisce un unico oggetto di tipo **tupla (`tuple`)**, contenente tutti i valori specificati. Una tupla è una sequenza ordinata e immutabile di elementi.

#### Esempio: calcolo dell'area e del perimetro di un rettangolo

```python
def calcola_rettangolo(base, altezza):
    area = base * altezza
    perimetro = 2 * (base + altezza)

    return area, perimetro


def main():
    area, perimetro = calcola_rettangolo(10, 5)

    print("Area:", area)
    print("Perimetro:", perimetro)


if __name__ == "__main__":
    main()
```

**Output:**

```text
Area: 50
Perimetro: 30
```

La funzione `calcola_rettangolo()` restituisce contemporaneamente i risultati delle due elaborazioni:

```python
return area, perimetro
```

Il programma chiamante può acquisire separatamente i due valori attraverso un'assegnazione multipla:

```python
area, perimetro = calcola_rettangolo(10, 5)
```

Questa operazione prende il nome di **unpacking (spacchettamento)** della tupla.

![Figura 4.6 – Restituzione di più valori mediante una tupla e assegnazione multipla.](images/23_restituzione_multipla.svg)

*Figura 4.6 – Restituzione di più valori mediante una tupla e assegnazione multipla.*

#### Acquisizione del risultato in una singola variabile

In alternativa, è possibile assegnare l'intera tupla restituita dalla funzione a una singola variabile.

```python
risultato = calcola_rettangolo(10, 5)
print(risultato)
```

**Output:** `(50, 30)`

Analogamente a quanto già visto per le liste, è possibile accedere ai singoli elementi della tupla mediante il relativo indice.

```python
print(risultato[0])
print(risultato[1])
```

**Output:**

```text
50
30
```

#### Corrispondenza tra valori restituiti e variabili

Quando si utilizza l'assegnazione multipla semplice, il numero delle variabili deve corrispondere al numero degli elementi restituiti.

| Istruzione | Esito |
|---|---|
| `risultato = calcola_rettangolo(10, 5)` | Corretta: acquisizione dell'intera tupla |
| `a, p = calcola_rettangolo(10, 5)` | Corretta: acquisizione separata dei due valori |
| `a, p, x = calcola_rettangolo(10, 5)` | Errata: troppe variabili |
| `a, = calcola_rettangolo(10, 5)` | Errata: numero insufficiente di variabili per l'unpacking |

Una mancata corrispondenza nel numero di elementi durante l'unpacking genera un errore di tipo `ValueError`.

### 4.10 Errori comuni nell'utilizzo di `print()` e `return`

#### Errore 1 – Confondere visualizzazione e restituzione

```python
def somma(a, b):
    print(a + b)


risultato = somma(10, 5)
print(risultato)
```

**Output:**

```text
15
None
```

La funzione visualizza il risultato dell'elaborazione, ma restituisce `None`.

**Soluzione:**

```python
def somma(a, b):
    return a + b
```

#### Errore 2 – Non utilizzare il valore restituito

```python
def somma(a, b):
    return a + b


somma(10, 5)
```

In questo caso la funzione viene eseguita correttamente e restituisce il valore `15`, ma tale valore non viene acquisito né utilizzato dal programma chiamante. Durante l'esecuzione di uno script Python non verrà visualizzato alcun risultato.

**Soluzione:**

```python
risultato = somma(10, 5)
print(risultato)
```

Oppure:

```python
print(somma(10, 5))
```

#### Errore 3 – Inserire istruzioni dopo un `return` incondizionato

```python
def somma(a, b):
    return a + b
    print("Elaborazione terminata")
```

L'istruzione `print()` non verrà mai eseguita.

**Soluzione:**

```python
def somma(a, b):
    print("Elaborazione in corso")
    return a + b
```

In questo caso la funzione visualizza un messaggio e restituisce il risultato dell'elaborazione. Non esiste infatti alcun divieto di utilizzare contemporaneamente `print()` e `return` all'interno della stessa funzione.

#### Errore 4 – Non prevedere un valore di ritorno per tutti i casi

```python
def is_positivo(numero):
    if numero > 0:
        return True
```

Se il numero è positivo, la funzione restituisce `True`. In tutti gli altri casi restituisce implicitamente `None`, anziché `False`.

| Chiamata | Risultato ottenuto | Risultato atteso |
|---|---|---|
| `is_positivo(10)` | `True` | `True` |
| `is_positivo(0)` | `None` | `False` |
| `is_positivo(-5)` | `None` | `False` |

**Soluzione:**

```python
def is_positivo(numero):
    if numero > 0:
        return True
    else:
        return False
```

> **BUONA PRATICA DI PROGRAMMAZIONE**
>
> Quando una funzione è progettata per restituire un risultato, è opportuno verificare che tutti i possibili percorsi di esecuzione prevedano la restituzione di un valore coerente con lo scopo della funzione.

#### Errore 5 – Terminare anticipatamente una funzione all'interno di un ciclo

Consideriamo una funzione che dovrebbe calcolare la somma di tutti gli elementi di una lista.

**Versione errata:**

```python
def calcola_somma(numeri):
    totale = 0

    for numero in numeri:
        totale = totale + numero
        return totale


risultato = calcola_somma([10, 20, 30])
print(risultato)
```

**Output:** `10`

L'istruzione `return` è stata inserita all'interno del ciclo `for`. Di conseguenza, la funzione termina al termine della prima iterazione, senza elaborare tutti gli elementi della lista.

**Versione corretta:**

```python
def calcola_somma(numeri):
    totale = 0

    for numero in numeri:
        totale = totale + numero

    return totale


risultato = calcola_somma([10, 20, 30])
print(risultato)
```

**Output:** `60`

L'istruzione `return` viene ora eseguita soltanto al termine del ciclo, dopo che tutti gli elementi della lista sono stati elaborati. Questo esempio evidenzia ancora una volta l'importanza dell'indentazione nella programmazione in Python.

### 4.11 Schema riepilogativo

| Concetto | Significato |
|---|---|
| `print()` | Visualizza informazioni destinate all'utente. |
| `return` | Termina la funzione e restituisce un eventuale valore al chiamante. |
| Valore di ritorno | Risultato restituito da una funzione. |
| `None` | Valore speciale che rappresenta l'assenza di un valore significativo. |
| Ritorno implicito | Restituzione automatica di `None` in assenza di un `return` esplicito. |
| `return` senza espressione | Termina la funzione restituendo `None`. |
| Terminazione anticipata | Interruzione dell'esecuzione della funzione prima di raggiungere la fine del suo corpo. |
| Codice irraggiungibile | Porzione di codice che non può essere eseguita. |
| `return` multipli | Presenza di più punti di uscita all'interno della stessa funzione. |
| Funzione predicato | Funzione che restituisce un valore booleano. |
| `tuple` | Sequenza ordinata e immutabile di elementi. |
| Unpacking | Estrazione degli elementi di una sequenza mediante assegnazione multipla. |

![Figura 4.7 – Scelta della modalità con cui una funzione svolge il proprio compito.](images/24_scelta_print_return.svg)

*Figura 4.7 – Scelta della modalità con cui una funzione svolge il proprio compito.*

---

## 5. Le quattro tipologie fondamentali di funzioni

Come abbiamo visto nelle sezioni precedenti, una funzione può ricevere dati in ingresso mediante i **parametri** e restituire il risultato di un'elaborazione mediante l'istruzione **`return`**.

Sulla base della presenza o meno di questi due elementi, possiamo individuare quattro tipologie fondamentali di funzioni.

| Tipologia | Parametri in ingresso | Valore di ritorno significativo |
|---|:---:|:---:|
| **1.** Funzioni senza parametri e senza valore di ritorno | No | No |
| **2.** Funzioni con parametri e senza valore di ritorno | Sì | No |
| **3.** Funzioni senza parametri e con valore di ritorno | No | Sì |
| **4.** Funzioni con parametri e con valore di ritorno | Sì | Sì |

![Figura 5.1 – Classificazione delle funzioni in base ai parametri e ai valori di ritorno significativi.](images/25_classificazione_tipologie.svg)

*Figura 5.1 – Classificazione delle funzioni in base ai parametri e ai valori di ritorno significativi.*

Ricordiamo che in Python tutte le funzioni che terminano normalmente restituiscono un valore. Pertanto, quando parliamo di funzioni senza valore di ritorno, intendiamo funzioni che non restituiscono un risultato significativo al chiamante e che restituiscono quindi `None`.

### 5.1 Funzioni senza parametri e senza valore di ritorno

Questa tipologia comprende le funzioni che svolgono un determinato compito senza ricevere dati dal programma chiamante e senza restituirgli un risultato significativo.

Sono generalmente utilizzate per eseguire operazioni che non richiedono dati esterni, come la visualizzazione di messaggi, titoli o menù.

#### Sintassi generale

```python
def nome_funzione():
    istruzioni
```

#### Esempio: visualizzazione di un menù

```python
def mostra_menu():
    print("====================")
    print("    MENU PRINCIPALE")
    print("====================")
    print("1. Inserimento dati")
    print("2. Visualizzazione dati")
    print("3. Esci")


def main():
    mostra_menu()


if __name__ == "__main__":
    main()
```

**Output:**

```text
====================
    MENU PRINCIPALE
====================
1. Inserimento dati
2. Visualizzazione dati
3. Esci
```

![Figura 5.2 – Funzione senza parametri che visualizza informazioni sullo schermo.](images/26_funzione_tipologia_1.svg)

*Figura 5.2 – Funzione senza parametri che visualizza informazioni sullo schermo.*

| Caratteristica | Descrizione |
|---|---|
| Nome | `mostra_menu()` |
| Parametri | Nessuno |
| Compito | Visualizzare il menù |
| Valore restituito | `None` |
| Destinatario delle informazioni | Utente |

La funzione viene richiamata semplicemente attraverso il suo nome, seguito dalle parentesi tonde vuote.

### 5.2 Funzioni con parametri e senza valore di ritorno

Questa tipologia comprende le funzioni che ricevono uno o più dati in ingresso, li utilizzano per svolgere un determinato compito, ma non restituiscono un risultato significativo al programma chiamante.

#### Sintassi generale

```python
def nome_funzione(parametro_1, parametro_2):
    istruzioni
```

#### Esempio: visualizzazione di un messaggio personalizzato

```python
def saluta(nome):
    print(f"Benvenuto nel programma, {nome}!")


def main():
    saluta("Mario")
    saluta("Giulia")
    saluta("Luca")


if __name__ == "__main__":
    main()
```

**Output:**

```text
Benvenuto nel programma, Mario!
Benvenuto nel programma, Giulia!
Benvenuto nel programma, Luca!
```

![Figura 5.3 – Funzione che riceve un argomento e visualizza un messaggio personalizzato.](images/27_funzione_tipologia_2.svg)

*Figura 5.3 – Funzione che riceve un argomento e visualizza un messaggio personalizzato.*

| Caratteristica | Descrizione |
|---|---|
| Nome | `saluta()` |
| Parametri | `nome` |
| Compito | Visualizzare un messaggio personalizzato |
| Valore restituito | `None` |
| Destinatario delle informazioni | Utente |

La funzione viene definita una sola volta, ma può produrre risultati differenti a seconda degli argomenti ricevuti durante le diverse chiamate.

### 5.3 Funzioni senza parametri e con valore di ritorno

Questa tipologia comprende le funzioni che non ricevono dati dal programma chiamante, ma restituiscono un risultato al termine della propria esecuzione.

Sono particolarmente utili per acquisire e validare dati inseriti dall'utente, generare valori casuali oppure ottenere informazioni da altre risorse.

#### Sintassi generale

```python
def nome_funzione():
    istruzioni
    return risultato
```

#### Esempio: acquisizione e validazione di un numero intero positivo

Realizziamo una funzione che acquisisce un numero intero da tastiera, verificando che sia maggiore di zero, e lo restituisce al programma chiamante.

```python
def leggi_numero_positivo():
    dato_valido = False

    while not dato_valido:
        try:
            numero = int(input("Inserisci un numero intero positivo: "))
        except ValueError:
            print("Errore: inserire un numero intero.")
        else:
            if numero > 0:
                dato_valido = True
            else:
                print("Errore: il numero deve essere maggiore di zero.")

    return numero


def main():
    numero = leggi_numero_positivo()

    print("Numero acquisito:", numero)


if __name__ == "__main__":
    main()
```

**Esempio di esecuzione:**

```text
Inserisci un numero intero positivo: abc
Errore: inserire un numero intero.
Inserisci un numero intero positivo: -5
Errore: il numero deve essere maggiore di zero.
Inserisci un numero intero positivo: 12
Numero acquisito: 12
```

![Figura 5.4 – Funzione che acquisisce autonomamente un dato e lo restituisce al chiamante.](images/28_funzione_tipologia_3.svg)

*Figura 5.4 – Funzione che acquisisce autonomamente un dato e lo restituisce al chiamante.*

| Caratteristica | Descrizione |
|---|---|
| Nome | `leggi_numero_positivo()` |
| Parametri | Nessuno |
| Compito | Acquisire e validare un numero |
| Valore restituito | Numero intero positivo (`int`) |
| Destinatario del risultato | Programma chiamante |

Questo esempio mostra come sia possibile racchiudere all'interno di una singola funzione l'intera procedura di acquisizione e validazione di un dato, rendendola riutilizzabile anche in altri programmi.

> **ATTENZIONE**
>
> Una funzione senza parametri non è necessariamente una funzione che non utilizza dati in ingresso.
>
> Essa può acquisire autonomamente dei dati mediante `input()` senza che questi le vengano trasmessi dal programma chiamante attraverso degli argomenti.

### 5.4 Funzioni con parametri e con valore di ritorno

Questa tipologia comprende le funzioni che ricevono uno o più dati in ingresso, effettuano un'elaborazione e restituiscono il risultato ottenuto al programma chiamante.

Rappresentano una delle tipologie maggiormente utilizzate nella programmazione modulare, poiché consentono di separare l'elaborazione dei dati dalle operazioni di acquisizione e visualizzazione.

#### Sintassi generale

```python
def nome_funzione(parametro_1, parametro_2):
    istruzioni
    return risultato
```

#### Esempio 1: calcolo dell'area di un rettangolo

```python
def calcola_area(base, altezza):
    area = base * altezza
    return area


def main():
    risultato = calcola_area(10, 5)

    print("Area del rettangolo:", risultato)


if __name__ == "__main__":
    main()
```

**Output:**

```text
Area del rettangolo: 50
```

![Figura 5.5 – Funzione che riceve due argomenti, elabora e restituisce il risultato.](images/29_funzione_tipologia_4.svg)

*Figura 5.5 – Funzione che riceve due argomenti, elabora e restituisce il risultato.*

| Caratteristica | Descrizione |
|---|---|
| Nome | `calcola_area()` |
| Parametri | `base`, `altezza` |
| Compito | Calcolare l'area del rettangolo |
| Valore restituito | Risultato della moltiplicazione |
| Destinatario del risultato | Programma chiamante |

La funzione non si occupa né dell'acquisizione dei dati da tastiera né della visualizzazione del risultato: il suo unico compito consiste nell'elaborare i dati ricevuti e restituire il risultato. Questo la rende particolarmente adatta al riutilizzo in programmi differenti.

#### Esempio 2: conteggio delle parole di una frase

Realizziamo una funzione che riceve una stringa e restituisce il numero di parole contenute al suo interno.

Per effettuare l'elaborazione utilizziamo:

- il metodo `split()`, che suddivide una stringa in una lista di sottostringhe, utilizzando come separatori gli spazi e gli altri caratteri di spaziatura;
- la funzione built-in `len()`, che restituisce il numero di elementi della lista ottenuta.

```python
def conta_parole(frase):
    parole = frase.split()
    return len(parole)


def main():
    risultato = conta_parole("Questa è una frase di esempio.")

    print("Numero di parole:", risultato)


if __name__ == "__main__":
    main()
```

**Output:**

```text
Numero di parole: 6
```

![Figura 5.6 – Elaborazione della stringa mediante split() e len() e restituzione del risultato.](images/30_conteggio_parole.svg)

*Figura 5.6 – Elaborazione della stringa mediante split() e len() e restituzione del risultato.*

L'istruzione:

```python
parole = frase.split()
```

genera la seguente lista:

```python
["Questa", "è", "una", "frase", "di", "esempio."]
```

Successivamente, l'istruzione:

```python
return len(parole)
```

calcola il numero di elementi della lista e restituisce il valore intero `6`.

Il metodo `split()`, quando utilizzato senza argomenti, gestisce correttamente anche la presenza di più spazi consecutivi tra le parole.

| Chiamata | Valore restituito |
|---|---:|
| `conta_parole("Ciao")` | 1 |
| `conta_parole("Ciao mondo")` | 2 |
| `conta_parole("Impariamo a programmare in Python")` | 5 |
| `conta_parole("Ciao    mondo")` | 2 |
| `conta_parole("")` | 0 |

Il conteggio si basa quindi sulle sottostringhe separate da caratteri di spaziatura, senza effettuare un'analisi linguistica delle parole o della punteggiatura.

Questo esempio mostra inoltre come una funzione definita dall'utente possa utilizzare al proprio interno altre funzioni e metodi già disponibili nel linguaggio Python.

### 5.5 Come scegliere la tipologia di funzione da utilizzare

Durante la fase di progettazione di una funzione, è opportuno individuare innanzitutto il compito che essa dovrà svolgere.

Successivamente, è possibile determinare la tipologia di funzione da implementare rispondendo a due semplici domande:

1. La funzione necessita di ricevere dati dal programma chiamante?
2. La funzione deve restituire un risultato al programma chiamante?

![Figura 5.7 – Flow chart decisionale per individuare la tipologia di funzione.](images/31_scelta_tipologia_funzione.svg)

*Figura 5.7 – Flow chart decisionale per individuare la tipologia di funzione.*

#### Esempi di progettazione

| Compito assegnato alla funzione | Parametri | Valore restituito | Tipologia |
|---|:---:|:---:|:---:|
| Visualizzare un menù | No | No | 1 |
| Visualizzare un messaggio di benvenuto | No | No | 1 |
| Visualizzare il nome di un utente ricevuto come argomento | Sì | No | 2 |
| Visualizzare i risultati di un'elaborazione ricevuti dal chiamante | Sì | No | 2 |
| Acquisire e validare un numero | No | Sì | 3 |
| Generare e restituire un numero casuale tra estremi prefissati | No | Sì | 3 |
| Calcolare la media degli elementi di una lista ricevuta | Sì | Sì | 4 |
| Calcolare l'area di una figura geometrica | Sì | Sì | 4 |
| Verificare se un numero ricevuto sia primo | Sì | Sì | 4 |
| Contare le parole di una frase ricevuta | Sì | Sì | 4 |

La scelta della tipologia dipende da come decidiamo di progettare la funzione e non esclusivamente dall'operazione che essa deve svolgere.

Ad esempio, una funzione che calcola una somma potrebbe acquisire autonomamente i due numeri mediante `input()` oppure riceverli attraverso dei parametri. Analogamente, potrebbe visualizzare direttamente il risultato oppure restituirlo al programma chiamante.

> **BUONA PRATICA DI PROGRAMMAZIONE**
>
> Prima di implementare il corpo di una funzione, è opportuno definirne l'interfaccia, stabilendo quali dati deve ricevere e quale risultato deve eventualmente restituire.
>
> Quando possibile, le funzioni dedicate all'elaborazione dovrebbero ricevere i dati attraverso i parametri e restituire i risultati mediante `return`, evitando di occuparsi direttamente dell'acquisizione e della visualizzazione.

### 5.6 Schema riepilogativo

| Caratteristica | Tipologia 1 | Tipologia 2 | Tipologia 3 | Tipologia 4 |
|---|:---:|:---:|:---:|:---:|
| Parametri in ingresso | No | Sì | No | Sì |
| Valore di ritorno significativo | No | No | Sì | Sì |
| `return` esplicito con risultato | No | No | Sì | Sì |
| Restituisce `None` | Sì | Sì | No | No |
| Può utilizzare `input()` | Sì | Sì | Sì | Sì |
| Può utilizzare `print()` | Sì | Sì | Sì | Sì |

#### Modelli sintattici di riferimento

**Tipologia 1 – Senza parametri, senza risultato restituito**

```python
def funzione():
    print("Ciao")

funzione()
```

**Tipologia 2 – Con parametri, senza risultato restituito**

```python
def funzione(a):
    print(a)

funzione(10)
```

**Tipologia 3 – Senza parametri, con risultato restituito**

```python
def funzione():
    a = int(input())
    return a

risultato = funzione()
```

**Tipologia 4 – Con parametri, con risultato restituito**

```python
def funzione(a, b):
    return a + b

risultato = funzione(10, 5)
```

> **DA RICORDARE**
>
> La presenza di parametri determina la possibilità di ricevere dati direttamente dal programma chiamante.
>
> La presenza di un `return` con un risultato significativo determina la possibilità di restituire tale risultato al programma chiamante.
>
> Le istruzioni `input()` e `print()` riguardano invece la comunicazione tra il programma e l'utente.

![Figura 5.8 – Distinzione tra comunicazione interna (parametri e return) e comunicazione con l’utente (input e print).](images/32_comunicazione_utente_chiamante.svg)

*Figura 5.8 – Distinzione tra comunicazione interna (parametri e return) e comunicazione con l’utente (input e print).*

---

## 6. Visibilità delle variabili: namespace e scope

Quando un programma Python viene organizzato mediante l'utilizzo di più funzioni, è necessario comprendere in quali parti del programma le variabili dichiarate possono essere utilizzate. Non tutte le variabili, infatti, sono accessibili da qualsiasi punto del programma.

Per comprendere questo comportamento è necessario introdurre due concetti fondamentali: **namespace** (spazio dei nomi) e **scope** (campo di visibilità).

### 6.1 Il namespace e lo scope

#### Il namespace (spazio dei nomi)

> **DEFINIZIONE – NAMESPACE**
>
> Un namespace è un ambiente nel quale vengono registrate le associazioni tra i nomi simbolici utilizzati in un programma e gli oggetti ai quali essi fanno riferimento.

Quando definiamo una variabile oppure una funzione, Python associa il relativo identificatore a un oggetto all'interno di uno specifico namespace.

```python
numero = 10
nome = "Mario"

def saluta():
    print("Ciao!")
```

![Figura 6.1 – Associazione tra identificatori e oggetti all’interno di un namespace.](images/33_namespace.svg)

*Figura 6.1 – Associazione tra identificatori e oggetti all’interno di un namespace.*

L'utilizzo dei namespace consente a Python di gestire gli identificatori utilizzati nelle diverse parti del programma, evitando che nomi identici appartenenti ad ambienti differenti entrino necessariamente in conflitto.

#### Lo scope (campo di visibilità)

> **DEFINIZIONE – SCOPE**
>
> Lo scope di un identificatore è la porzione di programma all'interno della quale tale identificatore è visibile e può essere utilizzato.

Mentre il namespace rappresenta l'ambiente nel quale sono registrati i nomi, lo scope determina da quali parti del programma tali nomi sono accessibili.

| Concetto | Significato | Domanda di riferimento |
|---|---|---|
| **Namespace** | Spazio dei nomi | Dove è registrato l'identificatore? |
| **Scope** | Campo di visibilità | Da dove posso utilizzare l'identificatore? |

### 6.2 I principali namespace in Python

Per il momento considereremo tre principali tipologie di namespace:

| Namespace | Descrizione |
|---|---|
| **Built-in namespace** | Contiene i nomi predefiniti messi a disposizione dal linguaggio Python, come `print`, `input` e `len`. |
| **Global namespace** | Contiene gli identificatori definiti al livello principale del modulo Python, al di fuori delle funzioni. |
| **Local namespace** | Contiene gli identificatori locali a una specifica chiamata di una funzione, compresi i suoi parametri formali. |

![Figura 6.2 – Rappresentazione semplificata dei principali ambienti di visibilità in Python.](images/34_ambienti_visibilita.svg)

*Figura 6.2 – Rappresentazione semplificata dei principali ambienti di visibilità in Python.*

Ogni chiamata di una funzione dispone quindi di un proprio namespace locale, distinto da quello delle altre chiamate.

In assenza di funzioni annidate, per un nome non dichiarato esplicitamente globale, la ricerca avviene generalmente nel seguente ordine (se un nome è riconosciuto come locale ma non ancora associato a un valore, non si passa alla ricerca globale: si veda la Sezione 6.9).

![Figura 6.3 – Ordine semplificato di ricerca dei nomi durante l’esecuzione di una funzione.](images/35_ricerca_identificatori.svg)

*Figura 6.3 – Ordine semplificato di ricerca dei nomi durante l’esecuzione di una funzione.*

Se Python non riesce a individuare l'identificatore richiesto, può generare un errore di tipo `NameError`.

### 6.3 Le variabili locali

> **DEFINIZIONE – VARIABILE LOCALE**
>
> Una variabile locale è una variabile appartenente al namespace locale di una funzione, utilizzabile all'interno della funzione alla quale appartiene.

Una variabile definita mediante una normale assegnazione all'interno di una funzione è, generalmente, una variabile locale.

#### Esempio: definizione di una variabile locale

```python
def calcola():
    numero = 10
    print("Valore locale:", numero)


def main():
    calcola()


if __name__ == "__main__":
    main()
```

**Output:**

```text
Valore locale: 10
```

La variabile `numero` appartiene al namespace locale della funzione `calcola()`. Non può quindi essere utilizzata direttamente all'interno della funzione `main()`.

#### Esempio errato: accesso a una variabile locale da un'altra funzione

```python
def calcola():
    numero = 10
    print("Valore locale:", numero)


def main():
    calcola()
    print(numero)


if __name__ == "__main__":
    main()
```

**Output ed errore:**

```text
Valore locale: 10
NameError: name 'numero' is not defined
```

La funzione `main()` tenta di utilizzare un identificatore che appartiene al namespace locale di un'altra funzione.

![Figura 6.4 – Una variabile locale non è direttamente accessibile da un’altra funzione.](images/36_visibilita_variabili_locali.svg)

*Figura 6.4 – Una variabile locale non è direttamente accessibile da un’altra funzione.*

#### Versione corretta mediante `return`

Se desideriamo utilizzare il valore elaborato dalla funzione `calcola()` anche all'interno della funzione `main()`, possiamo restituirlo mediante l'istruzione `return`.

```python
def calcola():
    numero = 10
    return numero


def main():
    risultato = calcola()
    print("Valore restituito:", risultato)


if __name__ == "__main__":
    main()
```

**Output:**

```text
Valore restituito: 10
```

In questo caso la variabile locale `numero` non diventa accessibile alla funzione `main()`: è il suo valore a essere restituito e associato alla variabile `risultato` del chiamante.

> **DA RICORDARE**
>
> Le variabili locali appartengono alla funzione nella quale sono definite. Per comunicare i risultati al programma chiamante possiamo utilizzare l'istruzione `return`.

### 6.4 Variabili locali omonime

Due o più funzioni possono utilizzare variabili locali aventi lo stesso nome, senza che queste interferiscano tra loro. Ciò è possibile perché ogni funzione, durante la propria esecuzione, dispone di un namespace locale indipendente.

```python
def funzione_1():
    numero = 10
    print("Funzione 1:", numero)


def funzione_2():
    numero = 20
    print("Funzione 2:", numero)


def main():
    numero = 30

    funzione_1()
    funzione_2()

    print("Funzione main:", numero)


if __name__ == "__main__":
    main()
```

**Output:**

```text
Funzione 1: 10
Funzione 2: 20
Funzione main: 30
```

Sebbene tutte e tre le funzioni utilizzino una variabile denominata `numero`, si tratta di tre identificatori appartenenti ad ambienti locali differenti.

![Figura 6.5 – Variabili locali omonime appartenenti a funzioni differenti.](images/37_variabili_locali_omonime.svg)

*Figura 6.5 – Variabili locali omonime appartenenti a funzioni differenti.*

La modifica della variabile `numero` all'interno di una delle funzioni non comporta la modifica delle variabili omonime appartenenti alle altre funzioni.

### 6.5 I parametri formali come variabili locali

Anche i parametri formali di una funzione appartengono al suo namespace locale. Nel momento in cui viene effettuata la chiamata, Python associa ciascun parametro formale al corrispondente argomento ricevuto.

```python
def somma(a, b):
    risultato = a + b
    return risultato


def main():
    numero_1 = 10
    numero_2 = 5

    totale = somma(numero_1, numero_2)

    print("Totale:", totale)


if __name__ == "__main__":
    main()
```

**Output:**

```text
Totale: 15
```

| Namespace locale di `main()` | Namespace locale di `somma()` |
|---|---|
| `numero_1 = 10` | `a = 10` |
| `numero_2 = 5` | `b = 5` |
| `totale = 15` | `risultato = 15` |

![Figura 6.6 – Parametri formali e ambiente locale del chiamante e del chiamato.](images/38_parametri_namespace_locale.svg)

*Figura 6.6 – Parametri formali e ambiente locale del chiamante e del chiamato.*

Al termine dell'esecuzione di `somma()`, le associazioni locali relative ad `a`, `b` e `risultato` non sono più disponibili direttamente.

Il risultato dell'elaborazione rimane tuttavia utilizzabile da parte di `main()`, poiché è stato restituito mediante `return` e associato alla variabile `totale`.

> **DA RICORDARE**
>
> Anche le variabili definite all'interno della funzione `main()` sono variabili locali. La funzione `main()` non costituisce un'eccezione alle normali regole di visibilità delle funzioni Python.

### 6.6 Le variabili globali

> **DEFINIZIONE – VARIABILE GLOBALE**
>
> Una variabile globale è una variabile definita al livello principale di un modulo Python, al di fuori delle funzioni, appartenente al namespace globale del modulo stesso.

A differenza delle variabili locali, le variabili globali possono essere utilizzate anche all'interno delle diverse funzioni definite nello stesso modulo, purché non siano nascoste da identificatori locali omonimi.

#### Esempio: lettura di una variabile globale

```python
numero = 100


def funzione_1():
    print("Funzione 1:", numero)


def funzione_2():
    print("Funzione 2:", numero)


def main():
    funzione_1()
    funzione_2()

    print("Funzione main:", numero)


if __name__ == "__main__":
    main()
```

**Output:**

```text
Funzione 1: 100
Funzione 2: 100
Funzione main: 100
```

La variabile `numero` è stata definita al di fuori di tutte le funzioni e può quindi essere letta da ciascuna di esse.

![Figura 6.7 – Accesso in lettura a una variabile globale da parte di differenti funzioni.](images/39_variabili_globali.svg)

*Figura 6.7 – Accesso in lettura a una variabile globale da parte di differenti funzioni.*

> **ATTENZIONE**
>
> Per leggere il valore di una variabile globale all'interno di una funzione non è necessario utilizzare la parola chiave `global`.

### 6.7 Variabili locali e globali omonime

Una funzione può contenere una variabile locale avente lo stesso nome di una variabile globale. In questo caso, all'interno della funzione, la variabile locale ha la precedenza rispetto a quella globale.

```python
numero = 100


def funzione_1():
    numero = 10
    print("Funzione 1:", numero)


def funzione_2():
    print("Funzione 2:", numero)


def main():
    funzione_1()
    funzione_2()

    print("Funzione main:", numero)


if __name__ == "__main__":
    main()
```

**Output:**

```text
Funzione 1: 10
Funzione 2: 100
Funzione main: 100
```

All'interno di `funzione_1()`, l'assegnazione `numero = 10` determina la creazione di una variabile locale, distinta dalla variabile globale omonima. La variabile globale non viene quindi modificata.

Questo comportamento prende il nome di **shadowing (oscuramento)**: un identificatore locale nasconde temporaneamente, nel proprio campo di visibilità, un identificatore appartenente a un ambiente esterno.

![Figura 6.8 – Precedenza dell’identificatore locale rispetto all’identificatore globale omonimo.](images/40_shadowing.svg)

*Figura 6.8 – Precedenza dell’identificatore locale rispetto all’identificatore globale omonimo.*

### 6.8 La parola chiave `global`

Abbiamo visto come sia possibile leggere il valore di una variabile globale direttamente dall'interno di una funzione. Se desideriamo invece assegnare un nuovo valore alla variabile globale dall'interno di una funzione, dobbiamo utilizzare la parola chiave `global`.

> **DEFINIZIONE – GLOBAL**
>
> La parola chiave `global` permette di indicare che un identificatore utilizzato all'interno di una funzione appartiene al namespace globale del modulo, anziché al namespace locale della funzione.

#### Sintassi generale

```python
global nome_variabile
```

È inoltre possibile dichiarare più identificatori globali mediante una singola istruzione.

```python
global variabile_1, variabile_2
```

#### 6.8.1 Modifica di una variabile senza utilizzare `global`

```python
numero = 100


def modifica():
    numero = 50
    print("Dentro la funzione:", numero)


def main():
    print("Prima della chiamata:", numero)

    modifica()

    print("Dopo la chiamata:", numero)


if __name__ == "__main__":
    main()
```

**Output:**

```text
Prima della chiamata: 100
Dentro la funzione: 50
Dopo la chiamata: 100
```

La funzione `modifica()` crea una nuova variabile locale denominata `numero`. Il valore della variabile globale rimane invariato.

#### 6.8.2 Modifica di una variabile utilizzando `global`

```python
numero = 100


def modifica():
    global numero

    numero = 50
    print("Dentro la funzione:", numero)


def main():
    print("Prima della chiamata:", numero)

    modifica()

    print("Dopo la chiamata:", numero)


if __name__ == "__main__":
    main()
```

**Output:**

```text
Prima della chiamata: 100
Dentro la funzione: 50
Dopo la chiamata: 50
```

L'istruzione `global numero` indica a Python che l'identificatore `numero` utilizzato nella funzione deve riferirsi alla variabile globale. Di conseguenza, l'assegnazione `numero = 50` modifica direttamente l'associazione presente nel namespace globale.

![Figura 6.9 – Differenza tra assegnazione locale e assegnazione globale mediante global.](images/41_clausola_global.svg)

*Figura 6.9 – Differenza tra assegnazione locale e assegnazione globale mediante global.*

### 6.9 L'errore `UnboundLocalError`

Un errore particolarmente comune si verifica quando si tenta di modificare una variabile globale utilizzando il suo valore precedente, senza aver utilizzato la parola chiave `global`.

#### Esempio errato

```python
contatore = 0


def incrementa():
    contatore = contatore + 1


def main():
    incrementa()
    print(contatore)


if __name__ == "__main__":
    main()
```

**Errore (il messaggio può variare in base alla versione di Python):**

```text
UnboundLocalError: cannot access local variable 'contatore' where it is not associated with a value
```

Python, rilevando un'assegnazione alla variabile `contatore` all'interno della funzione, considera tale identificatore come locale.

Tuttavia, per eseguire l'operazione `contatore = contatore + 1` è necessario conoscere il valore precedentemente associato alla variabile locale `contatore`, che non è ancora stato definito.

Di conseguenza, viene generato un errore di tipo `UnboundLocalError`. Questo errore rappresenta un caso particolare di `NameError`.

#### Versione corretta

```python
contatore = 0


def incrementa():
    global contatore

    contatore = contatore + 1


def main():
    incrementa()
    incrementa()
    incrementa()

    print("Contatore:", contatore)


if __name__ == "__main__":
    main()
```

**Output:**

```text
Contatore: 3
```

Grazie alla parola chiave `global`, la funzione può leggere il valore della variabile globale e assegnarle il nuovo risultato.

Lo stesso problema si verificherebbe utilizzando l'operatore di assegnazione incrementale `contatore += 1`. Anche in questo caso, per riassegnare la variabile globale dall'interno della funzione, è necessaria la dichiarazione `global`.

| Errore | Causa |
|---|---|
| `NameError` | L'identificatore richiesto non viene trovato negli ambienti di visibilità accessibili. |
| `UnboundLocalError` | Si tenta di utilizzare una variabile riconosciuta come locale alla funzione prima che le sia stato associato un valore. |

> **ATTENZIONE**
>
> Se Python riconosce un identificatore come locale a una funzione, non ricerca automaticamente una variabile globale omonima quando quella locale non è ancora stata inizializzata.

### 6.10 Visibilità e durata delle variabili locali

Ogni volta che una funzione viene chiamata, viene creato un nuovo ambiente locale. Le variabili locali di una funzione non conservano automaticamente il proprio valore tra una chiamata e la successiva.

```python
def incrementa():
    contatore = 0
    contatore += 1

    print(contatore)


def main():
    incrementa()
    incrementa()
    incrementa()


if __name__ == "__main__":
    main()
```

**Output:**

```text
1
1
1
```

Il risultato non è `1`, `2`, `3`, poiché ogni chiamata dispone di un nuovo ambiente locale e la variabile `contatore` viene inizializzata nuovamente a zero.

![Figura 6.10 – Creazione di un nuovo namespace locale a ogni chiamata della funzione.](images/42_durata_variabili_locali.svg)

*Figura 6.10 – Creazione di un nuovo namespace locale a ogni chiamata della funzione.*

| Concetto | Significato |
|---|---|
| **Visibilità (scope)** | Indica in quali parti del programma un identificatore può essere utilizzato. |
| **Durata (lifetime)** | Indica per quanto tempo un'associazione o un oggetto rimane disponibile durante l'esecuzione del programma. |

Generalmente, le associazioni locali vengono create durante la chiamata della funzione e cessano di essere direttamente disponibili quando questa termina. Gli oggetti ai quali tali identificatori fanno riferimento possono tuttavia continuare a esistere, ad esempio quando vengono restituiti al chiamante.

### 6.11 La visibilità delle variabili nei blocchi `if`, `while` e `for`

In alcuni linguaggi di programmazione, ogni blocco di istruzioni introduce un proprio campo di visibilità.

In Python, invece, i normali blocchi di selezione e iterazione non introducono un nuovo namespace locale. Una variabile definita all'interno di un blocco `if`, `while` o `for` appartiene quindi allo stesso ambiente nel quale si trova il blocco.

#### Esempio 1 – Struttura di selezione

```python
def main():
    if True:
        numero = 10

    print(numero)


if __name__ == "__main__":
    main()
```

**Output:** `10`

La variabile `numero`, pur essendo stata definita all'interno del blocco `if`, appartiene al namespace locale di `main()` e può essere utilizzata anche dopo la terminazione del blocco.

#### Esempio 2 – Struttura di iterazione

```python
def main():
    for i in range(1, 4):
        print(i)

    print("Valore finale di i:", i)


if __name__ == "__main__":
    main()
```

**Output:**

```text
1
2
3
Valore finale di i: 3
```

Anche la variabile `i` rimane accessibile dopo la terminazione del ciclo `for`.

![Figura 6.11 – Un blocco if non introduce un nuovo namespace locale in Python.](images/43_scope_blocchi.svg)

*Figura 6.11 – Un blocco if non introduce un nuovo namespace locale in Python.*

#### Attenzione alle assegnazioni condizionali

Il fatto che un blocco non introduca un nuovo namespace non garantisce che una variabile definita al suo interno sia stata effettivamente inizializzata.

```python
def main():
    if False:
        numero = 10

    print(numero)


if __name__ == "__main__":
    main()
```

In questo caso viene generato un errore `UnboundLocalError`, poiché le istruzioni contenute nel blocco `if` non vengono eseguite.

> **DA RICORDARE**
>
> In Python i blocchi `if`, `while` e `for` non introducono un proprio ambiente locale. Le funzioni, invece, dispongono di un proprio namespace locale.

### 6.12 Variabili globali o passaggio dei parametri?

Sebbene Python permetta di utilizzare variabili globali, nella programmazione modulare è generalmente preferibile utilizzare variabili locali, parametri e valori di ritorno.

L'utilizzo eccessivo delle variabili globali può infatti:

- creare dipendenze tra le diverse funzioni;
- rendere più difficile comprendere quali funzioni modificano determinati dati;
- aumentare la probabilità di errori;
- ridurre la riutilizzabilità delle funzioni;
- complicare le operazioni di testing e debugging.

#### Esempio: incremento di un contatore

**Versione A – Utilizzo di una variabile globale**

```python
contatore = 0


def incrementa():
    global contatore
    contatore += 1


def main():
    incrementa()
    incrementa()
    incrementa()

    print("Contatore:", contatore)


if __name__ == "__main__":
    main()
```

**Versione B – Utilizzo di parametri e `return`**

```python
def incrementa(numero):
    return numero + 1


def main():
    contatore = 0

    contatore = incrementa(contatore)
    contatore = incrementa(contatore)
    contatore = incrementa(contatore)

    print("Contatore:", contatore)


if __name__ == "__main__":
    main()
```

**Output di entrambe le versioni:**

```text
Contatore: 3
```

Sebbene il risultato sia identico, la seconda implementazione presenta alcuni vantaggi.

| Caratteristica | Versione A | Versione B |
|---|---|---|
| Utilizzo di variabili globali | Sì | No |
| Utilizzo di parametri | No | Sì |
| Utilizzo di `return` | No | Sì |
| Dipendenza da variabili esterne alla funzione | Sì | No |
| Riutilizzabilità della funzione | Limitata | Elevata |
| Facilità di testing | Minore | Maggiore |

La funzione della seconda versione può essere utilizzata con qualsiasi numero compatibile con l'operazione di incremento, indipendentemente dal nome della variabile utilizzata dal programma chiamante.

![Figura 6.12 – Confronto tra variabili globali e passaggio esplicito dei dati mediante parametri e return.](images/44_global_vs_parametri.svg)

*Figura 6.12 – Confronto tra variabili globali e passaggio esplicito dei dati mediante parametri e return.*

> **BUONA PRATICA DI PROGRAMMAZIONE**
>
> Quando possibile, è preferibile trasmettere i dati a una funzione mediante i parametri e acquisirne i risultati mediante `return`, limitando l'utilizzo delle variabili globali ai casi in cui siano effettivamente necessarie.

#### L'utilizzo delle costanti globali

Un utilizzo appropriato del namespace globale consiste nella definizione di valori che devono essere condivisi da più funzioni e che non dovrebbero essere modificati durante l'esecuzione del programma.

```python
ALIQUOTA_IVA = 0.22


def calcola_iva(importo):
    return importo * ALIQUOTA_IVA


def calcola_totale(importo):
    return importo + calcola_iva(importo)


def main():
    importo = 100

    print("IVA:", calcola_iva(importo))
    print("Totale:", calcola_totale(importo))


if __name__ == "__main__":
    main()
```

**Output:**

```text
IVA: 22.0
Totale: 122.0
```

Per convenzione, le costanti vengono identificate mediante nomi scritti interamente in maiuscolo, separando eventualmente le parole con il carattere underscore.

Python non impedisce tecnicamente la modifica di questi valori: l'utilizzo delle lettere maiuscole costituisce una convenzione attraverso la quale il programmatore segnala che un determinato valore non dovrebbe essere modificato.

### 6.13 Schema riepilogativo

#### Variabili locali e globali a confronto

| Caratteristica | Variabili locali | Variabili globali |
|---|---|---|
| Ambiente di appartenenza | Namespace locale | Namespace globale del modulo |
| Posizione della definizione | All'interno di una funzione | Al di fuori delle funzioni, o tramite `global` |
| Visibilità | All'interno della propria funzione | A livello di modulo e nelle sue funzioni, salvo oscuramento |
| Durata tipica dell'associazione | Durante la chiamata della funzione | Durante la vita del modulo |
| Accesso in lettura da altre funzioni | No, direttamente | Sì, salvo oscuramento |
| Riassegnazione da altre funzioni | No, direttamente | Mediante `global` |
| Possibilità di identificatori omonimi | Sì, in ambienti differenti | Un'associazione per nome nello stesso namespace |

#### Riepilogo dei concetti fondamentali

| Concetto | Significato |
|---|---|
| **Namespace** | Ambiente contenente le associazioni tra identificatori e oggetti. |
| **Scope** | Campo di visibilità di un identificatore. |
| **Lifetime** | Durata di un'associazione o di un oggetto. |
| **Local namespace** | Ambiente locale di una chiamata di funzione. |
| **Global namespace** | Ambiente globale del modulo. |
| **Built-in namespace** | Ambiente dei nomi predefiniti di Python. |
| **Variabile locale** | Variabile appartenente all'ambiente locale di una funzione. |
| **Variabile globale** | Variabile appartenente all'ambiente globale del modulo. |
| **Shadowing** | Oscuramento di un identificatore da parte di un identificatore omonimo appartenente a un ambiente più interno. |
| **`global`** | Parola chiave che permette di riferire un identificatore al namespace globale. |
| **`NameError`** | Errore relativo a un identificatore non trovato. |
| **`UnboundLocalError`** | Errore relativo all'utilizzo di una variabile locale non ancora associata a un valore. |

---

## 7. Il passaggio dei parametri: oggetti mutabili e immutabili

Nelle sezioni precedenti abbiamo analizzato le modalità attraverso le quali una funzione riceve dati dal programma chiamante mediante i parametri.

Dobbiamo ora comprendere che cosa accade quando un argomento viene trasmesso a una funzione e, soprattutto, se le modifiche effettuate all'interno della funzione possano avere conseguenze sui dati utilizzati dal programma chiamante.

Per comprendere questo comportamento è necessario introdurre i concetti di riferimento a un oggetto, oggetto mutabile e immutabile, riassegnazione di una variabile e modifica di un oggetto.

### 7.1 Le variabili come riferimenti a oggetti

In Python tutti i dati sono rappresentati mediante **oggetti**.

Quando assegniamo un valore a una variabile, Python associa il nome della variabile al corrispondente oggetto. La variabile rappresenta quindi un **riferimento** all'oggetto.

Consideriamo le seguenti istruzioni:

```python
a = 10
b = a
```

La variabile `a` viene associata all'oggetto di tipo `int` che rappresenta il numero `10`. Successivamente, anche la variabile `b` viene associata allo stesso oggetto.

![Figura 7.1 – Associazione di due variabili allo stesso oggetto.](images/45_riferimenti_oggetti.svg)

*Figura 7.1 – Associazione di due variabili allo stesso oggetto.*

Se successivamente eseguiamo l'istruzione:

```python
b = 20
```

la variabile `b` viene associata a un altro oggetto, mentre la variabile `a` continua a fare riferimento all'oggetto precedente.

![Figura 7.2 – Modifica del riferimento mediante la riassegnazione di una variabile.](images/46_riassegnazione_variabili.svg)

*Figura 7.2 – Modifica del riferimento mediante la riassegnazione di una variabile.*

Verifichiamo il comportamento mediante un semplice frammento di codice:

```python
a = 10
b = a

b = 20

print("a =", a)
print("b =", b)
```

**Output:**

```text
a = 10
b = 20
```

L'assegnazione `b = 20` non modifica l'oggetto associato ad `a`, ma modifica il riferimento associato alla variabile `b`.

Questa distinzione sarà fondamentale per comprendere il passaggio dei parametri alle funzioni.

### 7.2 Il passaggio dei parametri per riferimento

Quando una funzione viene chiamata, Python associa i suoi parametri formali agli oggetti forniti come argomenti dal programma chiamante. Non viene quindi creata automaticamente una copia dell'oggetto trasmesso.

Il libro di testo definisce questo meccanismo **passaggio dei parametri per riferimento**. Più precisamente, in Python si parla di **passaggio per condivisione (call by sharing)**, poiché il parametro formale e l'argomento possono fare riferimento allo stesso oggetto, pur rimanendo identificatori indipendenti.

> **DEFINIZIONE – PASSAGGIO PER CONDIVISIONE**
>
> Il passaggio per condivisione è un meccanismo mediante il quale il parametro formale di una funzione viene associato allo stesso oggetto fornito come argomento dal programma chiamante.

#### Esempio: calcolo del quadrato di un numero

```python
def quadrato(formale):
    risultato = formale ** 2
    return risultato


def main():
    attuale = 12

    esito = quadrato(attuale)

    print("Numero:", attuale)
    print("Quadrato:", esito)


if __name__ == "__main__":
    main()
```

**Output:**

```text
Numero: 12
Quadrato: 144
```

Analizziamo le quattro fasi principali dell'esecuzione.

![Figura 7.3 – Evoluzione dei riferimenti durante la chiamata e l’esecuzione di una funzione.](images/47_passaggio_riferimenti.svg)

*Figura 7.3 – Evoluzione dei riferimenti durante la chiamata e l’esecuzione di una funzione.*

1. Prima della chiamata, la variabile `attuale` è associata all'oggetto `12`.
2. Al momento della chiamata, il parametro `formale` viene associato allo stesso oggetto.
3. Durante l'elaborazione, il risultato del calcolo viene associato alla variabile locale `risultato`.
4. La funzione termina e il valore restituito viene associato alla variabile `esito` del chiamante.

Il parametro `formale` appartiene al namespace locale della funzione `quadrato()`, mentre la variabile `attuale` appartiene al namespace locale della funzione `main()`.

I due identificatori sono quindi indipendenti, anche se inizialmente fanno riferimento allo stesso oggetto.

> **DA RICORDARE**
>
> Quando viene trasmesso un argomento a una funzione, viene condiviso il riferimento all'oggetto, non creata automaticamente una copia dell'oggetto stesso.
>
> Gli effetti delle operazioni effettuate sul parametro dipendono anche dalla natura dell'oggetto ricevuto.

### 7.3 Oggetti mutabili e immutabili

In Python è possibile classificare gli oggetti in due categorie, sulla base della possibilità di modificarne il contenuto dopo la loro creazione.

> **DEFINIZIONE – OGGETTO IMMUTABILE (IMMUTABLE OBJECT)**
>
> Un oggetto immutabile è un oggetto il cui valore non può essere modificato dopo la sua creazione. Per ottenere un valore differente è necessario fare riferimento a un altro oggetto.

> **DEFINIZIONE – OGGETTO MUTABILE (MUTABLE OBJECT)**
>
> Un oggetto mutabile è un oggetto il cui contenuto può essere modificato anche dopo la sua creazione, senza dover necessariamente creare un nuovo oggetto.

#### Classificazione dei principali tipi di dato

| Tipo di dato | Descrizione | Mutabile |
|---|---|:---:|
| `int` | Numeri interi | No |
| `float` | Numeri in virgola mobile | No |
| `bool` | Valori booleani | No |
| `str` | Stringhe | No |
| `tuple` | Tuple | No |
| `list` | Liste | Sì |
| `dict` | Dizionari | Sì |
| `set` | Insiemi | Sì |

![Figura 7.4 – Classificazione dei principali tipi di dato sulla base della mutabilità.](images/48_mutabili_immutabili.svg)

*Figura 7.4 – Classificazione dei principali tipi di dato sulla base della mutabilità.*

#### Esempio di oggetto immutabile: un numero intero

```python
numero = 10
numero = numero + 5
```

In questo caso l'oggetto che rappresenta il numero `10` non viene modificato. Viene calcolato il valore `15` e la variabile `numero` viene associata all'oggetto che rappresenta il nuovo valore.

#### Esempio di oggetto mutabile: una lista

```python
numeri = [10, 20, 30]
numeri[0] = 50

print(numeri)
```

**Output:**

```text
[50, 20, 30]
```

In questo caso non viene riassegnata la variabile `numeri`: viene modificato direttamente il contenuto della lista alla quale essa fa riferimento.

### 7.4 Passaggio di un oggetto immutabile a una funzione

Quando viene trasmesso a una funzione un oggetto immutabile, il parametro formale viene inizialmente associato allo stesso oggetto fornito come argomento.

Tuttavia, non essendo possibile modificare direttamente l'oggetto, un'eventuale assegnazione effettuata sul parametro formale comporta una modifica del suo riferimento locale. La variabile del programma chiamante rimane invariata.

#### Esempio: passaggio di un numero intero

```python
def modifica_valore(parametro):
    parametro = 20

    print("Dentro la funzione:", parametro)


def main():
    numero = 10

    print("Prima della chiamata:", numero)

    modifica_valore(numero)

    print("Dopo la chiamata:", numero)


if __name__ == "__main__":
    main()
```

**Output:**

```text
Prima della chiamata: 10
Dentro la funzione: 20
Dopo la chiamata: 10
```

![Figura 7.5 – Effetti della riassegnazione di un parametro associato a un oggetto immutabile.](images/49_parametro_immutabile.svg)

*Figura 7.5 – Effetti della riassegnazione di un parametro associato a un oggetto immutabile.*

#### Come rendere disponibile il nuovo valore al chiamante?

Se desideriamo che il programma chiamante acquisisca il nuovo valore, possiamo utilizzare l'istruzione `return`.

```python
def modifica_valore(parametro):
    parametro = 20
    return parametro


def main():
    numero = 10

    print("Prima della chiamata:", numero)

    numero = modifica_valore(numero)

    print("Dopo la chiamata:", numero)


if __name__ == "__main__":
    main()
```

**Output:**

```text
Prima della chiamata: 10
Dopo la chiamata: 20
```

In questo caso la funzione non modifica direttamente la variabile `numero` del chiamante. È la funzione `main()` che, mediante l'assegnazione `numero = modifica_valore(numero)`, associa la propria variabile al valore restituito.

#### Il comportamento delle stringhe

Anche le stringhe sono oggetti immutabili.

```python
def modifica_testo(testo):
    testo = testo.upper()

    print("Dentro la funzione:", testo)


def main():
    messaggio = "Python"

    modifica_testo(messaggio)

    print("Dopo la chiamata:", messaggio)


if __name__ == "__main__":
    main()
```

**Output:**

```text
Dentro la funzione: PYTHON
Dopo la chiamata: Python
```

Il metodo `upper()` restituisce una stringa in maiuscolo senza modificare quella originale. Anche in questo caso, per utilizzare il nuovo valore all'esterno della funzione, sarebbe possibile ricorrere all'istruzione `return`.

### 7.5 Passaggio di un oggetto mutabile a una funzione

Quando viene trasmesso a una funzione un oggetto mutabile, il parametro formale viene associato allo stesso oggetto fornito come argomento dal programma chiamante.

A differenza degli oggetti immutabili, è però possibile modificare direttamente il contenuto dell'oggetto condiviso. Le modifiche effettuate sull'oggetto all'interno della funzione risultano quindi visibili anche al programma chiamante.

#### Esempio: modifica degli elementi di una lista

```python
def modifica_valori(lista):
    lista[0] = 5
    lista[1] = 10
    lista[2] = 15


def main():
    numeri = [30, 40, 50]

    print("Prima della chiamata:", numeri)

    modifica_valori(numeri)

    print("Dopo la chiamata:", numeri)


if __name__ == "__main__":
    main()
```

**Output:**

```text
Prima della chiamata: [30, 40, 50]
Dopo la chiamata: [5, 10, 15]
```

![Figura 7.6 – Modifica diretta del contenuto di un oggetto mutabile condiviso.](images/50_parametro_mutabile.svg)

*Figura 7.6 – Modifica diretta del contenuto di un oggetto mutabile condiviso.*

In questo esempio la funzione `modifica_valori()` non contiene alcuna istruzione `return`. Nonostante ciò, le modifiche effettuate sulla lista sono visibili anche all'interno della funzione `main()`.

Questo accade perché la funzione non ha modificato il riferimento associato al parametro `lista`, ma ha modificato direttamente il contenuto dell'oggetto condiviso.

#### Esempio: aggiunta di un elemento a una lista

Lo stesso comportamento si verifica utilizzando il metodo `append()`.

```python
def aggiungi_elemento(lista, elemento):
    lista.append(elemento)


def main():
    numeri = [10, 20, 30]

    aggiungi_elemento(numeri, 40)
    aggiungi_elemento(numeri, 50)

    print(numeri)


if __name__ == "__main__":
    main()
```

**Output:**

```text
[10, 20, 30, 40, 50]
```

La lista viene modificata direttamente durante ciascuna chiamata della funzione.

> **OSSERVAZIONE – IL MANTRA DELLE FUNZIONI**
>
> Questi esempi rappresentano una delle eccezioni al mantra introdotto nella Sezione 4.
>
> Una funzione può svolgere correttamente il proprio compito anche senza contenere un `print()` o un `return` esplicito, quando la sua responsabilità consiste nella modifica diretta di un oggetto mutabile.
>
> La funzione restituisce comunque implicitamente `None`.

### 7.6 Riassegnazione di una variabile e modifica di un oggetto

È fondamentale comprendere che il passaggio di un oggetto mutabile a una funzione non implica necessariamente che ogni operazione effettuata sul parametro produca effetti all'esterno della funzione.

Dobbiamo infatti distinguere due operazioni differenti.

| Operazione | Descrizione |
|---|---|
| **Riassegnazione (reassignment)** | Associa una variabile a un altro oggetto. |
| **Modifica dell'oggetto (mutation)** | Modifica il contenuto dell'oggetto esistente, mantenendo il riferimento allo stesso oggetto. |

#### Versione A – Riassegnazione del parametro formale

```python
def modifica_lista(lista):
    lista = [5, 10, 15]


def main():
    numeri = [30, 40, 50]

    modifica_lista(numeri)

    print(numeri)


if __name__ == "__main__":
    main()
```

**Output:**

```text
[30, 40, 50]
```

L'istruzione `lista = [5, 10, 15]` crea una nuova lista e associa a essa il parametro formale `lista`. La variabile `numeri` del chiamante continua invece a fare riferimento alla lista originale.

#### Versione B – Modifica diretta dell'oggetto

```python
def modifica_lista(lista):
    lista[0] = 5
    lista[1] = 10
    lista[2] = 15


def main():
    numeri = [30, 40, 50]

    modifica_lista(numeri)

    print(numeri)


if __name__ == "__main__":
    main()
```

**Output:**

```text
[5, 10, 15]
```

In questo secondo caso non viene creata una nuova lista: vengono modificati gli elementi dell'oggetto condiviso.

![Figura 7.7 – Differenza tra riassegnazione del parametro formale e modifica diretta dell’oggetto.](images/51_riassegnazione_vs_modifica.svg)

*Figura 7.7 – Differenza tra riassegnazione del parametro formale e modifica diretta dell’oggetto.*

#### Confronto tra le principali operazioni

Supponiamo che `lista` sia un parametro formale associato a una lista del programma chiamante.

| Istruzione | Tipo di operazione | Modifica la lista originale? |
|---|---|:---:|
| `lista = [1, 2, 3]` | Riassegnazione | No |
| `lista = lista + [4]` | Creazione di una nuova lista e riassegnazione | No |
| `lista[0] = 10` | Modifica di un elemento | Sì |
| `lista.append(10)` | Aggiunta di un elemento | Sì |
| `lista.remove(10)` | Rimozione di un elemento, se presente | Sì |
| `lista.sort()` | Ordinamento degli elementi | Sì |
| `lista.reverse()` | Inversione dell'ordine degli elementi | Sì |
| `lista.clear()` | Eliminazione di tutti gli elementi | Sì |
| `lista += [4]` | Estensione della lista esistente | Sì |

> **ATTENZIONE**
>
> La mutabilità di un oggetto rende possibile modificarne direttamente il contenuto, ma non significa che qualsiasi operazione effettuata sulla variabile che lo identifica comporti una modifica dell'oggetto stesso.

### 7.7 Come evitare la modifica involontaria di un oggetto mutabile

In alcune situazioni potrebbe essere necessario elaborare una lista all'interno di una funzione senza alterare quella originale.

Consideriamo, ad esempio, una funzione che riceve una lista di numeri e ne restituisce una versione ordinata.

#### Versione A – Ordinamento della lista originale

```python
def ordina_lista(lista):
    lista.sort()
    return lista


def main():
    numeri = [30, 10, 20]

    ordinati = ordina_lista(numeri)

    print("Lista originale:", numeri)
    print("Lista ordinata:", ordinati)


if __name__ == "__main__":
    main()
```

**Output:**

```text
Lista originale: [10, 20, 30]
Lista ordinata: [10, 20, 30]
```

Il metodo `sort()` modifica direttamente l'oggetto ricevuto. Di conseguenza, anche la lista utilizzata dal programma chiamante viene ordinata.

#### Versione B – Creazione di una copia della lista

Per evitare questo comportamento possiamo utilizzare il metodo `copy()`, che permette di creare una copia superficiale (*shallow copy*) di una lista.

```python
def ordina_lista(lista):
    copia_lista = lista.copy()
    copia_lista.sort()

    return copia_lista


def main():
    numeri = [30, 10, 20]

    ordinati = ordina_lista(numeri)

    print("Lista originale:", numeri)
    print("Lista ordinata:", ordinati)


if __name__ == "__main__":
    main()
```

**Output:**

```text
Lista originale: [30, 10, 20]
Lista ordinata: [10, 20, 30]
```

In questo caso la funzione opera su una nuova lista, lasciando invariata quella originale.

![Figura 7.8 – Creazione di una copia della lista per evitare modifiche all’oggetto originale.](images/52_copia_lista.svg)

*Figura 7.8 – Creazione di una copia della lista per evitare modifiche all’oggetto originale.*

Per semplici liste contenenti numeri o stringhe, come quelle utilizzate nei nostri esercizi, il metodo `copy()` è sufficiente allo scopo.

Nel caso di liste contenenti altre liste o altri oggetti mutabili, la copia superficiale presenta ulteriori particolarità che non approfondiremo in questa sede.

#### Una soluzione alternativa: `sorted()`

Python mette inoltre a disposizione la funzione built-in `sorted()`, che restituisce una nuova lista ordinata senza modificare la sequenza originale.

```python
def ordina_lista(lista):
    return sorted(lista)
```

| Metodo o funzione | Modifica la lista originale | Valore restituito |
|---|:---:|---|
| `lista.sort()` | Sì | `None` |
| `lista.copy()` | No | Nuova lista |
| `sorted(lista)` | No | Nuova lista ordinata |

> **BUONA PRATICA DI PROGRAMMAZIONE**
>
> Quando una funzione riceve un oggetto mutabile, è importante stabilire in fase di progettazione se essa debba modificare direttamente l'oggetto originale oppure operare su una sua copia.

### 7.8 Oggetti mutabili e variabili globali

Nella sezione precedente abbiamo visto che, per riassegnare una variabile globale dall'interno di una funzione, è necessario utilizzare la parola chiave `global`.

Tuttavia, quando una variabile globale è associata a un oggetto mutabile, è possibile modificarne il contenuto senza utilizzare tale parola chiave.

```python
numeri = [10, 20, 30]


def aggiungi_numero():
    numeri.append(40)


def main():
    aggiungi_numero()

    print(numeri)


if __name__ == "__main__":
    main()
```

**Output:**

```text
[10, 20, 30, 40]
```

In questo caso non è necessario utilizzare `global numeri`, poiché la funzione accede alla lista globale e ne modifica il contenuto, senza riassegnare la variabile.

Se invece volessimo associare la variabile globale a una nuova lista, sarebbe necessario utilizzare `global`.

```python
def sostituisci_lista():
    global numeri

    numeri = [100, 200, 300]
```

| Operazione all'interno della funzione | Richiede `global`? |
|---|:---:|
| `print(numeri)` | No |
| `numeri[0] = 100` | No |
| `numeri.append(40)` | No |
| `numeri.sort()` | No |
| `numeri = [100, 200, 300]` | Sì, per riassegnare la variabile globale |
| `numeri += [40]` | Sì, poiché è anche un'assegnazione al nome |

Rimane comunque preferibile trasmettere esplicitamente le liste alle funzioni mediante i parametri, anziché utilizzare direttamente variabili globali.

```python
def aggiungi_numero(lista, numero):
    lista.append(numero)


def main():
    numeri = [10, 20, 30]

    aggiungi_numero(numeri, 40)

    print(numeri)


if __name__ == "__main__":
    main()
```

**Output:** `[10, 20, 30, 40]`

Questa implementazione rende la funzione indipendente dal nome della lista utilizzata dal chiamante e maggiormente riutilizzabile.

### 7.9 Schema riepilogativo

#### Oggetti mutabili e immutabili a confronto

| Caratteristica | Oggetti immutabili | Oggetti mutabili |
|---|---|---|
| Esempi | `int`, `float`, `bool`, `str`, `tuple` | `list`, `dict`, `set` |
| Modifica diretta del contenuto | Non possibile | Possibile |
| Condivisione del riferimento durante la chiamata | Sì | Sì |
| Riassegnazione del parametro formale | Non modifica il riferimento del chiamante | Non modifica il riferimento del chiamante |
| Modifica diretta dell'oggetto condiviso | Non possibile | Visibile anche al chiamante |
| Necessità di `return` per trasmettere un nuovo valore al chiamante | Generalmente sì | Dipende dal compito della funzione |

| Concetto | Significato |
|---|---|
| **Oggetto** | Entità attraverso la quale Python rappresenta un dato. |
| **Riferimento** | Associazione tra un identificatore e un oggetto. |
| **Call by sharing** | Meccanismo di passaggio degli argomenti mediante condivisione dei riferimenti agli oggetti. |
| **Mutabilità** | Possibilità di modificare il contenuto di un oggetto dopo la sua creazione. |
| **Immutabilità** | Impossibilità di modificare il valore di un oggetto dopo la sua creazione. |
| **Riassegnazione** | Associazione di una variabile a un altro oggetto. |
| **Mutation** | Modifica diretta del contenuto di un oggetto. |
| **`copy()`** | Metodo che permette di creare una copia superficiale di una lista. |
| **Effetto collaterale (side effect)** | Effetto osservabile prodotto da una funzione oltre al valore di ritorno, ad esempio la modifica di un oggetto condiviso. |

![Figura 7.9 – Schema riepilogativo degli effetti delle operazioni sui parametri formali.](images/53_riepilogo_passaggio_oggetti.svg)

*Figura 7.9 – Schema riepilogativo degli effetti delle operazioni sui parametri formali.*

> **DA RICORDARE**
>
> In Python il meccanismo di passaggio degli argomenti è lo stesso per tutti i tipi di oggetti.
>
> Ciò che cambia è la possibilità di modificare direttamente il contenuto dell'oggetto ricevuto.
>
> Riassegnare un parametro formale non significa modificare la variabile del programma chiamante.

---

## 8. Modalità di passaggio degli argomenti

Nelle sezioni precedenti abbiamo visto come sia possibile trasmettere dati a una funzione attraverso il passaggio degli argomenti.

Python mette a disposizione differenti modalità attraverso le quali associare gli argomenti ai parametri formali di una funzione, rendendone più flessibile l'utilizzo.

In particolare, affronteremo gli argomenti posizionali (*positional arguments*), gli argomenti nominali (*keyword arguments*), i parametri obbligatori, i parametri opzionali e i valori predefiniti (*default values*).

### 8.1 Gli argomenti posizionali (positional arguments)

Il passaggio degli argomenti per posizione rappresenta la modalità più semplice e quella che abbiamo utilizzato prevalentemente negli esempi precedenti.

> **DEFINIZIONE – ARGOMENTI POSIZIONALI**
>
> Gli argomenti posizionali sono argomenti che vengono associati ai parametri formali di una funzione sulla base della posizione che occupano all'interno della chiamata.

#### Esempio: calcolo di una differenza

```python
def differenza(a, b):
    return a - b


def main():
    risultato = differenza(10, 5)
    print("Differenza:", risultato)


if __name__ == "__main__":
    main()
```

**Output:** `Differenza: 5`

Durante la chiamata della funzione il primo argomento, `10`, viene associato al primo parametro formale, `a`; il secondo argomento, `5`, viene associato al secondo parametro formale, `b`.

![Figura 8.1 – Associazione degli argomenti ai parametri formali in base alla posizione.](images/54_argomenti_posizionali.svg)

*Figura 8.1 – Associazione degli argomenti ai parametri formali in base alla posizione.*

Invertendo l'ordine degli argomenti, viene modificata la loro associazione ai parametri formali e, di conseguenza, anche il risultato dell'elaborazione.

| Chiamata | Parametro `a` | Parametro `b` | Risultato |
|---|---:|---:|---:|
| `differenza(10, 5)` | 10 | 5 | 5 |
| `differenza(5, 10)` | 5 | 10 | -5 |
| `differenza(20, 8)` | 20 | 8 | 12 |
| `differenza(8, 20)` | 8 | 20 | -12 |

> **DA RICORDARE**
>
> Nel passaggio degli argomenti per posizione, l'ordine degli argomenti determina la loro associazione ai parametri formali.

### 8.2 Gli argomenti nominali (keyword arguments)

Python consente di specificare esplicitamente, durante la chiamata di una funzione, il nome del parametro formale al quale associare ciascun argomento.

> **DEFINIZIONE – ARGOMENTI NOMINALI**
>
> Gli argomenti nominali, detti anche argomenti con nome, sono argomenti che vengono associati ai parametri formali specificandone direttamente il nome, indipendentemente dalla posizione occupata nella chiamata.

#### Sintassi generale

```python
nome_funzione(parametro_1=valore_1, parametro_2=valore_2)
```

#### Esempio

```python
def differenza(a, b):
    return a - b


def main():
    risultato_1 = differenza(a=10, b=5)
    risultato_2 = differenza(b=5, a=10)

    print("Prima differenza:", risultato_1)
    print("Seconda differenza:", risultato_2)


if __name__ == "__main__":
    main()
```

**Output:**

```text
Prima differenza: 5
Seconda differenza: 5
```

Nonostante sia stato invertito l'ordine degli argomenti, entrambe le chiamate producono lo stesso risultato, poiché l'associazione avviene mediante il nome dei parametri formali.

![Figura 8.2 – Confronto tra associazione per posizione e associazione mediante il nome del parametro.](images/55_argomenti_posizionali_nominali.svg)

*Figura 8.2 – Confronto tra associazione per posizione e associazione mediante il nome del parametro.*

Gli argomenti nominali risultano particolarmente utili quando una funzione dispone di numerosi parametri oppure quando si desidera rendere più comprensibile il significato dei dati trasmessi.

Consideriamo, ad esempio, le seguenti chiamate:

```python
calcola_rettangolo(10, 5)
```

```python
calcola_rettangolo(base=10, altezza=5)
```

La seconda modalità permette di comprendere immediatamente il significato dei due argomenti, senza dover consultare la definizione della funzione.

### 8.3 Utilizzo combinato di argomenti posizionali e nominali

Python permette di utilizzare contemporaneamente argomenti posizionali e nominali all'interno della stessa chiamata.

Per farlo è necessario rispettare due regole fondamentali, nelle normali chiamate trattate in questa lezione:

1. Gli argomenti posizionali devono precedere quelli nominali.
2. Uno stesso parametro non può ricevere più di un argomento.

Consideriamo la seguente funzione:

```python
def calcola_volume(lunghezza, larghezza, altezza):
    return lunghezza * larghezza * altezza
```

| Chiamata | Esito |
|---|---|
| `calcola_volume(10, 5, 3)` | Corretta |
| `calcola_volume(10, 5, altezza=3)` | Corretta |
| `calcola_volume(10, altezza=3, larghezza=5)` | Corretta |
| `calcola_volume(altezza=3, larghezza=5, lunghezza=10)` | Corretta |
| `calcola_volume(lunghezza=10, 5, 3)` | Errata: argomenti posizionali dopo quelli nominali |
| `calcola_volume(10, 5, larghezza=3)` | Errata: due argomenti associati a `larghezza` |

Tutte le chiamate corrette restituiscono il valore `150`.

Nel primo caso errato Python genera un errore di tipo `SyntaxError`, mentre nel secondo caso genera un `TypeError`.

> **ATTENZIONE**
>
> L'utilizzo degli argomenti nominali non richiede alcuna modifica alla definizione della funzione: rappresenta semplicemente una diversa modalità attraverso la quale effettuare la sua chiamata.

### 8.4 Parametri obbligatori e parametri opzionali

Nella definizione di una funzione è possibile specificare dei valori predefiniti da associare ai parametri formali nel caso in cui il programma chiamante non fornisca i corrispondenti argomenti.

| Tipologia | Descrizione |
|---|---|
| **Parametro obbligatorio (required parameter)** | Parametro per il quale è necessario fornire un argomento durante la chiamata della funzione. |
| **Parametro opzionale (optional parameter)** | Parametro al quale viene associato un valore predefinito qualora non venga fornito il corrispondente argomento. |

#### I valori predefiniti (default values)

> **DEFINIZIONE – VALORE DI DEFAULT**
>
> Un valore di default è un valore specificato nella definizione di una funzione, utilizzato automaticamente quando durante la chiamata non viene fornito l'argomento corrispondente.

#### Sintassi generale

```python
def nome_funzione(parametro_1, parametro_2=valore_default):
    istruzioni
    return risultato
```

In questo caso `parametro_1` è un parametro obbligatorio, mentre `parametro_2` è un parametro opzionale, al quale è stato associato un valore di default.

#### Esempio: messaggio di saluto personalizzato

```python
def saluta(nome, messaggio="Ciao"):
    print(f"{messaggio}, {nome}!")


def main():
    saluta("Mario")
    saluta("Giulia", "Buongiorno")
    saluta("Luca", "Buonasera")


if __name__ == "__main__":
    main()
```

**Output:**

```text
Ciao, Mario!
Buongiorno, Giulia!
Buonasera, Luca!
```

| Chiamata | `nome` | `messaggio` |
|---|---|---|
| `saluta("Mario")` | `"Mario"` | `"Ciao"` (default) |
| `saluta("Giulia", "Buongiorno")` | `"Giulia"` | `"Buongiorno"` |
| `saluta("Luca", "Buonasera")` | `"Luca"` | `"Buonasera"` |

Nella prima chiamata il programma fornisce soltanto l'argomento corrispondente al parametro `nome`. Python utilizza quindi automaticamente il valore di default `"Ciao"` per il parametro `messaggio`.

Nelle chiamate successive, invece, il valore di default non viene utilizzato, poiché il programma chiamante fornisce esplicitamente il secondo argomento.

![Figura 8.3 – Utilizzo del valore di default in assenza del corrispondente argomento.](images/56_valori_default.svg)

*Figura 8.3 – Utilizzo del valore di default in assenza del corrispondente argomento.*

#### Parametri opzionali e argomenti nominali

I parametri opzionali possono essere utilizzati anche in combinazione con gli argomenti nominali.

```python
def saluta(nome, messaggio="Ciao"):
    print(f"{messaggio}, {nome}!")
```

| Chiamata | Output |
|---|---|
| `saluta("Mario")` | Ciao, Mario! |
| `saluta(nome="Mario")` | Ciao, Mario! |
| `saluta("Mario", "Buongiorno")` | Buongiorno, Mario! |
| `saluta("Mario", messaggio="Buongiorno")` | Buongiorno, Mario! |
| `saluta(messaggio="Buongiorno", nome="Mario")` | Buongiorno, Mario! |

Tutte queste modalità di chiamata sono sintatticamente corrette.

### 8.5 Regole per la definizione dei parametri opzionali

Nella normale definizione di una funzione, i parametri obbligatori devono precedere quelli opzionali.

#### Definizione corretta

```python
def funzione(a, b=10, c=20):
    return a + b + c
```

In questo caso `a` è un parametro obbligatorio, `b` è un parametro opzionale con valore di default `10` e `c` è un parametro opzionale con valore di default `20`.

#### Definizione errata

```python
def funzione(a=10, b, c=20):
    return a + b + c
```

Python genera un errore di tipo `SyntaxError`, poiché il parametro obbligatorio `b` è stato collocato dopo un parametro opzionale.

![Figura 8.4 – Ordine dei parametri obbligatori e opzionali nella definizione di una funzione.](images/57_ordine_parametri.svg)

*Figura 8.4 – Ordine dei parametri obbligatori e opzionali nella definizione di una funzione.*

#### Omissione selettiva dei parametri opzionali

Consideriamo nuovamente la funzione:

```python
def funzione(a, b=10, c=20):
    return a + b + c
```

| Chiamata | `a` | `b` | `c` | Risultato |
|---|---:|---:|---:|---:|
| `funzione(5)` | 5 | 10 | 20 | 35 |
| `funzione(5, 8)` | 5 | 8 | 20 | 33 |
| `funzione(5, 8, 12)` | 5 | 8 | 12 | 25 |
| `funzione(5, c=30)` | 5 | 10 | 30 | 45 |
| `funzione(a=5, c=30)` | 5 | 10 | 30 | 45 |
| `funzione(5, b=15)` | 5 | 15 | 20 | 40 |

L'utilizzo degli argomenti nominali permette quindi di specificare soltanto alcuni parametri opzionali, lasciando che gli altri assumano il rispettivo valore di default. Non è invece possibile omettere il parametro obbligatorio `a`.

> **BUONA PRATICA DI PROGRAMMAZIONE**
>
> Per i nostri esercizi utilizzeremo come valori di default principalmente numeri, stringhe e valori booleani.
>
> È opportuno evitare l'utilizzo diretto di oggetti mutabili, come le liste, quali valori di default, poiché lo stesso oggetto potrebbe essere condiviso tra chiamate successive della funzione, producendo risultati inattesi.

### 8.6 Esempio applicativo: calcolo dell'area mediante parametri opzionali

Supponiamo di voler realizzare una funzione che permetta di calcolare l'area di tre differenti figure geometriche: quadrato, triangolo e trapezio.

Possiamo utilizzare una funzione dotata di tre parametri formali, due dei quali opzionali.

#### Progettazione della funzione

```text
def area(a, b=0, c=0):
```

| Argomenti forniti (nell'ordine previsto) | Figura geometrica | Significato dei parametri |
|---|---|---|
| Uno | Quadrato | `a`: lato |
| Due | Triangolo | `a`: base, `b`: altezza |
| Tre | Trapezio | `a`, `b`: basi, `c`: altezza |

#### Formule utilizzate

- Quadrato: A = a²
- Triangolo: A = (a × b) / 2
- Trapezio: A = ((a + b) × c) / 2

![Figura 8.5 – Figure geometriche e significato dei parametri per il calcolo delle rispettive aree.](images/58_figure_geometriche.svg)

*Figura 8.5 – Figure geometriche e significato dei parametri per il calcolo delle rispettive aree.*

#### Implementazione del programma

```python
def area(a, b=0, c=0):
    if b == 0 and c == 0:
        # Calcolo dell'area del quadrato
        risultato = a ** 2

    elif c == 0:
        # Calcolo dell'area del triangolo
        risultato = (a * b) / 2

    else:
        # Calcolo dell'area del trapezio
        risultato = ((a + b) * c) / 2

    return risultato


def main():
    print("Area del quadrato:", area(5))
    print("Area del triangolo:", area(5, 6))
    print("Area del trapezio:", area(5, 6, 7))


if __name__ == "__main__":
    main()
```

**Output:**

```text
Area del quadrato: 25
Area del triangolo: 15.0
Area del trapezio: 38.5
```

| Chiamata | `a` | `b` | `c` | Elaborazione |
|---|---:|---:|---:|---|
| `area(5)` | 5 | 0 (default) | 0 (default) | Quadrato |
| `area(5, 6)` | 5 | 6 | 0 (default) | Triangolo |
| `area(5, 6, 7)` | 5 | 6 | 7 | Trapezio |

![Figura 8.6 – Flow chart della funzione per il calcolo dell’area mediante parametri opzionali.](images/59_area_parametri_opzionali.svg)

*Figura 8.6 – Flow chart della funzione per il calcolo dell’area mediante parametri opzionali.*

La funzione utilizza i valori di default per determinare quale elaborazione effettuare e restituisce il risultato attraverso un'unica istruzione `return`.

> **OSSERVAZIONE**
>
> Questo esempio presuppone che le dimensioni delle figure geometriche fornite come argomenti siano sempre maggiori di zero e che vengano trasmesse nell'ordine previsto.
>
> Il valore `0` viene infatti utilizzato come valore convenzionale per distinguere i differenti casi di elaborazione.

L'esempio dimostra come i parametri opzionali possano modificare non soltanto i valori utilizzati durante un'elaborazione, ma anche il percorso di esecuzione delle istruzioni contenute nella funzione.

In un programma più articolato potrebbe comunque risultare preferibile definire tre funzioni distinte, ciascuna responsabile del calcolo dell'area di una specifica figura geometrica.

### 8.7 Errori comuni nel passaggio degli argomenti

Consideriamo la seguente funzione di riferimento:

```python
def funzione(a, b=10, c=20):
    return a + b + c
```

| Chiamata errata | Tipo di errore | Motivazione |
|---|---|---|
| `funzione()` | `TypeError` | Manca il parametro obbligatorio `a`. |
| `funzione(1, 2, 3, 4)` | `TypeError` | Sono stati forniti troppi argomenti. |
| `funzione(a=5, 10)` | `SyntaxError` | Un argomento posizionale segue un argomento nominale. |
| `funzione(5, a=10)` | `TypeError` | Al parametro `a` vengono associati due argomenti. |
| `funzione(5, d=10)` | `TypeError` | Il parametro `d` non esiste nella definizione della funzione. |

#### Un errore da evitare: confondere parametri opzionali e argomenti nominali

Le seguenti istruzioni utilizzano una sintassi apparentemente simile, ma svolgono compiti differenti.

**Nella definizione:**

```python
def funzione(a, b=10):
    return a + b
```

L'espressione `b=10` stabilisce il valore di default del parametro `b`.

**Nella chiamata:**

```python
risultato = funzione(5, b=15)
```

L'espressione `b=15` associa esplicitamente l'argomento `15` al parametro formale `b`. In questo caso il valore restituito sarà `20`.

> **DA RICORDARE**
>
> Un parametro opzionale riguarda la **definizione** di una funzione.
>
> Un argomento nominale riguarda la **chiamata** di una funzione.
>
> Si tratta di due concetti distinti, anche se possono essere utilizzati contemporaneamente.

### 8.8 Schema riepilogativo

| Concetto | Significato | Esempio |
|---|---|---|
| **Argomento posizionale** | Associato al parametro in base alla posizione. | `funzione(5, 10)` |
| **Argomento nominale** | Associato al parametro mediante il suo nome. | `funzione(a=5, b=10)` |
| **Parametro obbligatorio** | Richiede necessariamente un argomento. | `def funzione(a):` |
| **Parametro opzionale** | Può essere utilizzato senza fornire il corrispondente argomento. | `def funzione(a=10):` |
| **Valore di default** | Valore utilizzato in assenza del corrispondente argomento. | `a=10` nella definizione |
| **Chiamata mista** | Utilizzo combinato di argomenti posizionali e nominali. | `funzione(5, b=10)` |

#### Regole fondamentali (per le forme di definizione e chiamata studiate)

| Durante la definizione | Durante la chiamata |
|---|---|
| I parametri obbligatori precedono quelli opzionali. | Gli argomenti posizionali precedono quelli nominali. |
| I parametri opzionali dispongono di un valore di default. | Tutti i parametri obbligatori devono ricevere un argomento. |
| I parametri devono avere nomi distinti. | Uno stesso parametro non può ricevere più argomenti. |

---

## 9. Organizzazione di un programma mediante funzioni

Dopo aver analizzato la sintassi, le caratteristiche e le modalità di utilizzo delle funzioni in Python, possiamo applicare i concetti appresi alla progettazione e alla realizzazione di programmi completi.

L'obiettivo della programmazione modulare non consiste semplicemente nel suddividere il codice in più funzioni, ma nell'organizzare il programma in componenti, ciascuno dei quali possiede una responsabilità specifica.

### 9.1 La progettazione di un programma modulare

La progettazione di un programma mediante funzioni può essere suddivisa nelle seguenti fasi.

| Fase | Descrizione |
|---|---|
| **1. Analisi del problema** | Individuare i dati in ingresso, le elaborazioni richieste e i risultati attesi. |
| **2. Scomposizione del problema** | Suddividere il problema complessivo in sottoproblemi più semplici. |
| **3. Progettazione delle funzioni** | Individuare il compito, i parametri e gli eventuali valori di ritorno di ciascuna funzione. |
| **4. Implementazione** | Scrivere il codice delle singole funzioni. |
| **5. Integrazione** | Coordinare l'esecuzione delle funzioni mediante la funzione principale `main()`. |
| **6. Testing e debugging** | Verificare il funzionamento delle singole funzioni e del programma complessivo, individuando e correggendo eventuali errori. |

![Figura 9.1 – Principali fasi di progettazione e sviluppo. Le fasi possono essere ripetute per migliorare il programma.](images/60_progettazione_programma_modulare.svg)

*Figura 9.1 – Principali fasi di progettazione e sviluppo. Le fasi possono essere ripetute per migliorare il programma.*

È importante osservare che la progettazione delle funzioni dovrebbe precedere la scrittura del codice.

Prima di implementare una funzione, è opportuno stabilire quale compito deve svolgere, quali dati deve ricevere, quali elaborazioni deve effettuare e quale risultato deve eventualmente restituire.

In questo modo sarà possibile definire l'interfaccia della funzione secondo il modello **black box** introdotto nella Sezione 3.

> **BUONA PRATICA DI PROGRAMMAZIONE**
>
> Prima di scrivere il codice di una funzione, individua il suo compito, i suoi eventuali parametri e il suo eventuale valore di ritorno.

### 9.2 Separazione delle responsabilità

Nella progettazione dei programmi abbiamo già individuato una sequenza di operazioni fondamentali: richiesta, inserimento, validazione, elaborazione, visualizzazione.

![Figura 9.2 – Associazione delle fasi operative del programma alle rispettive funzioni.](images/61_separazione_responsabilita.svg)

*Figura 9.2 – Associazione delle fasi operative del programma alle rispettive funzioni.*

Attraverso la programmazione modulare possiamo affidare queste operazioni a funzioni differenti.

| Responsabilità | Strumenti principalmente utilizzati |
|---|---|
| Richiesta e acquisizione | `input()`, conversioni dei tipi di dato |
| Validazione | `if`, `while`, `try-except-else` |
| Elaborazione | Parametri, operatori, strutture di controllo, `return` |
| Visualizzazione | Parametri, `print()` |
| Coordinamento | `main()`, chiamate alle altre funzioni |

Questa organizzazione rispecchia il **principio di separazione delle responsabilità (Separation of Concerns)**, secondo il quale è opportuno affidare compiti differenti a componenti distinti del programma.

Una funzione può comunque raggruppare operazioni strettamente correlate, come l'acquisizione e la validazione di un dato.

La funzione `main()` assume il ruolo di coordinamento, occupandosi principalmente di stabilire l'ordine di esecuzione delle diverse operazioni e di gestire lo scambio dei dati tra le funzioni.

### 9.3 Esempio applicativo 1 – Calcolo dell'area e del perimetro di un cerchio

#### Analisi del problema

Si desidera realizzare un programma Python che acquisisca il raggio di un cerchio, verificando che sia un numero positivo, e ne calcoli e visualizzi l'area e il perimetro.

Le formule matematiche necessarie sono:

- **Perimetro (lunghezza della circonferenza):** P = 2 × π × r
- **Area:** A = π × r²

![Figura 9.3 – Rappresentazione geometrica del cerchio e formule utilizzate.](images/62_geometria_cerchio.svg)

*Figura 9.3 – Rappresentazione geometrica del cerchio e formule utilizzate.*

#### Scomposizione del problema e progettazione delle funzioni

Possiamo suddividere il problema in quattro sottoproblemi fondamentali.

| Funzione | Compito | Parametri | Valore restituito | Tipologia |
|---|---|---|---|:---:|
| `leggi_raggio()` | Acquisire e validare il raggio | Nessuno | Raggio | 3 |
| `calcola_perimetro()` | Calcolare il perimetro | `raggio` | Perimetro | 4 |
| `calcola_area()` | Calcolare l'area | `raggio` | Area | 4 |
| `stampa_risultati()` | Visualizzare i risultati | `raggio`, `perimetro`, `area` | `None` | 2 |

La funzione principale `main()` avrà il compito di coordinare l'esecuzione delle quattro funzioni.

![Figura 9.4 – Sequenza delle chiamate e dei valori restituiti nel programma di calcolo dell’area e del perimetro del cerchio.](images/63_programma_cerchio.svg)

*Figura 9.4 – Sequenza delle chiamate e dei valori restituiti nel programma di calcolo dell’area e del perimetro del cerchio.*

#### Implementazione del programma

```python
import math


# Acquisizione e validazione del raggio
def leggi_raggio():
    dato_valido = False

    while not dato_valido:
        try:
            raggio = float(input("Inserisci il raggio del cerchio: "))
        except ValueError:
            print("Errore: inserire un valore numerico.")
        else:
            if math.isfinite(raggio) and raggio > 0:
                dato_valido = True
            else:
                print("Errore: inserire un numero positivo e finito.")

    return raggio


# Calcolo del perimetro
def calcola_perimetro(raggio):
    return 2 * math.pi * raggio


# Calcolo dell'area
def calcola_area(raggio):
    return math.pi * raggio ** 2


# Visualizzazione dei risultati
def stampa_risultati(raggio, perimetro, area):
    print("\n--- RISULTATI ---")
    print(f"Raggio: {raggio:.2f}")
    print(f"Perimetro: {perimetro:.2f}")
    print(f"Area: {area:.2f}")


# Funzione principale
def main():
    raggio = leggi_raggio()

    perimetro = calcola_perimetro(raggio)
    area = calcola_area(raggio)

    stampa_risultati(raggio, perimetro, area)


# Punto di ingresso condizionale
if __name__ == "__main__":
    main()
```

#### Esempio di esecuzione

```text
Inserisci il raggio del cerchio: abc
Errore: inserire un valore numerico.
Inserisci il raggio del cerchio: -3
Errore: inserire un numero positivo e finito.
Inserisci il raggio del cerchio: 0
Errore: inserire un numero positivo e finito.
Inserisci il raggio del cerchio: 5

--- RISULTATI ---
Raggio: 5.00
Perimetro: 31.42
Area: 78.54
```

#### Analisi del funzionamento

La funzione `leggi_raggio()` si occupa interamente dell'acquisizione e della validazione del dato.

In particolare:

- il blocco `try-except-else` gestisce gli errori di conversione;
- il ciclo `while` permette di ripetere l'inserimento finché il dato non risulta valido;
- la funzione `math.isfinite()` verifica che il numero non rappresenti un valore infinito o non numerico (`NaN`);
- l'istruzione `return` restituisce il raggio validato.

Le funzioni `calcola_perimetro()` e `calcola_area()` ricevono il raggio come parametro e restituiscono i rispettivi risultati. La costante `math.pi` rappresenta un'approssimazione del valore matematico di π. L'esempio presuppone dimensioni ordinarie, tali da non superare i limiti di rappresentazione dei numeri `float` durante i calcoli.

La funzione `stampa_risultati()` riceve tutti i dati necessari e si occupa esclusivamente della loro visualizzazione.

La notazione `:.2f`, utilizzata all'interno delle f-string, permette di visualizzare un numero in virgola mobile con due cifre decimali, senza modificare il valore originale della variabile.

#### Il ruolo della funzione `main()`

Concentrandoci esclusivamente sulla funzione principale:

```python
def main():
    raggio = leggi_raggio()

    perimetro = calcola_perimetro(raggio)
    area = calcola_area(raggio)

    stampa_risultati(raggio, perimetro, area)
```

possiamo osservare come essa descriva sinteticamente l'intero funzionamento del programma.

Non è necessario analizzare il corpo delle singole funzioni per comprendere la sequenza delle operazioni effettuate. Questo costituisce uno dei principali vantaggi della programmazione modulare.

> **OSSERVAZIONE**
>
> La funzione `main()` non contiene direttamente né un `print()` né un `return` esplicito, poiché il suo compito consiste nel coordinare l'esecuzione delle altre funzioni.
>
> Rappresenta quindi un'altra delle eccezioni al mantra introdotto nella Sezione 4.

### 9.4 Esempio applicativo 2 – Analisi di una lista di valori numerici

#### Analisi del problema

Si desidera realizzare un programma Python che permetta all'utente di inserire una serie di numeri interi, memorizzandoli all'interno di una lista.

Il programma dovrà successivamente determinare:

- la somma dei valori;
- il valore minimo;
- il valore massimo;
- la media aritmetica;
- il numero di valori pari;
- il numero di valori dispari.

Il programma dovrà inoltre gestire la validazione dei dati inseriti dall'utente.

#### Scomposizione del problema e progettazione delle funzioni

| Funzione | Compito | Parametri | Valore restituito | Tipologia |
|---|---|---|---|:---:|
| `leggi_quantita()` | Acquisire il numero di elementi della lista | Nessuno | Quantità | 3 |
| `leggi_numeri()` | Acquisire e validare i numeri | `quantita` | Lista di numeri | 4 |
| `calcola_statistiche()` | Calcolare somma, minimo, massimo e media | `numeri` | Tupla di quattro valori | 4 |
| `conta_pari_dispari()` | Contare i numeri pari e dispari | `numeri` | Tupla di due valori | 4 |
| `stampa_risultati()` | Visualizzare i risultati | Lista e risultati | `None` | 2 |

![Figura 9.5 – Scomposizione funzionale e flusso dei dati del programma di analisi di una lista numerica. Le elaborazioni sono chiamate sequenzialmente da main().](images/64_programma_analisi_lista.svg)

*Figura 9.5 – Scomposizione funzionale e flusso dei dati del programma di analisi di una lista numerica. Le elaborazioni sono chiamate sequenzialmente da main().*

#### Implementazione del programma

```python
# Acquisizione e validazione della quantità
def leggi_quantita():
    dato_valido = False

    while not dato_valido:
        try:
            quantita = int(input("Quanti numeri vuoi inserire? "))
        except ValueError:
            print("Errore: inserire un numero intero.")
        else:
            if quantita > 0:
                dato_valido = True
            else:
                print("Errore: la quantità deve essere positiva.")

    return quantita


# Acquisizione e validazione dei numeri
def leggi_numeri(quantita):
    numeri = []

    for i in range(quantita):
        dato_valido = False

        while not dato_valido:
            try:
                numero = int(input(f"Inserisci il numero {i + 1}: "))
            except ValueError:
                print("Errore: inserire un numero intero.")
            else:
                dato_valido = True

        numeri.append(numero)

    return numeri


# Elaborazione delle statistiche
def calcola_statistiche(numeri):
    somma = sum(numeri)
    minimo = min(numeri)
    massimo = max(numeri)
    media = somma / len(numeri)

    return somma, minimo, massimo, media


# Conteggio dei numeri pari e dispari
def conta_pari_dispari(numeri):
    pari = 0
    dispari = 0

    for numero in numeri:
        if numero % 2 == 0:
            pari += 1
        else:
            dispari += 1

    return pari, dispari


# Visualizzazione dei risultati
def stampa_risultati(numeri, somma, minimo, massimo, media, pari, dispari):
    print("\n--- RISULTATI ---")
    print("Lista dei numeri:", numeri)
    print("Somma:", somma)
    print("Valore minimo:", minimo)
    print("Valore massimo:", massimo)
    print(f"Media: {media:.2f}")
    print("Numeri pari:", pari)
    print("Numeri dispari:", dispari)


# Funzione principale
def main():
    quantita = leggi_quantita()
    numeri = leggi_numeri(quantita)

    somma, minimo, massimo, media = calcola_statistiche(numeri)
    pari, dispari = conta_pari_dispari(numeri)

    stampa_risultati(numeri, somma, minimo, massimo, media, pari, dispari)


# Punto di ingresso condizionale
if __name__ == "__main__":
    main()
```

#### Esempio di esecuzione

```text
Quanti numeri vuoi inserire? 0
Errore: la quantità deve essere positiva.
Quanti numeri vuoi inserire? 5
Inserisci il numero 1: 10
Inserisci il numero 2: 5
Inserisci il numero 3: abc
Errore: inserire un numero intero.
Inserisci il numero 3: 8
Inserisci il numero 4: 3
Inserisci il numero 5: 14

--- RISULTATI ---
Lista dei numeri: [10, 5, 8, 3, 14]
Somma: 40
Valore minimo: 3
Valore massimo: 14
Media: 8.00
Numeri pari: 3
Numeri dispari: 2
```

#### Analisi delle principali funzioni

**La funzione `leggi_quantita()`**

Acquisisce e valida un numero intero positivo che rappresenta la quantità di elementi da inserire nella lista.

Garantire che la quantità sia maggiore di zero permette di evitare la creazione di una lista vuota e i conseguenti errori durante il calcolo del minimo, del massimo e della media.

**La funzione `leggi_numeri(quantita)`**

Utilizza un ciclo `for` per acquisire il numero di elementi richiesto e un ciclo `while`, associato al blocco `try-except-else`, per validare ciascun inserimento.

Ogni numero valido viene aggiunto alla lista mediante il metodo `append()`. Al termine dell'elaborazione viene restituita l'intera lista.

**La funzione `calcola_statistiche(numeri)`**

Utilizza quattro funzioni built-in già disponibili in Python:

| Funzione | Compito |
|---|---|
| `sum()` | Calcolare la somma degli elementi |
| `min()` | Individuare l'elemento di valore minimo |
| `max()` | Individuare l'elemento di valore massimo |
| `len()` | Determinare il numero di elementi |

I quattro risultati vengono restituiti mediante una tupla:

```python
return somma, minimo, massimo, media
```

La funzione presuppone che la lista ricevuta contenga almeno un elemento, condizione garantita dalla precedente validazione della quantità.

**La funzione `conta_pari_dispari(numeri)`**

Utilizza un ciclo `for` per analizzare gli elementi della lista e una struttura di selezione per stabilire se ciascun numero sia pari oppure dispari. Restituisce entrambi i contatori mediante una singola istruzione `return`.

#### Scambio dei dati e restituzione multipla

![Figura 9.6 – Passaggio di una lista a una funzione, restituzione multipla e unpacking della tupla.](images/65_analisi_lista_return.svg)

*Figura 9.6 – Passaggio di una lista a una funzione, restituzione multipla e unpacking della tupla.*

È importante osservare che, nonostante la lista sia un oggetto mutabile, le funzioni `calcola_statistiche()` e `conta_pari_dispari()` non ne modificano il contenuto.

Entrambe utilizzano la lista esclusivamente come sorgente dei dati da elaborare.

Il programma rappresenta quindi un'applicazione congiunta di numerosi concetti affrontati durante lo studio del linguaggio Python.

| Concetto | Applicazione nel programma |
|---|---|
| Selezione | Verifica della validità dei dati e della parità |
| Iterazione indefinita | Validazione mediante `while` |
| Iterazione definita | Acquisizione ed elaborazione mediante `for` |
| Gestione delle eccezioni | Utilizzo di `try-except-else` |
| Liste | Memorizzazione dei dati |
| Funzioni built-in | Elaborazione delle statistiche |
| Parametri | Trasmissione dei dati alle funzioni |
| `return` | Restituzione dei risultati |
| Tuple e unpacking | Restituzione e acquisizione multipla dei valori |
| Variabili locali | Indipendenza delle singole funzioni |
| Programmazione modulare | Separazione delle responsabilità |
| Punto di ingresso condizionale | Avvio della funzione `main()` |

### 9.5 Testing delle singole funzioni

Un importante vantaggio della programmazione modulare consiste nella possibilità di verificare il corretto funzionamento di una funzione indipendentemente dal resto del programma.

Consideriamo la funzione:

```python
def conta_pari_dispari(numeri):
    pari = 0
    dispari = 0

    for numero in numeri:
        if numero % 2 == 0:
            pari += 1
        else:
            dispari += 1

    return pari, dispari
```

Possiamo predisporre differenti casi di test, associando a ciascun insieme di dati in ingresso il risultato atteso.

| Dati in ingresso | Risultato atteso | Caso verificato |
|---|---|---|
| `[2, 4, 6]` | `(3, 0)` | Soltanto numeri pari |
| `[1, 3, 5]` | `(0, 3)` | Soltanto numeri dispari |
| `[1, 2, 3, 4]` | `(2, 2)` | Numeri pari e dispari |
| `[0]` | `(1, 0)` | Presenza dello zero |
| `[-3, -2]` | `(1, 1)` | Numeri negativi |
| `[]` | `(0, 0)` | Lista vuota |

Per effettuare una semplice verifica possiamo richiamare direttamente la funzione con i differenti argomenti.

```python
print(conta_pari_dispari([2, 4, 6]))
print(conta_pari_dispari([1, 3, 5]))
print(conta_pari_dispari([1, 2, 3, 4]))
print(conta_pari_dispari([0]))
print(conta_pari_dispari([-3, -2]))
print(conta_pari_dispari([]))
```

**Output:**

```text
(3, 0)
(0, 3)
(2, 2)
(1, 0)
(1, 1)
(0, 0)
```

Il confronto tra i risultati ottenuti e quelli attesi permette di verificare il comportamento della funzione nei casi considerati.

Non è quindi necessario eseguire ogni volta l'intero programma e inserire manualmente tutti i dati.

Questo approccio prende il nome di **testing delle singole unità funzionali (unit testing)**. Negli esempi proposti stiamo effettuando una verifica manuale; esistono anche strumenti che consentono di automatizzare tale procedimento.

### 9.6 Buone pratiche nella progettazione delle funzioni

| Buona pratica | Motivazione |
|---|---|
| Utilizzare nomi significativi e la convenzione `snake_case` | Migliorare la leggibilità del codice. |
| Assegnare un compito specifico a ciascuna funzione | Favorire modularità e manutenibilità. |
| Definire l'interfaccia prima dell'implementazione | Stabilire chiaramente i dati richiesti e i risultati attesi. |
| Utilizzare i parametri per trasmettere i dati | Ridurre le dipendenze tra le funzioni. |
| Utilizzare `return` nelle funzioni di elaborazione | Rendere i risultati riutilizzabili. |
| Separare acquisizione, elaborazione e visualizzazione | Favorire il riutilizzo del codice. |
| Privilegiare le variabili locali | Ridurre il rischio di modifiche indesiderate. |
| Limitare l'utilizzo delle variabili globali | Rendere il comportamento delle funzioni più prevedibile. |
| Evitare modifiche involontarie degli oggetti mutabili | Preservare i dati originali quando necessario. |
| Utilizzare `main()` | Coordinare le operazioni del programma. |
| Utilizzare il punto di ingresso condizionale | Favorire il riutilizzo delle funzioni attraverso i moduli. |
| Verificare separatamente il comportamento delle funzioni | Facilitare il testing e il debugging. |

### 9.7 Modello generale di riferimento

Il seguente modello rappresenta una possibile struttura di riferimento per la progettazione dei programmi Python che realizzeremo utilizzando le funzioni.

```python
# IMPORTAZIONE DEI MODULI
# Eventuali import


# DEFINIZIONE DELLE COSTANTI GLOBALI
# Eventuali costanti


# ACQUISIZIONE E VALIDAZIONE
def leggi_dati():
    ...
    return dati


# ELABORAZIONE
def elabora_dati(dati):
    ...
    return risultato


# VISUALIZZAZIONE
def stampa_risultati(risultato):
    print(risultato)


# FUNZIONE PRINCIPALE
def main():
    dati = leggi_dati()

    risultato = elabora_dati(dati)

    stampa_risultati(risultato)


# PUNTO DI INGRESSO CONDIZIONALE
if __name__ == "__main__":
    main()
```

Questo listato costituisce un modello concettuale, non un programma completo già funzionante: i simboli `...` rappresentano le istruzioni da implementare in relazione al problema da risolvere.

Naturalmente, a seconda della complessità del problema, potranno essere necessarie più funzioni di acquisizione, elaborazione o visualizzazione.

> **DA RICORDARE**
>
> Un programma modulare ben progettato non è semplicemente un programma contenente molte funzioni.
>
> È un programma nel quale ogni funzione possiede una responsabilità ben definita, i dati vengono scambiati in modo consapevole e la funzione principale coordina le operazioni necessarie alla risoluzione del problema.

---

## 10. Cenni alle funzioni ricorsive

### 10.1 Il concetto di ricorsione

Nelle sezioni precedenti abbiamo visto come una funzione possa richiamare altre funzioni durante la propria esecuzione.

In Python è inoltre possibile definire una funzione che richiami sé stessa. Questo particolare meccanismo prende il nome di **ricorsione**.

> **DEFINIZIONE – FUNZIONE RICORSIVA (RECURSIVE FUNCTION)**
>
> Una funzione ricorsiva è una funzione che, durante la propria esecuzione, richiama sé stessa allo scopo di risolvere un problema attraverso la sua scomposizione in problemi più semplici della stessa natura.

![Figura 10.1 – Confronto tra una normale chiamata di funzione e una chiamata ricorsiva.](images/66_chiamata_ricorsiva.svg)

*Figura 10.1 – Confronto tra una normale chiamata di funzione e una chiamata ricorsiva.*

La ricorsione costituisce una tecnica alternativa all'iterazione per la risoluzione di alcuni problemi che prevedono la ripetizione di determinate operazioni.

### 10.2 Caso base e passo ricorsivo

Affinché una funzione ricorsiva possa terminare correttamente, è necessario individuare due elementi fondamentali.

| Elemento | Descrizione |
|---|---|
| **Caso base (base case)** | Condizione nella quale la funzione può fornire direttamente il risultato, senza richiamare nuovamente sé stessa. |
| **Passo ricorsivo (recursive step)** | Operazione mediante la quale la funzione richiama sé stessa, affrontando una versione più semplice del problema. |

Ogni chiamata ricorsiva deve contribuire ad avvicinare il problema al caso base, garantendo così la terminazione logica della funzione per gli argomenti previsti, entro i limiti di esecuzione.

![Figura 10.2 – Struttura concettuale di una funzione ricorsiva che restituisce un risultato.](images/67_struttura_ricorsione.svg)

*Figura 10.2 – Struttura concettuale di una funzione ricorsiva che restituisce un risultato.*

> **ATTENZIONE**
>
> Una funzione ricorsiva priva di un caso base raggiungibile potrebbe continuare a richiamare sé stessa senza terminare normalmente.
>
> Python impone un limite alla profondità delle chiamate ricorsive e, quando tale limite viene superato, genera un errore di tipo `RecursionError`.

### 10.3 Esempio: calcolo del fattoriale di un numero

Un semplice esempio di applicazione della ricorsione è rappresentato dal calcolo del **fattoriale** di un numero intero non negativo.

Il fattoriale di un numero positivo n, indicato mediante il simbolo n!, è il prodotto di tutti i numeri interi positivi da 1 a n.

Ad esempio: **5! = 5 × 4 × 3 × 2 × 1 = 120**.

Per definizione: **0! = 1**.

Il fattoriale può essere espresso anche attraverso una definizione ricorsiva:

- n! = 1, se n = 0;
- n! = n × (n − 1)!, se n > 0.

Possiamo quindi individuare:

| Elemento | Applicazione al fattoriale |
|---|---|
| Caso base | 0! = 1 |
| Passo ricorsivo | n! = n × (n − 1)! |
| Avvicinamento al caso base | Diminuzione di `n` di un'unità a ogni chiamata |

#### Implementazione mediante una funzione ricorsiva

```python
def fattoriale(n):
    if n == 0:
        return 1
    else:
        return n * fattoriale(n - 1)


def main():
    risultato = fattoriale(5)

    print("Il fattoriale è:", risultato)


if __name__ == "__main__":
    main()
```

**Output:**

```text
Il fattoriale è: 120
```

La funzione presuppone che l'argomento ricevuto sia un numero intero maggiore o uguale a zero.

L'istruzione:

```python
return n * fattoriale(n - 1)
```

richiede una nuova esecuzione della stessa funzione, utilizzando come argomento il valore `n - 1`.

#### Rappresentazione semplificata del funzionamento

Consideriamo il calcolo del fattoriale di 3.

![Figura 10.3 – Rappresentazione semplificata delle chiamate ricorsive e della restituzione dei risultati nel fattoriale di 3.](images/68_fattoriale_ricorsivo.svg)

*Figura 10.3 – Rappresentazione semplificata delle chiamate ricorsive e della restituzione dei risultati nel fattoriale di 3.*

Le chiamate ricorsive proseguono fino al raggiungimento del caso base. A partire da quest'ultimo, le funzioni restituiscono progressivamente i risultati necessari al completamento delle elaborazioni precedenti.

### 10.4 Iterazione e ricorsione a confronto

Alcuni problemi possono essere risolti sia attraverso le strutture iterative sia attraverso le funzioni ricorsive.

Il calcolo del fattoriale, ad esempio, può essere implementato utilizzando un normale ciclo `for`.

#### Versione iterativa

```python
def fattoriale(n):
    risultato = 1

    for i in range(1, n + 1):
        risultato = risultato * i

    return risultato
```

#### Versione ricorsiva

```python
def fattoriale(n):
    if n == 0:
        return 1
    else:
        return n * fattoriale(n - 1)
```

Entrambe le funzioni, per argomenti interi non negativi entro i limiti di esecuzione, permettono di ottenere lo stesso risultato matematico.

| Caratteristica | Iterazione | Ricorsione |
|---|---|---|
| Meccanismo di ripetizione | Cicli `while` o `for` | Chiamate successive della stessa funzione |
| Terminazione | Condizione del ciclo o esaurimento degli elementi da iterare | Raggiungimento del caso base |
| Elaborazione | Ripetizione di un blocco di istruzioni | Scomposizione in problemi più semplici della stessa natura |
| Strumenti principali | Cicli e variabili | Funzioni, condizioni e `return` |
| Errore di progettazione possibile | Ciclo infinito | Superamento del limite di ricorsione |

La ricorsione può rappresentare una soluzione particolarmente elegante per alcuni problemi, ma richiede una corretta progettazione delle condizioni di terminazione.

Per i problemi affrontati durante il nostro corso continueremo a privilegiare le strutture iterative, già note e consolidate.

### 10.5 Schema riepilogativo

| Concetto | Significato |
|---|---|
| **Ricorsione** | Meccanismo mediante il quale una funzione richiama sé stessa. |
| **Funzione ricorsiva** | Funzione che utilizza la ricorsione. |
| **Caso base** | Condizione che permette di terminare la ricorsione senza ulteriori chiamate. |
| **Passo ricorsivo** | Chiamata della funzione a sé stessa con un problema più semplice. |
| **Progressione verso il caso base** | Riduzione progressiva del problema fino al raggiungimento della condizione di terminazione. |
| **`RecursionError`** | Errore generato quando viene superato il limite di profondità delle chiamate ricorsive. |

> **DA RICORDARE**
>
> Una funzione ricorsiva richiama sé stessa.
>
> Deve prevedere almeno un caso base raggiungibile e le chiamate ricorsive devono avvicinarsi progressivamente a tale caso.
>
> La ricorsione costituisce una tecnica alternativa all'iterazione per la risoluzione di determinati problemi.
