# Guida per Installare Git su Windows 11

Questa guida ti mostrerà come installare Git su Windows 11 in pochi semplici passaggi.

## Passo 1: Scarica Git

1. Vai al sito ufficiale di Git: [https://git-scm.com/](https://git-scm.com/).
2. Clicca su **Download for Windows** per scaricare l'ultima versione di Git per Windows.

## Passo 2: Avvia l'Installer di Git

1. Una volta completato il download, apri il file `.exe` per avviare l'installer di Git.
2. Verrà visualizzata una finestra di dialogo per il setup. Segui le istruzioni sullo schermo.

## Passo 3: Configurazione delle Opzioni di Installazione

Durante l'installazione, ti verranno chieste alcune opzioni. Ecco le impostazioni consigliate:

1. **Select Destination Location**: Lascia il percorso di default.
2. **Select Components**: Lascia tutte le caselle selezionate e clicca su **Next**.
3. **Adjusting Your PATH Environment**: Seleziona **Git from the command line and also from 3rd-party software**.
4. **Choosing the default editor used by Git**: Scegli un editor di testo che preferisci, come **Notepad** o **Visual Studio Code**.
5. **Configuring the line ending conversions**: Seleziona **Checkout Windows-style, commit Unix-style line endings**.

## Passo 4: Completa l'Installazione

1. Clicca su **Install** per avviare l'installazione.
2. Una volta completata, seleziona **Launch Git Bash** e **Finish**.

## Passo 5: Verifica l'Installazione

1. Apri **Git Bash** (puoi trovarlo cercando "Git Bash" nel menu Start).
2. Digita il seguente comando per verificare che Git sia stato installato correttamente:

   ```bash
   git --version
