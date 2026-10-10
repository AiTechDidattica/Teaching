print("Procedura di classificazione di un triangolo.\n")

# Input della lunghezza dei tre lati
a = float(input("Inserisci la lunghezza del primo lato: "))
b = float(input("Inserisci la lunghezza del secondo lato: "))
c = float(input("Inserisci la lunghezza del terzo lato: "))

# Verifica della validità del triangolo
if (a < b + c) and (b < a + c) and (c < a + b):
    print("\nI lati inseriti formano un triangolo valido.")
    
    # Classificazione del triangolo
    if a == b == c:
        print("Il triangolo risulta Equilatero.")
    elif a == b or b == c or a == c:
        print("Il triangolo risulta Isoscele.")
    else:
        print("Il triangolo risulta Scaleno.")
            
else:
    print("\nErrore: I lati inseriti NON formano un triangolo valido!")