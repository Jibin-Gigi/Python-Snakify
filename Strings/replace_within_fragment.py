'''
Given a string. Replace every occurrence of the letter h by the letter H, except for the first and the last ones.
'''

s = input()
print(s[ :s.find('h')+1 ]+ 
      s[s.find('h')+1 : s.rfind('h') ].replace('h','H') +
      s[s.rfind('h') :])