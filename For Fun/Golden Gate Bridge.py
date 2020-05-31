'''
Alex does stupid shit in Python: volume 1
'''

print("Y'all know the Golden Gate Bridge, right?"), "\".\n"
print("And you know yourself, right?"), "\".\n"
print("Well, what if we calculated how much of YOU it would take to build the length of the Golden Gate Bridge? Sounds fun, right?")

#Let's get jiggy with it
print("To calculate this very important statistic, all I'm gonna need to know your height. Don't worry; I won't share this with the government, maybe.")
userFeet = int(input("To start, tell me how tall you are in feet. "))
userInches = int(input("Nice. Now, in inches, please? "))

#Convert height to total inches
userTotalInches = int(userFeet * 12) + userInches
#Golden Gate Bridge is 107772 inches long
107772
userGoldenGateBridge = int((107772/userTotalInches))

#print(userGoldenGateBridge)
print("So, we know it would take about " + str(userGoldenGateBridge) + " of you to span the Golden Gate. Pretty cool, huh?")
