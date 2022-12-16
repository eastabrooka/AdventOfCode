
class Backpack:
    def __init__(self,Contents):

        SplitPoint = len(Contents)
        if SplitPoint %2 > 0 :
            print (" Not Even ")
        SplitPoint = SplitPoint /2

        self.Compartment1 = Contents[0:int(SplitPoint)]
        self.Compartment2 = Contents[int(SplitPoint):]


    def GetScore(self):

        len1 =  len ( self.Compartment1)
        len2 = len ( self.Compartment2)
        if (len1 != len2):
            print("error ")

        AppearsTwice = []
        for x in self.Compartment1:
            if x in self.Compartment2:
                AppearsTwice = [x]
        print("Appears Twice",AppearsTwice)

        if ord ( AppearsTwice[0]) >=97 and  ord ( AppearsTwice[0]) <= 122 :
            # Is between 97 and 122
            return(ord(AppearsTwice[0]) - 96)
        elif ord(AppearsTwice[0]) >= 65 and ord(AppearsTwice[0]) <= 90:
            return((ord(AppearsTwice[0]) - 64) + 26)



