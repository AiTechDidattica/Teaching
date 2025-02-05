# **Dipendenze nei Database Relazionali**

Nel modello relazionale, una **dipendenza** è una relazione tra gli **attributi** di una tabella. Comprendere le dipendenze è essenziale per la **normalizzazione**, ovvero il processo di organizzazione dei dati per ridurre la ridondanza e prevenire anomalie.

---

## **📌 Dipendenza Funzionale**
Una **dipendenza funzionale** tra due insiemi di attributi A e B in una relazione significa che, **se conosci il valore di A, allora puoi determinare univocamente il valore di B**.

Si scrive:

\[
A \rightarrow B
\]

Si legge "**A determina B**".  
Significa che due righe con lo stesso valore di A avranno sempre lo stesso valore di B.

### **Esempio**
| Matricola | Nome  | Cognome  |
|-----------|-------|---------|
| 101       | Alice | Rossi   |
| 102       | Bob   | Bianchi |
| 103       | Carla | Verdi   |

- Qui **Matricola → (Nome, Cognome)**, perché conoscendo la `Matricola`, posso determinare `Nome` e `Cognome`.

---

## **🔍 Tipi di Dipendenza Funzionale**

### **1️⃣ Dipendenza Parziale**
Si verifica quando un attributo **dipende solo da una parte** della chiave primaria, anziché dall’intera chiave.  
⚠️ **Viola la Seconda Forma Normale (2NF).**

### **Esempio (Non in 2NF)**  
| Matricola | Corso  | Nome  |
|-----------|--------|-------|
| 101       | INF101 | Alice |
| 101       | MAT201 | Alice |
| 102       | PHY301 | Bob   |

- La **chiave primaria** è **(Matricola, Corso)**.
- `Nome` dipende solo da `Matricola` e **non** dall'intera chiave `(Matricola, Corso)`.
- **Problema**: Se lo stesso studente partecipa a più corsi, `Nome` viene ripetuto.
- **Soluzione**: Separare in due tabelle.

**Tabella `Studenti`**
| Matricola | Nome  |
|-----------|-------|
| 101       | Alice |
| 102       | Bob   |

**Tabella `Partecipa`**
| Matricola | Corso  |
|-----------|--------|
| 101       | INF101 |
| 101       | MAT201 |
| 102       | PHY301 |

Ora `Nome` dipende solo da `Matricola` in una tabella separata. ✅

---

### **2️⃣ Dipendenza Transitiva**
Si verifica quando un attributo dipende **indirettamente** dalla chiave primaria, passando attraverso un altro attributo.  
⚠️ **Viola la Terza Forma Normale (3NF).**

### **Esempio (Non in 3NF)**
| Matricola | Corso  | CodiceDipartimento | NomeDipartimento |
|-----------|--------|--------------------|------------------|
| 101       | INF101 | 10                 | Informatica      |
| 102       | PHY301 | 20                 | Fisica           |

🔹 **Problema**:
- `NomeDipartimento` dipende da `CodiceDipartimento`, che a sua volta dipende da `Corso` → **Dipendenza transitiva**.
- Se cambia il nome del dipartimento, dobbiamo aggiornarlo in più righe.

**Soluzione:** Separare in due tabelle.

**Tabella `Partecipa`**
| Matricola | Corso  | CodiceDipartimento |
|-----------|--------|--------------------|
| 101       | INF101 | 10                 |
| 102       | PHY301 | 20                 |

**Tabella `Dipartimenti`**
| CodiceDipartimento | NomeDipartimento |
|--------------------|------------------|
| 10                 | Informatica      |
| 20                 | Fisica           |

Ora ogni attributo dipende direttamente dalla chiave primaria. ✅

---

### **3️⃣ Dipendenza da una Chiave Candidata**
Si verifica quando un attributo dipende da un insieme di attributi che **non è la chiave primaria**, ma potrebbe essere una **chiave candidata**.  
⚠️ **Viola la Boyce-Codd Normal Form (BCNF).**

### **Esempio (Non in BCNF)**
| Docente | Corso  | Aula |
|---------|--------|------|
| Rossi   | INF101 | A1   |
| Bianchi | PHY301 | A2   |
| Rossi   | MAT201 | A1   |

🔹 **Problema**:
- **Chiavi candidate**: `(Docente, Corso)` e `(Aula, Corso)`.
- **Dipendenza**: `Docente → Aula` (un docente ha sempre la stessa aula).
- Se `Rossi` cambia aula, dobbiamo aggiornare più righe → **Anomalia di aggiornamento!**

**Soluzione:** Creare una tabella separata per le aule dei docenti.

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

## **📌 Riepilogo delle Dipendenze**
| Tipo di Dipendenza | Descrizione | Effetto |
|--------------------|-------------|---------|
| **Dipendenza Funzionale** | Se A determina B, conoscendo A posso trovare B. | Base delle forme normali. |
| **Dipendenza Parziale** | Un attributo dipende solo da una parte della chiave primaria. | Viola la **2NF**. |
| **Dipendenza Transitiva** | Un attributo dipende da un altro che non è chiave primaria. | Viola la **3NF**. |
| **Dipendenza da Chiave Candidata** | Un attributo dipende da un insieme di attributi che non è la chiave primaria ma potrebbe esserlo. | Viola la **BCNF**. |

---

## **📢 Conclusione**
✔️ **Le dipendenze funzionali sono fondamentali per progettare database senza ridondanza.**  
✔️ **Normalizzare significa eliminare dipendenze parziali, transitive e anomalie sulle chiavi candidate.**  
✔️ **BCNF garant
