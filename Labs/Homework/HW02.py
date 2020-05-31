"""
Alex Yeh
alexanmy@usc.edu
ITP115, Summer 2020
Homework 02
"""

# Ask user for new vehicle's purchase price and if they have something to trade in

print("Welcome to my vehicle loan calculator!")
userNewCarPrice = float(input("What is the price of your new vehicle? "))
userDownPayment = float(input("What is the down payment for the vehicle? "))
userSalesTax = (float(input("And what is the sales tax on the transaction? (For 8.25% tax, enter 8.25): " )))

print("If you currently have a vehicle you'd like to trade in, you will be able to save on your new purchase." )
choice = input("Do you have a vehicle you'd like to trade in? [y/n] ")
userOldCarTradeIn = 0
userOldCarOwe = 0
if choice.lower() == "y" or choice.lower() == "yes":
    userOldCarTradeIn = float(input("Okay! What's your current vehicle's trade in value? "))
    userOldCarOwe = float(input("And how much do you currently owe on the vehicle? "))

else:
    print("Alright, now let me calculate your overall down payment and loan...")

# Down payment and loan calculation
totalDownPayment = userDownPayment + (userOldCarTradeIn - userOldCarOwe)
totalLoanAmount = (userNewCarPrice - totalDownPayment) * (1 + (userSalesTax/100))

# Display down payment and loan amount
print("It seems like your overall down payment is $" + str(round(totalDownPayment, 2)) + ",")
print("and your overall loan amount is $" + str(round(totalLoanAmount, 2)) + ".")

# Number of payments
print("What is the length of your loan?")
print("\t1. 3 years")
print("\t2. 4 years")
print("\t3. 5 years")
print("\t4. 6 years")

# Select choice
choice = input("Select an option: ")
userNumberOfPayments = 0
if choice == "1":
    print("You have selected a 3 year loan with a total of 36 monthly payments.")
    userNumberOfPayments = 36
elif choice == "2":
    print("You have selected a 4 year loan with a total of 48 monthly payments.")
    userNumberOfPayments = 48
elif choice == "3":
    print("You have selected a 5 year loan with a total of 60 monthly payments.")
    userNumberOfPayments = 60
elif choice == "4":
    print("You have selected a 6 year loan with a total of 72 monthly payments.")
    userNumberOfPayments = 72
else:
    print("Sorry, I don't know how to help ya!")

# Calculate the interest rate
percentDown = round((totalDownPayment/userNewCarPrice) * 100, 2)
userInterestRate = 0
if percentDown < 20:
    if choice == "1":
        print("With " + (str(percentDown)) + "% and a 3 year loan, we can offer you an interest rate of 4.00%")
        userInterestRate = 4
    if choice == "2":
        print("With " + (str(percentDown)) + "% and a 4 year loan, we can offer you an interest rate of 4.33%")
        userInterestRate = 4.33
    if choice == "3":
        print("With " + (str(percentDown)) + "% and a 5 year loan, we can offer you an interest rate of 4.66%")
        userInterestRate = 4.66
    if choice == "4":
        print("With " + (str(percentDown)) + "% and a 6 year loan, we can offer you an interest rate of 5.00%")
        userInterestRate = 5
elif percentDown >= 20:
    if choice == "1":
        print("With " + (str(percentDown)) + "% and a 3 year loan, we can offer you an interest rate of 3.70%")
        userInterestRate = 3.7
    if choice == "2":
        print("With " + (str(percentDown)) + "% and a 4 year loan, we can offer you an interest rate of 3.80%")
        userInterestRate = 3.8
    if choice == "3":
        print("With " + (str(percentDown)) + "% and a 5 year loan, we can offer you an interest rate of 3.90%")
        userInterestRate = 3.9
    if choice == "4":
        print("With " + (str(percentDown)) + "% and a 6 year loan, we can offer you an interest rate of 4.00%")
        userInterestRate = 4

# Calculate monthly payment
userMonthlyInterest = (userInterestRate/1200)
monthlyPaymentDenominator = 1 - (1+userMonthlyInterest)**(-userNumberOfPayments)
userMonthlyPayment = totalLoanAmount * (userMonthlyInterest/monthlyPaymentDenominator)

print("So it looks like your estimated monthly payment would be $" + str(round(userMonthlyPayment, 2)) + " a month.")
print("Thanks for using me! Hope I could help!")