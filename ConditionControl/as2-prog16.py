'''If the three sides of a triangle are entered through the keyboard, write a program to check
whether the triangle is isosceles, equilateral, scalene or right angled triangle'''

a = float(input("Enter 1st side of the triangle: "))
b = float(input("Enter 2nd of the triangle: "))
c = float(input("Enter 3rd side of the triangle: "))

if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print("The triangle is Equilateral.")
    elif a == b or b == c or a == c:
        print("The triangle is Isosceles.")
    elif (a**2 + b**2 == c**2) or (b**2 + c**2 == a**2) or (a**2 + c**2 == b**2):
        print("The triangle is Right-angled.")
    else:
        print("The triangle is Scalene.")
else:
    print("The given sides do not form a valid triangle.")
