# Comandi Principali di Git

Questa guida fornisce una panoramica dei comandi più comuni di Git, con esempi pratici.

## 1. Configurazione di Git

Imposta il nome utente e l'email (necessario una sola volta per configurare Git sul sistema).

```bash
git config --global user.name "Tuo Nome"
git config --global user.email "tuo@email.com"
```

## 2. Inizializzare un Repository

Crea un nuovo repository Git nella directory corrente.

```bash
git init
```

## 3. Controllare lo Stato del Repository

Visualizza lo stato dei file nel repository (modifiche non salvate, file non tracciati, ecc.).

```bash
git status
```

## 4. Aggiungere File al Staging

Aggiunge file specifici o tutti i file al _staging area_, pronti per il commit.

```bash
git add nome_file      # Aggiunge un singolo file
git add .              # Aggiunge tutti i file nella directory corrente
```

## 5. Creare un Commit

Salva le modifiche nel repository con un messaggio descrittivo.

```bash
git commit -m "Messaggio del commit"
```

## 6. Visualizzare la Cronologia dei Commit

Mostra l’elenco dei commit effettuati.

```bash
git log
```

## 7. Collegare un Repository Remoto

Collega il repository locale a uno remoto, come GitHub.

```bash
git remote add origin https://github.com/username/repository.git
```

## 8. Inviare le Modifiche al Repository Remoto

Invia i commit locali al repository remoto.

```bash
git push origin main   # Per la branch "main"
```

## 9. Scaricare le Modifiche dal Repository Remoto

Aggiorna il repository locale con le modifiche dal remoto.

```bash
git pull origin main   # Per la branch "main"
```

## 10. Creare e Cambiare Branch

Crea un nuovo branch e spostati su di esso.

```bash
git branch nome_branch  # Crea un nuovo branch
git checkout nome_branch  # Passa a un branch esistente
```

## 11. Unire un Branch (Merge)

Unisce un branch nel branch corrente.

```bash
git merge nome_branch
```

## 12. Annullare Modifiche

Annulla modifiche non salvate in un file.

```bash
git checkout -- nome_file
```

## 13. Clonare un Repository

Scarica un repository remoto e crea una copia locale.

```bash
git clone https://github.com/username/repository.git
```

---

