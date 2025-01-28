'''
Hour hand turned by α degrees since the midnight. 
Determine the angle by which minute hand turned since 
the start of the current hour. Input and output in this 
problems are floating-point numbers.
'''
alpha=float(input())
#alpha % 30 will give remaining angle after subtracting angle formed by each hour
#Then multiplied by 12,ie., to convert the angle in hour hand to minutes hand
#An hour hand completes one rotation in 12 hours and a minute hand completes rotation 12 times in 12 hours
print(alpha % 30 * 12)