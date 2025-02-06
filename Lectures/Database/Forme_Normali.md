# **Le Forme Normali nei Database Relazionali**

Le **forme normali** sono regole utilizzate nei database relazionali per ridurre la ridondanza e migliorare la coerenza dei dati. Qui vedremo le forme normali fino alla **Boyce-Codd Normal Form (BCNF)**.
---

Le forme normali si usano nella progettazione dei database relazionali per migliorare la qualità dei dati, eliminare ridondanze, ridurre il rischio di anomalie di aggiornamento e garantire l'integrità referenziale.

Obiettivi della normalizzazione
Eliminare la ridondanza: evitare la duplicazione non necessaria dei dati, che può portare a un maggiore utilizzo di spazio e a possibili errori nei dati.
Evitare le anomalie:
Anomalie di inserimento: si verificano quando l'inserimento di nuovi dati è impedito a causa della dipendenza da altri dati già esistenti.
Anomalie di aggiornamento: aggiornare un valore ripetuto in più tuple richiede più operazioni, aumentando il rischio di inconsistenze.
Anomalie di cancellazione: la rimozione di un dato può comportare la perdita di informazioni aggiuntive indesiderate.
Garantire la coerenza: ogni valore viene memorizzato in un'unica posizione, rendendo gli aggiornamenti più sicuri e affidabili.
Migliorare la flessibilità del database: permettendo di espandere e modificare il database senza introdurre incoerenze.

---

## **1° Forma Normale (1NF) - Eliminazione degli attributi multivalore**
Una relazione è in **1NF** se:
- ✅ Tutti gli attributi contengono **valori atomici** (non divisibili).
- ✅ Non ci sono insiemi, array o liste nei campi.

### **Esempio (Non in 1NF)**
| Matricola | Nome  | Corsi          |
|-----------|-------|---------------|
| 101       | Alice | INF101, MAT201 |
| 102       | Bob   | PHY301         |

### **Esempio (In 1NF)**
| Matricola | Nome  | Corso  |
|-----------|-------|--------|
| 101       | Alice | INF101 |
| 101       | Alice | MAT201 |
| 102       | Bob   | PHY301 |

---

## **2° Forma Normale (2NF) - Eliminazione delle dipendenze parziali**
Una relazione è in **2NF** se:
- ✅ È già in **1NF**.
- ✅ Ogni attributo non chiave dipende dall’intera chiave primaria (non solo da una parte).

### **Esempio (Non in 2NF)**
| Matricola | Corso  | Nome  | Docente |
|-----------|--------|-------|---------|
| 101       | INF101 | Alice | Rossi   |
| 102       | PHY301 | Bob   | Bianchi |
| 101       | MAT201 | Alice | Verdi   |

🔹 **Problema**:  
- La chiave primaria è **(Matricola, Corso)**.
- L'attributo **Nome** dipende solo da `Matricola`, violando la 2NF.

### **Esempio (In 2NF)**
**Tabella `Studenti`**
| Matricola | Nome  |
|-----------|-------|
| 101       | Alice |
| 102       | Bob   |

**Tabella `Partecipa`**
| Matricola | Corso  | Docente  |
|-----------|--------|---------|
| 101       | INF101 | Rossi   |
| 102       | PHY301 | Bianchi |
| 101       | MAT201 | Verdi   |

Ora ogni attributo dipende dalla chiave intera. ✅

---

## **3° Forma Normale (3NF) - Eliminazione delle dipendenze transitive**
Una relazione è in **3NF** se:
- ✅ È già in **2NF**.
- ✅ Ogni attributo non chiave dipende **direttamente** dalla chiave primaria.

### **Esempio (Non in 3NF)**
| Matricola | Corso  | CodiceDipartimento | NomeDipartimento |
|-----------|--------|--------------------|------------------|
| 101       | INF101 | 10                 | Informatica      |
| 102       | PHY301 | 20                 | Fisica           |
| 101       | MAT201 | 30                 | Matematica       |

🔹 **Problema**:  
- `NomeDipartimento` dipende da `CodiceDipartimento`, che a sua volta dipende da `Corso` → **Dipendenza transitiva!**

### **Esempio (In 3NF)**
**Tabella `Partecipa`**
| Matricola | Corso  | CodiceDipartimento |
|-----------|--------|--------------------|
| 101       | INF101 | 10                 |
| 102       | PHY301 | 20                 |
| 101       | MAT201 | 30                 |

**Tabella `Dipartimenti`**
| CodiceDipartimento | NomeDipartimento |
|--------------------|------------------|
| 10                 | Informatica      |
| 20                 | Fisica           |
| 30                 | Matematica       |

Ora ogni attributo dipende direttamente dalla chiave primaria. ✅

---

## **Boyce-Codd Normal Form (BCNF) - Eliminazione delle anomalie sulle chiavi candidate**
Una relazione è in **BCNF** se:
- ✅ È già in **3NF**.
- ✅ **Ogni determinante è una chiave candidata**.

🔹 **Chiave candidata** = Un insieme minimo di attributi che identifica univocamente una riga.

### **Esempio (Non in BCNF)**
| Docente | Corso  | Aula |
|---------|--------|------|
| Rossi   | INF101 | A1   |
| Bianchi | PHY301 | A2   |
| Rossi   | MAT201 | A1   |

🔹 **Problema**:  
- **Chiavi candidate**: `(Docente, Corso)` e `(Aula, Corso)`.  
- **Dipendenza**: `Docente → Aula` (un docente ha sempre la stessa aula).  
- Se Rossi cambia aula, dobbiamo aggiornare più righe → **Anomalia di aggiornamento!** ❌

### **Esempio (In BCNF)**
**Tabella `Corsi`**
| Corso  | Docente |
|--------|--------|
| INF101 | Rossi  |
| PHY301 | Bianchi |
| MAT201 | Rossi  |

**Tabella `Aule`**
| Docente | Aula |
|---------|------|
| Rossi   | A1   |
| Bianchi | A2   |

Ora ogni determinante è una chiave candidata. ✅

---

## **Riassunto delle Forme Normali**
| Forma Normale | Requisito |
|--------------|---------------------------------------------|
| **1NF**      | Nessun attributo multivalore o ripetuto. |
| **2NF**      | Nessuna dipendenza parziale (ogni colonna dipende dall’intera chiave primaria). |
| **3NF**      | Nessuna dipendenza transitiva. |
| **BCNF**     | Ogni determinante è una chiave candidata (nessuna anomalia sulle dipendenze). |

📌 **Conclusione**  
- **1NF** elimina i valori non atomici.  
- **2NF** elimina dipendenze parziali.  
- **3NF** elimina dipendenze transitive.  
- **BCNF** rafforza la 3NF eliminando tutte le anomalie nelle chiavi candidate.

Se vuoi approfondire, esistono anche la **4NF** (elimina dipendenze multi-valore) e la **5NF** (elimina dipendenze di join), ma BCNF è generalmente sufficiente per la maggior parte delle applicazioni pratiche. 🚀
