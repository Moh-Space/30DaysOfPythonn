##Day 2: 30 Days of Python programming
first_name = "Muhammad"
last_name = "Auwal"
full_name = "Muhammad Auwal"
country_code = 234
city = "yola"
age = 30
year = 2025
is_married = "No"
is_true = "Yeah"
is_light_on = "yes"
my_hero, school, hobby, likes, deslikes, favourite_smart_phone = "My_Dad", "BUK", "Learning_Researching_coding", "honesty", "fake people", "Samsung S4 Ultra"


print(type(first_name))
print(type(last_name))


#comparing the length of first_name and last_name

if len(first_name) > len(last_name):
    print("first_name is longer than last_name.")
elif len(first_name) < len(last_name):
    print("last_name is longer than first_name.")
else:
    print("Both names have the same length.")

num_one = 5
num_two = 4
total = (num_one + num_two)
diff = (num_one - num_two)
product = (num_one * num_two)
division = (num_one / num_two)
remainder = (num_one % num_two)
exp = (num_one ** num_two)
floor_division = (num_one // num_two)

#calculating radius of a circle

pi = 3.14
radius = 30
radius = float(input("enter the value for radius: "))
area_of_circle = pi * radius ** 2
#print("the area is: ",(area_of_circle))


#calculating circumference of a circle


pi = 3.14
radius = 30
radius = radius = float(input("enter the value for radius: "))
circum_of_circle = 2*pi*radius
#print("the circumference is: ",(circum_of_circle))


#using builtin functions to function to get first name, last name, country and age from a user

f_name = input("enter your first name: ")
l_name = input("enter your last name: ")
country = input("enter the name of your country: ")
age = int(input("what is your age: "))
#print(f_name, l_name, country, age)
