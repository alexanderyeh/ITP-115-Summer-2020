'''
Alex Yeh
alexanmy@usc.edu
ITP115, Summer 2020
Lab 01
'''

#Welcome!
print("Welcome to YehCalc V1.0!")
userFirstNumber = int(input("First, give me a number: "))
userSecondNumber = int(input("Give me one more: "))
result = 0

#Display menu
print("Alright, here's what I can do:")
print("\t1. Add")
print("\t2. Subtract")
print("\t3. Multiply")
print("\t4. Divide")
print("\t5. Exponent")

#Get operator
choice = int(input("What should I do with these bad boys? "))
if choice == 1:
    print("Let's add!")
    result = userFirstNumber + userSecondNumber
elif choice == 2:
    print("Let's subtract!")
    result = userFirstNumber - userSecondNumber
elif choice == 3:
    print("Let's multiply!")
    result = userFirstNumber * userSecondNumber
elif choice == 4:
    print("Let's divide!")
    #Check if denominator is 0
    if userSecondNumber == 0:
        print("You can't divide by ZERO, you buffoon!")
    else:       #Denominator isn't 0
        result = userFirstNumber / userSecondNumber
elif choice == 5:
    print("Let's...uh...exponent?")
    result = userFirstNumber ** userSecondNumber
else:
    print("bro idk lol")

#Display answer to the user
print("Result = " +str(result))
print("Thanks for using YehCalc!")