'''If a five-digit number is input through the keyboard, write a program to reverse the number.'''
num=int(input("Enter a five-digit number : "))
digit1 = num // 10000        
digit2 = (num // 1000) % 10  
digit3 = (num // 100) % 10   
digit4 = (num // 10) % 10    
digit5 = num % 10            
rev= (digit5 * 10000) + (digit4 * 1000) + (digit3 * 100) + (digit2 * 10) + digit1
print("The reversed number is:", rev)
