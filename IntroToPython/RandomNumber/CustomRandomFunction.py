import random

print ("Please enter a number: ")
number = input()
number = int(number)
print("Your number is: " + str(number))

def roll(number):
    result = random.randint(1, number)
    print("Below is a randomly selected number between 1 and " + str(number))
    print(result)



roll(number)

