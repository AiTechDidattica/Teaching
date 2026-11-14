# Es 1

while True:
    numero = int(input("Inserisci un numero intero positivo: "))
    
    if numero > 0:
            
        for i in range(1, numero + 1):
            print(i)
                
        print()
                
        for i in range(numero, 0, -1):
            print(i)
            
        break
    
    else:
        print("Sono accettati solo numeri interi maggiori di 0! RIPROVA!\n")
        continue