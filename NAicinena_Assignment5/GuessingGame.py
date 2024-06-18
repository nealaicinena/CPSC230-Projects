import random


def guess():
    return int(input("Please enter a guess: "))#asks user for a guess and returns it

def comparator(a, b): #compares two parameters
    if(a > b):
        return 0 #returns 0 if a is bigger
    elif(a < b):
        return 1 #returns 1 if b is bigger
    else:
        return -1 #returns -1 if they are the same
   
def remark(val): #meant to be used with the comparator function
    #^^tells the user if the first number is bigger, smaller, or the same as the second number^^
    if(val == 0):
        print("You guessed higher!") #returns higher if parameter is 0
    elif(val == 1):
        print("You guessed lower!") #returns lower if parameter is 1
    else:
        print("You got it!") #returns you guessed it if parameter is -1
        

def simulation(): #runs an entire guessing game
    print("This is a guessing game.") 
    print("You will guess a randomly generated number until you guess it.")
    print("I will tell you if your guess is higher or lower. ")
    #^^delivers prompts to the user on how the game works^^
    num = random.randint(0,100)#generates random number from 1-100
    userGuess = guess()#asks user for a guess and stores the users guess in userGuess
    remark(comparator(userGuess, num))#checks if the guess is higher or lower and tells the user
    while(comparator(userGuess, num) != -1): #while the users guess is not right...
        userGuess = guess()#ask the user to guess again and store as userGuess
        remark(comparator(userGuess, num)) #checks if the guess is higher or lower and tells the user

simulation() #runs 1 round of the guessing game




