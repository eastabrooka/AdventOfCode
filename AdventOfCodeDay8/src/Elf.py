import re

import src


def IsTreeVisible(Grid, TreePosition):
    '''
    A tree is visible if all of the other trees between it and an edge of the grid are shorter than it.
    Only consider trees in the same row or column; that is, only look up, down, left, or right from any given tree.
    '''

    EndOfGridY = Grid.GetX()
    EndOfGridX = Grid.GetY()
    CurrentPositionY = TreePosition[1]
    CurrentPositionX = TreePosition[0]

    CurrentTreeHeight = Grid.GetValue(CurrentPositionX,CurrentPositionY)
    HiddenCount = 0


    for Y in range(CurrentPositionY + 1, EndOfGridY+1):

        InspectedTreeHeight = Grid.GetValue(CurrentPositionX, Y)
        if InspectedTreeHeight >= CurrentTreeHeight:
            HiddenCount += 1
            break;

    for Y in range(CurrentPositionY - 1, -1, -1):
        InspectedTreeHeight = Grid.GetValue(CurrentPositionX, Y)
        if InspectedTreeHeight >= CurrentTreeHeight:
            #print("Covered Looking Down !")
            HiddenCount += 1
            break;

    for X in range(CurrentPositionX + 1, EndOfGridX + 1):
        InspectedTreeHeight = Grid.GetValue(X, CurrentPositionY)
        if InspectedTreeHeight >= CurrentTreeHeight:
            #print("Covered Looking Right !")
            HiddenCount += 1
            break;

    for X in range(CurrentPositionX - 1, -1, -1):
        InspectedTreeHeight = Grid.GetValue(X, CurrentPositionY)
        if InspectedTreeHeight >= CurrentTreeHeight:
            #print("Covered Looking Left !")
            HiddenCount += 1
            break;

    if HiddenCount == 4:
        print("Hidden", CurrentPositionX, CurrentPositionY)
        return False

    else:
        print("Visible", CurrentPositionX, CurrentPositionY)

        return True




class GridStorage:
    def __init__(self,x,y):
        self.LenX = x
        self.LenY = y
        self.Grid =  [[None for i in range(y)] for j in range(x)]

    def SetValue(self,x,y,Value):
        if y > self.LenY:
            print("Someones doing something dumb.")
        if x > self.LenX:
            print("Someones doing something dumb.")
        self.Grid[x-1][y-1] = Value

    def GetValue(self, x, y):
        if y > self.LenY:
            print("Someones doing something dumb.")
        if x > self.LenX:
            print("Someones doing something dumb.")

        return self.Grid[x-1][y-1]

    def GetSize(self):
        return(self.LenX,self.LenY)
        pass
    def GetX(self):
        return(self.LenX)
        pass
    def GetY(self):
        return(self.LenY)
        pass




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


    def GenerateVisibleGraph(self):
        ForestSize = self.Forest.GetSize()
        self.VisibleForest = src.GridStorage(ForestSize[0],ForestSize[1])
        self.VisibleCount = 0

        for y in range(2, self.VisibleForest.GetY()):
            for x in range(2, self.VisibleForest.GetX()):
                Visible = IsTreeVisible(self.Forest,(x,y))
                self.VisibleForest.SetValue(x,y,Visible)
                if Visible:
                    self.VisibleCount += 1




