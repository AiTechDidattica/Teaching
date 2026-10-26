import sqlite3

# Connessione al database
conn = sqlite3.connect("università.db")
cursor = conn.cursor()

# Query parametrizzata
query = "INSERT INTO Partecipa (Matricola, CodiceCorso, Voto) VALUES (?, ?, ?);"

# Dati da inserire
dati = [
    (101, 'INF101', 28),
    (102, 'MAT201', 30)
]

# Esecuzione della query
cursor.executemany(query, dati)

# Salvataggio delle modifiche
conn.commit()

# Chiusura della connessione
conn.close()
