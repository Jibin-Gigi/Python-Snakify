''' You are given a dictionary consisting of word pairs. Every word is a synonym the other word in its pair. 
    All the words in the dictionary are different.
    After the dictionary there's one more word given. Find a synonym for him. '''

# Read the number of word pairs
n = int(input())
# Initialize an empty dictionary for the synonyms
synonyms = {}

# Read each pair of synonyms and add them to the dictionary
for _ in range(n):
    word1, word2 = input().split()
    synonyms[word1] = word2
    synonyms[word2] = word1

# Read the word for which to find the synonym
word = input()
# Print the synonym of the given word
print(synonyms[word])
