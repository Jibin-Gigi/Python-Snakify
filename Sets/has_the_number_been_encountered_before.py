''' Given a sequence of numbers, determine if the next number has already been encountered. For each number, 
    print the word YES (in a separate line) if this number has already been encountered, and 
    print NO, if it has not already been encountered. '''


numbers = input().split()
seen = set()
for number in numbers:
    if number in seen:
        print("YES")
    else:
        seen.add(number)
        print("NO")
