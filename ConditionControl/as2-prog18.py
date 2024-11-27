# Input details from the user
health = input("Enter health condition (excellent/poor): ").lower()
age = int(input("Enter age: "))
location = input("Enter living location (city/village): ").lower()
gender = input("Enter gender (male/female): ").lower()

# Determine insurance details
if health == "excellent" and 25 <= age <= 35 and location == "city":
    if gender == "male":
        premium_rate = 4  # Rs. 4 per thousand
        max_policy_amount = 200000  # Rs. 2 lakhs
        print("The person is insured with a premium rate of Rs. " + str(premium_rate) + " per thousand.")
        print("The maximum policy amount is Rs. " + str(max_policy_amount) + ".")
    elif gender == "female":
        premium_rate = 3  # Rs. 3 per thousand
        max_policy_amount = 100000  # Rs. 1 lakh
        print("The person is insured with a premium rate of Rs. " + str(premium_rate) + " per thousand.")
        print("The maximum policy amount is Rs. " + str(max_policy_amount) + ".")
    else:
        print("Invalid gender input. The person is not insured.")
elif health == "poor" and 25 <= age <= 35 and location == "village" and gender == "male":
    premium_rate = 6  # Rs. 6 per thousand
    max_policy_amount = 10000  # Rs. 10,000
    print("The person is insured with a premium rate of Rs. " + str(premium_rate) + " per thousand.")
    print("The maximum policy amount is Rs. " + str(max_policy_amount) + ".")
else:
    print("The person is not insured.")
