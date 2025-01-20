#exercise 1
#to know the version of your python

import sys, math

print(sys.version)


addition = 3 + 4
print(addition)

subtraction = 3 - 4
print(subtraction)

multiplication = 3 * 4
print(multiplication)

modulus = 3 % 4
print(modulus)

division = 3/4
print(division)

exponential = 3**4
print(exponential)

floor_division = 3//4
print(floor_division)


my_name = "Muhammad Auwal"
family_name = "Asimi"
country = "Nigeria"
" i am enjoying 30 days of python"


#exercise 2
print(type(10))
print(type(9.8))
print(type(3.14))
print(type(4-4j))
print(type(['Asabeneh', 'Python', 'Finland']))
print(type("Muhammad Auwal"))
print(type("Asimi"))
print(type("Nigeria"))

#example of different python data types
integer, float_num, complex_num = 5, 2.3, 4 - 4j
string = "Muhammad Auwal"
Boolean = True or False
List = ['Abdulhamid','Auwal','ruqayyah','salim', 'Anty Zully','muktar']
dictionary = {'name': 'Alice', 'age': 30, 'city': 'New York'}
turple = {'food','money','health','happiness','enjoyment',2.3,True}
my_set = {1,2.3,4,5,6}

print(integer, float_num, complex_num, string, Boolean, dictionary, turple, my_set)


#to find euclidian distance  between (2,3) and (10,8)
#using formular 
x1, y1 = 2,3
x2, y2 = 10,8

Euclidian_distance = math.sqrt((x2-x1)**2 + (y2 - y1)**2)
print("the Euclidian Distance is: ", Euclidian_distance)

