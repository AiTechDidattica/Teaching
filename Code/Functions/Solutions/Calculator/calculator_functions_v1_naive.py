def somma(a, b):
    return a + b

def differenza(a, b):
    return a - b

def moltiplicazione(a, b):
    return a * b

def divisione(a, b):
    return a / b


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
            if value > 0:
                return value
            print("Inserisci un numero intero maggiore di zero!")

def main():
    val1 = check_input("Inserisci un numero intero positivo")
    val2 = check_input("Inserisci un altro valore intero positivo")

    operazione = check_operazione()

    risultato = 0
    if operazione == '+':
        risultato = somma(val1, val2)
    elif operazione == '-':
        risultato = differenza(val1, val2)
    elif operazione == 'x':
        risultato = moltiplicazione(val1, val2)
    else:
        risultato = round(divisione(val1, val2),2)

    print(f"{val1} {operazione} {val2} = {risultato}")

if __name__ == "__main__":
    main()
    
# Esercizio aggiuntivo: modificare il codice considerando come input ammissibile anche lo zero
