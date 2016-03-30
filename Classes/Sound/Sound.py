import sys
sys.path.append('C:/Users/Leth/Documents/Visual Studio 2015/Projects/CLI_TBCoverCombat_3-29-16-RC_1/GettingPodsToWork3-3-16/SoundFiles/SoundEffects')
import pygame
import os

weaponSoundEffectPath="SoundFiles/SoundEffects/WeaponSounds"
playerSoundEffectPath="SoundFiles/SoundEffects/PlayerSounds"
combatSoundEffectPath="SoundFiles/SoundEffects/CombatSounds"
enemySoundEffectPath="SoundFiles/SoundEffects/EnemySounds"
musicPath="SoundFiles/Music"

setupFilePath=os.path.join


class Sound(object):
    """Holds and plays all the various sounds"""

    pygame.init()


    def weaponSounds(self,weapon):
        pygame.mixer.init()
#giving two arguemtns allows it to search for the specigfic foldser in the project then the sound file.


        setupFilePath=os.path.join
        holdWeaponSounds={"Rifle":pygame.mixer.Sound(setupFilePath(weaponSoundEffectPath,"rifleShoot.wav")),
        "SMG":pygame.mixer.Sound(setupFilePath(weaponSoundEffectPath,"smgShootWav.wav")),
        "Shotgun":pygame.mixer.Sound(setupFilePath(weaponSoundEffectPath,"shotgunShoot.wav")),
        "Handgun":pygame.mixer.Sound(setupFilePath(weaponSoundEffectPath,"handgunShoot.wav")),
        "Knife":pygame.mixer.Sound(setupFilePath(weaponSoundEffectPath,"knifeSwing.wav")),
        "Laser":pygame.mixer.Sound(setupFilePath(weaponSoundEffectPath,"alienLaserShoot.wav")),
        "Grenade":pygame.mixer.Sound(setupFilePath(weaponSoundEffectPath,"grenadeBoom.wav")),
        "Shot Miss":pygame.mixer.Sound(setupFilePath(combatSoundEffectPath,"bulletWhizz.wav"))}
        
        returnedSound=holdWeaponSounds.get(weapon) 
        return returnedSound

    def userPainSounds(self,pain):

        holdPainSounds={1:pygame.mixer.Sound(setupFilePath(playerSoundEffectPath,"painSounds1.wav")),
        2:pygame.mixer.Sound(setupFilePath(playerSoundEffectPath,"painSounds2.wav")),
        3:pygame.mixer.Sound(setupFilePath(playerSoundEffectPath,"painSounds3.wav")),
        4:pygame.mixer.Sound(setupFilePath(playerSoundEffectPath,"painSounds4.wav")),
        5:pygame.mixer.Sound(setupFilePath(playerSoundEffectPath,"painSounds5.wav")),
        6:pygame.mixer.Sound(setupFilePath(playerSoundEffectPath,"painSounds6.wav")),
        7:pygame.mixer.Sound(setupFilePath(playerSoundEffectPath,"painSounds7.wav")),
        8:pygame.mixer.Sound(setupFilePath(playerSoundEffectPath,"painSounds8.wav")),
        9:pygame.mixer.Sound(setupFilePath(playerSoundEffectPath,"painSounds9.wav"))}
        
        returnedSound=holdPainSounds.get(pain)
        return returnedSound

    def enemyPainSounds(self,enemy):
        holdPainSounds={"Sectoid":pygame.mixer.Sound(setupFilePath(enemySoundEffectPath,"sectoidHitNoise.wav"))}
        
        returnedNoise=holdPainSounds.get(enemy)
        return returnedNoise

    def abilitySounds(self,move):
        holdAbilitySounds={"Taunt":pygame.mixer.Sound(setupFilePath(enemySoundEffectPath,"taunt.wav"))}

        returnedSound=holdAbilitySounds.get(move)
        return returnedSound

    def deathSounds(self,body):
        
        holdDeathSounds={"Sectoid":pygame.mixer.Sound(setupFilePath(enemySoundEffectPath,"sectoidDeath.wav")),
        "Player":pygame.mixer.Sound(setupFilePath(playerSoundEffectPath,"playerDeadPlaceholder.wav"))}

        returnedSound=holdDeathSounds.get(body)
        return returnedSound

    def coverHitSounds(self,cover):
        
        holdCoverHitSounds={"High Cover":pygame.mixer.Sound(setupFilePath(combatSoundEffectPath,"highCoverHit.wav")),
        "Low Cover":pygame.mixer.Sound(setupFilePath(combatSoundEffectPath,"lowCoverHit.wav")),
        "No Cover":pygame.mixer.Sound(setupFilePath(combatSoundEffectPath,"noCoverHit.wav")),
        "Cover Break":pygame.mixer.Sound(setupFilePath(combatSoundEffectPath,"coverBreak.wav"))}

        returnedSound=holdCoverHitSounds.get(cover)
        return returnedSound


    def reloadSounds(self,gun):
        holdReloadSounds={"Rifle":pygame.mixer.Sound(setupFilePath(weaponSoundEffectPath,"rifleReload.wav")),
        "SMG":pygame.mixer.Sound(setupFilePath(weaponSoundEffectPath,"smgReload.wav")),
        "Shotgun":pygame.mixer.Sound(setupFilePath(weaponSoundEffectPath,"shotgunCocking.wav")),
        "Handgun":pygame.mixer.Sound(setupFilePath(weaponSoundEffectPath,"handgunReload.wav"))}
        #"Knife":pygame.mixer.Sound(setupFilePath(weaponSoundEffectPath,"knifeSwing.wav")),
        #"Laser":pygame.mixer.Sound(setupFilePath(weaponSoundEffectPath,"alienLaserShoot.wav"))}

        returnedSound=holdReloadSounds.get(gun)
        return returnedSound

    def gameMusic(self,selection):
        holdGameMusic={1:setupFilePath(musicPath,"Mayham.mp3"),
        #2:setupFilePath(musicPath,"fortress.mp3"),
        2:setupFilePath(musicPath,"massDest.mp3"),
        3:setupFilePath(musicPath,"8492.mp3"),
        4:setupFilePath(musicPath,"grinder.mp3")}

        returnedMusic=holdGameMusic.get(selection)
        print (returnedMusic)
        return returnedMusic


    def worldMapMusic(self,tune):
        holdMapMusic={1:setupFilePath(musicPath,"briefing1.mp3")}
        
        returnedMusic=holdMapMusic.get(tune)
        return returnedMusic
