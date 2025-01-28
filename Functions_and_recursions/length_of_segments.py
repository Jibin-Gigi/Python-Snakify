''' Given four real numbers representing cartesian coordinates: (x1,y1),(x2,y2). 
    Write a function distance(x1, y1, x2, y2) to compute the distance between the points (x1,y1) and (x2,y2). 
    Read four real numbers and print the resulting distance calculated by the function. '''

from math import sqrt

def distance(x1, y1, x2, y2):
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
print(distance(x1, y1, x2, y2))