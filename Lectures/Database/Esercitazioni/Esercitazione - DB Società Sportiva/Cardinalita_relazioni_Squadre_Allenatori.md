# Le cardinalità delle relazioni: il caso SQUADRE–ALLENATORI

## 1. Introduzione al problema

Nella progettazione del database di una società sportiva abbiamo individuato diverse entità, tra cui `SQUADRE` e `ALLENATORI`.

L'entità `SQUADRE` rappresenta le squadre appartenenti alla società sportiva, mentre l'entità `ALLENATORI` rappresenta i professionisti incaricati della loro preparazione atletica e tecnica.

Tra queste due entità esiste una relazione che possiamo denominare **ALLENA**.

Tuttavia, sapere che un allenatore allena una squadra non è sufficiente per definire correttamente la struttura del database.

Dobbiamo prima rispondere a due domande fondamentali:

- **Quante squadre può allenare un singolo allenatore?**
- **Quanti allenatori possono essere assegnati a una singola squadra?**

Le risposte a queste domande determinano la **cardinalità della relazione**, cioè il numero di istanze di un'entità che possono essere associate alle istanze dell'altra entità.

Esaminiamo tre possibili scenari.

---

## 2. Primo scenario — Relazione uno a uno (1:1)

### Descrizione della situazione

La società sportiva stabilisce che:

- Ogni squadra può avere un solo allenatore.
- Ogni allenatore può essere responsabile di una sola squadra.

In questo caso, la relazione `ALLENA` è di tipo **1:1 (uno a uno)**.

### Rappresentazione concettuale

`SQUADRE (1) — ALLENA — (1) ALLENATORI`

### Traduzione nel modello relazionale

La relazione può essere rappresentata inserendo una chiave esterna in una delle due tabelle.

Ad esempio:

**ALLENATORI**

`id_allenatore` (PK), `nome`, `cognome`, `qualifica`

**SQUADRE**

`codice_squadra` (PK), `nome`, `categoria`, `allenatore` (FK, UNIQUE)

La chiave esterna `id_allenatore` permette di identificare l'allenatore assegnato a ciascuna squadra.

Il vincolo `UNIQUE` impedisce che lo stesso allenatore venga assegnato a più squadre.

### Esempio

**ALLENATORI**

| id_allenatore | nome  | cognome |
| ----------------- | ----- | ------- |
| AL01              | Mario | Rossi   |
| AL02              | Luca  | Bianchi |
| AL03              | Paolo | Verdi   |

**SQUADRE**

| codice_squadra | nome    | allenatore |
| -------------- | ------- | ----------------- |
| SQ01           | Fulmini | AL01              |
| SQ02           | Aquile  | AL02              |
| SQ03           | Tigri   | AL03              |

Ogni allenatore compare al massimo una volta nella colonna `allenatore` della tabella `SQUADRE`.

**Osservazione:** se ogni squadra deve obbligatoriamente avere un allenatore, la chiave esterna dovrà anche essere `NOT NULL`. Per garantire che ogni allenatore abbia necessariamente una squadra occorrono invece ulteriori vincoli.

---

## 3. Secondo scenario — Relazione uno a molti (1:N)

### Descrizione della situazione

La società sportiva modifica la propria organizzazione e stabilisce che:

- Ogni squadra può essere seguita da più allenatori.
- Ogni allenatore può essere assegnato a una sola squadra.

In questo caso, la relazione `ALLENA` diventa **1:N (uno a molti)**.

### Rappresentazione concettuale

`SQUADRE (1) — ALLENA — (N) ALLENATORI`

### Traduzione nel modello relazionale

In una relazione 1:N, la chiave esterna viene inserita nella tabella che si trova sul **lato molti (N)**.

Pertanto:

**SQUADRE**

`codice_squadra` (PK), `nome`, `categoria`

**ALLENATORI**

`id_allenatore` (PK), `nome`, `cognome`, `qualifica`, `codice_squadra` (FK)

La differenza rispetto al primo scenario è fondamentale: la chiave esterna `codice_squadra` viene ora inserita nella tabella `ALLENATORI`.

### Esempio

**SQUADRE**

| codice_squadra | nome    |
| -------------- | ------- |
| SQ01           | Fulmini |
| SQ02           | Aquile  |

**ALLENATORI**

| id_allenatore | nome   | cognome | codice_squadra |
| ----------------- | ------ | ------- | -------------- |
| AL01              | Mario  | Rossi   | SQ01           |
| AL02              | Luca   | Bianchi | SQ01           |
| AL03              | Paolo  | Verdi   | SQ02           |
| AL04              | Andrea | Neri    | SQ01           |

