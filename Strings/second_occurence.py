'''
Given a string that may or may not contain the letter of interest. 
Print the index location of the second occurrence of the letter f. 
If the string contains the letter f only once, then print -1, and 
if the string does not contain the letter f, then print -2.
'''

s = input()
first_occurrence = s.find('f')
if s.count('f') == 0:
    print(-2)
elif s.count('f') == 1:
    print(-1)
else:
    second_occurrence = s.find('f', first_occurrence + 1)
    print(second_occurrence)
