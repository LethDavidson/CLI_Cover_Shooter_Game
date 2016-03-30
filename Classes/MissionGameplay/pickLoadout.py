from Weapons import Weapons
from Grenade import Grenade
from Items import Magazine
from Sound import Sound
import os

class pickLoadout(object):
    """Selects weapons, items, and any additional tools for the upcoming mission"""
    def __init__(self):
        self.openSlots=5
 #i don't know what this variable is for??   

    def createWeaponList(self):
        weaponList=[]
        rifleMag=Magazine(4,"normal","Standard Rifle Magazine")
        smgMag=Magazine(6,"normal","Standard SMG Magazine")
        shotgunMag=Magazine(2,"normal","Standard Shotgun Magazine")
        handgunMag=Magazine(8,"normal","Standard Handgun Magazine")
        knifeMag=Magazine(1000,"normal","fake Knife Mag")
        
        rifleSound=Sound().weaponSounds("Rifle")
        rifleSound.set_volume(.75)
        smgSound=Sound().weaponSounds("SMG")
        smgSound.set_volume(.5)
        shotgunSound=Sound().weaponSounds("Shotgun")
        handgunSound=Sound().weaponSounds("Handgun")
        knifeSound=Sound().weaponSounds("Knife")
        
        rifleReloadSound=Sound().reloadSounds("Rifle")
        smgReloadSound=Sound().reloadSounds("SMG")
        shotgunReloadSound=Sound().reloadSounds("Shotgun")
        handgunReloadSound=Sound().reloadSounds("Handgun")


        Rifle=Weapons(80,3,4,10,rifleMag,rifleSound,rifleReloadSound,"Rifle")
        SMG=Weapons(70,3,6,15,smgMag,smgSound,smgReloadSound,"SMG")
        Shotgun=Weapons(70,6,2,10,shotgunMag,shotgunSound,shotgunReloadSound,"Shotgun")
        Handgun=Weapons(80,2,8,15,handgunMag,handgunSound,handgunReloadSound,"Handgun")
        Knife=Weapons(100,20,1000,40,knifeMag,knifeSound,None,"Knife")
        weaponList.append(Rifle),weaponList.append(SMG),weaponList.append(Shotgun),weaponList.append(Handgun),weaponList.append(Knife)
        return weaponList
#creates all of the weapons to be used in pick Loadout and for all actors




    def selectWeapons(self,weaponList):
        pickedWeapons=[]
        y=0
        b=0
        for each in range(len(weaponList)):
            b+=1
            print(b,": ",weaponList[each].getName(),": Accuracy: {ACC} Damage: {DAM} Ammo: {AMMO}, Critical Chance: {CRIT}".format(ACC=weaponList[each].getAcc(),DAM=weaponList[each].getDamage(),AMMO=weaponList[each].getMaxAmmo(),CRIT=weaponList[each].getCritChance()))
        while y==0:
            try:
                selection=(int(input("Pick your primary weapon")))
                selection-=1
                if selection in range(len(weaponList)):
                    break

            except:
                print ("That's not a valid weapon choice.\n")
                continue
        if selection in range(len(weaponList)):
            print ("You grabbed ",weaponList[selection])
            pickedWeapons.append(weaponList[selection])
            weaponList.pop(selection)
#this will clear the screen


            os.system('cls' if os.name=='nt' else 'clear')
            d=0
            for each in range(len(weaponList)):
                d+=1
                print(d,": ",weaponList[each].getName(),": Accuracy: {ACC} Damage: {DAM} Ammo: {AMMO}, Critical Chance: {CRIT}".format(ACC=weaponList[each].getAcc(),DAM=weaponList[each].getDamage(),AMMO=weaponList[each].getMaxAmmo(),CRIT=weaponList[each].getCritChance()))
        while y==0:
            try:
                secondary=(int(input("Pick your secondary weapon")))
                secondary-=1
                if secondary in range(len(weaponList)):
                    print ("You grabbed ",weaponList[secondary])
                    pickedWeapons.append(weaponList[secondary])
                    weaponList.pop(secondary)
                    break

            except:
                print ("That's not a valid weapon choice.\n")
                continue

            else:
                print ("Not a valid choice")
        else:
            print ("Not a valid choice")
        os.system('cls' if os.name=='nt' else 'clear')
        return pickedWeapons
#select prim and secondary. There's a way to consolidate picking both to less text, look into it later