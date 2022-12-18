
class Node:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
        pass



    def CheckForAdjacent(self,Node):
        def PlusOrMinus(Node,Target):
            AdjacentCount = 0
            if (Node.x + 1 == Target.x) or (Node.x - 1 == Target.x)  or (Node.x == Target.x):
                print("X Adjacent")
                AdjacentCount+=1
            if (Node.y + 1 == Target.y) or (Node.y - 1 == Target.y) or (Node.y  == Target.y):
                print("Y Adjacent")
                AdjacentCount+=1
            if (Node.z + 1 == Target.z) or (Node.z - 1 == Target.z) or (Node.z == Target.z):
                print("z Adjacent")
                AdjacentCount+=1
            if AdjacentCount >=2:
                return True

        if self.x == Node.x and self.y == Node.y and self.z == Node.z :
            print ("Is Itself")
        elif (PlusOrMinus(self,Node)):
            return True
        else:
            print("NoMatch")


        #Check for Best 2 / 3


        pass

class GridStorage:
    def __init__(self,x,y,z):
        self.LenX = x
        self.LenY = y
        self.LenZ = z
        self.Grid =  [[[None for k in range(z)]for i in range(y)] for j in range(x)]
        pass

    def SetValue(self,x,y,z,Value):
        if y > self.LenY or  x > self.LenX or z > self.LenZ:
            print("Someones doing something dumb.")
        self.Grid[x-1][y-1][z-1] = Value

    def GetValue(self, x, y,z):
        if y > self.LenY or  x > self.LenX or z > self.LenZ:
            print("Someones doing something dumb.")
        return self.Grid[x-1][y-1][z-1]


with open("day18.in") as file:
    data = [row.strip() for row in file.readlines()]

    MAX_X = 0
    MAX_Y = 0
    MAX_Z = 0

    NodeGraph =[]

    for Cube in data:
        print(Cube)
        Temp = Cube.split(",")
        Temp = [int(x) for x in Temp]

        if Temp[0] > MAX_X:
            MAX_X = Temp[0]
        if Temp[1] > MAX_Y:
            MAX_Y = Temp[1]
        if Temp[2] > MAX_Z:
            MAX_Z = Temp[2]

    print("Largest Axis: ",MAX_X ," ", MAX_Y ,"," ,MAX_Z )
    PlaySpace = GridStorage(MAX_X,MAX_Y,MAX_Z)

    for Cube in data:
        Temp = Cube.split(",")
        Temp = [int(x) for x in Temp]
        PlaySpace.SetValue(Temp[0],Temp[1],Temp[2],True )
        NodeGraph += [Node(Temp[0],Temp[1],Temp[2])]

    Link =[]
    for Connection in NodeGraph:
        print(Connection)
        for ScanBlock in NodeGraph:
            print("Checking if Adjacent")
            if ( Connection.CheckForAdjacent(ScanBlock)) :
                if ScanBlock in Link :
                    print("Already In the NodeGraph")
                else:
                    Link += [ScanBlock]

    temp = 6 * len(NodeGraph)
    temp -= len(Link)+1
    print (temp)


