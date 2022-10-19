import time #for pauses

firstRoom = 'true' #to activate the opening message
worldData = 'world1' #to allow expansion to world 2, 3, etc.
roomID = '2,2' #the current room (the character starts in room 2,2

choicein = str() #the player's choice (input)
choice = choicein.lower() #the player's choice in lowercase, to allow it to be recognised by the computer
skip = 'false' #to allow the choice statement after the initial description to loop if the player inputs an invalid answer

#inventory variables
ownSword = 'false'
ownRing = 'false'
chest = 'closed'
ownKey = 'false'
coins = 0

#character's stats
HPcharacter = 100
ATKcharacter = 10
DEFTIMEshield = 0

#item stats
ATKsword = 15

#enemy stats
HPenemyOGRE = 100
ATKenemyOGRE = 10

#fight mechanic variables
fight = str()
cont =  'false'
c = str()



while worldData == str('world1'):
    
    if roomID == str('1,1'): #this if statment triggers if the player is in this room
        print('You enter a room with only one exit, a door to the EAST.') #initial descrition
        time.sleep(3) #pause
        if ownSword == str('false'): #if statement runs if character doesn't have the sword
            print('There is a SWORD on the ground')
            time.sleep(2)
        else: #otherwise...
            print('There is no item in this room.')
            time.sleep(2)
        while skip == str('false'): #input loop
            choicein = input('') #takes input from player
            choice = choicein.lower() #converts it to lowercase and stores it in a variable to be called upon later
            #answer check - simple if and elif statements
            if choice == str('go north'):
                print('There is no exit here.') #no exit
                time.sleep(2)
            elif choice == str('go east'):
                roomID = '2,1' #there is an exit here, so this command moves the character to the room eastwards by modifying the roomID variable
                skip = 'true' #this skips out of the answer check loop to allow the layer to move on to another room
            elif choice == str('go south'):
                print('There is no exit here.') #no exit
                time.sleep(2)
            elif choice == str('go west'):
                print('There is no exit here.') #no exit
                time.sleep(2)
            elif choice == str('pick up item'):
                if ownSword == str('false'): #if the character doesn't have the sword...
                    ownSword = 'true' #...they pick it up
                    print('You obtained a SWORD.')
                    time.sleep(2)
                else: #otherwise...
                    print('There is no item in this room')
                    time.sleep(2)
            elif choice == str('inventory'): #this informs the player of any items they posess
                print('You have:')
                print(coins, ' GOLD COINs') #coins is a interger (the amount of coins the player has)
                #if they own a item in the list below, the are informed accordingly
                if ownSword == str('true'):
                      print('a SWORD')
                if ownRing == str('true'):
                      print('a SHINY RING')
                if ownKey == str('true'):
                      print('a KEY')
            else:
                print('Use the commands [go north], [go east], [go south], [go west], [pick up item] or [inventory].')
                time.sleep(5) #^if they fail to input a recognisable choice, this statement is printed as a guide^
        skip = 'false' #the skip...
        choicein = str() #...and choicein variables are reset
    
    if roomID == str('2,1'): #nothing special about this room
        print('You enter a room with 3 exits, a door to the NORTH, EAST and WEST.')
        time.sleep(5)
        print('There is no item in this room.')
        time.sleep(2)
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
                print('There is no exit here.')
                time.sleep(2)
            elif choice == str('go west'):
                roomID = '1,1'
                skip = 'true'
            elif choice == str('pick up item'):
                print('There is no item in this room.')
                time.sleep(3)
            elif choice == str('inventory'):
                print('You have:')
                print(coins, ' GOLD COINs')
                if ownSword == str('true'):
                      print('a SWORD')
                if ownRing == str('true'):
                      print('a SHINY RING')
                if ownKey == str('true'):
                      print('a KEY')
            else:
                print('Use the commands [go north], [go east], [go south], [go west], [pick up item] or [inventory].')
                time.sleep(5)
        skip = 'false'
        choicein = str()

    if roomID == str('3,1'): #noteable quality of room: shiny ring
        print('You enter a room with two exits, a door to the WEST and a tunnel to the EAST.')
        time.sleep(5)
        if ownRing == str('false'):
            print('There is a SHINY RING on the ground')
            time.sleep(2)
        else:
            print('There is no item in this room.')
            time.sleep(2)
        while skip == str('false'):
            choicein = input('')
            choice = choicein.lower()
            if choice == str('go north'):
                print('There is no exit here.')
                time.sleep(2)
            elif choice == str('go east'):
                roomID = '4,1'
                skip = 'true'
            elif choice == str('go south'):
                print('There is no exit here.')
                time.sleep(2)
            elif choice == str('go west'):
                roomID = '2,1'
                skip = 'true'
            elif choice == str('pick up item'): #see roomID(1,1) loop for 'pick up item' mechanic
                if ownRing == str('false'):
                    ownRing = 'true'
                    print('You obtained a SHINY RING.')
                    time.sleep(2)
                else:
                    print('There is no item in this room')
                    time.sleep(2)
            elif choice == str('inventory'):
                print('You have:')
                print(coins, ' GOLD COINs')
                if ownSword == str('true'):
                      print('a SWORD')
                if ownRing == str('true'):
                      print('a SHINY RING')
                if ownKey == str('true'):
                      print('a KEY')
            else:
                print('Use the commands [go north], [go east], [go south], [go west], [pick up item] or [inventory].')
                time.sleep(5)
        skip = 'false'
        choicein = str()
    
    if roomID == str('1,2'): #noteable quality of room: chest
        print('You enter a room with 2 exits, a door to the NORTH and to the EAST.')
        time.sleep(4)
        if chest == str('closed'): #notifying the player of the chest in the room...
            print('There is a CLOSED CHEST on the ground. You need a KEY to open it.') #...as such if it is closed...
            time.sleep(4)
        else:
            print('There is a OPEN CHEST on the ground. It is empty.') #...and as such if it is open
            time.sleep(4)
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
                print('There is no exit here.')
                time.sleep(2)
            elif choice == str('go west'):
                print('There is no exit here.')
                time.sleep(2)
            elif choice == str('open chest'): #note: 'pick up item' has been switched with 'open chest' fo this room
                if ownKey == str('true'): #the item KEY is required to open the chest
                    if chest == str('closed'): #if the chest's state is 'closed'...
                        print('You opened the CLOSED CHEST with a KEY. There is a GOLD COIN inside, which you pick up.')
                        coins = coins + 1 #a GOLD COIN is obtained
                        time.sleep(4)
                        chest = 'open' #the chest's state is set to 'open', for future reference
                    else:
                        print('The CHEST is already OPEN. It is empty.')
                        time.sleep(3)
                else: #if they don't have the KEY
                    print('You need a KEY to open the CLOSED CHEST.')
                    time.sleep(3)
            elif choice == str('inventory'):
                print('You have:')
                print(coins, ' GOLD COINs')
                if ownSword == str('true'):
                      print('a SWORD')
                if ownRing == str('true'):
                      print('a SHINY RING')
                if ownKey == str('true'):
                      print('a KEY')
            else:
                print('Use the commands [go north], [go east], [go south], [go west], [open chest] or [inventory].')
                time.sleep(5)
        skip = 'false'
        choicein = str

    if roomID == str('2,2'): #noteable quality of room: first room
        if firstRoom == str('true'): #if this is the first time the room is entered (indicated by the firstRoom variable)...
            print('You wake up from a deep slumber, and find yourself in a dark dungeon, with only a torch to light your way. You are in a room with 4 exits, a door to the NORTH, EAST, SOUTH and WEST.')
            time.sleep(9) #^...the opening message is provided^
            firstRoom = 'false' #firstRoom set to 'false' so this message isn't triggered again
        else: #otherwise...
            print('You enter a room with 4 exits, a door to the NORTH, EAST, SOUTH and WEST.') #...generic message
            time.sleep(5)
        print('There is no item in this room.')
        time.sleep(2)
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
                print('There is no item in this room.')
                time.sleep(2)
            elif choice == str('inventory'):
                print('You have:')
                print(coins, ' GOLD COINs')
                if ownSword == str('true'):
                      print('a SWORD')
                if ownRing == str('true'):
                      print('a SHINY RING')
                if ownKey == str('true'):
                      print('a KEY')
            else:
                print('Use the commands [go north], [go east], [go south], [go west], [pick up item] or [inventory].')
                time.sleep(5)
        skip = 'false'
        choicein = str()
    
    if roomID == str('3,2'): #nothing special about this room
        print('You enter a room with 2 exits, a door to the NORTH and WEST.')
        time.sleep(4)
        print('There is no item in this room.')
        time.sleep(2)
        while skip == str('false'):
            choicein = input('')
            choice = choicein.lower()
            if choice == str('go north'):
                roomID = '3,3'
                skip = 'true'
            elif choice == str('go east'):
                print('There is no exit here.')
                time.sleep(2)
            elif choice == str('go south'):
                print('There is no exit here.')
                time.sleep(2)
            elif choice == str('go west'):
                roomID = '2,2'
                skip = 'true'
            elif choice == str('pick up item'):
                print('There is no item in this room.')
                time.sleep(3)
            elif choice == str('inventory'):
                print('You have:')
                print(coins, ' GOLD COINs')
                if ownSword == str('true'):
                      print('a SWORD')
                if ownRing == str('true'):
                      print('a SHINY RING')
                if ownKey == str('true'):
                      print('a KEY')
            else:
                print('Use the commands [go north], [go east], [go south], [go west], [pick up item] or [inventory].')
                time.sleep(5)
        skip = 'false'
        choicein = str()

    if roomID == str('1,3'): #noteable quality of room: enemy
        print('You enter a room with 2 exits, a door to the EAST and to the SOUTH.')
        #fight mechanic
        if HPenemyOGRE > 0: #if the OGRE is not dead...
            if ownSword == str('true'): #if the player is in possesion of the SWORD...
                print('You encountered an OGRE.')
                time.sleep(2)
                #fight mechanic v.1
                while cont == 'false': #choice loop
                    print('Do you [run] or [fight]!')
                    c = input('')
                    #answer check - if and elif statements
                    if c.lower == str('fight'): #option 1 [-]
                        print('You decide to fight your enemy.')
                        time.sleep(2)
                        #battle loop
                        while HPenemyOGRE > 0: #while the OGRE is not dead
                            #show both entities health
                            print('Your HP', HPcharacter)
                            print('Enemy HP', HPenemyOGRE)
                            if HPcharacter == 0: #checks if character is DEAD
                                print('YOU DIED')
                                time.sleep(10)
                                exit() #ends program
                            fight = input('Do you: ACTIVATE [shield], ATTACK with [fist] or ATTACK with [sword]?') #input [~]
                            if fight.lower == str('shield'): #choice 1 [~]
                                print('You ACTIVATE your shield.')
                                DEFTIMEshield = DEFTIMEshield + 4 #activates shield for 4 turns
                                if HPenemyOGRE > 0: #[*]if the OGRE is alive...
                                    print('The OGRE attacks you.') #...it attacks you
                                    if DEFTIMEshield > 0: #if your shield is active
                                        print('Your shield softens the blow.')
                                        ATKenemyOGRE = ATKenemyOGRE/2 #the OGRE's attack is reduced
                                        DEFTIMEshield = DEFTIMEshield - 1 #-1 from remaining shield protection time
                                    HPcharacter = HPcharacter - ATKenemyOGRE #OGRE's ATk is taken away from the character's HP
                                    ATKenemyOGRE = 10 #the OGRE's ATK is reset (due to the shield being used and reducing it beforehand)
                                    time.sleep(2)
                                    fight = str() #choice is reset
                                else: #otherwise, the OGRE dies because of your attack, and you defeat it, reaping the rewards
                                    print('You defeated the OGRE.')
                                    time.sleep(2)
                                    print('You recieve a GOLD COIN.')
                                    time.sleep(2)
                                    coins = coins + 1
                                    cont = str('true')
                            elif fight.lower == str('fist'): #choice 2 [~]
                                print('You PUNCH the OGRE.')
                                HPenemyOGRE = HPenemyOGRE - ATKcharacter #your ATK is taken away from the OGRE's HP
                                if HPenemyOGRE > 0: #see previous loop [*]
                                    print('The OGRE attacks you.')
                                    if DEFTIMEshield > 0:
                                        print('Your shield softens the blow.')
                                        ATKenemyOGRE = ATKenemyOGRE/2
                                        DEFTIMEshield = DEFTIMEshield - 1
                                    HPcharacter = HPcharacter - ATKenemyOGRE
                                    ATKenemyOGRE = 10
                                    time.sleep(2)
                                    fight = str()
                                else:
                                    print('You defeated the OGRE.')
                                    time.sleep(2)
                                    print('You recieve a GOLD COIN.')
                                    time.sleep(2)
                                    coins = coins + 1
                                    cont = str('true')
                            elif fight.lower == str('sword'): #choice 3 [~]
                                print('You ATTACK the OGRE with your sword.')
                                HPenemyOGRE = HPenemyOGRE - (ATKcharacter + ATKsword) #your ATK, combined with the sword's ATK, is taken away from the OGRE's HP
                                if HPenemyOGRE > 0: #see previous loop [*]
                                    print('The OGRE attacks you.')
                                    if DEFTIMEshield > 0:
                                        print('Your shield softens the blow.')
                                        ATKenemyOGRE = ATKenemyOGRE/2
                                        DEFTIMEshield = DEFTIMEshield - 1
                                    HPcharacter = HPcharacter - ATKenemyOGRE
                                    ATKenemyOGRE = 10
                                    time.sleep(3)
                                    fight = str()
                                else:
                                    print('You defeated the OGRE.')
                                    time.sleep(2)
                                    print('You recieve a GOLD COIN.')
                                    time.sleep(2)
                                    coins = coins + 1
                                    cont = str('true')
                            else: #fallback guide [~]
                                print('Use the commands in [] to control your character')
                                time.sleep(3)
                    
                    elif c.lower == str('run'):  #option 2 [-]
                        print('You escape safely, and continue your journey')
                        time.sleep(3)
                        cont = 'true'
                    else: #fallback guide [-]
                        print('Use the commands in [] to control your character')
                        time.sleep(3)

                #variable reset        
                fight = str()
                cont =  'false'
                c = str()
            else: #otherwise, the character doesn't have the sword
                print('You encountered an OGRE.')
                time.sleep(2)
                #fight mechanic v.2 (similar to v.1, but with no sword option)
                while cont == 'false':
                    print('Do you [run] or [fight]!')
                    c = input('')
                    if c.lower == str('fight'):
                        print('You decide to fight your enemy.')
                        time.sleep(2)
                        
                        while HPenemyOGRE > 0:
                            print('Your HP', HPcharacter)
                            print('Enemy HP', HPenemyOGRE)
                            if HPcharacter == 0:
                                print('YOU DIED')
                                time.sleep(10)
                                exit()
                            fight = input('Do you: ACTIVATE [shield] or ATTACK with [fist]?')
                            if fight.lower == str('shield'):
                                print('You ACTIVATE your shield.')
                                DEFTIMEshield = DEFTIMEshield + 4
                                if HPenemyOGRE > 0:
                                    print('The OGRE attacks you.')
                                    if DEFTIMEshield > 0:
                                        print('Your shield softens the blow.')
                                        ATKenemyOGRE = ATKenemyOGRE/2
                                        DEFTIMEshield = DEFTIMEshield - 1
                                    HPcharacter = HPcharacter - ATKenemyOGRE
                                    ATKenemyOGRE = 10
                                    time.sleep(2)
                                    fight = str()
                                else:
                                    print('You defeated the OGRE.')
                                    time.sleep(2)
                                    print('You recieve a GOLD COIN.')
                                    time.sleep(2)
                                    coins = coins + 1
                                    cont = str('true')
                            elif fight.lower == str('fist'):
                                print('You PUNCH the OGRE.')
                                HPenemyOGRE = HPenemyOGRE - ATKcharacter
                                if HPenemyOGRE > 0:
                                    print('The OGRE attacks you.')
                                    if DEFTIMEshield > 0:
                                        print('Your shield softens the blow.')
                                        ATKenemyOGRE = ATKenemyOGRE/2
                                        DEFTIMEshield = DEFTIMEshield - 1
                                    HPcharacter = HPcharacter - ATKenemyOGRE
                                    ATKenemyOGRE = 10
                                    time.sleep(2)
                                    fight = str()
                                else:
                                    print('You defeated the OGRE.')
                                    time.sleep(2)
                                    print('You recieve a GOLD COIN.')
                                    time.sleep(2)
                                    coins = coins + 1
                                    cont = str('true')
                            else:
                                print('Use the commands in [] to control your character')
                                time.sleep(3)
                    
                    elif c.lower == str('run'):
                        print('You escape safely, and continue your journey')
                        time.sleep(3)
                        cont = 'true'
                    else:
                        print('Use the commands in [] to control your character')
                        time.sleep(3)
                        
                fight = str()
                cont =  'false'
                c = str()
        else: #otherwise... (the OGRE is already dead)
            print('There is no item in this room.')
            time.sleep(2)
        while skip == str('false'):
            choicein = input('')
            choice = choicein.lower()
            if choice == str('go north'):
                print('There is no exit here.')
                time.sleep(2)
            elif choice == str('go east'):
                roomID = '2,3'
                skip = 'true'
            elif choice == str('go south'):
                roomID = '1,2'
                skip = 'true'
            elif choice == str('go west'):
                print('There is no exit here.')
                time.sleep(2)
            elif choice == str('pick up item'):
                print('There is no item in this room.')
                time.sleep(3)
            elif choice == str('inventory'):
                print('You have:')
                print(coins, ' GOLD COINs')
                if ownSword == str('true'):
                      print('a SWORD')
                if ownRing == str('true'):
                      print('a SHINY RING')
                if ownKey == str('true'):
                      print('a KEY')
            else:
                print('Use the commands [go north], [go east], [go south], [go west], [pick up item] or [inventory].')
                time.sleep(5)
        skip = 'false'
        choicein = str()

    if roomID == str('2,3'): #nothing special about this room
        print('You enter a room with two exits, a door to the SOUTH and the WEST.')
        time.sleep(4)
        print('There is no item in this room.')
        time.sleep(2)
        while skip == str('false'):
            choicein = input('')
            choice = choicein.lower()
            if choice == str('go north'):
                print('There is no exit here.')
                time.sleep(2)
            elif choice == str('go east'):
                print('There is no exit here.')
                time.sleep(2)
            elif choice == str('go south'):
                roomID = '2,2'
                skip = 'true'
            elif choice == str('go west'):
                roomID = '1,3'
                skip = 'true'
            elif choice == str('pick up item'):
                print('There is no item in this room.')
                time.sleep(3)
            elif choice == str('inventory'):
                print('You have:')
                print(coins, ' GOLD COINs')
                if ownSword == str('true'):
                      print('a SWORD')
                if ownRing == str('true'):
                      print('a SHINY RING')
                if ownKey == str('true'):
                      print('a KEY')
            else:
                print('Use the commands [go north], [go east], [go south], [go west], [pick up item] or [inventory].')
                time.sleep(5)
        skip = 'false'
        choicein = str()

    if roomID == str('3,3'): #noteable quality of room: KEY
        print('You enter a room with only one exit, a door to the SOUTH.')
        time.sleep(3)
        if ownKey == str('false'):
            print('There is a KEY on the ground')
            time.sleep(2)
        else:
            print('There is no item in this room.')
            time.sleep(2)
        while skip == str('false'):
            choicein = input('')
            choice = choicein.lower()
            if choice == str('go north'):
                print('There is no exit here.')
                time.sleep(2)
            elif choice == str('go east'):
                print('There is no exit here.')
                time.sleep(2)
            elif choice == str('go south'):
                roomID = '3,2'
                skip = 'true'
            elif choice == str('go west'):
                print('There is no exit here.')
                time.sleep(2)
            elif choice == str('pick up item'): #see roomID(1,1) loop for 'pick up item' mechanic
                if ownKey == str('false'):
                    ownKey = 'true'
                    print('You obtained a KEY.')
                    time.sleep(2)
                else:
                    print('There is no item in this room')
                    time.sleep(2)
            elif choice == str('inventory'):
                print('You have:')
                print(coins, ' GOLD COINs')
                if ownSword == str('true'):
                      print('a SWORD')
                if ownRing == str('true'):
                      print('a SHINY RING')
                if ownKey == str('true'):
                      print('a KEY')
            else:
                print('Use the commands [go north], [go east], [go south], [go west], [pick up item] or [inventory].')
                time.sleep(5)
        skip = 'false'
        choicein = str()

    if roomID == str('4,1'): # B O N U S {but otherwise normal} R O O M !
        print('You enter a TUNNEL.')
        print('This room is unfinished, please contact your manufacturer.') #*bants* *references* *jokes* *lolage*
        while skip == str('false'):
            choicein = input('')
            choice = choicein.lower()
            if choice == str('go north'):
                print('There is no exit here.')
                time.sleep(2)
            elif choice == str('go east'):
                print('World2 is yet unfinished...')
                time.sleep(2)
            elif choice == str('go south'):
                print('There is no exit here.')
                time.sleep(2)
            elif choice == str('go west'):
                roomID = '3,1'
                skip = 'true'
            elif choice == str('pick up item'):
                print('There is no item in this room.')
                time.sleep(3)
            elif choice == str('inventory'):
                print('You have:')
                print(coins, ' GOLD COINs')
                if ownSword == str('true'):
                      print('a SWORD')
                if ownRing == str('true'):
                      print('a SHINY RING')
                if ownKey == str('true'):
                      print('a KEY')
            else:
                print('Use the commands [go north], [go east], [go south], [go west], [pick up item] or [inventory].')
                time.sleep(5)
        skip = 'false'
        choicein = str()
    
    time.sleep(1) #fin


#Original work of Thomas Newbold
#For personal use only
#Not to be distributed
#New Ideas Inc. MMXVIII
