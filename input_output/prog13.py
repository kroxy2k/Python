'''. If a five-digit number is input through the keyboard, write a program to print a new number
by adding one to each of its digits. For example if the number that is input is 12391 then the
output should be displayed as 23402.'''

num = int(input("Enter a five-digit number: "))
n1 = ((num//10000) + 1) % 10
n2 = ((num//1000) +1) % 10
n3 = ((num//100) + 1) % 10
n4 = ((num//10) + 1) %10
n5 = ((num//1) + 1) % 10
ntot=(n1*10000)+(n2*1000)+(n3*100)+(n4*10)+(n5*1)
print("The new number is:",ntot)
