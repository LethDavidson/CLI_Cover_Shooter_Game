import sys
sys.path.append("Classes/Sound")
from Sound import Sound
from Pods import Pods
from collections import Counter
from Player import Player
from Cover import Cover
import pygame
import random
import os
import time

class Combat(object):

    def __init__(self,done=0):
        self.done=0


    pygame.init()

    #**************************
    #PRE-COMBAT MUSIC SETUP
    #**************************

    def setCombatMusic():
        musicRNG=random.randint(1,4)
        print (musicRNG)
        music=Sound().gameMusic(musicRNG)
        pygame.mixer.music.load(music)
        

    #**************************
    #POST-FIGHT WRAP-UP
    #**************************

    def returnToMap():
        victory=0


   
    #*********************************************************************************
    #ACTOR TURNS
    #*********************************************************************************

    def playerTurn(self,pod,user,alienBattleMap,playerBattleMap,shotMissSound,playerEquipment):
        playerTurn=1
        
        while playerTurn==1:  
                currentWeapon=user.getCurrentPlayerWeapon()
                playerAction=Combat.userInterface(pod,user,alienBattleMap,playerBattleMap,shotMissSound)
                if playerAction[0]==1 and currentWeapon.getMagAmmo() > 0:
                    finishShoot=Combat.playerShoot(pod,user,alienBattleMap,playerBattleMap,shotMissSound)
                    if finishShoot ==0: 
                        continue
                    else:
                        Combat.spendPlayerAmmo(currentWeapon)
                        user.tickAimTimerDown(1)

                elif playerAction[0]==1 and currentWeapon.getMagAmmo() <= 0:     
                      print ("Can't fire, out of ammo!")
                      continue  
                elif playerAction[0]==2:
                    finishItem=Combat.playerItem(pod,user,alienBattleMap,playerBattleMap,shotMissSound)
                    if finishItem==0:
                        continue
                    else:
                        user.tickAimTimerDown(1)
                elif playerAction[0]==3:
                    Combat.playerCover=user.hunkerDown()
                    user.tickAimTimerDown(1)
                elif playerAction[0]==4:
                    user.takeAim(2)
                    user.tickAimTimerDown(1)

                elif playerAction[0]==5:
                    user.changeCover(playerBattleMap)
                    os.system('cls' if os.name=='nt' else 'clear')
                    continue
                elif playerAction[0]==6:
                    user.switchWeapons()
                    os.system('cls' if os.name=='nt' else 'clear')
                    continue
                elif playerAction[0]==7:
                    user.reloadGun(0)
                
                elif playerAction[0]==8:
                    finishReload=Combat.manualReload(user,playerEquipment,playerAction[1],playerAction[2])
                    if finishReload==0:
                        continue
                    else:
                        user.tickAimTimerDown(1)
                elif playerAction[0]==9:
                    print ("You get the hell out of there")
                    return 1
                
                
                else:
                    print ("That's not a valid command choice")
                    os.system('cls' if os.name=='nt' else 'clear')
                    continue
#playeraction[0] is command choice, [1] and [2] are backupmag and rawmagammoinfo for manualreload to avoid creating duplicates in that function
                    
                user.turnPass(Combat.passTurn())
                #print ("ALIEN BATTLE MAP")
                #for each in alienBattleMap:
                    #print (each,": Cover Value:",alienBattleMap[each].getCovValue()," Aim Penalty:",alienBattleMap[each].getAimPen()," Cover HP:",alienBattleMap[each].getHP())
                
                print ("\n")
                playerTurn=0

    def alienTurn(user,pod,actions,alienCoverStats,playerCopyAlienCover,alienBattleMap,playerBattleMap,shotMissSound):
                playerCovPos=user.getCoverPosition()

                pastCoverPoints=[]
                newCoverPoint=0
                t=0
                takenCover=[]
                for each in range(0,len(pod)):
                    t+=1
                    actions.append(pod[each].action())
