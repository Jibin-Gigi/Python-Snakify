'''
Given a three-digit number. Find the sum of its digits.
'''

number = int(input("Enter a number: "))
total = 0
while number > 0:
    total += number % 10
    number //= 10
print(total)

'''
a=int(input())
total=0
for i in range(3):
    total=total + (a%10)
    a=a//10
print(total)
'''