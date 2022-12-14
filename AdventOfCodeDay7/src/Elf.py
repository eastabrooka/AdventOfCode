import re
class Directory:
    def __init__(self,DirName,CurrentParent):
        self.DirName = DirName
        self.ParentDir = CurrentParent
        self.Tree = [None]
        self.DirSize = 0
        pass

    def AddTreeResult(self, File,CurrentDir):
        if "dir" in File:
            Temp = File.strip("\n")
            Temp = Temp.split(" ")

            TempDir = Directory(Temp[1],CurrentDir)
            self.Tree += [TempDir]
        else:
            self.Tree += [File]

    def CDUp(self):
        return self.ParentDir

    def FindDirectory(self,FindString,CurrentParent):
        TempStr = FindString.strip("\n")
        TempStr = TempStr.split(" ")
        TempStr = TempStr[2]

        for x in self.Tree:
            if (isinstance(x, str)):
                if x in FindString:
                    x = Directory(FindString,CurrentParent)
                    return x
            elif x is None:
                pass
            else:
                if x.DirName in FindString:
                    return x