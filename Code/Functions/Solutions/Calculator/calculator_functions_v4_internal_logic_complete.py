def somma(a, b):
    return a + b

def differenza(a, b):
    return a - b

def moltiplicazione(a, b):
    return a * b

# Ibput arguments:
# --------------------
# a: numeratore >= 0
# b: denominatore > 0
# --------------------
# --------------------
# --------------------
# Output arguments;
# --------------------
# esito: Esito dell'operazione di divisione
#   True: Operazione Riuscitat
#   False: Operazione non Riuscita
# --------------------
# messaggio: Comunicazione esito operazione
# --------------------
# risultato: Risultato dell'operazione di divisione
#   None: Nel caso di divisione per zero
# --------------------
def divisione(a, b):
    if b == 0:
        return False, "Divisione per zero non consentita!", None
    else:
        return True, "OK", a / b

def check_operazione():
    while True:
        operazione = input("Scegli operazione [+ - x /]: ")

        if operazione not in ['+', '-', 'x', '/']:
            print("Selezione Operazione Scorretta!")
            continue
        return operazione


def check_input(prompt):
    while True:
        try:
            value = int(input(prompt + ": "))
        except ValueError as ve:
            print("input non conforme!")
            continue
        else:
            if value < 0:
                print("Inserisci un numero intero uguale o maggiore di zero!")
            else:
                return value

def main():
    val1 = check_input("Inserisci un numero intero maggiore o uguale a zero")
    val2 = check_input("Inserisci un altro valore intero maggiore o uguale a zero")

    operazione = check_operazione()

    risultato = 0
    if operazione == '+':
        risultato = somma(val1, val2)
    elif operazione == '-':
        risultato = differenza(val1, val2)
    elif operazione == 'x':
        risultato = moltiplicazione(val1, val2)
    else:
        esito, messaggio, risultato = divisione(val1, val2)

        if not esito:
            while val2 == 0:
                print(messaggio)
                val2 = check_input("Per il denominatore della divisione, inserire un valore MAGGIORE DI ZERO")
            esito, messaggio, risultato = divisione(val1, val2)

        risultato = round(risultato, 2)

    print(f"{val1} {operazione} {val2} = {risultato}")

if __name__ == "__main__":
    main()
