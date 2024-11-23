import random

casual_numbers = [random.randint(1, 10) for num in range(0, 10)]

even_odd = ["even" if number % 2 == 0 else "odd" for number in casual_numbers]

print(casual_numbers)
print(f'There are {even_odd.count("even")} even numbers and {even_odd.count("odd")} odd numbers.')

even = 0
for number in casual_numbers:
    if number % 2 == 0:
        even += 1

print(casual_numbers)
print(f"There are {even} even numbers and {len(casual_numbers) - even} odd numbers")
