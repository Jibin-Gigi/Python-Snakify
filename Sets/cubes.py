'''  Alice and Bob like to play with colored cubes. Each child has its own set of cubes and each cube has a distinct color, 
    but they want to know how many unique colors exist if they combine their block sets. To determine this, 
    the kids enumerated each distinct color with a random number from 0 to 108. At this point their enthusiasm dried up, 
    and you are invited to help them finish the task. Given two integers that indicate the number of blocks in Alice's and 
    then Bob's sets N and M. The following N lines contain the numerical color value for each cube in Alice's set. 
    Then the last M rows contain the numberical color value for each cube in Bob's set.

    Find three sets: the numerical colors of cubes in both sets, the numerical colors of cubes only in Alice's set, 
    and the numerical colors of cubes only in Bob's set. For each set, print the number of elements in the set, 
    followed by the numerical color elements, sorted in ascending order. '''

n, m = map(int, input().split())
Alice=set()
Bob=set()
for _ in range(n):
    Alice.add(int(input()))
for _ in range(m):
    Bob.add(int(input()))
    
common = Alice & Bob
print(len(common), *sorted(common))

only_alice = Alice - Bob
print(len(only_alice), *sorted(only_alice))

only_bob = Bob - Alice
print(len(only_bob), *sorted(only_bob))