#move aliencover to 1 index from0 index if this doesn't work.
#WAIT fuck no. I'm getting the number of items, not the exact number when I'm using range(len(ect)). I need to check the value of each number, not how many it has. It's a list of int, not obj, damn that should work. Gah
                    c=0
                    while c==0:
                      #i just need to figure out which element to delete upon the lopp so that it doens't select the same ones over and over or get into a loop where the answer is deleted before it'sp oroperly checked.  
                        #pastCoverPoints.append(pod[each].returnCoverPosition())

                        alienCoverStats.append(pod[each].takeCover(alienBattleMap,pod,each))
                        if pod[each].returnCoverPosition() in takenCover:
                            
                            print ("Taking cover again")
                            continue
                        else:
                            takenCover.append(pod[each].returnCoverPosition())
                            print (range(len(takenCover)))
                            c=1


                    
                    if actions[each]=="shoot":
                        Combat.alienShoot(each,pod,user,playerBattleMap,playerCovPos,shotMissSound)

                    if actions[each]=="taunt":
                        Combat.alienTaunt(pod,each,user)

                    playerCopyAlienCover.append(alienCoverStats)
                    alienCoverStats[:]=[]
                        
                    
                    time.sleep(0.5)
                    print ("-------------------------------------")
                takenCover[:]=[]
                actions[:]=[]

                print ("End of alien turn.\n\n")
#send all of this mag data rather than creating it again once it works.

