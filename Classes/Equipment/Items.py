import Weapons
from itertools import count
from collections import Counter

class Items(object):
    """Creates all of the items"""

    def getName(self):
        return self.name

    def __str__(self):
        return ("{NAME}".format(NAME=self.name))       

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
#********************************
#RETURN VARIABLES
#********************************   
    def getAmmo(self):
        return len(self.holdBullets)
#Get all of the current bullets

    def getAmmoType(self):
        return self.ammoType
#gets what type of bullets they are

    def getAmmoAmount(self):
        return self.startingSize
#gets the full starting size of the mag

    def getCurrentAmmoAmount(self):
        return (len(self.holdBullets))
#also returns current bullets? I think I redid some work here... hmm, look for that.




class ammoBelt(Items):
    def __init__(self,startingMags,magType,ammoType,ammoAmount,name):
        self.holdingMags=[]
        self.startingMags=startingMags
        self.magType=magType
        self.name=name
        self.ammoType=ammoType
        self.ammoAmount=ammoAmount
        for each in range(self.startingMags):
            self.holdingMags.append(Magazine(self.ammoAmount,magType, ammoType.getName()))

    def getMags(self):
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
#get the type of magazine and how many there are. This is a real mess, there must be better ways.

#********************************
#CHANGE HELD MAGAZINE OBJECTS
#********************************

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



    def changeMag(self,mag):
        #returnedMag=self.holdingMags[0]
        if mag.getAmmo()>0:
            self.holdingMags.append(mag)

        #return returnedMag

#********************************
#RETURN CLASS VARIABLES
#********************************
    def getMagNumber(self):
        return self.holdingMags

    def getMagName(self):
        return self.name
