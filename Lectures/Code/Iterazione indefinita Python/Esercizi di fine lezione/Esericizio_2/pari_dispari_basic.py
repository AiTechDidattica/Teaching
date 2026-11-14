a = int(input("Inserisci A: "))
b = 0

while True:
    b = int(input("Inserisci B (maggiore di A): "))
    
    if a < b:
        break
    
    print("Errore: A deve essere minore di B.")
        
print("Numeri pari:")
for i in range(a, b + 1):
    if i % 2 == 0:
        print(i, end=" ")

print("\nNumeri dispari:")
for i in range(a, b + 1):
    if i % 2 != 0:
        print(i, end=" ")
