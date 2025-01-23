# Traccia 2: Sistema di Prenotazione Ristorante

Scrivi un programma in Python per un sistema di prenotazione al ristorante. Il programma deve includere le seguenti classi:

1. **Tavolo**: rappresenta un tavolo con un numero identificativo e una capienza massima.
2. **Prenotazione**: rappresenta una prenotazione con nome del cliente, numero di persone e tavolo assegnato.
3. **Ristorante**: contiene una lista di tavoli disponibili e prenotazioni, con i seguenti metodi:
    - `aggiungi_tavolo(tavolo)`: aggiunge un tavolo al ristorante.
    - `effettua_prenotazione(nome_cliente, num_persone)`: cerca un tavolo adatto e crea una prenotazione se possibile.
    - `visualizza_prenotazioni()`: mostra tutte le prenotazioni.

### Descrizione dei campi delle entità

#### Classe `Tavolo`:
- **numero**: intero, identifica univocamente il tavolo.
- **capienza**: intero, rappresenta il numero massimo di persone che il tavolo può ospitare.
- **occupato**: booleano, indica se il tavolo è attualmente occupato (True) o libero (False).

#### Classe `Prenotazione`:
- **nome_cliente**: stringa, rappresenta il nome del cliente che ha effettuato la prenotazione.
- **num_persone**: intero, rappresenta il numero di persone incluse nella prenotazione.
- **tavolo**: oggetto di tipo `Tavolo`, rappresenta il tavolo assegnato per la prenotazione.

#### Classe `Ristorante`:
- **tavoli**: lista, contiene tutti gli oggetti di tipo `Tavolo` aggiunti al ristorante.
- **prenotazioni**: lista, contiene tutte le prenotazioni attive (oggetti di tipo `Prenotazione`).

### Esempio di esecuzione:

```python
# Creazione dei tavoli
tavolo1 = Tavolo(1, 4)
tavolo2 = Tavolo(2, 2)

# Creazione del ristorante
ristorante = Ristorante()

# Aggiunta dei tavoli
ristorante.aggiungi_tavolo(tavolo1)
ristorante.aggiungi_tavolo(tavolo2)

# Effettuare prenotazioni
ristorante.effettua_prenotazione("Mario Rossi", 2)
# Output: Prenotazione confermata: Mario Rossi, Tavolo 2

ristorante.effettua_prenotazione("Anna Bianchi", 5)
# Output: Nessun tavolo disponibile per 5 persone.

# Visualizzazione delle prenotazioni
ristorante.visualizza_prenotazioni()
# Output:
# Prenotazioni attuali:
# - Cliente: Mario Rossi, Tavolo: 2
