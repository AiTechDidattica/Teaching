# Esercitazione svolta – Le relazioni tra le tabelle di un database

## 1. Introduzione

In una base di dati relazionale, le informazioni vengono organizzate in **tabelle**, ciascuna delle quali rappresenta una determinata categoria di elementi.

Le tabelle possono essere collegate attraverso attributi comuni, utilizzando le **chiavi primarie (PK)** e le **chiavi esterne (FK)**.

La *molteplicità* di una relazione indica quanti record di una tabella possono essere associati ai record di un'altra tabella.

Le principali molteplicità sono:

- **Uno a uno (1:1):** a ogni record della prima tabella può corrispondere al massimo un record della seconda e viceversa.
- **Uno a molti (1:N):** a un record della prima tabella possono corrispondere più record della seconda, mentre ogni record della seconda può essere associato al massimo a uno della prima.
- **Molti a molti (N:M):** a un record della prima tabella possono corrispondere più record della seconda e viceversa.

> **Precisazione:** le sigle 1:1, 1:N e N:M descrivono il numero massimo di associazioni; l'obbligatorietà di un'associazione è un vincolo distinto.

Vediamo come queste relazioni vengono realizzate attraverso esempi concreti, utilizzando direttamente le tabelle relazionali e non il modello E/R.

---

## 2. Relazione uno a uno (1:1)

### Esempio: dipendenti e badge aziendali

Un'azienda registra i propri dipendenti e i badge personali assegnati per accedere agli uffici.

Ogni dipendente può possedere un solo badge e ogni badge può essere assegnato a un solo dipendente.

**Tabella DIPENDENTI**

| id_dipendente (PK) | nome | cognome |
|---|---|---|
| D01 | Marco | Rossi |
| D02 | Laura | Bianchi |
| D03 | Anna | Verdi |

**Tabella BADGE**

| id_badge (PK) | codice_accesso | id_dipendente (FK, UNIQUE) |
|---|---|---|
| B101 | 45821 | D01 |
| B102 | 73915 | D02 |
| B103 | 28640 | D03 |

**Rappresentazione sintetica:**

```text
DIPENDENTI (1) ───────── (1) BADGE
```

### Spiegazione

La tabella `DIPENDENTI` identifica ciascun dipendente mediante la chiave primaria `id_dipendente`.

La tabella `BADGE` contiene una propria chiave primaria (`id_badge`) e una chiave esterna (`id_dipendente`), che fa riferimento alla tabella `DIPENDENTI`.

**Attenzione:** la sola presenza della chiave esterna non garantisce una relazione 1:1. È necessario che `id_dipendente` nella tabella `BADGE` abbia anche un **vincolo di unicità (`UNIQUE`)**, così da impedire che più badge siano associati allo stesso dipendente.

Nell'esempio tutti i dipendenti hanno un badge; in generale, il vincolo `UNIQUE` garantisce l'associazione **al massimo** a un badge, non l'obbligo di possederne uno.

---

## 3. Relazione uno a molti (1:N)

### Esempio: clienti e ordini

Un negozio registra i propri clienti e gli ordini effettuati.

Ogni cliente può effettuare più ordini nel tempo, mentre ogni ordine appartiene a un solo cliente.

**Tabella CLIENTI**

| id_cliente (PK) | nome | cognome |
|---|---|---|
| C01 | Marco | Rossi |
| C02 | Laura | Bianchi |
| C03 | Anna | Verdi |

**Tabella ORDINI**

| id_ordine (PK) | data_ordine | importo | id_cliente (FK) |
|---|---|---|---|
| O101 | 05/10/2026 | 120,00 | C01 |
| O102 | 08/10/2026 | 75,00 | C02 |
| O103 | 12/10/2026 | 210,00 | C01 |
| O104 | 15/10/2026 | 50,00 | C03 |
| O105 | 18/10/2026 | 90,00 | C01 |

**Rappresentazione sintetica:**

```text
CLIENTI (1) ───────── (N) ORDINI
```

### Spiegazione

La chiave primaria `id_cliente` identifica univocamente ciascun cliente.

Nella tabella `ORDINI`, l'attributo `id_cliente` è una chiave esterna che indica quale cliente ha effettuato ciascun ordine.

Osservando le tuple, notiamo che:

- Il cliente `C01` compare in tre ordini differenti.
- Il cliente `C02` compare in un solo ordine.
- Il cliente `C03` compare in un solo ordine.

**La chiave esterna può quindi ripetersi nella tabella ORDINI**, poiché uno stesso cliente può effettuare più ordini.

La relazione 1:N si realizza inserendo la chiave esterna nella tabella che si trova dal lato **N** della relazione.

