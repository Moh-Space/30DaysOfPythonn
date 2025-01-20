my_age = 50
my_height = 5.7
complex_num = 1j


#a script that prompts the user to enter the base and height of the triangle and calculate an area of this triangle (area =0.5*b*h)
print("***** Area of Triangle *****")
Base = int(input("enter the base of the triangle: "))
height = int(input("enter the height of the triangle: "))
area_of_triangle = Base*height
print("the Area of a Triangle is: ",area_of_triangle)

#a script for perimeter of a triangle


print("***** Perimeter of Triangle *****")
side_A = int(input("enter side A: "))
side_B = int(input("enter side B: "))
side_C = int(input("enter side C: "))
perimeter_of_triangle = side_A+side_B+side_C
print("the Perimeter of a Triangle is: ",perimeter_of_triangle)


#a script to get the length and width of a triangle

lngt = int(input("enter the length of the triangle: "))
wdth = int(input("enter the width of the triangle: "))
area_of_triangle = lngt*wdth
perimeter = 2*(lngt*wdth)
print ("The Area of a Triangle is: ", area_of_triangle)
print("the perimeter of a trinagle is: ",2*(lngt*wdth))

#radius of a circle

import math
pi = 3.14
r = int(input("Enter the value of a radius: "))
area_of_circle = pi*r*r
print("The Area of a circle is: ", area_of_circle)

#script to find a slope

x1,y1 = 2,2
x2,y2 = 6,10

slope = (y2 - y1/x2 - x1)
ED = math.sqrt(x2-x1)+(y2-y1)
print ("The Euclidian Distance is: ",ED)
print("The Slope is: ",slope)


#comparing the slope Euclidean Distance

if ED > slope:
    print("Euclidean Distance is greater than Slope")
else:
    print("Slope is greater than ED")


#calculating the value of Y

x = -9
y = x**2 + 6*x + 9

print("The value of Y is: ",y)


#finding the lenght of pyton and dragon

word_1 = "python"
word_2 = "dragon"
len(word_1)
len(word_2)
compare = (word_2 == word_1)
print(compare)

if "on" in word_1 and "on" in word_2:
    print("The word ON is in " ,word_1, word_2)
else:
    print("The word ON is not found in ", word_1, word_2)
    
#checking sentence

sentence = "I hope this course is not full of jargon"
if "jargon" in sentence:
    print("The word jargon is found in ", sentence)
else:
    print("word not found in ", sentence)

print("on" in word_1)
print('on' in word_2)


#finfing and converting length
py_length = len("python")  

# Convert the length to float
length_as_float = float(py_length)  

length_as_string = str(length_as_float)  

print("Length:", py_length)
print("Length as float:", length_as_float)
print("Length as string:", length_as_string)

# Input a number
number = int(input("Enter a number: "))

# Check if the number is even
if number % 2 == 0:
    print(f"{number} is even.")
else:
    print(f"{number} is not even.")


#prompt to calculate employee pay

Num_of_hours = int(input("enter the number of hours you worked: "))
rate = float(input("enter your hourly rate: "))
pay = (Num_of_hours * rate)
print(pay)


#
SECONDS_IN_A_YEAR = 365 * 24 * 60 * 60  # Number of seconds in a year
LIFESPAN_YEARS = 100  # Longest lifespan

years = int(input("Enter the number of years: "))


if years > LIFESPAN_YEARS:
    print(f"A person cannot live more than {LIFESPAN_YEARS} years!")
else:
    seconds_lived = years * SECONDS_IN_A_YEAR
    print(f"In {years} years, a person can live approximately {seconds_lived} seconds.")

#A Python script to print number

ones = ("1 1 1 1 1\n2 1 2 4 8\n3 1 3 9 27\n4 1 4 16 64\n5 1 5 25 125")
print(ones)

floor_div = (7//3)
int_value = int(2.7)
if floor_div == int_value:
    print("the value are the same")
else:
    print("is not the same")


# Check if the type of '10' is equal to the type of 10
deci_num = type('10') == type(10)
print("Is the type of '10' equal to the type of 10?:", deci_num)

# Check if int('9.8') is equal to 10
try:
    result2 = int('9.8') == 10
except ValueError:
    result2 = "Error: Cannot convert '9.8' to an integer."
print("Is int('9.8') equal to 10?:", result2)

