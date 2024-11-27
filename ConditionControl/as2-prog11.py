'''. Given the coordinates (x, y) of a center of a circle and it’s radius, write a program which will
determine whether a point lies inside the circle, on the circle or outside the circle. (Hint: Use
sqrt( ) and pow( ) functions)'''
import math
x1=int(input("Enter the x-coordinate of the center of the circle:"))
y1=int(input("Enter the y-coordinate of the center of the circle:"))
r=int(input("Enter the radius of the circle:"))
x2=int(input("Enter the x-coordinate of the point:"))
y2=int(input("Enter the y-coordinate of the point:"))
distance=math.sqrt((x2-x1)^2 + (y2-y1)^2)
if (distance==r):
    print("The point lies on the circle",distance,"=",r)
elif (distance>r):
    print("The point lies outside the circle",distance,">",r)
else:
    print("The point lies inside the circle",distance,"<",r)