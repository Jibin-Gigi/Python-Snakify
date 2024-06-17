''' Given the text: the first line contains the number of lines, then given the lines of words. 
    Print the word in the text that occurs most often. If there are many such words, 
    print the one that is less in the alphabetical order. '''


# Read the number of lines
n = int(input())
# Initialize an empty dictionary to store the frequency of each word
word_freq = {}

# Read each line and update the frequency of each word
for _ in range(n):
    line = input().split()
    for word in line:
        word_freq[word] = word_freq.get(word, 0) + 1

# Find the word that occurs most often and is least in alphabetical order
most_common_word = min(sorted(word_freq), key=lambda k: (-word_freq[k], k))

# Print the most common word
print(most_common_word)
