'''If a five-digit number is input through the keyboard, write a program to calculate the sum of
its digits.(Hint: Use the modulus operator '%')
'''
num=int(input("Enter a five-digit number:"))
digit1 = num// 10000        
digit2 = (num// 1000) % 10  
digit3 = (num // 100) % 10   
digit4 = (num // 10) % 10    
digit5 = num % 10            
sum= digit1 + digit2 + digit3 + digit4 + digit5
print("Sum of its five digit is:",sum)