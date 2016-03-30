import random
import sys
sys.path.append('C:/Users/Leth/Documents/Visual Studio 2015/Projects/CLI_TBCoverCombat_3-29-16-RC_1/GettingPodsToWork3-3-16/Classes/Sound')
from Sound import Sound

class Sectoid(object):
    def __init__(self,name,hp=8,taunt=0,defense=10,cover=0,aimPen=0):
        self.name=name
        self.hp=hp
        self.playerTaunt=taunt
        self.alive=1
        self.defense=defense
        self.cover=cover
        self.aimPenalty=aimPen
        self.coverPosition=0
        self.wepSound=Sound().weaponSounds("Laser")
        self.deathSound=Sound().deathSounds("Sectoid")
        self.tauntSound=Sound().abilitySounds("Taunt")
        self.uponHit=Sound().enemyPainSounds("Sectoid")

#***********************************************************************
#ACTIONS ALIEN CAN TAKE
#***********************************************************************
    
    def action(self):
        action=0
        tRNG=random.randint(1,5)
        if tRNG==1:
            action="taunt"
        else:
            action="shoot"

        return action

    def taunt(self):     
        self.tauntSound.play()
        print ('{name} taunts you! \n It yells, "Gleep gloop!\n"'.format(name=self.name))
        pissOff=1
        return pissOff     

    def takeCover(self,alienBattleMap,pod,whichAlien):
        alienChooseCover=Sectoid.randomSample(alienBattleMap,pod,whichAlien)
        self.cover=alienBattleMap[alienChooseCover].getCovValue()
        self.aimPenalty=alienBattleMap[alienChooseCover].getAimPen()
        self.coverPosition=alienChooseCover
        return self.cover, self.aimPenalty,self.coverPosition

    def shoot(self,playerDef):
        targetHit=0
        print ("{NAME} shoots!\n".format(NAME=self.name))
        self.wepSound.play()
        adjustedHitChance=Sectoid.calcHitChance(self,playerDef)
        hitCoverRNG=random.randint(1,2)
        RNG=random.randint(1,100)
        if RNG <= adjustedHitChance:
            print ("Alien Chance to Hit: ", adjustedHitChance)
            print ("Alien's Roll: ", RNG,"\n")
            print ("Ouch! You're hit!\n")
            targetHit=1

        else:
            if hitCoverRNG==1:
                print ("Alien Chance to Hit: ", adjustedHitChance)
                print ("Alien's Roll: ", RNG,"\n")
                targetHit=3

            else:
                print ("Alien Chance to Hit: ", adjustedHitChance)
                print ("Alien's Roll: ", RNG,"\n")
                print ("It misses!\n")
                targetHit=2

        return targetHit



#******************************************************
#RNG FOR COVER SELECTION
#***************************************************   

    def randomCoverType(alienBattleMap):
        typeRNG=random.randrange(len(alienBattleMap))
        x=typeRNG
        return x

    def randomSample(alienBattleMap,pod,whichAlien):
        mapRNG=random.randrange(len(alienBattleMap))
        answer=mapRNG
        return answer


#************************************************
#ALIEN STAT CALCULATION
#*************************************************

    def getDefense(self):
        defense=self.defense+self.cover
        return defense
    
    def damage(self,DMGval):
        if self.hp > self.hp-DMGval:
            self.uponHit.play()
        self.hp-=DMGval
        if self.hp <=0:
            self.hp=0;
        if self.hp > 0:
            self.action
        if self.hp==0:
            print ("You killed it!")
        return self.hp

    def calcHitChance(self,playerDef):
        baseHitChance=80
        adjustedHitChance=baseHitChance-playerDef-self.aimPenalty
        if adjustedHitChance<0:
            adjustedHitChance=0
        if adjustedHitChance>100:
            adjustedHitChance=100
        return adjustedHitChance

#************************************************************
#RETURN CLASS VARIABLES
#************************************************************

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name

    def getName(self):
        return self.name
    
    def getHP(self):
        return self.hp

    def returnCoverPosition(self):
        return self.coverPosition

    def returnCoverValue(self):
        if self.cover==40:
            cover="High cover"
        elif self.cover==20:
            cover="Low cover"
        else:
            cover="No cover"
        return cover

    def playAlienDeath(self):
        self.deathSound.play()

    def playHitSound(self):
        self.uponHit.play()