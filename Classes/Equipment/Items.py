import Weapons
from itertools import count
from collections import Counter

class Items(object):
    """description of class"""


    def getName(self):
        return self.name


    def __str__(self):
        return ("{NAME}".format(NAME=self.name))       
#move Grenade/Medkit/Magazines in here.

#grenade

#medkit

#magazine
#full of bullet objects, max count is determined by weapon type user has. That info will be passed onto it.
#or make dif magazines for each type of weapon?

class Magazine(Items):
    def __init__(self,size,ammoType,name):
        self.holdBullets=[]
        self.startingSize=size
        self.ammoType=ammoType
        self.name=name
        for i in range(self.startingSize):
#creates standard bullets. Make accomidations for other bullet types later.
            self.holdBullets.append(Weapons.Bullet(False,False,True,ammoType))

    def spendBullets(self,amount):
        for each in range(amount):
            if len(self.holdBullets) > 0:
                self.holdBullets.pop(0)
            else:
                print ("Can't fire, out of ammo!")
    
    def getAmmo(self):
        return len(self.holdBullets)

    def getAmmoType(self):
        return self.ammoType

    def getAmmoAmount(self):
        return self.startingSize

    def getCurrentAmmoAmount(self):
        return (len(self.holdBullets))





class ammoBelt(Items):
    def __init__(self,startingMags,magType,ammoType,ammoAmount,name):
        self.holdingMags=[]
        self.startingMags=startingMags
        self.magType=magType
        self.name=name
        self.ammoType=ammoType
        self.ammoAmount=ammoAmount
        for each in range(self.startingMags):
#pass this the actual magazine object somehow and extract the actual object's name that way later.
            self.holdingMags.append(Magazine(self.ammoAmount,magType, ammoType.getName()))

    def getMags(self):
        #magNames=[]
        #for each in range(len(self.holdingMags)):
            #magNames.append(self.holdingMags[each].getName())
        returnedMags=[]
        a=0
        b=0
        c=0
        d=0
        e=0
        for each in range(len(self.holdingMags)):
            if self.holdingMags[each].getName()=="Standard Rifle Magazine":
                a+=1
            elif self.holdingMags[each].getName()=="Standard SMG Magazine":
                b+=1
            elif self.holdingMags[each].getName()=="Standard Shotgun Magazine":
                c+=1
            elif self.holdingMags[each].getName()=="Standard Handgun Magazine":
                d+=1
            elif self.holdingMags[each].getName()=="fake Knife Mag":
                e+=1

        #for idx, type in enumerate (self.holdingMags):
         #   if rifleMagName == self.holdingMags[type].getName():
          #      idx+=1
           # elif smgMagName == self.holdingMags[type].getName():
            #    x+=1
        rifleMagCount="Rifle Magazines: " + str(a)
        smgMagCount="SMG Magazines: " + str(b)
        shotgunMagCount="Shotgun Mags: " + str(c)
        handgunMags="Handgun Mags: " + str(d)
        knifeMags="Knife Slashes: " + str(e)
        if a >= 1:
            returnedMags.append(rifleMagCount)
        elif b >=1:
            returnedMags.append(smgMagCount)
        elif c>=1:
            returnedMags.append(shotgunMagCount)
        elif d >=1:
            returnedMags.append(handgunMags)
        elif e >=1:
            returnedMags.append(knifeMags)
        
        return returnedMags

    def addMag(self,mag):
        self.holdingMags.append(mag)

    def removeMag(self,pick):
        if pick > 0:
            returnedMag=self.holdingMags[pick]
            self.holdingMags.pop(pick)
        else:
            returnedMag=self.holdingMags[0]
            self.holdingMags.pop(0)
        return returnedMag
        

    def getMagName(self):
        return self.name

    def changeMag(self,mag):
        #returnedMag=self.holdingMags[0]
        if mag.getAmmo()>0:
            self.holdingMags.append(mag)

        #return returnedMag

    def getMagNumber(self):
        return self.holdingMags
        
        """x=0
        magCount=[]
        line=""
        for each in range(len(self.holdingMags)):
            x+=1
            line=(x,". ",self.holdingMags[each].getCurrentAmmoAmount())
            magCount.append(line)
        return magCount"""