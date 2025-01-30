## SQL per Creazione Tabelle
```sql
-- Creazione della tabella 'Utente'
CREATE TABLE Utente (
    UtenteID INTEGER PRIMARY KEY,
    Nome TEXT NOT NULL,
    Email TEXT UNIQUE NOT NULL
);

-- Creazione della tabella 'Libro'
CREATE TABLE Libro (
    LibroID INTEGER PRIMARY KEY,
    Titolo TEXT NOT NULL,
    Autore TEXT NOT NULL
);

-- Creazione della tabella di relazione 'Prestito'
CREATE TABLE Prestito (
    PrestitoID INTEGER PRIMARY KEY,
    UtenteID INTEGER NOT NULL,
    LibroID INTEGER NOT NULL,
    DataInizio DATE NOT NULL,
    DataFine DATE NOT NULL,
    FOREIGN KEY (UtenteID) REFERENCES Utente(UtenteID),
    FOREIGN KEY (LibroID) REFERENCES Libro(LibroID)
);

```
---

## Esempi di Query

### 1. Inserire un nuovo utente e un libro
```sql
-- Aggiungi un utente
INSERT INTO Utente (Nome, Email) VALUES ('Mario Rossi', 'mario@example.com');

-- Aggiungi un libro
INSERT INTO Libro (Titolo, Autore) VALUES ('1984', 'George Orwell');
```

### 2. Registrare un prestito
```sql
-- Aggiungi un prestito
INSERT INTO Prestito (UtenteID, LibroID, DataInizio, DataFine)
VALUES (1, 1, '2024-11-01', '2024-11-15');
```

### 3. Recuperare tutti i libri presi in prestito da un utente
```sql
-- Trova tutti i libri presi in prestito da un utente
SELECT Libro.Titolo, Prestito.DataInizio, Prestito.DataFine
FROM Prestito
JOIN Libro ON Prestito.LibroID = Libro.LibroID
WHERE Prestito.UtenteID = 1;
```
