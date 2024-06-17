''' One day, going through old books in the attic, a student Bob found English-Latin dictionary. 
    By that time he spoke English fluently, and his dream was to learn Latin. 
    So finding the dictionary was just in time.Unfortunately, full-fledged language studying process 
    requires also another type of dictionary: Latin-English. For lack of a better way he decided to    
    make a second dictionary using the first one.

    As you know, the dictionary consists of words, each of which contains multiple translations. 
    For each Latin word that appears anywhere in the dictionary, Bob has to find all its translations 
    (that is, all English words, for which our Latin word is among its translations), 
    and take them and only them as the translations of this Latin word.

    Help him to create a Latin-English.

    The first line contains a single integer N — the number of English words in the dictionary. 
    Followed by N dictionary entries. Each entry is contained on a separate line, 
    which contains first the English word, then a hyphen surrounded by spaces and then comma-separated 
    list with the translations of this English word in Latin. All the words consist only of 
    lowercase English letters. The translations are sorted in lexicographical order. 
    The order of English words in the dictionary is also lexicographic.

    Print the corresponding Latin-English dictionary in the same format. In particular, 
    the first word line should be the lexicographically minimal translation of the Latin word, 
    then second in that order, etc. Inside the line the English words should be sorted also lexicographically. '''


# Read the number of English words in the dictionary
n = int(input())

# Initialize a dictionary to store Latin-English translations
latin_to_english = {}

# Read each English word and its Latin translations
for _ in range(n):
    entry = input().split(' - ')
    english_word = entry[0]
    latin_words = entry[1].split(', ')
    for latin_word in latin_words:
        if latin_word not in latin_to_english:
            latin_to_english[latin_word] = []
        latin_to_english[latin_word].append(english_word)

# Sort the dictionary and print Latin-English translations
sorted_latin = sorted(latin_to_english.keys())
print(len(sorted_latin))
for latin_word in sorted_latin:
    english_translations = sorted(latin_to_english[latin_word])
    print("{} - {}".format(latin_word, ', '.join(english_translations)))
