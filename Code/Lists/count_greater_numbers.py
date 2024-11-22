import random

n = 10

numbers = [random.randint(1,10) for _ in range(n)]
print(numbers)

greater_numbers = [1 if num > 5 else 0 for num in numbers ]
print(greater_numbers)

print(f"Numeri maggiori di 5: {sum(greater_numbers)}")
