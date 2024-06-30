'''Ques: The program is supposed to calculate the sum of  distance between three points from each other.

For
x1 = 1 y1 = 1
x2 = 2 y2 = 4
x3 = 3 y3 = 6

Distance is calculated as : sqrt(x2-x1)2 + (y2-y1)2'''
import math
x1=1
x2=2
x3=3
y1=1
y2=4
y3=6
d1=math.sqrt((x2-x1)**2 + (y2-y1)**2)
d2=math.sqrt((x2-x3)**2 + (y2-y3)**2)
d3=math.sqrt((x3-x1)**2 + (y3-y1)**2)
print(d1)
print(d2)
print(d3)