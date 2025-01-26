numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
negative_and_zero = [num for num in numbers if num <= 0]
print(negative_and_zero)


list_of_lists = [[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]

# Flatten the list
flattened_list = [item for list1 in list_of_lists for list2 in list1 for item in list2]

print(flattened_list)

#list comprehension create the following list of tuples:

[(0, 1, 0, 0, 0, 0, 0),
(1, 1, 1, 1, 1, 1, 1),
(2, 1, 2, 4, 8, 16, 32),
(3, 1, 3, 9, 27, 81, 243),
(4, 1, 4, 16, 64, 256, 1024),
(5, 1, 5, 25, 125, 625, 3125),
(6, 1, 6, 36, 216, 1296, 7776),
(7, 1, 7, 49, 343, 2401, 16807),
(8, 1, 8, 64, 512, 4096, 32768),
(9, 1, 9, 81, 729, 6561, 59049),
(10, 1, 10, 100, 1000, 10000, 100000)]



turple_result = [(i, 1, i, i**2, i**3, i**4, i**5) for i in range(11)]
print(turple_result)

#generating the list of tuples using list comprehension 
result = [(i, 1, i, i**2, i**3, i**4, i**5) for i in range(11)]

for item in result:
    print(item)


#flatening list of countries

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

flattened = [[country.upper(), country[:3].upper(), capital.upper()] for sublist in countries for country, capital in sublist]

print(flattened)


#coverting to list of dictionaries
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

# Convert to list of dictionaries
countries_dict_list = [
    {"country": country.upper(), "city": city.upper()} 
    for sublist in countries 
    for country, city in sublist
]

print(countries_dict_list)

#conversion to concatenated list

names = [[('Muhammad', 'Auwal')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]


names_list = [
    f"{first} {last}" 
    for sublist in names 
    for first, last in sublist
]

print(names_list)


#using lambda to calculate slope
# Lambda to calculate slope or y-intercept
linear_solver = lambda x1, y1, x2, y2, calc: (y2 - y1) / (x2 - x1) if calc == 'slope' else y1 - ((y2 - y1) / (x2 - x1)) * x1

# Example usage
point1 = (1, 2)
point2 = (4, 8)

# Calculate slope
slope = linear_solver(*point1, *point2, 'slope')
print(f"Slope: {slope}")

# Calculate y-intercept
y_intercept = linear_solver(*point1, *point2, 'intercept')
print(f"Y-Intercept: {y_intercept}")


