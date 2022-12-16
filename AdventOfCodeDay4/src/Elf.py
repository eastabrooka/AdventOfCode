def Iterate( Range1, Range2):
    Count = 0
    for x in Range1:
        if x in Range2:
            Count += 1

    if Count >= len(Range2):
        return True

class SpaceCleaner:
    def __init__(self,Pairs):

        self.Range1 = Pairs[0]
        self.Range2 = Pairs[1]

        self.Pairs = Pairs



    def CheckForOverlap(self):

        LowerPair = []
        UpperPair = []

        A = self.Range1.split("-")
        B = self.Range2.split("-")

        for x in range(int(A[0]),int(A[1])+1):
            LowerPair += [x]
        for x in range(int(B[0]),int(B[1])+1):
            UpperPair += [x]


        if (Iterate(LowerPair,UpperPair) or Iterate(UpperPair,LowerPair) ):
            return True


        pass


