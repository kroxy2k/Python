'''. Any year is entered through the keyboard, write a program to determine whether the year is
leap or not. Use the logical operators && and ||.'''
year = int(input("Enter a year: "))
if year % 4 == 0 and (year % 100 != 0 or year % 400==0):
    print(year,"is a leap year")
else:
    print(year,"is not a leap year")