'''Given three points (x1, y1), (x2, y2) and (x3, y3), write a program to check if all the three
points fall on one straight line'''

x1=int(input("Enter X1:"))
y1=int(input("Enter Y1:"))
x2=int(input("Enter X2:"))
y2=int(input("Enter Y2:"))
x3=int(input("Enter X3:"))
y3=int(input("Enter Y3:"))
A=(x2-x1)/(y2-y1)
B=(x3-x2)/(y3-y2)
C=(x1-x3)/(y1-y3)
if A==B==C:
    print("All three points fall on the straight line")
else:
    print("All three points do not fall on the straight line")