# Concatenate using the + operator
word = 'Thirty' + ' ' + 'Days' + ' ' + 'Of' + ' ' + 'Python'
print(word)

# Concatenating using join()
word2 = ' '.join(['Thirty', 'Days', 'Of', 'Python'])
print(word2)

# Concatenating using + operator
word3 = 'Coding' + ' ' + 'FOr' + ' ' + 'All'
print(word3)

# Define the variable
company = "Coding for All"
print(company)


# Length of the variable
company = "Coding for All"
print(len(company))

# Uppercasing of the variable
company = "Coding for All"
print(company.upper())

# Uppercasing of the variable
company = "Coding for All"
print(company.lower())

# Camel-casing
company = "Coding for All"
print(company.capitalize())

company = "Coding for All"
print(company.swapcase())

# slicing
word_to_slice = "Coding For All"
slicing = word_to_slice[:word_to_slice.find(" ")]

print("sliced word:", slicing)

# Using 'in' to check if 'Coding' exists

word_check = "Coding For All"
if "Coding" in word_check:
    print("The word 'Coding' is found.")
else:
    print("The word 'Coding' is not found.")

# replacing
word_to_replace = "Coding For All"
new_word = word_to_replace.replace("Coding", "Python")
print(new_word)


# Original string
text = "Python for Everyone"
new_text = text.replace("All", "Everyone")
print(new_text)


sentence = "Python for All"
split_text = (sentence.split())
print(split_text)

Tech_Giants = ("Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon")
splitting = Tech_Giants.split()
print (splitting)

# Indexing
checks = "Coding For All"
indexing = checks[0]
print(indexing)

# Indexing
checks = "Coding For All"
indexing = checks[-1]
print(indexing)

# Indexing
checks = "Coding For All"
indexing = checks[10]
print(indexing)


# Accronyming
Words = "Python For Everyone"
acronym = ''.join(word[0] for word in Words.split())
print(acronym)

#Accronyming 2
accronym = "Coding For All"
Accronym_arrangement = ''.join(word[0]for word in accronym.split())
print(Accronym_arrangement)


# Inddexing Words
text = "Coding For All"

index_F = text.index('F')
print(index_F)

text = "Coding For All"
index_C = text.index('C')
print(index_C)


# rFinding
text = "Coding For All People"
lastindex_of_l = text.rfind('l')
print(lastindex_of_l)

# Original sentence
sentence = "You cannot end a sentence with because because because is a conjunction"
first_occurrence_find = sentence.find("because")
print("Using find():", first_occurrence_find)
first_occurrence_index = sentence.index("because")
print("Using index():", first_occurrence_index)


# Original sentence
sentence = "You cannot end a sentence with because because because is a conjunction"

last_occurrence = sentence.rindex("because")
print("The last occurrence of 'because' is at index: ", last_occurrence)

# Slicing Words
sentence = "You cannot end a sentence with because because because is a conjunction"
start_index = sentence.find("because because because")
end_index = start_index + len("because because because")
sliced_sentence = sentence[:start_index] + sentence[end_index:]
print(sliced_sentence)

# using startswith()
text = "Coding For All"
starts_with_coding = text.startswith("Coding")
print(starts_with_coding)


# using endswith()
text = "Coding For All"
ends_with_coding = text.endswith("coding")
print(ends_with_coding)

# strpping text
text = "   Coding For All      "
cleaned_text = text.strip()
print(cleaned_text)

# Checking identifiers
print("30DaysOfPython".isidentifier())
print("thirty_days_of_python".isidentifier())

# Joining Python libraries
py_libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
joined_libraries = '# '.join(py_libraries)
print(joined_libraries)


#OR

# Joining Python libraries
libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
libraries_with_hash = ['#' + library for library in libraries]
result = ' '.join(libraries_with_hash)
print(result)

# Sentences with newline escape sequence
text = "I am enjoying this challenge.\nI just wonder what is next."
print(text)

# Text with tab escape sequence
text = "Name\t\tAge\tCountry\tCity\nAsabeneh\t250\tFinland\tHelsinki"
print(text)

# Variables
radius = 10
area = 3.14 * radius ** 2
output = "The area of a circle with radius {} is {:.0f} meters square.".format(radius, area)
print(output)


#Initiate Variables
a, b = 8, 6
output = (
    "{} + {} = {}\n"
    "{} - {} = {}\n"
    "{} * {} = {}\n"
    "{} / {} = {:.2f}\n"
    "{} % {} = {}\n"
    "{} // {} = {}\n"
    "{} ** {} = {}".format(
        a, b, a + b,
        a, b, a - b,
        a, b, a * b,
        a, b, a / b,
        a, b, a % b,
        a, b, a // b,
        a, b, a ** b
    )
)
print(output)









