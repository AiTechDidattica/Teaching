# Es 1

inserimento_invalido = True


while inserimento_invalido:
    
    try:
    
        # Variabile che contiene il valore massimo da visualizzare sia in ordine crescente che decrescente
        numero = int(input("Inserisci un numero intero positivo: "))
    
    except ValueError:
    
        print("Sono accettati solo valori numerici come input! RIPROVA!\n")
        continue
    
    else:
        if numero > 0:
            inserimento_invalido = False 
            
            for i in range(1, numero + 1):
                print(i)
                
            print()
                
            for i in range(numero, 0, -1):
                print(i)
            
        else:
            print("Sono accettati solo numeri interi maggiori di 0! RIPROVA!\n")