#it only sends back the corrent ammo amount/correct mag if it's 1. hmm...
#fixed it, I put a 0 in the wrong place.
    def manualReload(user,playerEquipment,backupMags,rawBackupMagNumbers):
                currentWepBelt=user.getSpecificAmmoBelt()
                p=0
                for every in range(len(rawBackupMagNumbers[currentWepBelt])):
                        p+=1
                        print ("{MAGTYPE} Mag {NUMBER} ammo".format(MAGTYPE=backupMags[currentWepBelt][:1],NUMBER=p),":",rawBackupMagNumbers[currentWepBelt][every].getCurrentAmmoAmount(),end=", ")
                        if p == (len(rawBackupMagNumbers[currentWepBelt])):
                            p=0
                            print ("\n")
                approvedMag=0
                while approvedMag==0:
                    pickMag=(input("Which magazine do you reload with? Or hit B to go back?"))
                    if not pickMag:
                        continue
                    if pickMag == "b" or pickMag == "B":                    
                        os.system('cls' if os.name=='nt' else 'clear')
                        return 0
                    try:
                        pickMag=(int(pickMag)-1)
                    except ValueError:
                        print ("Not a number")
                    
                        continue
                    if pickMag not in range (len(rawBackupMagNumbers[currentWepBelt])):
                        continue
                    else:
                        approvedMag=1

                user.reloadGun(pickMag)
                print ("Ready to go!")
                        

    #*********************************************************************************
    #RESULTS OF PLAYER COMBAT ACTIONS
    #*********************************************************************************


    def playerShoot(pod,user,alienBattleMap,playerBattleMap,shotMissSound):
        print (pod)

        approvedShot=0
        while approvedShot==0:
                choice=(input("\nChoose which enemy to drop, or enter B to go back.: "))
                if not choice:
                    continue
                if choice == "b" or choice == "B":                    
                    os.system('cls' if os.name=='nt' else 'clear')
                    return 0
                try:
                    choice=int(choice)
                except ValueError:
                    print ("Not a number")
                    
                    continue
                if choice not in range (len(pod)):
                    continue
                else:
                    approvedShot=1


        listChoice=choice-1
        os.system('cls' if os.name=='nt' else 'clear')
        for x in range (len(pod)+1):
            x+=1
            if choice==x:
                targetHit=user.gunshotAccuracy(pod[listChoice].getDefense(),alienBattleMap,1)

            else:
                continue
        
            coverPosition=pod[listChoice].returnCoverPosition()
            if targetHit==1:
                pod[listChoice].damage(user.returnWepDamage())
                checkTargetHealth=pod[listChoice].damage(0)
                if checkTargetHealth==0:
                    if listChoice in range(len(pod)):
                            pod[0].playAlienDeath()
                            pod.pop(listChoice)
                            
                
            elif targetHit==2:
                shotMissSound.play()
                print ("You missed!")
                
            elif targetHit==3:
                print ("You hit it's cover!")
                #alienBattleMap[coverPosition].playHitSound()
                alienBattleMap[coverPosition].takeDamage(user.returnWepDamage())


            print ("End of player turn\n------------------------------------------")
        
            
    def playerItem(pod,user,alienBattleMap,playerBattleMap,shotMissSound):

        playerInventory=user.getInventory()
        y=0
        for each in range(len(playerInventory)):
            y+=1
            print (y,": ",playerInventory[each])

        selection=Combat.errorCheckForInt(len(playerInventory),"Which item will you use? Or hit B to go back:")

        selection=(int(selection))-1
        if selection in range(len(playerInventory)):
                    
            itemToUse=user.getSpecificInventoryItem(selection)
                
            if itemToUse.getName() == "Grenade":
                   x=0
                   for each in range(len(pod)):
                        x+=1
                        print (x,": ", pod[each].getName(),", ",end="")
                   approvedEnemy=0
                   while approvedEnemy==0:
                       chooseEnemy=(input("Use grenade on which enemy? or hit B to go back\n"))
                       if not chooseEnemy:
                           continue
                       if chooseEnemy == "b" or chooseEnemy == "B":
                           return 0
                       try:
                        chooseEnemy=(int(chooseEnemy)-1)
                       except ValueError:
                           print ("Not a number")
                           continue
                       if chooseEnemy not in range (len(pod)):
                           continue
                       print ("About to go into item usage")
                       if chooseEnemy in range(len(pod)):
                           itemToUse.playSound()
                           print ("You hit {ENEMY} with a grenade!".format(ENEMY=pod[chooseEnemy].getName()))
                           pod[chooseEnemy].damage(itemToUse.explode())
                           user.removeItem(selection)
                           checkTargetHealth=pod[chooseEnemy].damage(0)
                           if checkTargetHealth==0:
                                if chooseEnemy in range(len(pod)):
                                    pod.pop(chooseEnemy)

                           return 1
            if itemToUse.getName() == "Medkit":
                healSelection=(input("Heal yourself for {AMOUNT}? Y/N or B for back.\n".format(AMOUNT=itemToUse.getHealAmount())))
                if healSelection=="Y" or healSelection=="y":
                    user.healing(itemToUse.getHealAmount())
                    return 1

    def spendPlayerAmmo(weapons):
        weapons.spendAmmo(1)
     
    #********************************************************************************
    #RESULTS OF ALIEN COMBAT ACTIONS
    #******************************************************************************** 
    def alienShoot(each,pod,user,playerBattleMap,playerCovPos,shotMissSound):
    
        gunshot=pod[each].shoot(user.returnDef())
        if gunshot==1:
            user.damage(2)
            Combat.userPainSound()
            checkPlayerHP=user.damage(0)
            if checkPlayerHP==0:
                user.playDeathSound()
                print ("\nYou're dead soldier! Your sacrifice shall not be forgotten.")
                done=1
               
        if gunshot==2:
            shotMissSound.play()
            print ("It misses!")
        if gunshot==3:
            #playerBattleMap[playerCovPos].playHitSound()
            playerBattleMap[playerCovPos].takeDamage(3)

    def alienTaunt(pod,each,user):
        ailment=pod[each].taunt()
        playerResist=user.status(ailment)
        if playerResist==1:
            print ("That pisses you off! Your chance to hit is reduced by 20% for 1 turn.\n")
        else:
            print ("You don't give a damn.\n")

    #**********************************************************************************************
    #MISC COMBAT FUNCTIONS
    #**********************************************************************************************
    def checkIfVictory(pod,user):
        if len(pod)==0 or user.getHP()<=0:
            pygame.mixer.music.fadeout(1000)
            done=1
        else:
            done=0
        return done
    
    def fleeCombat():
        pygame.mixer.music.fadeout(1000)
        done=1
        return done

    def healUnit(user,itemUse):
        selfheal=(input("Heal yourself for {HEALAMOUNT}? Y/N : ".format(HEALAMOUNT=itemUse.getHealAmount())))
        if selfheal=="Y" or "y":
            user.healing(itemUse.getHealAmount())

    def passTurn():
        passturn=1


    def userInterface(pod,user,alienBattleMap,playerBattleMap,shotMissSound):
           
            totalHealth=[]
            playerTurn=1
            while playerTurn==1:
                for each in range(len(pod)):
                    alienDefense=pod[each].getDefense()
                    chanceToHit=user.getHitChance(alienDefense)
                #this is the big fucking confusing HUD.

                currentWeapon=user.getCurrentPlayerWeapon()
                for a in range(len(pod)):
                    totalHealth.append(pod[a].getHP())
                print ("{player} HP: {pHP}\nIn {COVTYPE} at point {COVLOCATION} out of {TOTALCOVPOINTS}.\nYou are {TAUNTSTATUS}, and {AIMSTATUS}.\n".format(player=user.getName(),pHP=user.getHP(),COVTYPE=user.getCoverValue(),COVLOCATION=user.getCoverPosition()+1,TOTALCOVPOINTS=len(playerBattleMap),TAUNTSTATUS=user.getTauntStatus(),AIMSTATUS=user.getAimStatus()))
                print ("\t\t\tTotal Alien Cover Points: {COVPOINTS}".format(COVPOINTS=len(alienBattleMap)))
                for each in range(len(pod)):
                    print ("\t\t\t{ENEMY} has {HP} HP and is behind {COVERTYPE} at enemy point {COVLOCATION} with a {ENEMYHITCHANCE}% chance to hit you.\n\t\t\tYou have a {CHANCETOHIT}% chance to hit {ENEMY}.\n".format(ENEMY=pod[each].getName(),HP=pod[each].getHP(),COVERTYPE=pod[each].returnCoverValue(),COVLOCATION=pod[each].returnCoverPosition()+1,ENEMYHITCHANCE=pod[each].calcHitChance(user.returnDef()),CHANCETOHIT=chanceToHit))
                #print (user.returnPlayerWeapons.getname())
                print ("Weapon:",currentWeapon.getName(),"\tAmmo:", currentWeapon.getMagAmmo())
