from Pods import Pods
from collections import Counter
from Player import Player
from Cover import Cover
from missionGenerator import missionGenerator
from Sound import Sound
import random
import pygame
import os
class worldMap(object):
    """Map where player picks what missions they go on using generated info."""




    def __init__(self):
        self.pickedMission=None
#********************************
#CREATE MUSIC
#********************************
    pygame.init()
    def createMusic():
        music=Sound().worldMapMusic(1)
        pygame.mixer.music.load(music)
        pygame.mixer_music.play()

#********************************
#MISSION SELECTION
#********************************

    def importMissions(self):
        missions=[]
        missionGen=missionGenerator()
        mission1=missionGen.createMission()
#0 is opName,1 is pod, 2 is user, 3 is alienBattleMap, 4 is playerBattleMap, 5 is briefing
        mission2=missionGen.createMission()
        mission3=missionGen.createMission()

        missions.append(mission1)
        missions.append(mission2)
        missions.append(mission3)
        return missions

    def worldMapIntro(self,missionList):

        worldMap.createMusic()
        x=0
        y=0
        print ("\n\nAlien incursions have been reported at these locations. Our troops are awaiting your go-ahead Commander.\n")
        for each in range(len(missionList)):
            x+=1
            
            print (x," ",missionList[each][5])
        while y==0:
            try:
                selection=(int(input("Select the mission you wish to go on")))
                if selection in range(len(missionList)+1):
                    break
                
            except:
                x=0
                print ("That's not an avalible location.")
                os.system('cls' if os.name=='nt' else 'clear')
                print ("\n\nAlien incursions have been reported at these locations. Our troops are awaiting your go-ahead Commander.\n")
                for each in range(len(missionList)):
                    x+=1
            
                    print (x," ",missionList[each][5])                
                    continue
                    

        if selection in range(len(missionList)+1):
            self.pickedMission=selection
            return selection
        else:
            print ("Try again")


    def getSelectedMission(self):
        return self.pickedMission