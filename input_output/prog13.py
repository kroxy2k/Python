'''. If a five-digit number is input through the keyboard, write a program to print a new number
by adding one to each of its digits. For example if the number that is input is 12391 then the
output should be displayed as 23402.'''
# Taking input from the user
num = input("Enter a five-digit number: ")
d1 = (int(num[0]) + 1) % 10
d2 = (int(num[1]) + 1) % 10
d3 = (int(num[2]) + 1) % 10
d4 = (int(num[3]) + 1) % 10
d5 = (int(num[4]) + 1) % 10

# Combine digits into a new number using string concatenation
new_num = str(d1) + str(d2) + str(d3) + str(d4) + str(d5)

# Output the new number
print("The new number is:", new_num)
