import random


# MiniTask 18


# Function name is tossCoin()
# No Paramaters
# Asks for heads or tails from the user in the event that the dice game is a tie.
# It then compares the input value to the randomly generated heads or tails and
# prints a message to user.
# It calls the startGame() function to keep the game going.
# No return value

def tossCoin():
    headsOrTails = input()
    if headsOrTails == "heads":
        headsOrTails = 0
    elif headsOrTails == "tails":
        headsOrTails = 1

    heads = 0;
    tails = 1;

    resultFromToss = random.randint(heads,tails)
    if resultFromToss < 1 and resultFromToss == headsOrTails:
        print("Heads! You win!")
    elif resultFromToss < 1 and resultFromToss != headsOrTails:
        print("It's Heads! You lose.")
    elif resultFromToss > 0 and resultFromToss == headsOrTails:
        print("It's Tails! You win.")
    elif resultFromToss > 0 and resultFromToss != headsOrTails:
        print("It's Tails! You lose.")
    print("Let's play again!")
    startGame()


# Function name is startGame()
# No parameters
# This function starts the game and prompts the user to input a die side value
# It then stores the value and calls the roll() function
# No return value

def startGame():
    print ("How many sided die do you want? Please enter a number between 0 and 64: ")
    numSides = input()
    numSides = int(numSides)
    print("Your number is: " + str(numSides))
    roll(numSides)

# The function name is roll()
# The function takes in numSides as an int, provide by user input
# This function checks to see if the user input is within the specified die sides 0 to 64
# It then creates to random rolls for the player and the computer and then prints the result
# of the winner or loser.
# the game is continued by calling the startGame() function.
# This function returns -1 if the input value is out of bounds

def roll(numSides):

    if numSides > 0 and numSides < 64:
        playerOne = random.randint(1, numSides)
        playerTwo = random.randint(1, numSides)
        if playerOne > playerTwo:
            print("You win! " + str(playerOne) + " to " + str(playerTwo))
        elif playerTwo > playerOne:
            print("Computer Wins! " + str(playerTwo) + " to " + str(playerOne))
        elif playerTwo == playerOne:
            print("It's a tie! " + str(playerTwo) + " to " + str(playerOne))
            print("Let's toss a coin, Heads or Tails? " )
            tossCoin()
        
    else:
        print("Number of sides should be between 0 and 64")
        startGame()
        return -1

    
    
startGame()








