'''Given the length and breadth of a rectangle, write a program to find whether the area of the
rectangle is greater than its perimeter. For example, the area of the rectangle with length = 5
and breadth = 4 is greater than its perimeter'''

len=int(input("Enter the length of rectangle:"))
br=int(input("Enter the breadth of rectangle:"))
area=len*br
per=2*(len+br)
if area==per:
    print("Area is equal to perimeter",area,"==",per)
elif area>per:
    print("Area is greater than perimeter",area,">",per)
else:
    print("Area is less than perimeter",area,"<",per)