from Sound import Sound
class Grenade(object):
    def __init__(self,damage=4):
        self.name="Grenade"
        self.damage=damage
        self.boomSound=Sound().weaponSounds("Grenade")

#*************************************
#RETURN CLASS VARIABLES
#*************************************

    def playSound(self):
        return self.boomSound.play()

    def explode(self):
        return self.damage

    def getName(self):
        return self.name