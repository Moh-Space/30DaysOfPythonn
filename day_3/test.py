# Check if the type of '10' is equal to the type of 10
result1 = type('10') == type(10)
print("Is the type of '10' equal to the type of 10?:", result1)

# Check if int('9.8') is equal to 10
try:
    result2 = int('9.8') == 10
except ValueError:
    result2 = "Error: Cannot convert '9.8' to an integer."
print("Is int('9.8') equal to 10?:", result2)
