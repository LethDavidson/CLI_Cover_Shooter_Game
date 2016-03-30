import sys
sys.path.append('C:/Users/Leth/Documents/Visual Studio 2015/Projects/CLI_TBCoverCombat_3-29-16-RC_1/GettingPodsToWork3-3-16/TextInput/MissionGeneration')
from Pods import Pods
from collections import Counter
from Player import Player
from Cover import Cover
from pickLoadout import pickLoadout
import random
import os

genTextFolder="TextInput/MissionGeneration"

class missionGenerator(object):
    """description of class"""

    #def __init__(self,selectedWeapons):
     #   self.selectedWeapons=selectedWeapons

#********************************
#MISSION GENERATION
#********************************

    def createPods():
        podSpawner=Pods()
        pod1=podSpawner.makeup()
        return pod1

    def createPlayer():
        user=Player()
        return user

    def importBriefingTexts(pod,alienCoverMap,playerCoverMap):
        coverDen=""
        enemyDen=""

        greetings=missionGenerator.briefingRNGAssignments("intro_before_destination.txt")
        destination=missionGenerator.briefingRNGAssignments("destination_list.txt")
        fewEnemies=missionGenerator.briefingRNGAssignments("few_enemies.txt")
        manyEnemies=missionGenerator.briefingRNGAssignments("many_enemies.txt")
        lowCoverDensity=missionGenerator.briefingRNGAssignments("low_cover_density.txt")
        highCoverDensity=missionGenerator.briefingRNGAssignments("high_cover_density.txt")
        firstPartOpName=missionGenerator.briefingRNGAssignments("opNameAdj.txt")
        secondPartOpName=missionGenerator.briefingRNGAssignments("opNameNoun.txt")
        opName="Operation "+firstPartOpName+" "+secondPartOpName
   

        if len(alienCoverMap)+len(playerCoverMap) <= 10:
            coverDen=lowCoverDensity
        else:
            coverDen=highCoverDensity

        if len(pod) <= 2:
            enemyDen=fewEnemies
        else:
            enemyDen=manyEnemies

        briefing= ("{opNAME}\n\n{INTRO} {DESTINATION}\n{ENEMY_COUNT}\n{COVER_DENSITY}\n".format(opNAME=opName,INTRO=greetings,DESTINATION=destination,ENEMY_COUNT=enemyDen,COVER_DENSITY=coverDen))
        return opName,briefing

    def giveBriefing(briefing):
        print (briefing)


    def briefingRNGAssignments(txtFileName):
        brief=""    
        with open(os.path.join("TextInput\MissionGeneration",txtFileName),"r") as textFile:
    
            holdTextLines=textFile.read().splitlines()
            chooseLineRNG=random.randrange(len(holdTextLines))
            brief=holdTextLines[chooseLineRNG]
            textFile.close()
            return brief
#creates Textfile by fusing file location with file sent by mission gen, then chooses a line at random to return


    def createBattleMaps(coverManager):
        alienBattleMap=missionGenerator.createAlienBattleMap(coverManager)
        playerBattleMap=missionGenerator.createPlayerBattleMap(coverManager)
        return alienBattleMap,playerBattleMap

    def createPlayerBattleMap(coverManager):
        playerBattleMap=coverManager.coverLayout()
        return playerBattleMap

    def createAlienBattleMap(coverManager):
        alienBattleMap=coverManager.coverLayout()
        return alienBattleMap



    def generateMissionVariables():
        pod=missionGenerator.createPods()
        user=missionGenerator.createPlayer()
        coverManager=Cover(None)
        battleMaps=missionGenerator.createBattleMaps(coverManager)

        alienBattleMap=battleMaps[0]
        playerBattleMap=battleMaps[1]

        briefing=missionGenerator.importBriefingTexts(pod,alienBattleMap,playerBattleMap)
        return briefing[0],pod,user,alienBattleMap,playerBattleMap,briefing[1]
        
            
    def createMission(self):
        missionStorage=[]
        missionStorage=missionGenerator.generateMissionVariables()
        missionDetails=[]
        for i in range(1):
#0=missionName,1=pod,2=user,3=alienbatmap,4=playbatmap,5=briefingtext
            missionDetails.append(missionStorage[0])
            missionDetails.append(missionStorage[1])
            missionDetails.append(missionStorage[2])
            missionDetails.append(missionStorage[3])
            missionDetails.append(missionStorage[4])
            missionDetails.append(missionStorage[5])

        return missionDetails