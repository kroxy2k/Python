'''If the three sides of a triangle are entered through the keyboard, write a program to check
whether the triangle is valid or not. The triangle is valid if the sum of two sides is greater than
the largest of the three sides.'''

a = float(input("Enter 1st side of the triangle: "))
b = float(input("Enter 2nd of the triangle: "))
c = float(input("Enter 3rd side of the triangle: "))
if a + b > c and a + c > b and b + c > a:
    print("The triangle is valid")
else:
    print("The triangle is not valid")