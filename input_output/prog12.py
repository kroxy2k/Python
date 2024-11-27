'''If the total selling price of 15 items and the total profit earned on them is input through the
keyboard, write a program to find the cost price of one item.'''
# Taking input from the user
TsellPr=int(input("Enter total selling price of 15 items:"))
Tprofit=int(input("Enter total profit earned on 15 items:"))
# Calculating the cost price of one item
CP=(Tprofit/(15))+(TsellPr/(15))
print("Cost price of one item is:",CP)
