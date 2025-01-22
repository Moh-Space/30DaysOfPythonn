# empty list
empty_list = []

# Declaring a list with more than 5 items
fruits = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig']

# Finding the length of the list
length_of_fruits = len(fruits)
print("Length of the fruits list:", length_of_fruits)

# Get the first item, middle item, and last item of the list
first_item = fruits[0]
middle_item = fruits[len(fruits) // 2]
last_item = fruits[-1]

print("First item:", first_item)
print("Middle item:", middle_item)
print("Last item:", last_item)

# mixed_data_types
mixed_data_types = ['John Doe', 25, 5.9, 'Single', '123 Main Street, Springfield']
print("Mixed data types list:", mixed_data_types)


# Declare the list
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

# Print the list
print("IT Companies List:", it_companies)

# Print the number of companies in the list
number_of_companies = len(it_companies)
print("Number of companies:", number_of_companies)

# Print the first, middle, and last company
first_company = it_companies[0]
middle_company = it_companies[len(it_companies) // 2]
last_company = it_companies[-1]

print("First company:", first_company)
print("Middle company:", middle_company)
print("Last company:", last_company)

# Modify one of the companies
it_companies[1] = 'Alphabet'  # Changing 'Google' to 'Alphabet'
print("List after modification:", it_companies)

# Add an IT company to the list
it_companies.append('Tesla')
print("List after adding a company:", it_companies)

# Insert an IT company in the middle of the list
middle_index = len(it_companies) // 2
it_companies.insert(middle_index, 'Spotify')
print("List after inserting a company in the middle:", it_companies)

# Changing of the it_companies names to uppercase (excluding IBM)
it_companies[0] = it_companies[0].upper()
print("List after changing a name to uppercase:", it_companies)

# Join the it_companies with '#; '
joined_companies = '#; '.join(it_companies)
print("Joined companies:", joined_companies)

# Check if a certain company exists in the list
company_to_check = 'Oracle'
exists = company_to_check in it_companies
print(f"Does {company_to_check} exist in the list? {exists}")


# Declaring the list
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

# Sort the list
it_companies.sort()
print("Sorted list:", it_companies)

# Reverse the list in descending order
it_companies.reverse()
print("Reversed list (descending):", it_companies)

# Slice out the first 3 companies
first_three_companies = it_companies[:3]
print("First three companies:", first_three_companies)

# Slice out the last 3 companies
last_three_companies = it_companies[-3:]
print("Last three companies:", last_three_companies)

# Slice out the middle IT company or companies
middle_index = len(it_companies) // 2
if len(it_companies) % 2 == 0:
    middle_companies = it_companies[middle_index - 1:middle_index + 1]  # Two middle companies
else:
    middle_companies = [it_companies[middle_index]]  # Single middle company
print("Middle IT company/companies:", middle_companies)

# Remove the first IT company from the list
it_companies.pop(0)
print("List after removing the first company:", it_companies)

# Remove the middle IT company or companies from the list
middle_index = len(it_companies) // 2
if len(it_companies) % 2 == 0:
    del it_companies[middle_index - 1:middle_index + 1]  # Remove two middle companies
else:
    del it_companies[middle_index]
print("List after removing the middle company/companies:", it_companies)

# Remove the last IT company from the list
it_companies.pop(-1)
print("List after removing the last company:", it_companies)

# Removing all
it_companies.clear()
print("List after removing all companies:", it_companies)

# Destroy the IT companies list using try and except exception method
del it_companies
try:
    print(it_companies)
except NameError:
    print("The IT companies list has been destroyed.")

# Joining list using + operator
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']
full_stack = front_end + back_end
print(full_stack)

# List of ages
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# 1. Sort the list and find the min and max age
ages.sort()
min_age = min(ages)
max_age = max(ages)
print("Sorted ages:", ages)
print("Minimum age:", min_age)
print("Maximum age:", max_age)


ages.append(min_age)
ages.append(max_age)
print("Ages after adding min and max again:", ages)


ages.sort()  
n = len(ages)
if n % 2 == 0:
    median_age = (ages[n // 2 - 1] + ages[n // 2]) / 2 
else:
    median_age = ages[n // 2]
print("Median age:", median_age)

average_age = sum(ages) / len(ages)
print("Average age:", average_age)

#Find the range of ages
age_range = max_age - min_age
print("Range of ages:", age_range)

min_avg_diff = abs(min_age - average_age)
max_avg_diff = abs(max_age - average_age)
print("Absolute difference (min - average):", min_avg_diff)
print("Absolute difference (max - average):", max_avg_diff)


# 1. Create an empty tuple
empty_tuple = ()
print("Empty tuple:", empty_tuple)

# 2. Create tuples containing names of sisters and brothers
sisters = ('Aisha', 'Fatima', 'Maryam')
brothers = ('Ahmed', 'Khalid', 'Musa')

# 3. Join brothers and sisters tuples and assign it to siblings
siblings = sisters + brothers
print("Siblings:", siblings)

# 4. How many siblings do you have?
number_of_siblings = len(siblings)
print("Number of siblings:", number_of_siblings)

# 5. Modify the siblings tuple to add father and mother and assign it to family_members
family_members = siblings + ('My Dad', 'My Mum')
print("Family members:", family_members)



#EXERCISE LEVEL 2
countries = [
    'Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola', 'Antigua and Barbuda',
    'Argentina', 'Armenia', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain',
    'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bhutan', 'Bolivia',
    'Bosnia and Herzegovina', 'Botswana', 'Brazil', 'Brunei', 'Bulgaria', 'Burkina Faso',
    'Burundi', 'Cambodia', 'Cameroon', 'Canada', 'Cape Verde', 'Central African Republic',
    'Chad', 'Chile', 'China', 'Colombi', 'Comoros', 'Congo (Brazzaville)', 'Congo', 
    'Costa Rica', "Cote d'Ivoire", 'Croatia', 'Cuba', 'Cyprus', 'Czech Republic', 'Denmark',
    'Djibouti', 'Dominica', 'Dominican Republic', 'East Timor (Timor Timur)', 'Ecuador',
    'Egypt', 'El Salvador', 'Equatorial Guinea', 'Eritrea', 'Estonia', 'Ethiopia', 'Fiji',
    'Finland', 'France', 'Gabon', 'Gambia, The', 'Georgia', 'Germany', 'Ghana', 'Greece',
    'Grenada', 'Guatemala', 'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti', 'Honduras',
    'Hungary', 'Iceland', 'India', 'Indonesia', 'Iran', 'Iraq', 'Ireland', 'Israel', 'Italy',
    'Jamaica', 'Japan', 'Jordan', 'Kazakhstan', 'Kenya', 'Kiribati', 'Korea, North',
    'Korea, South', 'Kuwait', 'Kyrgyzstan', 'Laos', 'Latvia', 'Lebanon', 'Lesotho', 'Liberia',
    'Libya', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Macedonia', 'Madagascar', 'Malawi',
    'Malaysia', 'Maldives', 'Mali', 'Malta', 'Marshall Islands', 'Mauritania', 'Mauritius',
    'Mexico', 'Micronesia', 'Moldova', 'Monaco', 'Mongolia', 'Morocco', 'Mozambique',
    'Myanmar', 'Namibia', 'Nauru', 'Nepal', 'Netherlands', 'New Zealand', 'Nicaragua',
    'Niger', 'Nigeria', 'Norway', 'Oman', 'Pakistan', 'Palau', 'Panama', 'Papua New Guinea',
    'Paraguay', 'Peru', 'Philippines', 'Poland', 'Portugal', 'Qatar', 'Romania', 'Russia',
    'Rwanda', 'Saint Kitts and Nevis', 'Saint Lucia', 'Saint Vincent', 'Samoa', 'San Marino',
    'Sao Tome and Principe', 'Saudi Arabia', 'Senegal', 'Serbia and Montenegro', 'Seychelles',
    'Sierra Leone', 'Singapore', 'Slovakia', 'Slovenia', 'Solomon Islands', 'Somalia',
    'South Africa', 'Spain', 'Sri Lanka', 'Sudan', 'Suriname', 'Swaziland', 'Sweden',
    'Switzerland', 'Syria', 'Taiwan', 'Tajikistan', 'Tanzania', 'Thailand', 'Togo', 'Tonga',
    'Trinidad and Tobago', 'Tunisia', 'Turkey', 'Turkmenistan', 'Tuvalu', 'Uganda', 'Ukraine',
    'United Arab Emirates', 'United Kingdom', 'United States', 'Uruguay', 'Uzbekistan',
    'Vanuatu', 'Vatican City', 'Venezuela', 'Vietnam', 'Yemen', 'Zambia', 'Zimbabwe'
]
# Find the middle index

middle_index = len(countries) // 2

# Get the middle country
middle_country = countries[middle_index]

print("The middle country is:", middle_country)

# Given list of countries
countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']

# Dividing the list into two parts
mid_index = len(countries) // 2
if len(countries) % 2 == 0:
    first_half = countries[:mid_index]
    second_half = countries[mid_index:]
else:
    first_half = countries[:mid_index + 1]
    second_half = countries[mid_index + 1:]

# Unpacking the first three countries and the rest as Scandic countries

countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']

mid_index = len(countries) // 2
if len(countries) % 2 == 0:
    first_half = countries[:mid_index]
    second_half = countries[mid_index:]
else:
    first_half = countries[:mid_index + 1]
    second_half = countries[mid_index + 1:]

# Unpacking the first three countries and the rest as Scandic countries
first, second, third, *scandic_countries = countries

# Printing the results
print("First half of the list:", first_half)
print("Scandic countries:", scandic_countries)


# Unpacking siblings and parents from family_members
family_members = ('John', 'Jane', 'Tom', 'Lucy', 'Paul', 'Mary')
siblings = family_members[2:4]  # Tom and Lucy
parents = family_members[:2]  # John and Jane

# Create fruits, vegetables, and animal products tuples
fruits = ('apple', 'banana', 'orange')
vegetables = ('carrot', 'potato', 'spinach')
animal_products = ('milk', 'egg', 'cheese')

# Joining three tuples
food_stuff_tp = fruits + vegetables + animal_products

# Converting the tuple to a list
food_stuff_lt = list(food_stuff_tp)

# Slice out the middle item(s) from the tuple or list
middle_item_tuple = food_stuff_tp[len(food_stuff_tp)//2] 
middle_item_list = food_stuff_lt[len(food_stuff_lt)//2]  

# Slicing out the first three items and last three items from the list
first_three_items = food_stuff_lt[:3]
last_three_items = food_stuff_lt[-3:]

# Deleting the food_stuff_tp tuple completely
del food_stuff_tp


nordic_countries = ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden')

# Check if 'Estonia' is a nordic country
print('Estonia' in nordic_countries)  # This will return False

# Check if 'Iceland' is a nordic country
print('Iceland' in nordic_countries)  # This will return True


it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}

# Length of the set
print(len(it_companies))

# Adding 'Twitter' to the set
it_companies.add('Twitter')
print(it_companies)

# Adding multiple IT companies
it_companies.update({'Netflix', 'Spotify', 'Snapchat'})
print(it_companies)


# Remove a company, e.g., 'Facebook'
it_companies.remove('Facebook')
print(it_companies)


A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}

# Union of A and B
union_AB = A .union(B)  
print(union_AB)

# Intersection of A and B
intersection_AB = A & B  
print(intersection_AB)

# Check if A is a subset of B
is_subset = A.issubset(B)
print(is_subset)

# Check if A and B are disjoint sets
are_disjoint = A.isdisjoint(B)
print(are_disjoint)

# Union of A with B and B with A (order doesn't matter)
union_A_B = A | B
union_B_A = B | A  # Same as union_A_B
print(union_A_B, union_B_A)

# Symmetric difference between A and B
symmetric_difference = A ^ B  # or A.symmetric_difference(B)
print(symmetric_difference)

# Deleting the sets
del A
del B
#set A and B have been deleted


ages = [22, 19, 24, 25, 26, 24, 25, 24]
ages_set = set(ages)

print("Length of the list:", len(ages))
print("Length of the set:", len(ages_set))

# Compare the lengths
if len(ages) > len(ages_set):
    print("The list is bigger.")
else:
    print("they are the same size.")


#String: A sequence of characters, used for storing textual data. It is immutable, meaning it cannot be changed once created.
#Example: 'hello'

#List: A collection of ordered items that can be of different types. Lists are mutable, meaning their elements can be modified.
#Example: [1, 2, 3, 'apple']

#Tuple: Similar to a list but immutable. Once created, the items in a tuple cannot be changed, added, or removed.
#Example: (1, 2, 3)

#Set: A collection of unordered unique items. It does not allow duplicate values and is also mutable.
#Example: {1, 2, 3}


sentence = "I am a teacher and I love to inspire and teach people."
words = sentence.split()  # Split the sentence into words
unique_words = set(words)  # Convert to a set to get unique words

print("Unique words:", unique_words)
print("Number of unique words:", len(unique_words))








