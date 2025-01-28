''' Given a number n, followed by n lines of text, print the number of distinct words that appear in the text.
    For this, we define a word to be a sequence of non-whitespace characters, seperated by one or more whitespace or 
    newline characters. Punctuation marks are part of a word, in this definition. ''' 


words = set()
for _ in range(int(input())):
    words.update(input().split())
print(len(words))
