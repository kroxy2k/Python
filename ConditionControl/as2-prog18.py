health = input("Enter health condition (excellent/poor): ").lower()
age = int(input("Enter age: "))
location = input("Enter living location (city/village): ").lower()
gender = input("Enter gender (male/female): ").lower()

if health == "excellent" and 25 <= age <= 35 and location == "city":
    if gender == "male":
        premium_rate = 4  
        max_policy_amount = 200000  
        print("The person is insured with a premium rate of Rs. " + str(premium_rate) + " per thousand.")
        print("The maximum policy amount is Rs. " + str(max_policy_amount) + ".")
    elif gender == "female":
        premium_rate = 3  
        max_policy_amount = 100000  
        print("The person is insured with a premium rate of Rs. " + str(premium_rate) + " per thousand.")
        print("The maximum policy amount is Rs. " + str(max_policy_amount) + ".")
    else:
        print("Invalid gender input. The person is not insured.")
elif health == "poor" and 25 <= age <= 35 and location == "village" and gender == "male":
    premium_rate = 6  
    max_policy_amount = 10000  
    print("The person is insured with a premium rate of Rs. " + str(premium_rate) + " per thousand.")
    print("The maximum policy amount is Rs. " + str(max_policy_amount) + ".")
else:
    print("The person is not insured.")
