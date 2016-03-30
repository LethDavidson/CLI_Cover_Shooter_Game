from Sound import Sound

import pygame

class Weapons(object):
    """description of class"""
    
    #magazine=Magazine(False,False,True,"Magazine")

    def __init__(self,acc,dam,ammo,crit,magazine,sound,reloadSound,name):
        self.magSize=[]
        self.accuracy=acc
        self.damage=dam
        self.ammo=ammo
        self.critChance=crit
        self.name=name
        self.maxAmmo=ammo
        self.magSize=magazine
        self.sound=sound
        self.reloadSound=reloadSound

#********************************
#RETURN WEAPON VARIABLES
#********************************
    def getName(self):
        return self.name 

    def getAcc(self):
        return self.accuracy

    def getCritChance(self):
        return self.critChance


    def getDamage(self):
        return self.damage
    
    def getMagazine(self):
        return self.magSize
    
    def getMaxAmmo(self):
        return self.maxAmmo
#********************************
# CURENT MAGAZINE INSIDE OF WEAPON VARIABLES
#********************************
    def getMagName(self):
        return self.magSize.getName()

    def __str__(self):
        return ("{NAME}".format(NAME=self.name))

    def getMagAmmo(self):
        return self.magSize.getAmmo()

    def getMagAmmoType(self):
        return self.magSize.getAmmoType()

#********************************
#MODIFIY MAGAZINE
#********************************
    def spendAmmo(self,amount):
        self.sound.play()
        self.magSize.spendBullets(amount)

    def reload(self,newMag):
        oldMag=self.magSize
        self.magSize=newMag
        self.reloadSound.play()
        print ("Reloaded!")
        return oldMag

class Bullet(Weapons):
    #by default the bullet class gives no benefits, but different bullet types can give stat bonuses. Modify those bonuses based on what type of bullet is called.
    def __init__(self,AP,tracer,normal,name):
        Weapons.__init__(self,0,0,0,0,0,None,None,"Bullet")
        self.AP=AP
        self.tracer=tracer
        self.normal=normal

    def getType():
        ammoType=""
        if self.AP==True:
            ammoType="AP"
        if self.tracer==True:
            ammoType="tracer"
        if self.normal==True:
            ammoType="normal"
        return ammoType

#********************************
#CREATE DIFFERENT BULLET TYPES
#********************************
    def tracerBullets(self):
        if self.tracer==True:
            self.accuracy+=10
            self.critChance-=10

    def APBullets(self):
        if self.AP==True:
            #code it doing reduced damage to enemies behind cover if cover is hit
            self.accuracy-=5

    