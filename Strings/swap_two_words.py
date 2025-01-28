'''
Given a string consisting of exactly two words separated by a space. 
Print a new string with the first and second word positions swapped 
(the second word is printed first).
'''
s=input()
space=s.find(' ')
print(s[space+1:] +' '+ s[:space] )
    
