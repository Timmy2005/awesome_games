# This is the Game Input module.
# It allows the player to perform actions by typing in what looks like a console.
#
# FOR COLLABORATORS:
# This is the format for inputting commands:
#
# print("Question here. (ex. What is your name?)")
# <variable> = raw_input("> ")
#
# Do it EXACTLY as shown above. Copy and paste if you need to.

global corNumberX
global corNumberY
global witchX
global witchY
global direction

import random
import time
from Store import store
from inventory import showInventory
from inventory import showStats
from battleEngine import battleInput
from battleEngine import monsterRandomize
from battleEngine import playerHealthDev
from battleEngine import use_weapons

corNumberX = 5
corNumberY = 1
witchX = 2  # random.randint(0,10)
witchY = 2  # random.randint(0,10)
direction = ['north', 'south', 'east', 'west']


def playerAction():
    global corNumberX
    global corNumberY
    global witchY
    global witchX


def monsterEncounter():  # I think this would be better than monsterMove for a few reasons. Just an idea, though.
    monsterChance = random.randint(1, 5)
    if monsterChance >= 4:
        monsterRandomize()
        use_weapons()
        battleInput()
        playerHealth = playerHealthDev()
        if playerHealth < 1:
            print""
            print"GAME OVER -- You ran out of lives."
            time.sleep(3)
            quit()



def playerAction():
    global corNumberX
    global corNumberY
    global direction

    print("You are at X:" + str(corNumberX) + " Y:" + str(corNumberY))
    playerInput = raw_input("> ").lower()
    if playerInput == "north":
        if corNumberY == 10:
            if corNumberX == 3:
                print"You need a key to go in there."
                time.sleep(1.5)
                playerAction()
            else:
                print"You can't go there! Those are the dungeon walls."
                time.sleep(1.5)
                playerAction()
        corNumberY = corNumberY + 1
        monsterEncounter()
        playerAction()
    elif playerInput == "south":  # Yeah! Go 'elif'!
        if corNumberY == 0:
            print"Don't be silly! You still have a princess to save!"
            time.sleep(1.5)
            playerAction()
        else:
            corNumberY = corNumberY - 1
            monsterEncounter()
            playerAction()
    elif playerInput == "east":
        if corNumberX == 10:
            print"Whoa! You almost fell of the cliff!"
            time.sleep(1.5)
            playerAction()
        else:
            corNumberX = corNumberX + 1
            monsterEncounter()
            playerAction()
    elif playerInput == "west":
        if corNumberX == 0:
            print"You don't want to go in there! That forest doesn't have anything in it"
            time.sleep(1)
            playerAction()
        else:
            corNumberX = corNumberX - 1
            monsterEncounter()
            playerAction()
    elif playerInput == "inventory":
        showInventory()  # This function is defined in the 'inventory.py' file.
        playerAction()
    elif playerInput == "store":
        store()
        playerAction()
    elif playerInput == "exitgame":
        print("Are you sure you want to quit? ('yes' or 'no')")
        exitConfirm = raw_input("> ")
        if exitConfirm == "yes":
            print("Exiting the game...")
            time.sleep(1)
            print("GAME OVER -- I don't see why they used you to save the princess.")
            time.sleep(3)
            exit()
        elif exitConfirm == "no":
            print("Will not exit the game.")
            playerAction()
        else:
            print("Invalid answer.")
            print("Will not exit the game.")
            playerAction()
    elif playerInput == "stats":
        showStats()
        playerAction()

    elif playerInput == "help":
        print("Balls.")

    else:
        print("Invalid command.")
        playerAction()
    

        # if monster
        # X == corNumberX:
        #       if monsterY == corNumberY:
        #               battleInput()
        # And I'll let Timmy2005 finish the code.


gameStart()
corNumberX = 5
corNumberY = 1
print"Input command"
print"Type 'help' for help"
playerAction()
