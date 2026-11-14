# Es 1
N = int(input("Inserisci un numero positivo intero"))
while True:
    if N > 0:
        for i in range(1, N + 1):
            print(i)
        break
    else:
        N = int(input("Inserisci un altro nuovo int positivo")) 
        continue

while True:
    for i in range(N, 0, -1):
        print(i)
    break
