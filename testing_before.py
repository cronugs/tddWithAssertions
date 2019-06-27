
def even_number_of_evens(numbers):
        evens = 0

        for i in numbers:                
                if i %2 == 0:
                        evens+=1

        if len(numbers) == 0:
                return False

        if evens == 0:
                return False

        elif evens %2 == 0:
                return True

        elif evens %2 != 0:
               return False   

assert even_number_of_evens([]) == False, "No numbers"
assert even_number_of_evens([2, 4]) == True, "Two even numbers"
assert even_number_of_evens([2, 3]) == False, "Two numbers, only one even"
assert even_number_of_evens([2, 3, 9, 10, 13, 7, 8]) == False, "Odd number of numbers"
assert even_number_of_evens([2, 3, 9, 10, 13, 7, 8, 5, 12]) == True, "Even Number of evens"
assert even_number_of_evens([1, 3, 9]) == False, "No even numbers"

print("All tests passed")