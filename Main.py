import pdb

import os
#pdb.set_trace()
from pprint import pprint
import sys

sys.path.append('Classes/MissionGameplay')
sys.path.append('Classes/Equipment')
sys.path.append('Classes/Actors')

from worldMap import worldMap
from Combat import Combat
from pickLoadout import pickLoadout
from Items import ammoBelt
from Items import Magazine

import pygame

#pprint(sys.path)

"""This will be the main file where worldMap,inv,combat,and other such gamestates go on."""


missionMap=worldMap()
fightItOut=Combat()
loadoutGenerator=pickLoadout()

def gatherMapData():
    holdPlayerMissions=[]
    holdPlayerMissions=missionMap.importMissions()
    return holdPlayerMissions

def gatherMapBriefing(missionList):
    holdIntro=missionMap.worldMapIntro(missionList)-1
    return holdIntro

def setupLoadout(missionSelection,actorMapData):
    holdSecondaryAmmo=[]
    holdWeapons=[]
    ammoBelts=[]
    holdWeapons=loadoutGenerator.createWeaponList()
    selectedWeapons=loadoutGenerator.selectWeapons(holdWeapons)

    primaryWeaponMagazine=selectedWeapons[0].getMagazine()
    secondaryWeaponMagazine=selectedWeapons[1].getMagazine()
    
    firstAmmoPack=ammoBelt(6,primaryWeaponMagazine.getAmmoType(),primaryWeaponMagazine,primaryWeaponMagazine.getAmmoAmount(),"Primary Ammo Belt")

    secondAmmoPack=ammoBelt(6,secondaryWeaponMagazine.getAmmoType(),secondaryWeaponMagazine,secondaryWeaponMagazine.getAmmoAmount(),"Secondary Ammo Belt")

    ammoBelts.append(firstAmmoPack), ammoBelts.append(secondAmmoPack)
    actorMapData[missionSelection][2].playerWeapons(selectedWeapons)
    actorMapData[missionSelection][2].equipAmmoBelt(ammoBelts)
    return selectedWeapons

def combatMode(actorMapData,missionSelect,selectedWeapons):
    pod=actorMapData[missionSelect][1]
    user=actorMapData[missionSelect][2]
    alienBattleMap=actorMapData[missionSelect][3]
    playerBattleMap=actorMapData[missionSelect][4]
    done=0
    fightItOut.combat(pod,user,playerBattleMap,alienBattleMap,selectedWeapons)
    
    
def main():
    actorMapData=gatherMapData()
    for each in range(len(actorMapData)):
        missionSelection=gatherMapBriefing(actorMapData)
        os.system('cls' if os.name=='nt' else 'clear')
        selectedWeapons=setupLoadout(missionSelection,actorMapData)
        os.system('cls' if os.name=='nt' else 'clear')
        pygame.mixer.music.stop()
        combatMode(actorMapData,missionSelection,selectedWeapons)
        actorMapData.pop(missionSelection)
    
main()
    