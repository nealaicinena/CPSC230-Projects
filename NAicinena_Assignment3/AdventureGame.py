import random

#asks user if they want to go inside castle
direction = input("Welcome young explorer! You have arrived at the foot of a castle. The fortified towers rise over you and flood your view. Do you wish to go inside? [Yes][No]: ")

#if the input isnt the options, it will keep asking the user to put something in agian until it is one of the options
while(direction != "Yes" and direction != "No"):
    direction = input("Your input is not a valid input. Please pick one of these options [Yes][No]: ")
if(direction == "Yes"):
    insideBool = True
elif(direction == "No"):
    insideBool = False

#sets all stats and encounters to false and 0
death = False
beastDeath = False
door = 0
profit = 0
beastEncounter = False
deathOdds = 99
bedMoney = False

#generates number to see if you die
#generates from 0-100 and if higher than deathOdds, you die
if(random.randint(0,100) > deathOdds):
    death = True
    insideBool = False
#while loop runs as long as you are inside
while(insideBool):
    #first main room
    if(door == 0):
        if(random.randint(0,100) > deathOdds):
            death = True
            insideBool = False
            break #breaks of of the rooms so that the death statements can print
        direction = input("You enter the main room and 2 doors present you. Do you want to enter the left or right door? [Left][Right][exit]: ")
        #if the input isnt the options, it will keep asking the user to put something in agian until it is one of the options
        while(direction != "Left" and direction != "Right" and direction != "exit"):
            direction = input("Your input is not valid. Try again: ")
        if(direction == "Left"):
            door = 1 #sends you to left room
        elif(direction == "Right"):
            door = 2 #sends you to right room
        elif(direction == "exit"):
            insideBool = False #you leave the castle
            break #breaks out of the rooms so that you can leave
    if(door == 1):
        if(random.randint(0,100) > deathOdds):
            death = True
            insideBool = False
            break
        if(profit == 0): #only lets you take money if you haven't taken it before, otherwise you leave the room
            direction = input("You enter the room. There is a chest against the wall with a small bag of coins. Would you like to take it?[Yes][No][exit]: ")
            #if the input isnt the options, it will keep asking the user to put something in agian until it is one of the options
            while(direction != "Yes" and direction != "No" and direction != "exit"):
                direction = input("Your input is not valid. Try again: ")
            if(direction == "Yes"): 
                profit += 20
                print("You take the coins. You now have", profit, "gold")
            if(direction == "exit"):
                insideBool = False
                break
            print("There is nothing else to do here. You go back to the main room")
            door = 0 
        else:
            print("You already have entered the room and taken everything in here. Try a different room.")
            door = 0 #sends you back to the main room because you already took the money
    if(door == 2): #well room
        if(random.randint(0,100) > deathOdds):
            death = True
            insideBool = False
            break
        direction = input("You enter the room and there is a large well in the middle. Most likely used for water for the castle dwellers. You see three more doors. Which do you enter?[Left][Middle][Right][exit]: ")
        #if the input isnt the options, it will keep asking the user to put something in agian until it is one of the options
        while(direction != "Left" and direction != "Middle" and direction != "Right" and direction != "exit"):
            direction = input("Your input is not valid. Try again: ")
        if(direction == "Left"):
            door = 3 #sends you to beast room
        elif(direction == "Middle"):
            door = 4 #sends you to bed room
        elif(direction == "Right"):
            door = 5 #sends you to room with king
        elif(direction == "exit"):
            insideBool = False
    if(door == 3): #beast room
        if(random.randint(0,100) > deathOdds):
            death = True
            insideBool = False
            break
        if(beastEncounter == False): #if you already killed the beast, you cannot kill him again
            direction = input("You notice a giant beast in this room. You also notice an entrance to another room. Do you wish to fight, go through the new door, or go back from where you came?[Fight]][Back][Door][exit]: ")
            #if the input isnt the options, it will keep asking the user to put something in agian until it is one of the options
            while(direction != "Back" and direction != "Door" and direction != "Fight" and direction != "exit"):
                direction = input("Your input is not valid. Try again: ")
            if(direction == "Back"):
                door = 2
            elif(direction == "Door"):
                door = 4
            elif(direction == "exit"):
                insideBool = False
            elif(direction == "Fight"):
                if(random.randint(1, 2) == 1): # 50/50 chance you win or you die from the beast
                    direction = input("You slay the beast! You loot him and collect 500 gold and a great axe. Do you want to go back or go through the new door?[Door][Back][exit]: ")
                    profit += 500
                    beastEncounter = True #sets encounter as true so that you cannot kill the beast again if you come back to the same room
                    #if the input isnt the options, it will keep asking the user to put something in agian until it is one of the options
                    while(direction != "Back" and direction != "Door" and direction != "Fight" and direction != "exit"):
                        direction = input("Your input is not valid. Try again: ")
                    if(direction == "Back"):
                        door = 2
                    elif(direction == "Door"):
                        door = 4
                else:
                    beastDeath = True
                    insideBool = False
        else:
            print("You have already killed the beast and there is nothing else to do here. You go back to the well room.")
            door = 2 #sends you back to the main room because you already killed the beast
    if(door == 4): #bed money room
        if(random.randint(0,100) > deathOdds):
            death = True
            insideBool = False
            break
        if(bedMoney == False): #does not let you take money if you already grabbed the money
            bedMoney = True #sets money as true so you cannot take it again if you come back
            direction = input("You enter the room and there is a bed. Do you wish to search the bed?[Yes][No][exit]: ")
            #if the input isnt the options, it will keep asking the user to put something in agian until it is one of the options
            while(direction != "Yes" and direction != "No" and direction != "exit"):
                direction = input("Your input is not valid. Try again: ")
            if(direction == "Yes"):
                profit += 20000
            print("Congragulations! You find 20,000 gold! You are rich!")
            if(direction == "exit"):
                insideBool = False
                break
        print("There is nothing else in this room. You go to walk to the well room")
        door = 2
    if(door == 5): #king room
        if(random.randint(0,100) > deathOdds):
            death = True
            insideBool = False
            break
        print("The king of the castle is inside and notices you. He is angry that you have entered his castle without asking and chases you out. You flee before he summons his army to deal with you.")
        print("You are forced to leave the castle")
        insideBool = False
if(insideBool == False and beastDeath == False and death == False): #if you leave, did not die to the beast, and did not get poisoned, you get to leave
    print("You leave the castle and go back home. You leave with", profit, "gold")
    print("This is the end of your journey adventurer.")
    if(profit > 0): #only says good job if you collected some money
        print("Good job today.")
    else:
        print("You did not do so well as you did not collect any gold :(")
    print("---GAME OVER---")
if(death): #kills you using the random integer
    print("It's a trap! Poisonous gas is triggered by a pressure plate that you stepped on and you suffocate and die")
    print("You never escaped the castle. I am sorry adventurer")
    print("---GAME OVER---")
if(beastDeath): #kills you if you failed to kill the beast :(
    print("The giant beast grabs you before you can get a swing and you die!")
    print("I'm sorry adventurer. This is the end for you.")
    print("---GAME OVER---")