#It has something to do with this. FIrst and second ammo belt position don't hange, as such it's not atually uipdating. 
                backupMags=user.getBackupMagsName()
                rawBackupMagNumbers=user.getBackupMagAmount()
                print ("Current Magazines: ", backupMags[0],",",backupMags[1])
                p=0
                for each in range(len(rawBackupMagNumbers)):
                    for every in range(len(rawBackupMagNumbers[each])):
                        p+=1
                        print ("{MAGTYPE} Mag {NUMBER} ammo".format(MAGTYPE=backupMags[each][:1],NUMBER=p),":",rawBackupMagNumbers[each][every].getCurrentAmmoAmount(),end=", ")
                        if p == (len(rawBackupMagNumbers[each])):
                            p=0
                            print ("\n")


                print ("Current Items: ",end="")
                for each in range(len(user.getInventory())-1):
            
                    print (user.getItemNames(each), end=", ")
                
                print (user.getItemNames(each+1), end="")   
                print("\n")
                totalHealth[:]=[]
                print ("\n1.Shoot at enemy: Take a single shot at an enemy, ends turn.\n2.Use an item: Use an item from your inventory, ends turn.\n3.Get Down: Gain a 30% def boost for the turn, ends turn\n4.Aim next shot: Gain a 50% aim boost for the next turn, ends turn.\n5.Change Cover: Switches your current cover, does not end turn.\n6.Switch Weapons: Switches your current weapon, does not end turn.\n7.Reload Weapon: Reloads your current weapon with next available magazine, ends turn.\n8.Choose Magazine: Manually select which magazine to reload with, ends turn.\n9.Flee Combat:Exit combat and return to mission selection screen.\n\n")

                try:
                    playerAction=(int(input("What action will you take? ")))
                except ValueError:
                    print ("Not a number, try again")
                    os.system('cls' if os.name=='nt' else 'clear')
                    continue

                return playerAction,backupMags,rawBackupMagNumbers

    def displayAmmoInMags(ammoBelts):
        for each in ammoBelts[0]:
            print (ammoBelts[0][each].getCurrentAmmoAmount())
                
    def userPainSound():
        painRNG=random.randrange(1,9)
        pain=Sound().userPainSounds(painRNG)
        pain.play()

    def areWeDone(self,yesOrNo):
        done=0
        if yesOrNo==0:
            self.done=0
        else:
            self.done=1
        return self.done

    def errorCheckForInt(listReference,specificPrompt):
        approvedCheck=0
        while approvedCheck==0:
                checkedValue=(input(specificPrompt))
                if not checkedValue:
                    continue
                if checkedValue == "b" or checkedValue == "B":
                    os.system('cls' if os.name=='nt' else 'clear')
                    return checkedValue
                try:
                    checkedValue=int(checkedValue)-1
                except ValueError:
                    print("That's not a number mate, try again.")
                    continue
                if checkedValue not in range(len(listReference)):
                    continue
                else:
                    approvedCheck=1
                    return checkedValue
   #used when I want a specific index for a list later, and to keep out wrong numbers, letters, or blank spaces.    
        
    #********************************************************************
    #MAIN LOOPS
    #********************************************************************
    def combat(self,pod,user,playerBattleMap,alienBattleMap,playerEquipment,ranAway=0,playerDead=0):
    #taunt and shoot are shorthand for alien action options
        
        if ranAway !=0:
            done=1
        if playerDead!=0:
            done=1
        taunt="taunt"
        shoot="shoot"
        battleTurn=1 #1=Player,2=Alien.
        shotMissed=Sound().weaponSounds("Shot Miss")
        shotMissed.set_volume(1)
        turn=0 #turn ticks when turn passes, allowing for status aliments to fade after turns
        
        Combat.setCombatMusic()
        shotMissed.play()
        
        pygame.mixer.music.set_volume(1)
        pygame.mixer.music.play(-1,0)

    #*****************************************
    #lists holding combat actions/reactions
    #--------------------------------------
        actions=[] #actions holds enemy action choices.
        #totalHealth=[] #pulls hp from enemies in pod for ui purposes
        alienCoverStats=[] #pulls cover stats from enemiesi n pod for ui purposes
        playerCopyAlienCover=[] #copy of aliencoverstats made after they are cleared each turn. For long-term ui storage
    #*****************************************


    #main combat loop
        done=0
        while done==0:
            #At the start of combat, player chooses which cover they'll take.
            print ("You've touched down and found the enemies. Press the coorisponding number key to get into that over point.")
            os.system('cls' if os.name=='nt' else 'clear')
            user.changeCover(playerBattleMap)
            os.system('cls' if os.name=='nt' else 'clear')
    #show pod, make action selection, turn passed and it switches to alien.
            while battleTurn==1:
                ranAway=Combat.playerTurn(self,pod,user,alienBattleMap,playerBattleMap,shotMissed,playerEquipment)
                if ranAway==1:
                    done=1
                    os.system('cls' if os.name=='nt' else 'clear')
                    break
                print ("back to main, done=",done)
                done=Combat.checkIfVictory(pod,user)
                
                time.sleep(0.5)
                battleTurn=2
#if player chooses to run away, it returns runAway as 1. if 1, then done=1 and loop breaks, running funct again. ranAway, despite being an intitalized variable, stayed 1 and thus done
#also stayed 1. So with done=1, then there's no game loop and it's back to the main screen. Easy-peasy.

    #gets player position,then each alien in pod takes an action and cover. either taunt or shoot. clear results each time but store in sep list 1st
            while battleTurn==2:
                Combat.alienTurn(user,pod,actions,alienCoverStats,playerCopyAlienCover,alienBattleMap,playerBattleMap,shotMissed)
                playerDead=Combat.checkIfVictory(pod,user)
                if playerDead==1:
                    done=1
                    break
                
                input("Enter any key then hit enter to progress to your turn")
                battleTurn=1
   
