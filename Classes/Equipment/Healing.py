class Healing(object):
    def __init__(self,name,amount=0):
        self.name=name
        self.healing=amount
        
#*****************************
#MEDKIT HEALING 
#*****************************
    def heal(self,healing):
        self.healing+=healing
        return self.healing

    def getName(self):
        return self.name

    def getHealAmount(self):
        return self.healing