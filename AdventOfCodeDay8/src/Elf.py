import re

class GridStorage:
    def __init__(self,x,y):
        CellsY = [None] * x
        CellsY = [[None] * y



class Forest:
    def __init__(self):
        self.Forest = []
        pass

    def GetTreeHeight(self,x,y):
        TreeHeight = self.Forest[y][x]

        print("At",x, ", " ,y,"  ",  TreeHeight)
        return 5
        pass
    def GetTreeHeightTouple(self,TreePosition):

        x = TreePosition[0]
        y = TreePosition[1]

        TreeHeight = self.Forest[TreePosition[1]][TreePosition[0]]

        print("At",x, ", " ,y,"  ",  TreeHeight)
        return int(TreeHeight)
        pass



    def AddRow(self,Row):
        self.Forest += [Row]

    def GetInnerGridXY(self):
        y = len(self.Forest)
        x = len ( self.Forest[0])
        self.ForestXY = (x,y)
        self.InnerXY = (x-2,y-2)

    def GetTotalForestHeight(self):
        return self.ForestXY[1]

    def GetTotalForestLength(self):

        return self.ForestXY[0]

    def IsTreeVisible(self,TreePosition):
        '''
        A tree is visible if all of the other trees between it and an edge of the grid are shorter than it. 
        Only consider trees in the same row or column; that is, only look up, down, left, or right from any given tree.
        '''

        print ("Tree to Generate Mask from is at position ", TreePosition)
        #LookUp
        EndOfGridY = self.GetTotalForestHeight()
        EndOfGridX = self.GetTotalForestLength()
        CurrentPositionY = TreePosition[1]
        CurrentPositionX = TreePosition[0]

        CurrentTreeHeight = self.GetTreeHeightTouple(TreePosition)
        HiddenCount = 0

        for Y in range(CurrentPositionY+1,EndOfGridY):

            InspectedTreeHeight = self.GetTreeHeight(TreePosition[0],Y)
            print("Looking at X", TreePosition[0], "Y", Y,"Tree was at ",InspectedTreeHeight)
            if InspectedTreeHeight>CurrentTreeHeight:
                print("Covered Looking Up !")
                HiddenCount+=1
                break;

        for Y in range(CurrentPositionY-1,-1,-1):
            print("Looking at X",TreePosition[0], "Y",Y)
            InspectedTreeHeight = self.GetTreeHeight(TreePosition[0],Y)
            if InspectedTreeHeight>CurrentTreeHeight:
                print("Covered Looking Down !")
                HiddenCount+=1
                break;

        for X in range(CurrentPositionX+1,EndOfGridX+1):
            print("Looking at X",X, "Y",TreePosition[1])
            InspectedTreeHeight = self.GetTreeHeight(X,TreePosition[1])
            if InspectedTreeHeight>CurrentTreeHeight:
                print("Covered Looking Right !")
                HiddenCount+=1
                break;

        for X in range(CurrentPositionX-1,-1,-1):
            print("Looking at X",X, "Y",TreePosition[1])
            InspectedTreeHeight = self.GetTreeHeight(X,TreePosition[1])
            if InspectedTreeHeight>CurrentTreeHeight:
                print("Covered Looking Left !")
                HiddenCount+=1
                break;
        if HiddenCount == 4:
            return False
        else:
            return True

    def GenerateVisibleGraph(self):

        VisibleForest = Forest()

        for x in range(1,self.InnerXY[0]+1):
            for y in range(1, self.InnerXY[1]+1):
                print ( x,y )
                self.VisibleGraph[y][x] = self.IsTreeVisible((x,y))


