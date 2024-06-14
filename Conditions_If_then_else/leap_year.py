''' Given the year number. You need to check if this year is a leap year. 
    If it is, print LEAP, otherwise print COMMON.

    The rules in Gregorian calendar are as follows:
    1)a year is a leap year if its number is exactly divisible by 4 and is not exactly divisible by 100
    2)a year is always a leap year if its number is exactly divisible by 400 '''

year=int(input())
if year % 400==0 or (year % 4==0 and year%100 !=0):
    print('LEAP')
else:
    print('COMMON')
