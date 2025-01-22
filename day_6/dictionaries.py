# Create an empty dictionary called dog
dog = {}

# Add name, color, breed, legs, age to the dog dictionary
dog['name'] = 'Buddy'
dog['color'] = 'Brown'
dog['breed'] = 'Golden Retriever'
dog['legs'] = 4
dog['age'] = 5

# Create a student dictionary
student = {
    'first_name': 'Muhammad',
    'last_name': 'Auwal',
    'gender': 'Male',
    'age': 20,
    'marital_status': 'Single',
    'skills': ['Python', 'JavaScript'],
    'country': 'Nigeria',
    'city': 'Adamawa',
    'address': 'Sarki Yamma Aliyu Street Yola Town',
}

# length of the student dictionary
student_length = len(student)
print("Length of the student dictionary:", student_length)

# value of skills and check the data type
skills = student['skills']
print("Skills:", skills)
print("Data type of skills:", type(skills))  

# Modify the skills values by adding one or two skills
student['skills'].extend(['HTML', 'CSS'])
print("Updated skills:", student['skills'])

# Get the dictionary keys as a list
keys = list(student.keys())
print("Keys:", keys)

# Get the dictionary values as a list
values = list(student.values())
print("Values:", values)

# Change the dictionary to a list of tuples using items() method
items = list(student.items())
print("List of tuples:", items)

# Delete one of the items in the dictionary
del student['address']
print(student)

# Delete one of the dictionaries (e.g. dog)
del dog
print("Dog dictionary deleted")
