

print("Iterating 0 to 10 using for loop:")
for i in range(11):
    print(i, end=" ")
print() 

print("Iterating 0 to 10 using while loop:")
i = 0
while i <= 10:
    print(i, end=" ")
    i += 1
print()  


for i in range(1, 8):  # Loop from 1 to 7
    print('#' * i)


for i in range(8): 
    for j in range(8):  
        print('#', end=' ')  
    print() 


# Loop from 0 to 10
for i in range(11):  
    print(f"{i} x {i} = {i * i}")

#Iterating through Items
items = ['Python', 'Numpy', 'Pandas', 'Django', 'Flask']
for item in items:
    print(item)


#printing even numbers
for i in range(0, 101):
    if i % 2 == 0:
        print(i, end=' ')  
print()


# Print odd numbers on the same line
for i in range(0, 101):
    if i % 2 != 0:
        print(i, end=' ')  
print() 


sum_evens = 0  # Initialize sum for even numbers
sum_odds = 0   # Initialize sum for odd numbers

for i in range(101):  # Iterate from 0 to 100
    if i % 2 == 0:    # Check if the number is even
        sum_evens += i
    else:             # If the number is odd
        sum_odds += i

print("The sum of all even numbers from 0 to 100 is:", sum_evens)
print("The sum of all odd numbers from 0 to 100 is:", sum_odds)


#printing in reversed order
fruits = ['banana', 'orange', 'mango', 'lemon']
for i in range(len(fruits) // 2):
    fruits[i], fruits[-i - 1] = fruits[-i - 1], fruits[i] 

print("Reversed list:", fruits)



#Languages count


# Extract countries containing the word "land"
countries = [
    'Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola', 
    'Antigua and Barbuda', 'Argentina', 'Armenia', 'Australia', 
    'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh', 
    'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bhutan', 
    'Bolivia', 'Bosnia and Herzegovina', 'Botswana', 'Brazil', 
    'Brunei', 'Bulgaria', 'Burkina Faso', 'Burundi', 'Cambodia', 
    'Cameroon', 'Canada', 'Cape Verde', 'Central African Republic', 
    'Chad', 'Chile', 'China', 'Colombi', 'Comoros', 'Congo (Brazzaville)', 
    'Congo', 'Costa Rica', "Cote d'Ivoire", 'Croatia', 'Cuba', 'Cyprus', 
    'Czech Republic', 'Denmark', 'Djibouti', 'Dominica', 
    'Dominican Republic', 'East Timor (Timor Timur)', 'Ecuador', 'Egypt', 
    'El Salvador', 'Equatorial Guinea', 'Eritrea', 'Estonia', 'Ethiopia', 
    'Fiji', 'Finland', 'France', 'Gabon', 'Gambia, The', 'Georgia', 
    'Germany', 'Ghana', 'Greece', 'Grenada', 'Guatemala', 'Guinea', 
    'Guinea-Bissau', 'Guyana', 'Haiti', 'Honduras', 'Hungary', 'Iceland', 
    'India', 'Indonesia', 'Iran', 'Iraq', 'Ireland', 'Israel', 'Italy', 
    'Jamaica', 'Japan', 'Jordan', 'Kazakhstan', 'Kenya', 'Kiribati', 
    'Korea, North', 'Korea, South', 'Kuwait', 'Kyrgyzstan', 'Laos', 
    'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libya', 'Liechtenstein', 
    'Lithuania', 'Luxembourg', 'Macedonia', 'Madagascar', 'Malawi', 
    'Malaysia', 'Maldives', 'Mali', 'Malta', 'Marshall Islands', 
    'Mauritania', 'Mauritius', 'Mexico', 'Micronesia', 'Moldova', 'Monaco', 
    'Mongolia', 'Morocco', 'Mozambique', 'Myanmar', 'Namibia', 'Nauru', 
    'Nepal', 'Netherlands', 'New Zealand', 'Nicaragua', 'Niger', 'Nigeria', 
    'Norway', 'Oman', 'Pakistan', 'Palau', 'Panama', 'Papua New Guinea', 
    'Paraguay', 'Peru', 'Philippines', 'Poland', 'Portugal', 'Qatar', 
    'Romania', 'Russia', 'Rwanda', 'Saint Kitts and Nevis', 'Saint Lucia', 
    'Saint Vincent', 'Samoa', 'San Marino', 'Sao Tome and Principe', 
    'Saudi Arabia', 'Senegal', 'Serbia and Montenegro', 'Seychelles', 
    'Sierra Leone', 'Singapore', 'Slovakia', 'Slovenia', 'Solomon Islands', 
    'Somalia', 'South Africa', 'Spain', 'Sri Lanka', 'Sudan', 'Suriname', 
    'Swaziland', 'Sweden', 'Switzerland', 'Syria', 'Taiwan', 'Tajikistan', 
    'Tanzania', 'Thailand', 'Togo', 'Tonga', 'Trinidad and Tobago', 
    'Tunisia', 'Turkey', 'Turkmenistan', 'Tuvalu', 'Uganda', 'Ukraine', 
    'United Arab Emirates', 'United Kingdom', 'United States', 'Uruguay', 
    'Uzbekistan', 'Vanuatu', 'Vatican City', 'Venezuela', 'Vietnam', 
    'Yemen', 'Zambia', 'Zimbabwe'
]


countries_with_land = [country for country in countries if 'land' in country]

# Print the result
print("Countries containing 'land':", countries_with_land)


