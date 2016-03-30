import sys
sys.path.append('C:/Users/Leth/Documents/Visual Studio 2015/Projects/CLI_TBCoverCombat_3-29-16-RC_1/GettingPodsToWork3-3-16/Classes/Equipment')
import random
from Grenade import Grenade
from Healing import Healing
from Items import ammoBelt
from Sound import Sound

import os
import time

from Weapons import Weapons

#You!
class Player(object):
 
    def __init__(self,weapons=[],hp=20,imparement=0,defense=30,buff=0):
        self.name="Trooper"
        self.hp=hp
        self.imparement=imparement
        
        self.inventory=[Grenade(),Grenade(),Grenade(),Grenade(),Healing("Medkit",10),Healing("Medkit",10)]
        self.ammoBelt=None
        self.seconaryAmmoBelt=None
        self.defense=defense
        self.aimPenalty=0
        self.coverPosition=0
        self.buff=buff
        self.weapons=weapons
        self.cover=0
        self.currentWeapon=None
        self.deathSound=Sound().deathSounds("Player")
#************************************************************************************
#ACTIONS PLAYER CAN TAKE
#************************************************************************************
    def changeCover(self,playerBattleMap):
        coverSet=0
        while coverSet==0:
            for each in playerBattleMap:
                print (each+1,": Cover Value:",playerBattleMap[each].getCovValue()," Aim Penalty:",playerBattleMap[each].getAimPen()," Cover HP:",playerBattleMap[each].getHP())
            try:
                chooseCover=(int(input("Which cover do you take?"))-1)
                
            except:
                print ("That's not a valid option, try again.\n\n")
                continue

            if chooseCover in playerBattleMap:
                playerCover=playerBattleMap[chooseCover].getCovValue()
                playerAimPen=playerBattleMap[chooseCover].getAimPen()
                self.cover=playerCover
                playerCovPos=chooseCover
                self.defense=30
                self.defense=self.defense+playerCover
                self.aimPenalty=playerAimPen
                self.coverPosition=playerCovPos
                coverSet=1
            
            else:
                print ("That's not a valid cover option")
                continue
            

    def gunshotAccuracy(self,enemyDef,alienBattleMap,coverPosition):
        #taunted/pissed off is 1. # calculates shot%, factoring in cover and any status ailments

        targetHit=0
        pissedOff=0
        takingAim=0
        #print ("DEBUG*** This is the status element= ",self.imparement)
        #print ("DEBUG*** this is your buff number: ",self.buff)
        if self.imparement==1:
            pissedOff=20
        if self.buff==1:
            takingAim=-50
        print ("BANG!")

        baseHitChance=self.currentWeapon.getAcc()
        #print (baseHitChance,enemyDef,self.aimPenalty,pissedOff,takingAim,"   ",baseHitChance-enemyDef-self.aimPenalty-pissedOff-takingAim)
        adjustedHitChance=baseHitChance-enemyDef-self.aimPenalty-pissedOff
        if adjustedHitChance<0:
            adjustedHitChance=0
        if adjustedHitChance>100:
            adjustedHitChance=100
        adjustedHitChance-=takingAim
        print ("Chance to hit: ", adjustedHitChance)
        hitCoverRNG=random.randint(1,2)
        RNG=random.randint(1,100)
        if RNG <= adjustedHitChance:
            
            print ("Hit Roll: ", RNG,"\n")
            print ("That's a hit!")
            targetHit=1
        else:
            if hitCoverRNG==1:
                print ("Hit Roll: ", RNG,"\n")
                targetHit=3
            else:
                print ("Hit Roll: ", RNG,"\n")
            #print ("Damn, you missed!")"
                targetHit=2
        return targetHit
 
    def useItem(self):
        for idx,item in enumerate(self.inventory):
            idx+=1
            print(idx,item)
        
        item=(input("Which item do you want to use?"))
        if item=="B" or item=="b":
            print ("Nope")
            os.system('cls' if os.name=='nt' else 'clear')
            return

        else:
            try:
                item=(int(item))
            except:
                print ("not a number")
                os.system('cls' if os.name=='nt' else 'clear')
                return
        
        if item >=1:
            item-=1

        if item not in range(len(self.inventory)):
            print ("Not a valid item number, pick another or hit B to go back:")
            os.system('cls' if os.name=='nt' else 'clear')
            return

        sendItem=self.inventory[item]
        return sendItem,item

    #make this adaptable to more than 2 weapons later on
    def switchWeapons(self):
        if self.currentWeapon==self.weapons[0]:
            self.currentWeapon=self.weapons[1]
            print (self.currentWeapon)

        elif self.currentWeapon==self.weapons[1]:
            self.currentWeapon=self.weapons[0]
            print(self.currentWeapon)
    
    def hunkerDown(self):
        self.defense+=30

    def takeAim(self,playerBuff):
        self.buff+=playerBuff

    def getSpecificAmmoBelt(self):
        if self.currentWeapon==self.weapons[0]:
            return 0

        elif self.currentWeapon==self.weapons[1]:
            return 1        


