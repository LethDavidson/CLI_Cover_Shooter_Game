import sys
sys.path.append('C:/Users/Leth/Documents/Visual Studio 2015/Projects/CLI_TBCoverCombat_3-29-16-RC_1/GettingPodsToWork3-3-16/Classes/Actors')
sys.path.append('C:/Users/Leth/Documents/Visual Studio 2015/Projects/CLI_TBCoverCombat_3-29-16-RC_1/GettingPodsToWork3-3-16/Classes/MissionGameplay')
from collections import Counter
from collections import deque
from Sectoid import Sectoid

from Player import Player
from pickLoadout import pickLoadout
from Cover import Cover
import Items
import Weapons
import random

"""This is where I test shit out before slotting it into the rest of the program. """
class test(object):
   #At start of turn, remaining aliens decide what actions to take.
    def main():
        user=Player()
        enemies=[]
        johnny=Sectoid("Johnny")
        jimmy=Sectoid("Jimmy")
        jannus=Sectoid("Jannus")
        enemies.append(johnny)
        enemies.append(jimmy)
        enemies.append(jannus)
        turn=0
        what=deque(["I'M","TYRANOSAURUS","ALAN"])
        """iter(test)
        print (test)
        a=(int(input()))
        for i in test:
            print (i)
        lost=["butt","butt","dong"]
        count=Counter(lost)
        print (count)
        print (count["butt"])
        for each in range (count["butt"]):
            turn+=1
            print ("bang")
        for each in range (count["dong"]):
            turn+=1
            print ("GRR!")
        for x in range (turn):
            print (x)
            print (enemies[x].health())

    
        actions=[]
        for each in range(0,len(enemies)):
            actions.append(enemies[each].action())
            if actions[each]=="shoot":
            
                gunshot=enemies[each].shoot(20)
                if gunshot==1:
                    print ("player takes 2 damage!\n")
                    user.damage(2)
            if actions[each]=="taunt":
                ailment=enemies[each].taunt()
                playerResist=user.status(ailment)
                if playerResist==1:
                    print ("you get PO'D")
                else:
                    print ("No shits given")
            
    
#this will let the pod number choose a cover number that's inique to them, so no two choose the same one.
#or at least the requation works foor that. I gotta slot this into existing code somehow.

   def randomSample():
        ecx={0:[40,20,10],1:[40,20,10],2:[20,0,6],3:[0,-20,0]}
        enemies=["mon1","mon2"]
        alf=random.sample(range(0,len(list(ecx))),1)
        return alf

for i in range(2000):
    alf=test.randomSample()
    print (alf)"""
"""
cover=Cover()
covLay=cover.coverLayout()
covLay[0].takeDamage(4)
print (covLay[0].hp)

coverDict={}
RNG=random.randint(1,10)
typeRNG=random.randint(1,3)
for i in range (RNG):
    if typeRNG==1:
        coverDict[i]=Cover(40,20,12)
    elif typeRNG==2:
        coverDict[i]=Cover(20,0,6)
    elif typeRNG==3:
        coverDict[i]=Cover(0,-20,0)
"""
"""
class pet(object):
    

    def __init__(self,name,species):
        self.name=name
        self.species=species

    def getName(self):
        return self.name

    def getSpecies(self):
        return self.species
#overriders default PRINT return. define what happens when print (instance) happens.
    def __str__(self):
        return ("{NAME} is a {SPECIES}.".format(NAME=self.name,SPECIES=self.species))


class Dog(pet):
    def __init__(self,name,chases_cats):
        pet.__init__(self,name,"Dog")
        self.chases_cats=chases_cats

    def chasesCats(self):
        return self.chases_cats

class Cat(pet):
    def __init__(self,name,hates_dogs):
        pet.__init__(self,name,"Cat")
        self.hates_dogs=hates_dogs

    def hatesDogs(self):
        return self.hates_dogs

mister_pet=pet("Mister","Dog")
mister_dog=Dog("Mister",True)

#Dog is a pet, but pet is not a Dog.
print(isinstance(mister_pet,pet))
print(isinstance(mister_pet,Dog))
print(isinstance(mister_dog,pet))
print(isinstance(mister_dog,Dog))
#can't call chase_cats from Pet, but can from Dog as Dog is it's own thing with Pet structure

print( mister_pet.getName())
print (mister_dog.getName())

fido=Dog("Fido",False)
Ralph=Dog("Ralph",True)
Minx=Cat("Minx",True)
Ehx=Cat("Ehx",False)

print (fido)
print (Ralph)
print (Minx)
print (Ehx)

print ("{NAME} chases cats: {ANSWER}".format(NAME=fido.getName(),ANSWER=fido.chasesCats()))
#a class with two sub classes, and variabvles specific to those classes. Sub classes can use class methods that are not defined
#as being exclusivly for the class. But Classes cannot just calll subclass variables.


"""

"""
pickWeps=[]
user=Player()
wepGen=pickLoadout()
wepList=wepGen.createWeaponList()
pickWeps=wepGen.selectWeapons(wepList)
user.playerWeapons(pickWeps)
playerWeapons=user.returnPlayerWeapons()
print (playerWeapons[0].getName())
print (playerWeapons[0].getAmmo())
print (playerWeapons[0].getMaxAmmo())
for each in range(12):
    print ("BANG ")
    playerWeapons[0].spendAmmo()
    print (playerWeapons[0].getAmmo())
    if playerWeapons[0].getAmmo()==0:
        print ("RELOADING!")
        playerWeapons[0].reload()
"""

"""
test1=["pigs","pugs"]

test2=test1[1]
print (test2)
test2=test1[0]
print (test2)

if test2==test1[0]:
    test2=test1[1]

elif test2==test1[1]:
    test2=test1[0]

print (test2)
"""

"""
Rifle=Weapons.Weapons(80,5,4,10,rifleMag,"Rifle")

print(rifleMag.getAmmo())
print (Rifle.getMagAmmo())

for each in range(12):
    ammo=Rifle.getMagAmmo()
    if ammo > 0:
        print ("BANG")
        Rifle.spendAmmo(1)
        print (Rifle.getMagAmmo())
    else:
        print ("Empty!")"""
"""
rifleMag=Items.Magazine(4,"normal","Standard Rifle Magazine")
print (rifleMag.getName())
ammoBelt=Items.ammoBelt(rifleMag.getAmmo(),rifleMag.getAmmoType(),"Ammo Belt")

print (ammoBelt.getName)
print (ammoBelt.getMags())
print ("\n\n\n")
#THIS IS WHAT I WAS DOING. GET ROWDY IN TEST 2 AND GET JOEY AT TAIL END OF TEST1. THIS IS THE TEST FOR MOVING GUN MAG(test2) TO AMMO BELT (test1) AND MAG[0] FROM BELT TO GUN.
test1=["Rowdy","Rodey","Piper"]
test2=[test1.pop(0)]
#this moves the first to the back
#test1+=[test1.pop(0)]
#this removes the first, leaving only the back
#test1.pop(0)

test1.append(test2[0])
test2.pop(0)
test2=[test1.pop(0)]

print (test1)
print (test2)
"""

user=Player()
print (user.getName())

"""This will be the main file where worldMap,inv,combat,and other such gamestates go on."""
x=input("enter a num")
try:
    x=(int(x))
except:
    print ("That was  aletter, exception workign")
