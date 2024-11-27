'''A cashier has currency notes of denominations 10, 50 and 100. If the amount to be withdrawn
is input through the keyboard in hundreds, find the total number of currency notes of each
denomination the cashier will have to give to the withdrawer.'''

amt=int(input("Enter the amount:"))
h=amt//100
amt=amt%100
f=amt//50
amt=amt%50
t=amt//10
print("The cashier will have to give",h,"notes of 100")
print("The cashier will have to give",f,"notes of 50")
print("The cashier will have to give",t,"notes of 10")