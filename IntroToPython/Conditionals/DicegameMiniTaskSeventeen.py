import random

numSides = 3;

def roll(numSides):
    if numSides > 0 and numSides < 64:
        result = random.randint(1, numSides)
        return result
        
    else:
        print("Number of sides should be between 0 and 64")


playerOne = roll(numSides)
playerTwo = roll(numSides)


if playerOne > playerTwo:
    print("Player One wins! " + str(playerOne) + " to " + str(playerTwo))
elif playerTwo > playerOne:
    print("Player Two wins! " + str(playerTwo) + " to " + str(playerOne))
else:
    print("It's a tie! " + str(playerTwo) + " to " + str(playerOne))

