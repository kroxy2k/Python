''' A library charges a fine for every book returned late. For first 5 days the fine is 50 paise, for
6-10 days fine is one rupee and above 10 days fine is 5 rupees. If you return the book after 30
days your membership will be cancelled. Write a program to accept the number of days the
member is late to return the book and display the fine or the appropriate message.
'''
days= int(input("Enter the number of days the book is returned late: "))
if days <= 0:
    print("No fine. Thank you for returning the book on time!")
elif days <= 5:
    fine = days * 0.50  
    print("The fine is Rs.",fine)
elif days<= 10:
    fine = days * 1.00  
    print("The fine is Rs.",fine)
elif days <= 30:
    fine = days* 5.00  
    print("The fine is Rs.",fine)
else:
    print("Your membership is cancelled due to late return beyond 30 days.")
