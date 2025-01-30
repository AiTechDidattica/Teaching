
# Introduzione ai Database

## Cos'è un Database?
Un **database** è una raccolta organizzata di dati, progettata per essere facilmente accessibile, gestita e aggiornata. I database sono utilizzati in vari contesti, da applicazioni personali fino a sistemi aziendali complessi.

I principali vantaggi dell'utilizzo di un database sono:
- **Organizzazione dei dati**: I dati sono strutturati in modo da consentire un recupero efficiente.
- **Ridondanza ridotta**: La progettazione elimina duplicati inutili di dati.
- **Integrità dei dati**: Le regole imposte sul database garantiscono dati affidabili.
- **Sicurezza**: Accesso controllato per proteggere i dati.

---

## Tecnologie dei Database

### 1. Database Relazionali (RDBMS)
I database relazionali organizzano i dati in tabelle, utilizzando relazioni per connettere i dati tra le tabelle. Le loro caratteristiche principali includono:
- Struttura basata su tabelle (righe e colonne).
- Utilizzo di SQL come linguaggio di interrogazione.
- Garantisce proprietà ACID (Atomicità, Consistenza, Isolamento, Durabilità).

**Esempi di RDBMS**:
- MySQL
- PostgreSQL
- Oracle Database

### 2. Database NoSQL
I database NoSQL sono progettati per gestire grandi volumi di dati non strutturati o semi-strutturati e sono utili in applicazioni distribuite.
- **Document Store**: Archivia dati come documenti JSON o BSON (es. MongoDB).
- **Graph Database**: Archivia relazioni complesse tra entità (es. Neo4j).

**Quando scegliere NoSQL?**
- Necessità di scalabilità orizzontale.
- Dati non strutturati o semi-strutturati.

### 3. Database NewSQL
Una combinazione di RDBMS e NoSQL, progettata per sistemi moderni che richiedono scalabilità con le proprietà dei database relazionali.

---

## I DBMS (Database Management System)

Un **DBMS** è un software che gestisce i dati all'interno di un database. Esempi di compiti gestiti da un DBMS:
- Definizione della struttura del database.
- Inserimento, aggiornamento ed eliminazione dei dati.
- Controllo della concorrenza.
- Recupero dei dati tramite query.

**Vantaggi dei DBMS**:
1. **Centralizzazione**: I dati sono archiviati in un unico sistema.
2. **Sicurezza**: Accessi controllati e audit.
3. **Condivisione**: Utenti multipli possono accedere simultaneamente ai dati.

---

## Modello Entità-Relazione (E-R)

Il **modello E-R** è un modo visuale per progettare il database. Usa concetti come:
- **Entità**: Oggetti distinti (es. `Studente` o `Corso`).
- **Attributi**: Proprietà delle entità (es. `Nome`).
- **Relazioni**: Collegamenti logici tra entità.

### Esempio: Sistema Universitario
- **Entità**:
  - `Studente`: Attributi `Matricola`, `Nome`, `Cognome`.
  - `Corso`: Attributi `CodiceCorso`, `Titolo`, `CFU`.
- **Relazione**:
  - `Partecipa`: Collegamento tra `Studente` e `Corso`, con attributo `Voto`.

### Diagramma UML (Modello E-R)
```simpletext
+------------------+       +------------------+       +------------------+
|    Studente      |       |    Partecipa     |       |      Corso       |
+------------------+       +------------------+       +------------------+
| Matricola (PK)   |<----->| Matricola (FK)   |<----->| CodiceCorso (PK) |
| Nome             |       | CodiceCorso (FK) |       | Titolo           |
| Cognome          |       | Voto             |       | CFU              |
+------------------+       +------------------+       +------------------+

```
---

## Modello Relazionale

Il modello relazionale traduce il modello E-R in un insieme di tabelle. Ogni entità diventa una tabella, e le relazioni possono diventare tabelle con chiavi esterne.

### Schema Relazionale
**Tabelle**:
1. **Studente**:
   - **Chiave primaria**: `Matricola`.
2. **Corso**:
   - **Chiave primaria**: `CodiceCorso`.
3. **Partecipa**:
   - **Chiave primaria**: Combinazione di `Matricola` e `CodiceCorso`.
   - **Chiavi esterne**:
     - `Matricola` (riferisce a `Studente`).
     - `CodiceCorso` (riferisce a `Corso`).

### Definizione di Chiavi
- **Chiave primaria**: Un attributo (o un insieme di attributi) che identifica univocamente una tupla.
  - Es. `Matricola` nella tabella `Studente`.
- **Chiave esterna**: Un attributo che punta alla chiave primaria di un'altra tabella.
  - Es. `Matricola` nella tabella `Partecipa`.
- **Superchiave**: Qualsiasi insieme di attributi che identifica univocamente una tupla.

**Esempio**:
- Nella tabella `Partecipa`, la combinazione di `Matricola` e `CodiceCorso` forma la chiave primaria.

### Query sulle Chiavi Esterne
Recuperare gli studenti con il nome del corso e il voto:
```sql
SELECT s.Nome, s.Cognome, c.Titolo, p.Voto
FROM Studente s
JOIN Partecipa p ON s.Matricola = p.Matricola
JOIN Corso c ON p.CodiceCorso = c.CodiceCorso;
```

---

## Conclusione

La progettazione di un database inizia con un buon modello concettuale e prosegue con la traduzione in schemi relazionali. La comprensione dei concetti di chiavi, relazioni e l'uso di strumenti visuali come i diagrammi UML è fondamentale per creare sistemi efficienti.
