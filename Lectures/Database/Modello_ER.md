# Modello Entità-Relazione: Sistema Universitario

## Introduzione
Il modello entità-relazione (E-R) è una metodologia di progettazione di database utilizzata per rappresentare i dati in modo concettuale. Questo modello si basa su tre componenti principali:
- **Entità**: rappresentano oggetti del mondo reale con attributi specifici.
- **Relazioni**: definiscono le associazioni tra entità.
- **Attributi**: descrivono le proprietà delle entità e delle relazioni.

L'obiettivo del modello E-R è fornire una rappresentazione chiara e strutturata dei dati, facilitando la successiva implementazione del database relazionale.

### Concetti avanzati del Modello E-R
Oltre agli elementi di base, il modello E-R prevede alcune estensioni avanzate:
- **Generalizzazione e Specializzazione**: la generalizzazione è il processo di astrarre attributi comuni da più entità in un'entità padre. La specializzazione è il processo inverso, in cui un'entità viene suddivisa in sottoentità più specifiche.
- **Aggregazione**: permette di trattare una relazione come se fosse un'entità, utile quando una relazione ha attributi propri.
- **Normalizzazione**: è il processo di organizzazione dei dati per ridurre ridondanze e migliorare l'integrità del database.

## Elementi del Modello E-R

### Entità
Le entità sono gli oggetti principali del modello, che possono essere:
- **Entità forti**: hanno un'identità propria e una chiave primaria univoca.
- **Entità deboli**: dipendono da un'altra entità per la loro identificazione e necessitano di una chiave esterna per essere identificate univocamente.

### Relazioni
Le relazioni descrivono l'associazione tra due o più entità. Le principali tipologie di relazioni sono:
- **Uno a Uno (1:1)**: Un'istanza di un'entità è associata a una sola istanza di un'altra entità.
- **Uno a Molti (1:N)**: Un'istanza di un'entità è associata a più istanze di un'altra entità, ma non viceversa.
- **Molti a Molti (M:N)**: Più istanze di un'entità possono essere associate a più istanze di un'altra entità.

### Cardinalità
La cardinalità di una relazione definisce il numero massimo e minimo di istanze che possono essere coinvolte. I valori comuni sono:
- **(0,1)**: Un'entità può partecipare a una relazione al massimo una volta.
- **(1,1)**: L'entità deve partecipare esattamente una volta alla relazione.
- **(0,N)**: L'entità può partecipare alla relazione un numero arbitrario di volte, inclusa l'assenza di partecipazione.
- **(1,N)**: L'entità deve partecipare almeno una volta alla relazione, ma può essere associata a più istanze.

## Normalizzazione
La normalizzazione è un processo volto a eliminare ridondanze e anomalie nei dati. Le principali forme normali sono:
- **Prima Forma Normale (1NF)**: Ogni attributo deve contenere solo valori atomici.
- **Seconda Forma Normale (2NF)**: Deve essere in 1NF e tutti gli attributi non chiave devono dipendere completamente dalla chiave primaria.
- **Terza Forma Normale (3NF)**: Deve essere in 2NF e non devono esserci dipendenze transitive tra attributi non chiave.

## Entità nel Sistema Universitario

### Studente
- **Matricola** (Chiave primaria)
- **Nome**
- **Cognome**

### Corso
- **CodiceCorso** (Chiave primaria)
- **Titolo**
- **CFU** (Crediti Formativi Universitari)

## Relazione

### Partecipa
- **Descrizione**: Rappresenta l'iscrizione di uno studente a un corso.
- **Collega**: Studente ↔ Corso
- **Attributo**: Voto (valutazione dello studente nel corso)
- **Cardinalità**: Un corso può avere molti studenti iscritti (1:N), mentre uno studente può iscriversi a più corsi (N:1), risultando in una relazione molti a molti (M:N).

## Trasformazione in Schema Relazionale
Per trasformare il modello E-R in schema relazionale, possiamo definire le seguenti tabelle:

```sql
CREATE TABLE Studente (
    Matricola VARCHAR(10) PRIMARY KEY,
    Nome VARCHAR(50),
    Cognome VARCHAR(50)
);

CREATE TABLE Corso (
    CodiceCorso VARCHAR(10) PRIMARY KEY,
    Titolo VARCHAR(100),
    CFU INT
);

CREATE TABLE Partecipa (
    Matricola VARCHAR(10),
    CodiceCorso VARCHAR(10),
    Voto INT,
    PRIMARY KEY (Matricola, CodiceCorso),
    FOREIGN KEY (Matricola) REFERENCES Studente(Matricola),
    FOREIGN KEY (CodiceCorso) REFERENCES Corso(CodiceCorso)
);

erDiagram
    STUDENTE ||--o{ PARTECIPA : "si iscrive"
    CORSO ||--o{ PARTECIPA : "ha studenti"
    STUDENTE {
        string Matricola PK
        string Nome
        string Cognome
    }
    CORSO {
        string CodiceCorso PK
        string Titolo
        int CFU
    }
    PARTECIPA {
        string Matricola FK
        string CodiceCorso FK
        int Voto
    }
