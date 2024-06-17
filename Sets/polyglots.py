''' Each student at a certain school speaks a number of languages. We need to determine which languges are spoken 
    by all the students, which languages are spoken by at least one student.Given, the number of students, 
    and then for each student given the number of languages they speak followed by the name of each language spoken, 
    find and print the number of languages spoken by all the students, followed by a list the languages by name, 
    then print the number of languages spoken by at least one student, followed by the list of the languages by name. 
    Print the languages in alphabetical order. ''' 


# Read the number of students
num_students = int(input())
# Initialize sets for languages spoken by all students and at least one student
all_languages = set()
any_languages = set()

# Loop through each student
for _ in range(num_students):
    # Read the number of languages this student speaks
    num_languages = int(input())
    # Use a set comprehension to read the languages for this student
    languages = {input() for _ in range(num_languages)}
    # Update the set of languages spoken by all students using set intersection
    all_languages = languages if not all_languages else all_languages & languages
    # Update the set of languages spoken by at least one student using set union
    any_languages |= languages

# Print the number of languages spoken by all students and the list of these languages
print(len(all_languages))
for language in sorted(all_languages):
    print(language)

# Print the number of languages spoken by at least one student and the list of these languages
print(len(any_languages))
for language in sorted(any_languages):
    print(language)
