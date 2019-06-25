from random import randint

numbers = []

for num in range(20):
    numbers.append(randint(0, 50))

def even_number_of_evens(numbers):
    if len(numbers) == 0:
        return False

assert even_number_of_evens(numbers) == False, "No numbers"

print(numbers)