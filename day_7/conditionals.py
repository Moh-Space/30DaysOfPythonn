#checking driving age

age = int(input("Enter your age: "))

if age >= 18:
    print("You are old enough to drive.")
else:
    years_to_wait = 18 - age
    print(f"You need to wait {years_to_wait} more year(s) to drive.")

#comparing ages


my_age = int(input("Enter my age: "))
your_age = int(input("Enter your age: "))

if my_age > your_age:
    difference = my_age - your_age
    if difference == 1:
        print(f"I am older than you by {difference} year.")
    else:
        print(f"I am older than you by {difference} years.")
elif my_age < your_age:
    difference = your_age - my_age
    if difference == 1:
        print(f"You are older than me by {difference} year.")
    else:
        print(f"You are older than me by {difference} years.")
else:
    print("We are the same age!")

#comparing Numbers
a = float(input("Enter the first number (a): "))
b = float(input("Enter the second number (b): "))

if a > b:
    print("a is greater than b.")
elif a < b:
    print("a is smaller than b.")
else:
    print("a is equal to b.")

#grading students using chained expression/comparison

score = int(input("Enter the student's score: "))

if 80 <= score <= 100:
    grade = 'A'
elif 70 <= score <= 79:
    grade = 'B'
elif 60 <= score <= 69:
    grade = 'C'
elif 50 <= score <= 59:
    grade = 'D'
elif 0 <= score <= 49:
    grade = 'F'
else:
    grade = "Invalid score. Please enter a number between 0 and 100."

print(f"The student's grade is: {grade}")



#weather Check

month = input("Enter the month: ").strip().capitalize()

if month in ["September", "October", "November"]:
    season = "Autumn"
elif month in ["December", "January", "February"]:
    season = "Winter"
elif month in ["March", "April", "May"]:
    season = "Spring"
elif month in ["June", "July", "August"]:
    season = "Summer"
else:
    season = "Invalid month. Please enter a valid month name."

print(f"The season is: {season}")


fruits = ['banana', 'orange', 'mango', 'lemon']

fruit_to_check = input("Enter a fruit: ").strip().lower()

if fruit_to_check in fruits:
    print("That fruit already exists in the list.")
else:
    fruits.append(fruit_to_check)
    print(f"{fruit_to_check.capitalize()} has been added to the list.")
    print("The updated list of fruits:", fruits)


person = {
    'first_name': 'Muhammad',
    'last_name': 'Auwal',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

output = []

# Check if the person dictionary has 'skills' key
if 'skills' in person:
    # Add the middle skill
    skills = person['skills']
    middle_skill = skills[len(skills) // 2]
    output.append(f"The middle skill is: {middle_skill}")
    
    # Add Python skill check result
    has_python = 'Python' in skills
    output.append(f"Has Python skill: {has_python}")
    
    # Determine the type of developer
    if skills == ['JavaScript', 'React']:
        output.append("He is a front end developer")
    elif 'Node' in skills and 'Python' in skills and 'MongoDB' in skills:
        output.append("He is a backend developer")
    elif 'React' in skills and 'Node' in skills and 'MongoDB' in skills:
        output.append("He is a fullstack developer")
    else:
        output.append("Unknown title")
        
# Check if the person is married and lives in Finland
if person['is_marred'] and person['country'] == 'Finland':
    output.append(f"{person['first_name']} {person['last_name']} lives in Finland. He is married.")

# Print all output in one line
print(output)
