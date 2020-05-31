'''
Alex Yeh
alexanmy@usc.edu
ITP115, Summer 2020
Lab 01
'''

#Ask for user input
print("Welcome to your MadLibs hell, binch!")
userName = input("By what pathetic title do you refer yourself? ")
favoriteFood = input("What mindless dribble do you shovel into your piehole once your inevitable depression hits? And, please, in plural... ")
favNumString = str(input("...Favorite number? What is this, second grade's baby o' clock nappy time? ...Well, just answer the question. "))
favIllness = input("What's your favorite illness? Call that pretty sick...heh. ")

#Do the conversion
userName = userName.strip().title()
favoriteFood = favoriteFood.strip().lower()
favNumInt = int(favNumString)
totalSadness = 4 * favNumInt + 2
favIllness = favIllness.strip()

#print values
print(userName)
print(favoriteFood)
print(totalSadness)

#Make user output
message = "In an attempt to feel something for once, pathetic loser " + userName + " ate " + favNumString + " of his so-called" + " \"" + favoriteFood + "\".\n"
print(message)
message2 = "This poor fucker is clearly saddled with, like, " + str(totalSadness) + " metric tons of loneliness! "
print(message2)
message3 = "Because " + userName + " ate so many " + favoriteFood + "," + " they spent five hours on the toilet suffering from " + favIllness + ". How unfortunate!"
print(message3)
