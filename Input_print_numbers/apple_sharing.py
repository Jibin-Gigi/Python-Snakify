'''N students take K apples and distribute them among each other evenly.
   The remaining (the undivisible) part remains in the basket. 
   How many apples will each single student get? 
   How many apples will remain in the basket?'''

#Read no.of students
n = int(input())

#Read No.of apple
k = int(input())

#Print no.apples each single student will get
print(k // n)

#Print no.apples that will remain in the basket
print(k % n)