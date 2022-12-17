import re


class CraneOperations:
    def __init__(self,Data):
        self.Data = Data
        pass

    def AddSplitter(self, Line):
        RollingBuffer = []

        Temp = Line.split(" ")

        RollingCounter = 0
        for x in Temp:
            if len(x) == 0:
                RollingCounter+=1
                if RollingCounter == 4:
                    RollingCounter = 0
                    RollingBuffer +=[" "]
            else:
                RollingCounter =0
                RollingBuffer += [x]
        return RollingBuffer

    def AddOperations(self,Line):
        if "move" in Line:
            print("Process")
            CommandIndex = Line.split(" ")

            NumberToMove = int(CommandIndex[1])
            From = int(CommandIndex[3])
            To = int(CommandIndex[5])

            Transit = []
            for x in range (0,NumberToMove):
                Transit += [self.Collums[int(From)-1].pop()]

            print("Moving ", Transit)

            Transit.reverse()
            for x in Transit:
                self.Collums[To-1].append(x)
            print("Her")


    def AddCrates(self,Crates):
        #ArrayOfCrates = Crates.split(" ")

        ArrayOfCrates = self.AddSplitter(Crates)
        index = 0
        for Add in ArrayOfCrates:
            if len(Add)==1:
                pass
            else:
                self.Collums[index].insert(0,Add.strip("\n"))
            index+=1

    def GenerateStacks(self):
        print("Generating Stacks")
        self.Collums = []
        for x in range (1,int(self.GridLen)+1):
            self.Collums +=[[]]
        print (self.Collums)


    def FindColsOfContainers(self):
        lineNumber = 1
        for x in self.Data:
            if x =='\n':
                print("found it at line #",lineNumber)
                break
            lineNumber+=1

        line = self.Data[lineNumber-2]
        line = line.strip("\n")
        grid = line.split("   ")
        print(grid)
        self.GridLen = grid[len(grid)-1]
        return lineNumber-2