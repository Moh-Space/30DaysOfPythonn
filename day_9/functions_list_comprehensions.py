#functions to add two numbers

def add_two_numbers(a, b):
    return a + b

#function for area of a circle 
import math

def area_of_circle(r):
    return math.pi * r * r

#function to convert celcius to fahrenheit
def convert_celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

#functions to check season
print("functions to check season")
def check_season(month):
    month = month.lower()
    if month in ['december', 'january', 'february']:
        return "Winter"
    elif month in ['march', 'april', 'may']:
        return "Spring"
    elif month in ['june', 'july', 'august']:
        return "Summer"
    elif month in ['september', 'october', 'november']:
        return "Autumn"
    else:
        return "Invalid month"

#function to calculate slope
def calculate_slope(x1, y1, x2, y2):
    if x1 == x2:
        return "Slope is undefined (vertical line)."
    return (y2 - y1) / (x2 - x1)
#function to calculate quadratic equation
print("Function to print quadratic equation")
def solve_quadratic_eqn(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return root1, root2
    elif discriminant == 0:
        root = -b / (2 * a)
        return root
    else:
        return "No real roots"

#function to print list in new line
def print_list(lst):
    for item in lst:
        print(item)

#function to print reversed list

def reverse_list(arr):
    reversed_arr = []
    for item in arr:
        reversed_arr.insert(0, item)
    return reversed_arr

#function to capitalise each item
def capitalize_list_items(lst):
    return [item.capitalize() for item in lst]


#function to add an item to a list
def add_item(lst, item):
    lst.append(item)
    return lst

#dunction to remove
def remove_item(lst, item):
    if item in lst:
        lst.remove(item)
    return lst

#funtion to retin a number
def sum_of_numbers(number):
    return sum(range(number + 1))

#function to calculate odd numbers in a given range
def sum_of_odds(number):
    return sum(i for i in range(number + 1) if i % 2 != 0)

#function to calculate even numbers in a given range
def sum_of_even(number):
    return sum(i for i in range(number + 1) if i % 2 == 0)

#function sum even and odd
def evens_and_odds(number):
    evens = sum(1 for i in range(number + 1) if i % 2 == 0)
    odds = sum(1 for i in range(number + 1) if i % 2 != 0)
    return f"Number of evens: {evens}, Number of odds: {odds}"
#function to get factorial of a number
def factorial(number):
    if number < 0:
        return "Factorial is not defined for negative numbers."
    result = 1
    for i in range(1, number + 1):
        result *= i
    return result
#function to return if a value is empty
def is_empty(value):
    return not bool(value)

#function to cslculate mean
def calculate_mean(numbers):
    return sum(numbers) / len(numbers) if numbers else 0

#function to calculate median
def calculate_median(numbers):
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    mid = n // 2
    if n % 2 == 0:  
        return (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2
    return sorted_numbers[mid]  
#function to calculate mode
from collections import Counter

def calculate_mode(numbers):
    counts = Counter(numbers)
    max_count = max(counts.values())
    return [key for key, value in counts.items() if value == max_count]


#function to calculate range
def calculate_range(numbers):
    return max(numbers) - min(numbers) if numbers else 0

#function to calculate variance
def calculate_variance(numbers):
    mean = calculate_mean(numbers)
    return sum((x - mean) ** 2 for x in numbers) / len(numbers) if numbers else 0

#function to calculate standard deviation
import math

def calculate_std(numbers):
    variance = calculate_variance(numbers)
    return math.sqrt(variance)


#function to check if number is prime
def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


#checking if all items in a list are unique
def all_unique(lst):
    return len(lst) == len(set(lst))


#checking if all items in a list have the same data type
def all_same_type(lst):
    return all(isinstance(item, type(lst[0])) for item in lst)

#function to check if a variable is a valid python variable
def is_valid_variable(variable_name):
    import keyword
    return variable_name.isidentifier() and not keyword.iskeyword(variable_name)
