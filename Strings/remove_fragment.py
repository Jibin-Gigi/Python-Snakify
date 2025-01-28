'''
Given a string in which the letter h occurs at least twice. 
Remove from that string the first and the last occurrence of the 
letter h, as well as all the characters between them.
'''

s = input()
s = s[:s.find('h')] + s[s.rfind('h') + 1:]
print(s)