La squadra `SQ01` è seguita da tre allenatori: `AL01`, `AL02` e `AL04`.

Questo è possibile perché **una chiave esterna può contenere valori ripetuti**.

La ripetizione di `SQ01` non rappresenta un errore: indica semplicemente che più allenatori sono associati alla stessa squadra.

A differenza della relazione 1:1, non viene imposto un vincolo `UNIQUE` sulla chiave esterna.

---

## 4. Terzo scenario — Relazione molti a molti (N:M)

### Descrizione della situazione

La società sportiva decide di adottare un'organizzazione più flessibile:

- Ogni squadra può essere seguita da più allenatori.
- Ogni allenatore può seguire contemporaneamente più squadre.

La relazione `ALLENA` diventa quindi **N:M (molti a molti)**.

### Rappresentazione concettuale

`SQUADRE (N) — ALLENA — (M) ALLENATORI`

### Perché non è sufficiente una semplice chiave esterna?

Se inserissimo `allenatore` nella tabella `SQUADRE`, potremmo rappresentare direttamente un solo allenatore per squadra.

Viceversa, inserendo `codice_squadra` nella tabella `ALLENATORI`, potremmo rappresentare direttamente una sola squadra per allenatore.

Nessuna delle due soluzioni sarebbe sufficiente a rappresentare correttamente la nuova organizzazione.

### Introduzione della tabella associativa

Per risolvere il problema si introduce una nuova tabella, denominata `INCARICHI`.

Il modello relazionale diventa:

**SQUADRE**

`codice_squadra` (PK), `nome`, `categoria`

**ALLENATORI**

`id_allenatore` (PK), `nome`, `cognome`, `qualifica`

**INCARICHI**

`codice_squadra` (PK, FK), `id_allenatore` (PK, FK)

La tabella `INCARICHI` contiene due chiavi esterne che fanno riferimento alle chiavi primarie delle rispettive entità.

La coppia (`codice_squadra`, `id_allenatore`) costituisce una **chiave primaria composta**, impedendo la registrazione duplicata della stessa associazione.

### Esempio

**INCARICHI**

| codice_squadra | id_allenatore |
| -------------- | ----------------- |
| SQ01           | AL01              |
| SQ01           | AL02              |
| SQ02           | AL01              |
| SQ02           | AL03              |
| SQ03           | AL02              |

Dai dati possiamo osservare che:

- `SQ01` è allenata sia da `AL01` sia da `AL02`.
- `AL01` allena sia `SQ01` sia `SQ02`.
- Ogni riga rappresenta una specifica associazione tra una squadra e un allenatore.

La relazione N:M originaria viene quindi trasformata, nel modello relazionale, in **due relazioni 1:N**:

`SQUADRE (1) — (N) INCARICHI`

`ALLENATORI (1) — (N) INCARICHI`

La tabella associativa può inoltre contenere attributi che descrivono la relazione stessa, come `data_inizio`, `data_fine` o `tipo_incarico`.

---

## 5. Confronto tra le tre cardinalità

| Cardinalità | Regola organizzativa                                    | Soluzione nel modello relazionale                 |
| ----------- | ------------------------------------------------------- | ------------------------------------------------- |
| **1:1**     | Un allenatore per squadra e una squadra per allenatore  | FK in una delle due tabelle, con vincolo `UNIQUE` |
| **1:N**     | Più allenatori per squadra, una squadra per allenatore  | FK nella tabella `ALLENATORI`, sul lato N         |
| **N:M**     | Più allenatori per squadra e più squadre per allenatore | Tabella associativa `INCARICHI` con due FK     |

## 6. Considerazioni conclusive

Questo esempio permette di comprendere un principio fondamentale della progettazione dei database:

**La cardinalità di una relazione non dipende dal nome delle entità coinvolte, ma dalle regole che descrivono il funzionamento della realtà da rappresentare.**

Le entità `SQUADRE` e `ALLENATORI` rimangono le stesse nei tre scenari. A cambiare sono le regole organizzative della società sportiva e di conseguenza, la struttura del modello relazionale.

È quindi necessario analizzare attentamente la descrizione del problema prima di decidere dove collocare le chiavi esterne o se introdurre una tabella associativa.

**Nota:** le cardinalità 1:1, 1:N e N:M descrivono le molteplicità massime. Per completare la progettazione occorre anche stabilire la partecipazione minima, cioè se un'associazione sia obbligatoria oppure facoltativa. Ad esempio, una squadra può esistere temporaneamente senza allenatore? Un allenatore può essere registrato senza avere ancora una squadra assegnata?
