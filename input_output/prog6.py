'''Two numbers are input through the keyboard into two locations C and D. Write a program to
interchange the contents of C and D.
'''
c=int(input("Enter the first number:"))
d=int(input("Enter the second number:"))
print("Before swapping C :",c,"and D :",d)
temp=c
c=d
d=temp
print("After swapping C :",c,"and D :",d)