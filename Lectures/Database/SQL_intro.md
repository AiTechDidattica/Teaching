
# Introduzione a SQL

## Cos'è SQL?
**SQL (Structured Query Language)** è un linguaggio standard utilizzato per interagire con i database relazionali. Consente di definire strutture di dati, manipolare e recuperare dati.

---

## Categorie di Comandi SQL

### 1. DDL (Data Definition Language)
Definisce la struttura e lo schema del database.

### 2. DML (Data Manipulation Language)
Gestisce i dati all'interno delle tabelle.

### 3. DCL (Data Control Language)
Gestisce i permessi e i privilegi.

### 4. TCL (Transaction Control Language)
Gestisce le transazioni nel database.

---

## SQL DDL - Definizione dello Schema

Esempio basato sul nostro modello relazionale:

### Creazione delle Tabelle
```sql
CREATE TABLE Studente (
    Matricola INT PRIMARY KEY,
    Nome VARCHAR(50),
    Cognome VARCHAR(50)
);

CREATE TABLE Corso (
    CodiceCorso VARCHAR(10) PRIMARY KEY,
    Titolo VARCHAR(100),
    CFU INT
);

CREATE TABLE Partecipa (
    Matricola INT,
    CodiceCorso VARCHAR(10),
    Voto INT,
    PRIMARY KEY (Matricola, CodiceCorso),
    FOREIGN KEY (Matricola) REFERENCES Studente(Matricola),
    FOREIGN KEY (CodiceCorso) REFERENCES Corso(CodiceCorso)
);
```

### Modifica delle Tabelle
Aggiungere un attributo alla tabella `Studente`:
```sql
ALTER TABLE Studente ADD DataNascita DATE;
```

Eliminare un attributo:
```sql
ALTER TABLE Studente DROP COLUMN DataNascita;
```

Eliminazione di una tabella:
```sql
DROP TABLE Partecipa;
```

---

## SQL DML - Manipolazione dei Dati

### Inserimento di Dati
```sql
INSERT INTO Studente (Matricola, Nome, Cognome) VALUES
(101, 'Marco', 'Rossi'),
(102, 'Lucia', 'Bianchi');

INSERT INTO Corso (CodiceCorso, Titolo, CFU) VALUES
('INF101', 'Informatica', 6),
('MAT201', 'Matematica', 9);

INSERT INTO Partecipa (Matricola, CodiceCorso, Voto) VALUES
(101, 'INF101', 28),
(102, 'MAT201', 30);
```

### Aggiornamento dei Dati
Modificare il voto di Marco:
```sql
UPDATE Partecipa
SET Voto = 30
WHERE Matricola = 101 AND CodiceCorso = 'INF101';
```

### Cancellazione dei Dati
Eliminare il corso `MAT201`:
```sql
DELETE FROM Corso WHERE CodiceCorso = 'MAT201';
```

---

## SQL Query - Recupero dei Dati

### Selezione di Base
```sql
SELECT * FROM Studente;
```

Selezionare solo alcuni attributi:
```sql
SELECT Nome, Cognome FROM Studente;
```

### Filtro con `WHERE`
```sql
SELECT * FROM Partecipa WHERE Voto >= 30;
```

### Ordinamento
```sql
SELECT * FROM Studente ORDER BY Cognome ASC;
```

---

## Operazioni Avanzate

### JOIN
#### INNER JOIN
```sql
SELECT s.Nome, s.Cognome, c.Titolo, p.Voto
FROM Studente s
JOIN Partecipa p ON s.Matricola = p.Matricola
JOIN Corso c ON p.CodiceCorso = c.CodiceCorso;
```

#### LEFT JOIN
```sql
SELECT s.Nome, s.Cognome, c.Titolo
FROM Studente s
LEFT JOIN Partecipa p ON s.Matricola = p.Matricola
LEFT JOIN Corso c ON p.CodiceCorso = c.CodiceCorso;
```

### Tabella riepilogativa JOIN
| JOIN Type   | Include solo corrispondenze? | Include righe senza corrispondenza? |
|------------|-----------------------------|----------------------------------|
| **INNER JOIN** | ✅ Sì                        | ❌ No                           |
| **LEFT JOIN**  | ❌ No (mantiene tutte le righe della prima tabella) | ✅ Sì (NULL per la seconda tabella) |
| **RIGHT JOIN** | ❌ No (mantiene tutte le righe della seconda tabella) | ✅ Sì (NULL per la prima tabella) |
| **FULL JOIN**  | ❌ No                        | ✅ Sì (NULL dove manca) |

#### Alcuni database (come MySQL) non supportano direttamente FULL JOIN. In questi casi si può simulare con LEFT JOIN UNION RIGHT JOIN.

### Funzioni Aggregate
#### Conteggio degli studenti per corso:
```sql
SELECT CodiceCorso, COUNT(Matricola) AS NumeroStudenti
FROM Partecipa
GROUP BY CodiceCorso;
```

#### Media dei voti per corso:
```sql
SELECT CodiceCorso, AVG(Voto) AS MediaVoto
FROM Partecipa
GROUP BY CodiceCorso;
```

### Query con `HAVING`
Filtrare corsi con media superiore a 28:
```sql
SELECT CodiceCorso, AVG(Voto) AS MediaVoto
FROM Partecipa
GROUP BY CodiceCorso
HAVING AVG(Voto) > 28;
```

---

## Controllo delle Transazioni (TCL)
Esempio di transazione:
```sql
BEGIN TRANSACTION;

UPDATE Partecipa SET Voto = 29 WHERE Matricola = 101 AND CodiceCorso = 'INF101';
DELETE FROM Corso WHERE CodiceCorso = 'MAT201';

-- Confermare la transazione
COMMIT;

-- Annullare in caso di errore
ROLLBACK;
```
## Proprietà ACID delle transazioni
ACID è un acronimo che descrive le quattro proprietà fondamentali delle transazioni in un sistema di gestione di basi di dati (DBMS). Queste proprietà assicurano che le transazioni siano gestite in modo affidabile. ACID sta per:

- Atomicità (Atomicity): La transazione è un'unità indivisibile. O tutte le operazioni vengono completate con successo, oppure, in caso di errore, tutte vengono annullate (rollback), ripristinando lo stato iniziale del database.

- Coerenza (Consistency): La transazione porta il database da uno stato coerente a un altro stato coerente, rispettando tutte le regole e i vincoli definiti nel sistema.

- Isolamento (Isolation): Le transazioni vengono eseguite in modo indipendente l'una dall'altra, senza che le operazioni di una transazione siano visibili ad altre transazioni fino al completamento (commit).

- Durabilità (Durability): Una volta che una transazione è stata completata con successo (commit), i suoi effetti sono permanenti e sopravvivono anche in caso di guasti di sistema, come un crash del database o del server.

Queste proprietà garantiscono che le operazioni sul database siano sicure e che non vengano compromesse da errori o malfunzionamenti.

---
## Conclusione
SQL è uno strumento potente per gestire e interrogare i dati nei database relazionali. La combinazione di comandi base e operazioni avanzate permette di rispondere a esigenze semplici e complesse.