---

## 4. Relazione molti a molti (N:M)

### Esempio: studenti e corsi

Una scuola organizza corsi pomeridiani ai quali gli studenti possono iscriversi.

Ogni studente può frequentare più corsi e ogni corso può essere frequentato da più studenti.

**Tabella STUDENTI**

| id_studente (PK) | nome | cognome |
|---|---|---|
| S01 | Marco | Rossi |
| S02 | Laura | Bianchi |
| S03 | Anna | Verdi |

**Tabella CORSI**

| id_corso (PK) | nome_corso | durata_ore |
|---|---|---|
| C01 | Python | 30 |
| C02 | Inglese | 25 |
| C03 | Robotica | 40 |

Osserviamo alcune iscrizioni:

- Marco Rossi frequenta Python e Robotica.
- Laura Bianchi frequenta Python e Inglese.
- Anna Verdi frequenta Inglese e Robotica.

Non possiamo rappresentare correttamente queste associazioni inserendo una **singola chiave esterna** in `STUDENTI` oppure in `CORSI`: ciascuna riga dovrebbe infatti poter essere collegata a più righe dell'altra tabella.

### La soluzione: una tabella di collegamento

Introduciamo una terza tabella, chiamata `ISCRIZIONI`.

**Tabella ISCRIZIONI**

| id_studente (PK, FK) | id_corso (PK, FK) | data_iscrizione |
|---|---|---|
| S01 | C01 | 01/10/2026 |
| S01 | C03 | 02/10/2026 |
| S02 | C01 | 01/10/2026 |
| S02 | C02 | 03/10/2026 |
| S03 | C02 | 03/10/2026 |
| S03 | C03 | 04/10/2026 |

**Rappresentazione mediante la tabella di collegamento:**

```text
STUDENTI (1) ─── (N) ISCRIZIONI (N) ─── (1) CORSI

          STUDENTI (N) ↔ (M) CORSI
       (relazione logica complessiva)
```

### Spiegazione

La tabella `ISCRIZIONI` contiene due chiavi esterne:

- `id_studente`, che fa riferimento alla tabella `STUDENTI`;
- `id_corso`, che fa riferimento alla tabella `CORSI`.

Questi due attributi costituiscono anche una **chiave primaria composta**.

Ciò significa che uno studente può comparire più volte nella tabella `ISCRIZIONI`, così come un corso, ma la stessa coppia (`id_studente`, `id_corso`) non può essere ripetuta.

Per esempio, `S01` compare due volte perché Marco Rossi frequenta due corsi. Analogamente, `C01` compare due volte perché il corso Python è frequentato da due studenti.

La relazione N:M viene quindi trasformata, nel modello logico-relazionale, in **due relazioni 1:N**, attraverso una tabella di collegamento.

---

## 5. Confronto delle tre molteplicità

| Molteplicità | Realizzazione nel modello relazionale | Aspetto fondamentale |
|---|---|---|
| **1:1** | Chiave esterna con vincolo `UNIQUE` | Una FK non può ripetersi |
| **1:N** | Chiave esterna nella tabella dal lato N | Una FK può ripetersi |
| **N:M** | Terza tabella con due chiavi esterne | Le due FK identificano le associazioni |

---

## 6. Verifica della comprensione

**Domanda 1.** Nella tabella `ORDINI`, perché il valore `C01` può comparire più volte?

- A. Perché una chiave primaria può ripetersi.
- B. Perché è una chiave esterna e uno stesso cliente può effettuare più ordini.
- C. Perché ogni ordine può appartenere a più clienti.

**Risposta corretta: B.** `id_cliente` è una FK non univoca: più ordini possono riferirsi allo stesso cliente.

**Domanda 2.** Quale vincolo distingue l'esempio 1:1 da quello 1:N?

- A. Il vincolo `UNIQUE` sulla chiave esterna.
- B. La presenza di due chiavi primarie.
- C. L'assenza di una chiave esterna.

**Risposta corretta: A.** Il vincolo `UNIQUE` impedisce che due badge si riferiscano allo stesso dipendente.

**Domanda 3.** Perché `ISCRIZIONI` utilizza una chiave primaria composta?

- A. Per permettere duplicati della stessa iscrizione.
- B. Per identificare ogni coppia studente-corso senza duplicarla.
- C. Per impedire a uno studente di frequentare più corsi.

**Risposta corretta: B.** La coppia identifica un'associazione specifica, pur permettendo a ciascuno studente più corsi e a ogni corso più studenti.

---

## 7. Esercitazione riepilogativa – Gestione di un'azienda commerciale

### 7.1 Descrizione del problema

