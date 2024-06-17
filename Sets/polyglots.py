''' Each student at a certain school speaks a number of languages. We need to determine which languges are spoken 
    by all the students, which languages are spoken by at least one student.Given, the number of students, 
    and then for each student given the number of languages they speak followed by the name of each language spoken, 
    find and print the number of languages spoken by all the students, followed by a list the languages by name, 
    then print the number of languages spoken by at least one student, followed by the list of the languages by name. 
    Print the languages in alphabetical order. ''' 


# Read the number of students
n = int(input())
# Initialize sets for languages spoken by all students and at least one student
all_langs = set()
any_langs = set()

# Loop through each student
for _ in range(n):
    # Read the number of languages this student speaks
    k = int(input())
    # Use a set comprehension to read the languages for this student
    langs = {input() for _ in range(k)}
    # Update the set of languages spoken by all students using set intersection
    all_langs = langs if not all_langs else all_langs & langs
    # Update the set of languages spoken by at least one student using set union
    any_langs |= langs

# Print the number of languages spoken by all students and the list of these languages
print(len(all_langs))
for lang in sorted(all_langs):
    print(lang)

# Print the number of languages spoken by at least one student and the list of these languages
print(len(any_langs))
for lang in sorted(any_langs):
    print(lang)
