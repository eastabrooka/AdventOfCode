
class Backpack:
    def __init__(self,Pack1,Pack2,Pack3):
        self.Compartment1 = Pack1
        self.Compartment2 = Pack2
        self.Compartment3 = Pack3


    def FindMatch(self):
        AppearsThrice = ""
        for x in self.Compartment1:
            for y in self.Compartment2:
                for z in self.Compartment3:
                    if x == y and y == z :
                        AppearsThrice = x
                        return AppearsThrice

    def GetScore(self):
        AppearsThrice = self.FindMatch()

        if ord ( AppearsThrice[0]) >=97 and  ord ( AppearsThrice[0]) <= 122 :
            # Is between 97 and 122
            return(ord(AppearsThrice[0]) - 96)
        elif ord(AppearsThrice[0]) >= 65 and ord(AppearsThrice[0]) <= 90:
            return((ord(AppearsThrice[0]) - 64) + 26)