Un'azienda commerciale intende realizzare una base di dati per gestire i propri dipendenti, i reparti aziendali, i progetti e le attività svolte.

L'organizzazione prevede che:

- Ogni dipendente possa essere assegnato a un solo reparto, mentre ciascun reparto può comprendere più dipendenti.
- A ciascun dipendente possa essere assegnato un solo badge identificativo, utilizzabile esclusivamente dal dipendente al quale è associato.
- Ogni dipendente possa partecipare a più progetti aziendali e ciascun progetto possa coinvolgere più dipendenti.

L'obiettivo è rappresentare queste informazioni attraverso tabelle relazionali, individuando le chiavi primarie, le chiavi esterne e le molteplicità delle relazioni.

### 7.2 Individuazione delle tabelle

Per rappresentare il sistema sono necessarie cinque tabelle.

**Tabella REPARTI**

| id_reparto (PK) | nome_reparto |
|---|---|
| R01 | Amministrazione |
| R02 | Informatica |
| R03 | Commerciale |

**Tabella DIPENDENTI**

| id_dipendente (PK) | nome | cognome | id_reparto (FK) |
|---|---|---|---|
| D01 | Marco | Rossi | R02 |
| D02 | Laura | Bianchi | R01 |
| D03 | Anna | Verdi | R02 |
| D04 | Luca | Neri | R03 |

**Tabella BADGE**

| id_badge (PK) | codice_accesso | id_dipendente (FK, UNIQUE) |
|---|---|---|
| B101 | 45821 | D01 |
| B102 | 73915 | D02 |
| B103 | 28640 | D03 |
| B104 | 59173 | D04 |

**Tabella PROGETTI**

| id_progetto (PK) | nome_progetto | budget |
|---|---|---|
| P01 | Nuovo sito web | 15000 |
| P02 | Gestione magazzino | 22000 |
| P03 | Campagna pubblicitaria | 12000 |

**Tabella PARTECIPAZIONI**

| id_dipendente (PK, FK) | id_progetto (PK, FK) | ore_assegnate |
|---|---|---|
| D01 | P01 | 80 |
| D01 | P02 | 50 |
| D02 | P02 | 40 |
| D03 | P01 | 60 |
| D03 | P02 | 70 |
| D04 | P03 | 90 |
| D02 | P03 | 30 |

### 7.3 Analisi delle relazioni

**Rappresentazione sintetica dei collegamenti (non E/R):**

```text
             REPARTI
                (1)
                 │
                (N)
             DIPENDENTI (1) ───────── (1) BADGE
                (1)
                 │
                (N)
           PARTECIPAZIONI (N) ────── (1) PROGETTI
```

**Relazione REPARTI–DIPENDENTI (1:N)**

Il reparto `R02` è associato sia al dipendente `D01` sia al dipendente `D03`. La chiave esterna `id_reparto` può quindi ripetersi nella tabella `DIPENDENTI`.

**Relazione DIPENDENTI–BADGE (1:1)**

Ogni badge è associato a un solo dipendente. Il vincolo `UNIQUE` sull'attributo `id_dipendente` nella tabella `BADGE` impedisce di assegnare più badge allo stesso dipendente.

**Relazione DIPENDENTI–PROGETTI (N:M)**

Il dipendente `D01` partecipa ai progetti `P01` e `P02`. Allo stesso tempo, il progetto `P01` coinvolge sia `D01` sia `D03`.

La tabella `PARTECIPAZIONI` permette di rappresentare questa relazione molti a molti mediante due relazioni uno a molti. La coppia (`id_dipendente`, `id_progetto`) costituisce la chiave primaria composta.

### 7.4 Riepilogo

| Tabelle coinvolte | Molteplicità | Realizzazione |
|---|---|---|
| REPARTI – DIPENDENTI | 1:N | FK in DIPENDENTI |
| DIPENDENTI – BADGE | 1:1 | FK con `UNIQUE` in BADGE |
| DIPENDENTI – PROGETTI | N:M | Tabella PARTECIPAZIONI |

### 7.5 Osservazioni conclusive

Questo esempio evidenzia un aspetto fondamentale della progettazione relazionale: **la molteplicità non dipende semplicemente dalla presenza di attributi comuni, ma dai vincoli imposti alle associazioni tra i record**.

In particolare, una relazione N:M non viene rappresentata direttamente con una singola chiave esterna, ma richiede una tabella di collegamento.

> **Da ricordare:** la molteplicità massima di una relazione e l'obbligatorietà della partecipazione sono concetti distinti. Ad esempio, il fatto che un dipendente possa avere un solo badge non implica che debba necessariamente averne uno.
