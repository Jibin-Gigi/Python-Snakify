'''
Given a string in which the letter h occurs at least two times, 
reverse the sequence of characters enclosed 
between the first and last appearances.
'''

s = input()
print(s[:s.find('h') + 1]
      + s[s.rfind('h') - 1:s.find('h'):-1]
      + s[s.rfind('h') :])
