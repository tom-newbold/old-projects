# -*- coding: utf-8 -*-
import time
import sys

firstRoom = 'true'
worldData = 'world1'
roomID = '2,2'

choicein = str()
choice = choicein.lower()
skip = 'false'

ownSword = 'false'
ownRing = 'false'
chest = 'closed'
ownKey = 'false'
coins = 0

HPcharacter = 100
ATKcharacter = 10

ATKsword = 15
DEFTIMEshield = 0

HPenemyOGRE = 100
ATKenemyOGRE = 10

fight = str()
cont =  False
rf = str('')
cl = str('')

def printScrolling(string):
    for i in range(len(string)):
        print(string[i],end="",flush=True)
        if ord(string[i]) == ord(","):
            time.sleep(0.16)
        elif ord(string[i]) == ord("."):
            time.sleep(0.36)
        time.sleep(0.03)
    sys.stdout.write("\n")

while worldData == str('world1'):
    
    if roomID == str('1,1'):
        printScrolling('You enter a room with only one exit, a door to the EAST.')
        if ownSword == str('false'):
            printScrolling('There is a SWORD on the ground')
        else:
            printScrolling('There is no item in this room.')
        while skip == str('false'):
            choicein = input('')
            choice = choicein.lower()
            if choice == str('go north'):
                printScrolling('There is no exit here.')
            elif choice == str('go east'):
                roomID = '2,1'
                skip = 'true'
            elif choice == str('go south'):
                printScrolling('There is no exit here.')
            elif choice == str('go west'):
                printScrolling('There is no exit here.')
            elif choice == str('pick up item'):
                if ownSword == str('false'):
                    ownSword = 'true'
                    printScrolling('You obtained a SWORD.')
                else:
                    printScrolling('There is no item in this room')
            elif choice == str('inventory'):
                printScrolling('You have:')
                printScrolling(coins, ' GOLD COINs')
                if ownSword == str('true'):
                      printScrolling('a SWORD')
                if ownRing == str('true'):
                      printScrolling('a SHINY RING')
                if ownKey == str('true'):
                      printScrolling('a KEY')
            else:
                printScrolling('Use the commands [go north], [go east], [go south], [go west], [pick up item] or [inventory].')
        skip = 'false'
        choicein = str()
    
    if roomID == str('2,1'):
        printScrolling('You enter a room with 3 exits, a door to the NORTH, EAST and WEST.')
        printScrolling('There is no item in this room.')
        while skip == str('false'):
            choicein = input('')
            choice = choicein.lower()
            if choice == str('go north'):
                roomID = '2,2'
                skip = 'true'
            elif choice == str('go east'):
                roomID = '3,1'
                skip = 'true'
            elif choice == str('go south'):
                printScrolling('There is no exit here.')
            elif choice == str('go west'):
                roomID = '1,1'
                skip = 'true'
            elif choice == str('pick up item'):
                printScrolling('There is no item in this room.')
            elif choice == str('inventory'):
                printScrolling('You have:')
                printScrolling(coins, ' GOLD COINs')
                if ownSword == str('true'):
                      printScrolling('a SWORD')
                if ownRing == str('true'):
                      printScrolling('a SHINY RING')
                if ownKey == str('true'):
                      printScrolling('a KEY')
            else:
                printScrolling('Use the commands [go north], [go east], [go south], [go west], [pick up item] or [inventory].')
        skip = 'false'
        choicein = str()

    if roomID == str('3,1'):
        printScrolling('You enter a room with two exits, a door to the WEST and a tunnel to the EAST.')
        if ownRing == str('false'):
            printScrolling('There is a SHINY RING on the ground')
        else:
            printScrolling('There is no item in this room.')
        while skip == str('false'):
            choicein = input('')
            choice = choicein.lower()
            if choice == str('go north'):
                printScrolling('There is no exit here.')
            elif choice == str('go east'):
                roomID = '4,1'
                skip = 'true'
            elif choice == str('go south'):
                printScrolling('There is no exit here.')
            elif choice == str('go west'):
                roomID = '2,1'
                skip = 'true'
            elif choice == str('pick up item'):
                if ownRing == str('false'):
                    ownRing = 'true'
                    printScrolling('You obtained a SHINY RING.')
                else:
                    printScrolling('There is no item in this room')
            elif choice == str('inventory'):
                printScrolling('You have:')
                printScrolling(coins, ' GOLD COINs')
                if ownSword == str('true'):
                      printScrolling('a SWORD')
                if ownRing == str('true'):
                      printScrolling('a SHINY RING')
                if ownKey == str('true'):
                      printScrolling('a KEY')
            else:
                printScrolling('Use the commands [go north], [go east], [go south], [go west], [pick up item] or [inventory].')
        skip = 'false'
        choicein = str()
    
    if roomID == str('1,2'):
        printScrolling('You enter a room with 2 exits, a door to the NORTH and to the EAST.')
        if chest == str('closed'):
            printScrolling('There is a CLOSED CHEST on the ground. You need a KEY to open it.')
        else:
            printScrolling('There is a OPEN CHEST on the ground. It is empty.')
        while skip == str('false'):
            choicein = input('')
            choice = choicein.lower()
            if choice == str('go north'):
                roomID = '1,3'
                skip = 'true'
            elif choice == str('go east'):
                roomID = '2,2'
                skip = 'true'
            elif choice == str('go south'):
                printScrolling('There is no exit here.')
            elif choice == str('go west'):
                printScrolling('There is no exit here.')
            elif choice == str('open chest'):
                if ownKey == str('true'):
                    if chest == str('closed'):
                        printScrolling('You opened the CLOSED CHEST with a KEY. There is a GOLD COIN inside, which you pick up.')
                        coins = coins + 1
                        chest = 'open'
                    else:
                        printScrolling('The CHEST is already OPEN. It is empty.')
                else:
                    printScrolling('You need a KEY to open the CLOSED CHEST.')
            elif choice == str('inventory'):
                printScrolling('You have:')
                printScrolling(coins, ' GOLD COINs')
                if ownSword == str('true'):
                      printScrolling('a SWORD')
                if ownRing == str('true'):
                      printScrolling('a SHINY RING')
                if ownKey == str('true'):
                      printScrolling('a KEY')
            else:
                printScrolling('Use the commands [go north], [go east], [go south], [go west], [open chest] or [inventory].')
        skip = 'false'
        choicein = str

    if roomID == str('2,2'):
        if firstRoom == str('true'):
            printScrolling('You wake up from a deep slumber, and find yourself in a dark dungeon, with only a torch to light your way. You are in a room with 4 exits, a door to the NORTH, EAST, SOUTH and WEST.')
            firstRoom = 'false'
        else:
            printScrolling('You enter a room with 4 exits, a door to the NORTH, EAST, SOUTH and WEST.')
        printScrolling('There is no item in this room.')
        while skip == str('false'):
            choicein = input('')
            choice = choicein.lower()
            if choice == str('go north'):
                roomID = '2,3'
                skip = 'true'
            elif choice == str('go east'):
                roomID = '3,2'
                skip = 'true'
            elif choice == str('go south'):
                roomID = '2,1'
                skip = 'true'
            elif choice == str('go west'):
                roomID = '1,2'
                skip = 'true'
            elif choice == str('pick up item'):
                printScrolling('There is no item in this room.')
            elif choice == str('inventory'):
                printScrolling('You have:')
                printScrolling(coins, ' GOLD COINs')
                if ownSword == str('true'):
                      printScrolling('a SWORD')
                if ownRing == str('true'):
                      printScrolling('a SHINY RING')
                if ownKey == str('true'):
                      printScrolling('a KEY')
            else:
                printScrolling('Use the commands [go north], [go east], [go south], [go west], [pick up item] or [inventory].')
        skip = 'false'
        choicein = str()
    
    if roomID == str('3,2'):
        printScrolling('You enter a room with 2 exits, a door to the NORTH and WEST.')
        printScrolling('There is no item in this room.')
        while skip == str('false'):
            choicein = input('')
            choice = choicein.lower()
            if choice == str('go north'):
                roomID = '3,3'
                skip = 'true'
            elif choice == str('go east'):
                printScrolling('There is no exit here.')
            elif choice == str('go south'):
                printScrolling('There is no exit here.')
            elif choice == str('go west'):
                roomID = '2,2'
                skip = 'true'
            elif choice == str('pick up item'):
                printScrolling('There is no item in this room.')
            elif choice == str('inventory'):
                printScrolling('You have:')
                printScrolling(coins, ' GOLD COINs')
                if ownSword == str('true'):
                      printScrolling('a SWORD')
                if ownRing == str('true'):
                      printScrolling('a SHINY RING')
                if ownKey == str('true'):
                      printScrolling('a KEY')
            else:
                printScrolling('Use the commands [go north], [go east], [go south], [go west], [pick up item] or [inventory].')
        skip = 'false'
        choicein = str()

    if roomID == str('1,3'):
        printScrolling('You enter a room with 2 exits, a door to the EAST and to the SOUTH.')
        if HPenemyOGRE > 0:
            if ownSword == str('true'):
                printScrolling('You encountered an OGRE.')
                while cont == False:
                    printScrolling('Do you [run] or [fight]!')
                    rf = input('')
                    cl = rf.lower()
                    if cl == str('fight'):
                        printScrolling('You decide to fight your enemy.')
                        while HPenemyOGRE > 0:
                            printScrolling('Your HP', HPcharacter)
                            printScrolling('Enemy HP', HPenemyOGRE)
                            if HPcharacter == 0:
                                printScrolling('YOU DIED')
                                printScrolling('Press enter to exit...')
                                input('')
                                exit()
                            fight = input('Do you: ACTIVATE [shield], ATTACK with [fist] or ATTACK with [sword]?')
                            if fight.lower == str('shield'):
                                printScrolling('You ACTIVATE your shield.')
                                DEFTIMEshield = DEFTIMEshield + 4
                                if HPenemyOGRE > 0:
                                    printScrolling('The OGRE attacks you.')
                                    if DEFTIMEshield > 0:
                                        printScrolling('Your shield softens the blow.')
                                        ATKenemyOGRE = ATKenemyOGRE/2
                                        DEFTIMEshield = DEFTIMEshield - 1
                                    HPcharacter = HPcharacter - ATKenemyOGRE
                                    ATKenemyOGRE = 10
                                    fight = str()
                                else:
                                    printScrolling('You defeated the OGRE.')
                                    printScrolling('You recieve a GOLD COIN.')
                                    coins = coins + 1
                                    cont = True
                            elif fight.lower == str('fist'):
                                printScrolling('You PUNCH the OGRE.')
                                HPenemyOGRE = HPenemyOGRE - ATKcharacter
                                if HPenemyOGRE > 0:
                                    printScrolling('The OGRE attacks you.')
                                    if DEFTIMEshield > 0:
                                        printScrolling('Your shield softens the blow.')
                                        ATKenemyOGRE = ATKenemyOGRE/2
                                        DEFTIMEshield = DEFTIMEshield - 1
                                    HPcharacter = HPcharacter - ATKenemyOGRE
                                    ATKenemyOGRE = 10
                                    fight = str()
                                else:
                                    printScrolling('You defeated the OGRE.')
                                    printScrolling('You recieve a GOLD COIN.')
                                    coins = coins + 1
                                    cont = True
                            elif fight.lower == str('sword'):
                                printScrolling('You ATTACK the OGRE with your sword.')
                                HPenemyOGRE = HPenemyOGRE - (ATKcharacter + ATKsword)
                                if HPenemyOGRE > 0:
                                    printScrolling('The OGRE attacks you.')
                                    if DEFTIMEshield > 0:
                                        printScrolling('Your shield softens the blow.')
                                        ATKenemyOGRE = ATKenemyOGRE/2
                                        DEFTIMEshield = DEFTIMEshield - 1
                                    HPcharacter = HPcharacter - ATKenemyOGRE
                                    ATKenemyOGRE = 10
                                    fight = str()
                                else:
                                    printScrolling('You defeated the OGRE.')
                                    printScrolling('You recieve a GOLD COIN.')
                                    coins = coins + 1
                                    cont = True
                            else:
                                printScrolling('Use the commands in [] to control your character')
                    elif cl == str('run'):
                        printScrolling('You escape safely, and continue your journey')
                        cont = True
                    else:
                        printScrolling('Use the commands in [] to control your character')
                fight = str()
                cont =  False
                rf = str('')
                cl = str('')
            else:
                printScrolling('You encountered an OGRE.')
                while cont == False:
                    printScrolling('Do you [run] or [fight]!')
                    rf = input('')
                    cl = rf.lower()
                    if cl == str('fight'):
                        printScrolling('You decide to fight your enemy.')
                        while HPenemyOGRE > 0:
                            printScrolling('Your HP', HPcharacter)
                            printScrolling('Enemy HP', HPenemyOGRE)
                            if HPcharacter == 0:
                                printScrolling('YOU DIED')
                                printScrolling('Press enter to exit...')
                                input('')
                                exit()
                            fight = input('Do you: ACTIVATE [shield] or ATTACK with [fist]?')
                            if fight.lower == str('shield'):
                                printScrolling('You ACTIVATE your shield.')
                                DEFTIMEshield = DEFTIMEshield + 4
                                if HPenemyOGRE > 0:
                                    printScrolling('The OGRE attacks you.')
                                    if DEFTIMEshield > 0:
                                        printScrolling('Your shield softens the blow.')
                                        ATKenemyOGRE = ATKenemyOGRE/2
                                        DEFTIMEshield = DEFTIMEshield - 1
                                    HPcharacter = HPcharacter - ATKenemyOGRE
                                    ATKenemyOGRE = 10
                                    fight = str()
                                else:
                                    printScrolling('You defeated the OGRE.')
                                    printScrolling('You recieve a GOLD COIN.')
                                    coins = coins + 1
                                    cont = True
                            elif fight.lower == str('fist'):
                                printScrolling('You PUNCH the OGRE.')
                                HPenemyOGRE = HPenemyOGRE - ATKcharacter
                                if HPenemyOGRE > 0:
                                    printScrolling('The OGRE attacks you.')
                                    if DEFTIMEshield > 0:
                                        printScrolling('Your shield softens the blow.')
                                        ATKenemyOGRE = ATKenemyOGRE/2
                                        DEFTIMEshield = DEFTIMEshield - 1
                                    HPcharacter = HPcharacter - ATKenemyOGRE
                                    ATKenemyOGRE = 10
                                    fight = str()
                                else:
                                    printScrolling('You defeated the OGRE.')
                                    printScrolling('You recieve a GOLD COIN.')
                                    coins = coins + 1
                                    cont = True
                            else:
                                printScrolling('Use the commands in [] to control your character')
                    elif cl == str('run'):
                        printScrolling('You escape safely, and continue your journey')
                        cont = True
                    else:
                        printScrolling('Use the commands in [] to control your character')
                fight = str()
                cont =  False
                rf = str('')
                cl = str('')
        else:
            printScrolling('There is no item in this room.')
        while skip == str('false'):
            choicein = input('')
            choice = choicein.lower()
            if choice == str('go north'):
                printScrolling('There is no exit here.')
            elif choice == str('go east'):
                roomID = '2,3'
                skip = 'true'
            elif choice == str('go south'):
                roomID = '1,2'
                skip = 'true'
            elif choice == str('go west'):
                printScrolling('There is no exit here.')
            elif choice == str('pick up item'):
                printScrolling('There is no item in this room.')
            elif choice == str('inventory'):
                printScrolling('You have:')
                printScrolling(coins, ' GOLD COINs')
                if ownSword == str('true'):
                      printScrolling('a SWORD')
                if ownRing == str('true'):
                      printScrolling('a SHINY RING')
                if ownKey == str('true'):
                      printScrolling('a KEY')
            else:
                printScrolling('Use the commands [go north], [go east], [go south], [go west], [pick up item] or [inventory].')
        skip = 'false'
        choicein = str()

    if roomID == str('2,3'):
        printScrolling('You enter a room with two exits, a door to the SOUTH and the WEST.')
        printScrolling('There is no item in this room.')
        while skip == str('false'):
            choicein = input('')
            choice = choicein.lower()
            if choice == str('go north'):
                printScrolling('There is no exit here.')
            elif choice == str('go east'):
                printScrolling('There is no exit here.')
            elif choice == str('go south'):
                roomID = '2,2'
                skip = 'true'
            elif choice == str('go west'):
                roomID = '1,3'
                skip = 'true'
            elif choice == str('pick up item'):
                printScrolling('There is no item in this room.')
            elif choice == str('inventory'):
                printScrolling('You have:')
                printScrolling(coins, ' GOLD COINs')
                if ownSword == str('true'):
                      printScrolling('a SWORD')
                if ownRing == str('true'):
                      printScrolling('a SHINY RING')
                if ownKey == str('true'):
                      printScrolling('a KEY')
            else:
                printScrolling('Use the commands [go north], [go east], [go south], [go west], [pick up item] or [inventory].')
        skip = 'false'
        choicein = str()

    if roomID == str('3,3'):
        printScrolling('You enter a room with only one exit, a door to the SOUTH.')
        if ownKey == str('false'):
            printScrolling('There is a KEY on the ground')
        else:
            printScrolling('There is no item in this room.')
        while skip == str('false'):
            choicein = input('')
            choice = choicein.lower()
            if choice == str('go north'):
                printScrolling('There is no exit here.')
            elif choice == str('go east'):
                printScrolling('There is no exit here.')
            elif choice == str('go south'):
                roomID = '3,2'
                skip = 'true'
            elif choice == str('go west'):
                printScrolling('There is no exit here.')
            elif choice == str('pick up item'):
                if ownKey == str('false'):
                    ownKey = 'true'
                    printScrolling('You obtained a KEY.')
                else:
                    printScrolling('There is no item in this room')
            elif choice == str('inventory'):
                printScrolling('You have:')
                printScrolling(coins, ' GOLD COINs')
                if ownSword == str('true'):
                      printScrolling('a SWORD')
                if ownRing == str('true'):
                      printScrolling('a SHINY RING')
                if ownKey == str('true'):
                      printScrolling('a KEY')
            else:
                printScrolling('Use the commands [go north], [go east], [go south], [go west], [pick up item] or [inventory].')
        skip = 'false'
        choicein = str()

    if roomID == str('4,1'):
        printScrolling('You enter a TUNNEL.')
        printScrolling('This room is unfinished, please contact your manufacturer.')
        while skip == str('false'):
            choicein = input('')
            choice = choicein.lower()
            if choice == str('go north'):
                printScrolling('There is no exit here.')
            elif choice == str('go east'):
                printScrolling('World2 is yet unfinished...')
            elif choice == str('go south'):
                printScrolling('There is no exit here.')
            elif choice == str('go west'):
                roomID = '3,1'
                skip = 'true'
            elif choice == str('pick up item'):
                printScrolling('There is no item in this room.')
            elif choice == str('inventory'):
                printScrolling('You have:')
                printScrolling(coins, ' GOLD COINs')
                if ownSword == str('true'):
                      printScrolling('a SWORD')
                if ownRing == str('true'):
                      printScrolling('a SHINY RING')
                if ownKey == str('true'):
                      printScrolling('a KEY')
            else:
                printScrolling('Use the commands [go north], [go east], [go south], [go west], [pick up item] or [inventory].')
        skip = 'false'
        choicein = str()

#*{F~I~N}*

#Original work of Thomas Newbold
#For personal use only
#Not to be distributed
#New Ideas Inc. MMXVIII
