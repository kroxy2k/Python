import math
len=float(input("Enter Length of Rectangle: "))
br=float(input("Enter bredth of Rectangle: "))
r=float(input("Enter radius of circle: "))
per=2*(len + br)
ar_rec=len*br
cir=2*(math.pi*r)
ar_cir=math.pi*r*r
print("Perimeter of rectangle :",per)
print("Area of rectangle :",ar_rec)
print(f"Circumference of circle :{cir:.2f}")
print(f"Area of circle :{ar_cir:.2f}")