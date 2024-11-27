cp=int(input("Enter cost price: "))
sp=int(input("Enter selling price: "))
total=sp-cp
if  total>0:
    print("Profit amt:",total)
else:
    print("Loss incured:",total)
