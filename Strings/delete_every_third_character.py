'''
Given a string. Delete from it all the characters whose indices are divisible by 3.
'''
s = input("Enter the string: ")
result = ''

for i in range(len(s)):
    if i % 3 != 0:
        result += s[i]

print(result)
