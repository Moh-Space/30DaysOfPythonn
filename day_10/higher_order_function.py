#change the First letter of every country

countries = ['Afghanistan', 'Finland', 'Iceland', 'Ireland', 'Swaziland', 'Thailand', 'Poland']
countries_uppercase = list(map(str.upper, countries))
print("Countries in uppercase:", countries_uppercase)

numbers = [1, 2, 3, 4, 5]
numbers_squared = list(map(lambda x: x**2, numbers))
print("Squared numbers:", numbers_squared)


names = ['Alice', 'Bob', 'Charlie']
names_uppercase = list(map(str.upper, names))
print("Names in uppercase:", names_uppercase)


countries_with_land = list(filter(lambda x: 'land' in x, countries))
print("Countries containing 'land':", countries_with_land)


countries_six_chars = list(filter(lambda x: len(x) == 6, countries))
print("Countries with exactly six characters:", countries_six_chars)


countries_six_or_more = list(filter(lambda x: len(x) >= 6, countries))
print("Countries with six or more letters:", countries_six_or_more)


countries_starting_e = list(filter(lambda x: x.startswith('E'), countries))
print("Countries starting with 'E':", countries_starting_e)


even_squares = list(filter(lambda x: x % 2 == 0, map(lambda x: x**2, numbers)))
print("Even squares:", even_squares)


def get_string_lists(lst):
    return list(filter(lambda x: isinstance(x, str), lst))

mixed_list = [1, 'hello', 3.14, 'world', True, 'Python']
string_items = get_string_lists(mixed_list)
print("String items:", string_items)


from functools import reduce
sum_numbers = reduce(lambda x, y: x + y, numbers)
print("Sum of all numbers:", sum_numbers)


def country_count_by_letter(countries):
    result = {}
    for country in countries:
        first_letter = country[0]
        if first_letter in result:
            result[first_letter] += 1
        else:
            result[first_letter] = 1
    return result


countries = [
    'Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola', 'Antigua and Barbuda', 
    'Argentina', 'Armenia', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas', 
    'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 
    'Bhutan', 'Bolivia', 'Bosnia and Herzegovina', 'Botswana', 'Brazil', 'Brunei', 
    'Bulgaria', 'Burkina Faso', 'Burundi', 'Cambodia', 'Cameroon', 'Canada', 
    'Cape Verde', 'Central African Republic', 'Chad', 'Chile', 'China', 'Colombia', 
    'Comoros', 'Congo (Brazzaville)', 'Congo', 'Costa Rica', "Cote d'Ivoire", 
    'Croatia', 'Cuba', 'Cyprus', 'Czech Republic', 'Denmark', 'Djibouti', 'Dominica', 
    'Dominican Republic', 'East Timor (Timor Timur)', 'Ecuador', 'Egypt', 
    'El Salvador', 'Equatorial Guinea', 'Eritrea', 'Estonia', 'Ethiopia', 'Fiji', 
    'Finland', 'France', 'Gabon', 'Gambia, The', 'Georgia', 'Germany', 'Ghana', 
    'Greece', 'Grenada', 'Guatemala', 'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti', 
    'Honduras', 'Hungary', 'Iceland', 'India', 'Indonesia', 'Iran', 'Iraq', 'Ireland', 
    'Israel', 'Italy', 'Jamaica', 'Japan', 'Jordan', 'Kazakhstan', 'Kenya', 'Kiribati', 
    'Korea, North', 'Korea, South', 'Kuwait', 'Kyrgyzstan', 'Laos', 'Latvia', 
    'Lebanon', 'Lesotho', 'Liberia', 'Libya', 'Liechtenstein', 'Lithuania', 
    'Luxembourg', 'Macedonia', 'Madagascar', 'Malawi', 'Malaysia', 'Maldives', 
    'Mali', 'Malta', 'Marshall Islands', 'Mauritania', 'Mauritius', 'Mexico', 
    'Micronesia', 'Moldova', 'Monaco', 'Mongolia', 'Morocco', 'Mozambique', 
    'Myanmar', 'Namibia', 'Nauru', 'Nepal', 'Netherlands', 'New Zealand', 'Nicaragua', 
    'Niger', 'Nigeria', 'Norway', 'Oman', 'Pakistan', 'Palau', 'Panama', 'Papua New Guinea', 
    'Paraguay', 'Peru', 'Philippines', 'Poland', 'Portugal', 'Qatar', 'Romania', 
    'Russia', 'Rwanda', 'Saint Kitts and Nevis', 'Saint Lucia', 'Saint Vincent', 
    'Samoa', 'San Marino', 'Sao Tome and Principe', 'Saudi Arabia', 'Senegal', 
    'Serbia and Montenegro', 'Seychelles', 'Sierra Leone', 'Singapore', 'Slovakia', 
    'Slovenia', 'Solomon Islands', 'Somalia', 'South Africa', 'Spain', 'Sri Lanka', 
    'Sudan', 'Suriname', 'Swaziland', 'Sweden', 'Switzerland', 'Syria', 'Taiwan', 
    'Tajikistan', 'Tanzania', 'Thailand', 'Togo', 'Tonga', 'Trinidad and Tobago', 
    'Tunisia', 'Turkey', 'Turkmenistan', 'Tuvalu', 'Uganda', 'Ukraine', 
    'United Arab Emirates', 'United Kingdom', 'United States', 'Uruguay', 'Uzbekistan', 
    'Vanuatu', 'Vatican City', 'Venezuela', 'Vietnam', 'Yemen', 'Zambia', 'Zimbabwe'
]

def get_first_ten_countries(countries):
    return countries[:10]
def get_last_ten_countries(countries):
    return countries[-10:]

count_by_letter = country_count_by_letter(countries)
print("Country count by starting letter:", count_by_letter)

# Get the first ten countries
first_ten = get_first_ten_countries(countries)
print("First ten countries:", first_ten)

# Get the last ten countries
last_ten = get_last_ten_countries(countries)
print("Last ten countries:", last_ten)

