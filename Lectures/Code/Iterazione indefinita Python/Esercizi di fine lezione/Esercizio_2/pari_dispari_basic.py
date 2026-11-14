a = int(input("Inserisci A: "))
b = 0

while True:
    b = int(input("Inserisci B (maggiore di A): "))
    
    if a < b:
        print("\nNumeri: ")
        for numero in range(a, b + 1):
            print(numero, end=" " )
            
        print("\n\nNumeri pari: ")
        for i in range(a, b + 1):
            if i % 2 == 0:
                print(i, end=" ")

        print("\n\nNumeri dispari: ")
        for i in range(a, b + 1):
            if i % 2 != 0:
                print(i, end=" ")
        
        break
    
    else:
        print("Errore: A deve essere minore di B.\n")
        continue
    