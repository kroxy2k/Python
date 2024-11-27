r=int(input("Enter Ram's age: "))
s=int(input("Enter Shyam's age: "))
a=int(input("Enter Ajay's age: "))
if r>s and r>a:
    print("Ram is oldest",r)
elif s>r and s>a:
    print("Shyam is oldest",s)
else:
    print("Ajay is oldest",a)