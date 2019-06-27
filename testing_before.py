
def is_even(num):
        return num % 2 == 0
'''
def even_number_of_evens(numbers):
        evens = 0
        for i in numbers:                
                if is_even(i):
                        evens+=1        

        if evens == 0:
                return False
        else :
                return is_even(evens)   
'''

# The code above can be further refactored into a more pythonic form
def even_number_of_evens(numbers):

        evens = sum([1 for n in numbers if is_even(n)])
        return False if evens == 0 else is_even(evens)

assert even_number_of_evens([]) == False, "No numbers"
assert even_number_of_evens([2, 4]) == True, "Two even numbers"
assert even_number_of_evens([2, 3]) == False, "Two numbers, only one even"
assert even_number_of_evens([2, 3, 9, 10, 13, 7, 8]) == False, "Odd number of numbers"
assert even_number_of_evens([2, 3, 9, 10, 13, 7, 8, 5, 12]) == True, "Even Number of evens"
assert even_number_of_evens([1, 3, 9]) == False, "No even numbers"

print("All tests passed")