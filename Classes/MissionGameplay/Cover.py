import random
from Sound import Sound

class Cover(object):
    def __init__(self,covVal=0,aimPen=-20,hp=0,hitSound=None,breaking=None):
        self.coverValue=covVal
        self.aimPenalty=aimPen
        self.hp=hp
        self.totalMakeup=[covVal,aimPen,hp]
        self.layout=None
        self.uponHitSound=hitSound
        self.uponBreaking=breaking
#***************************************************
#BUILDING COVER LAYOUTS
#*******************************************************
    def coverLayout(self):
    #randomly generates a cover map x number of times. Player and alien will both pull map from results. Give more structure later so maps aren't balls.
        holdCover={}
        covLayStorage={}
        RNG=random.randint(3,7)

        for b in range(4):
            for i in range (RNG):
                typeRNG=Cover.randomCoverType()
                if typeRNG==1:
                    holdCover[i]=Cover(40,20,12,Sound().coverHitSounds("High Cover"),Sound().coverHitSounds("Cover Break"))
                elif typeRNG==2:
                    holdCover[i]=Cover(20,0,6,Sound().coverHitSounds("Low Cover"),Sound().coverHitSounds("Cover Break"))
                elif typeRNG==3:
                    holdCover[i]=Cover(0,-20,0,Sound().coverHitSounds("No Cover"),Sound().coverHitSounds("Cover Break"))
                    
            covLayStorage[b]=holdCover
        
        coverLayoutRNG=random.randrange(len(covLayStorage))
        selectCoverLayout=coverLayoutRNG

        try:
            returnedLayout=covLayStorage[selectCoverLayout]
        except:
            print ("There's no cover layout stored to that key")

        self.layout=returnedLayout
        return returnedLayout

   
    def randomCoverType():
        typeRNG=random.randint(1,3)
        x=typeRNG
        return x

#********************************************
#CHANGE OBJECT VARIABLES
#********************************************

    def takeDamage(self,damage):
        self.uponHitSound.play()
        self.hp-=damage
        
        print ("Cover is hit!")
        if self.hp <=0:
            self.hp=0
        if self.hp==0 and self.coverValue != 0:
            self.uponBreaking.play()
            print ("That cover busted!\n")
            self.coverValue=0
            self.aimPenalty=-20
        else:
            print ("Empty ground is hit.\n")

#**********************************
#RETURN CLASS VARIABLES
#**********************************
    def getCovValue(self):
        return self.coverValue

    def getAimPen(self):
        return self.aimPenalty

    def getHP(self):
        return self.hp

    def getTotalCoverPoints(self):
        coverPoints=0
        for each in range(len(self.layout)):
            coverPoints+=1
        return coverPoints

    def playHitSound(self):
        self.uponHitSound.play()

    def coverBreak(self):
        self.uponBreaking.play()