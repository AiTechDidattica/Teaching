# Traccia 1: Gestione Biblioteca

Scrivi un programma in Python per gestire una biblioteca. Il programma deve includere le seguenti classi:

1. **Libro**: rappresenta un libro con attributi come titolo, autore e codice ISBN.
2. **Biblioteca**: contiene una lista di libri e i seguenti metodi:
    - `aggiungi_libro(libro)`: aggiunge un libro alla biblioteca.
    - `rimuovi_libro(isbn)`: rimuove un libro usando il codice ISBN.
    - `cerca_libro(titolo)`: cerca un libro per titolo e restituisce i dettagli del libro se esiste.

### Descrizione dei campi delle entità

#### Classe `Libro`:
- **titolo**: stringa, rappresenta il titolo del libro.
- **autore**: stringa, rappresenta il nome dell'autore del libro.
- **isbn**: stringa, rappresenta il codice identificativo univoco del libro.

#### Classe `Biblioteca`:
- **libri**: lista, contiene tutti gli oggetti di tipo `Libro` aggiunti alla biblioteca.

### Esempio di esecuzione:

```python
# Creazione dei libri
libro1 = Libro("Il Signore degli Anelli", "J.R.R. Tolkien", "12345")
libro2 = Libro("1984", "George Orwell", "67890")

# Creazione della biblioteca
biblioteca = Biblioteca()

# Aggiunta dei libri
biblioteca.aggiungi_libro(libro1)
biblioteca.aggiungi_libro(libro2)

# Ricerca di un libro
biblioteca.cerca_libro("1984")
# Output: Trovato: Titolo: 1984, Autore: George Orwell, ISBN: 67890

# Rimozione di un libro
biblioteca.rimuovi_libro("12345")

# Ricerca di un libro non più presente
biblioteca.cerca_libro("Il Signore degli Anelli")
# Output: Libro non trovato.
