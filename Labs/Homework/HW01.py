'''
Alex Yeh
alexanmy@usc.edu
ITP115, Summer 2020
Lab 01
'''

#DEAR ALEX PLEASE COMMENT OUT ALL YOUR PRINT OUTPUT IN THE LATER CALCULATIONS SO YOU DON'T GET DEDUCTED THANKS -Alex
#LIKE, I DON'T KNOW BUT THAT SEEMS VERY IMPORTANT

#Welcoming message and stats
print("Hey there! Looks like I'll be calculating your BMI.")
userName = input("First things first: can you tell me your name? ")
userFeet = int(input("Great! Next, I'll take your height in feet and inches. First, how tall are you in feet? "))
userInches = int(input("Thank you! Now, in inches? "))
userPounds = float(input("Perfect. Last thing: how much do you weigh in pounds? (Don't have to be self-conscious!) "))

#Now we calculate height in total inches...
userTotalInches = int(userFeet * 12) + userInches
print("So it looks like your total height in inches is...", userTotalInches, "inches. Neat!")

#Next, total height in meters...
userMeters = float(userTotalInches/39.3701)
print("For our non-American friends, that would be", userMeters, "meters...")

#Then, we calculate mass in kilograms...
userKilo = float(userPounds/2.20462)
print("...and", userKilo, "kilograms.", "Got it?")

#Now we're ready to calculate BMI!
print("Now, let me just calculate your BMI from what you've just told me...")
userBMI = float(userKilo/(userMeters**2))
print (userName + "'s BMI is " + str(userBMI) + ". Hope that's helpful!")