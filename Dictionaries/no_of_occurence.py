''' The text is given in a single line. For each word of the text count the number of its occurrences before it.
    A word is a sequence of non-whitespace characters. Two consecutive words are separated by one or more spaces. 
    Punctiation marks are a part of a word, by this definition. '''


# Read the input text in a single line
text = input()
# Split the text into words
words = text.split()
# Initialize a dictionary to store the count of each word
word_count = {}

# Iterate over each word in the list
for word in words:
    # Print the current count of the word from the dictionary, defaulting to 0 if not found
    print(word_count.get(word, 0), end=' ')
    # Update the count of this word in the dictionary by incrementing it by 1
    word_count[word] = word_count.get(word, 0) + 1