#make this work with magazine objects
    def reloadGun(self,pick):
        if self.currentWeapon==self.weapons[0]:
            
            print ("current wep = wep [0]")
            newMag=self.ammoBelt[0].removeMag(pick)
            print (newMag.getName())
            oldMag=self.currentWeapon.reload(newMag)
            self.ammoBelt[0].changeMag(oldMag)
        if self.currentWeapon==self.weapons[1]:

            print ("current wep = wep [1]")
            newMag=self.ammoBelt[1].removeMag(pick)
            print (newMag.getName())
            oldMag=self.currentWeapon.reload(newMag)
            self.ammoBelt[1].changeMag(oldMag)
    
#**************************************************
#ALTER YOUR STATS (HP/DEF/AIM/STATUS)
#**************************************************

    def setDefense(self,playerCoverBonus):
        self.defense=30
        self.defense=self.defense+playerCoverBonus

    def setAimPen(self,playerAimPen):
        self.aimPenalty=0
        self.aimPenalty=self.aimPenalty+playerAimPen

    def status(self,ailment):
        #status aliments, good and ill, will check here to see if they pass or fail
        #taunt is 1, aiming is 2, resisted is 0
        inflicted=0
        checking=ailment
        baseResist=70
        rRNG=random.randint(1,100)
        if rRNG <= baseResist:
            if checking==1:
                self.imparement=1

        return self.imparement
    
    def healing(self,amount):
        self.hp+=amount
        if self.hp >= 20:
            self.hp = 20
        return self.hp

    def damage(self,damage):
        self.hp-=damage
        if self.hp <=0:
            self.hp=0
        return self.hp

    def turnPass(self,turn):
        if self.imparement!=0:
            self.imparement=0
        return self.imparement

    def tickAimTimerDown(self,timeTick):
        self.buff=self.buff-timeTick
        if self.buff<0:
            self.buff=0

#*********************************************
# PLAYER ITEMS AND WEAPONS
#*********************************************

    def playerWeapons(self,selectedWeapons):
        self.weapons=selectedWeapons
        self.currentWeapon=self.weapons[0]

    def equipAmmoBelt(self,belts):
        self.ammoBelt=belts


    def removeItem(self,item):
        self.inventory.pop(item)


#***********************************
#RETURN CLASS VARIABLES
#***********************************
    def getName(self):
        return self.name

    def getCoverPosition(self):
        return self.coverPosition

    def getHP(self):
        return self.hp


    def returnPlayerWeapons(self):
        return self.weapons

    def returnDef(self):
        return self.defense
    
    def getItemNames(self,itemNum):
        return self.inventory[itemNum].getName()

    def returnWepDamage(self):
        return self.weapons[0].getDamage()

    def returnWeaponNames(self):
        return self.weapons[0].getName(), self.weapons[1].getName()

    def getCurrentPlayerWeapon(self):
        return self.currentWeapon

    def getBackupMags(self):
        return self.ammoBelt[0].getMags(), self.ammoBelt[1].getMags()

    def getBackupMagAmount(self):
        return self.ammoBelt[0].getMagNumber(), self.ammoBelt[1].getMagNumber()
        
    def getBackupMagsName(self):
        primMagName=self.ammoBelt[0].getMags()
        primMagName=(str(primMagName)[2:-2])

        secMagName=self.ammoBelt[1].getMags()
        secMagName=(str(secMagName)[2:-2])
        
        
        return primMagName,secMagName

    def getCoverValue(self):
        if self.cover==40:
            cover="High cover"
        elif self.cover==20:
            cover="Low cover"
        else:
            cover="No cover"
        return cover

    def playDeathSound(self):
        self.deathSound.play()

    def getTauntStatus(self):
        if self.imparement==1:
            returnPrint=("taunted")
        else:
            returnPrint=("not taunted")
        return returnPrint

    def getAimStatus(self):
        if self.buff==1:
            returnAim=("taking aim")
        else:
            returnAim=("not taking aim")
        return returnAim



    def getHitChance(self,targetInfo):
#largely copied code. Consolidate gunshot acc and this somehow

        targetHit=0
        pissedOff=0
        takingAim=0
        #print ("DEBUG*** This is the status element= ",self.imparement)
        #print ("DEBUG*** this is your buff number: ",self.buff)
        if self.imparement==1:
            pissedOff=20
        if self.buff==1:
            takingAim=-50
        

        baseHitChance=self.currentWeapon.getAcc()
        adjustedHitChance=baseHitChance-targetInfo-self.aimPenalty-pissedOff
        adjustedHitChance-=takingAim
        if adjustedHitChance<0:
            adjustedHitChance=0
        if adjustedHitChance>100:
            adjustedHitChance=100
        return adjustedHitChance


    def getInventory(self):
        return self.inventory

    def getSpecificInventoryItem(self,item):
        print (self.inventory[item])
        return self.inventory[item]