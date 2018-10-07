import random


# Working on 18 here
heads = 0;
tails = 1;

def tossCoin():
    headsOrTails = input()
    if headsOrTails == "heads":
        headsOrTails = 0
    elif headsOrTails == "tails":
        headsOrTails = 1

    resultFromToss = random.randint(heads,tails)
    if resultFromToss < 1 and resultFromToss == headsOrTails:
        print("Heads! You win!")
    elif resultFromToss < 1 and resultFromToss != headsOrTails:
        print("It's Heads! You lose.")
    elif resultFromToss > 0 and resultFromToss == headsOrTails:
        print("It's Tails! You win.")
    elif resultFromToss > 0 and resultFromToss != headsOrTails:
        print("It's Tails! You lose.")
    return resultFromToss




print ("How many sided die do you want? Please enter a number between 0 and 64: ")
numSides = input()
numSides = int(numSides)
print("Your number is: " + str(numSides))

def roll(numSides):

    if numSides > 0 and numSides < 64:
        result = random.randint(1, numSides)
        return result
        
    else:
        print("Number of sides should be between 0 and 64")
        return -1

playerOne = roll(numSides)
playerTwo = roll(numSides)


if playerOne > playerTwo:
    print("You win! " + str(playerOne) + " to " + str(playerTwo))
elif playerTwo > playerOne:
    print("Computer Wins! " + str(playerTwo) + " to " + str(playerOne))
else:
    print("It's a tie! " + str(playerTwo) + " to " + str(playerOne))
    print("Let's toss a coin, Heads or Tails? " )

tossCoin()

    
    









