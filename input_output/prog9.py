num = int(input("Enter a four digit number: "))
fdgt = num % 10
ldgt = num // 1000
sum = fdgt + ldgt
print("Sum of first digit and last digit:", sum)