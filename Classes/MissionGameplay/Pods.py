

from Sectoid import Sectoid
import random
class Pods(object):
    """ the various possible enemy encounters that can show up.
use this to hardcode who goes when in a turn in regards to a group. Allows for direct control.
Not a dynamic solution, but good for now. Integrate multiple mods in a turn later."""
#************************************
#CREATING ENEMY GROUPS (PODS)
#***********************************

    def makeup(self):
        p1S1,p1S2,p1S3=Sectoid("Sectoid1"),Sectoid("Sectoid2"),Sectoid("Sectoid3")
        p2S1,P2S2=Sectoid("Sectoid1"),Sectoid("Sectoid2")
        pod1ThreeMan=[p1S1,p1S2,p1S3]
        pod2TwoMan=[p2S1,P2S2]
        storage={1:pod1ThreeMan,2:pod2TwoMan}
        podRNG=random.randint(1,len(storage))
        selectPod=podRNG
        try:
            returnedPod=storage[selectPod]
        except:
            print("There's no pod stored to that index number")
        return returnedPod

    
#***********************************
#RETURN CLASS VARIABLES
#***********************************
    def name(self):
        return self.name