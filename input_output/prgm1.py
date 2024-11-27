sal=float(input("Enter Ramesh's Salary:"))
dearness_sal=(sal*40)/100
rent=(sal*20)/100
gross_sal=(sal - (dearness_sal + rent))
print(f"Ramesh's gross salary is:{gross_sal:.2f}")