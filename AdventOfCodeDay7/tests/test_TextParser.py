from unittest import TestCase
import src

def CheckForDirectories(Tree):
    if (isinstance(Tree, src.Directory)):
        return True
    elif (isinstance(Tree, str)):
        return False

def CheckForTree(Tree):
    try :
        if len(Tree.Tree)>0:
            return Tree.Tree
    except:
        return Tree

def ExtractSize(Input):
    if Input:
        temp = Input.split(" ")
        return temp[0]
    else:
        return 0

ListOfDirSizes =[]

DirectoriesUnderLimitSum = 0
def Traverse(Root):
    AnyDirs = False
    SizeSum = 0
    DirList = []
    print("Opening Dir",Root.DirName)
    for Element in CheckForTree(Root):
        if Element is None:
            pass
        else :
            if (CheckForDirectories(Element)):
                Traverse(Element)
                AnyDirs = True
                DirList +=[Element]
            else:
                #Add to SizeSum
                Root.DirSize += int(ExtractSize(Element))
                print("Adding File ",Element,"To Total for this Dir. The total is currently",Root.DirSize)

    for Element in DirList:
        print("There was a Folder in this LS, Lets add that too")
        print("Adding" , Element.DirSize ," From ", Element.DirName)
        Root.DirSize += Element.DirSize

    global ListOfDirSizes
    ListOfDirSizes += [Root.DirSize]
    print("CD ..")

class TestTextParser(TestCase):

    def test_read_file_case1(self):
        Test = src.TextParser()
        Test.ReadFile("../input_files/case1.txt")

        root = src.Directory("Root",None)
        CurrentHandle = root
        ReportInProgress = False

        for x in Test.FileReadIn:

            if ("$" in x):
                #print("Command",x)

                if ("$ cd /" in x):
                    #print("Set Hndl to Root")
                    CurrentHandle = root

                elif ("$ ls" in x):
                    #print("Starting Read In")
                    ReportInProgress = True

                elif ("$ cd .." in x):
                    #print("Change Directory Up")
                    CurrentHandle = CurrentHandle.CDUp()

                elif ("$ cd" in x):
                    #print("Change Directory")
                    #Check For Dir, If No Dir, Then create one.
                    CurrentHandle = CurrentHandle.FindDirectory(x,CurrentHandle)
            else:
                #print("Result",x)
                CurrentHandle.AddTreeResult(x,CurrentHandle)

        #print("Done")
        Traverse(root)
        print("Here")

        global ListOfDirSizes
        print(ListOfDirSizes)
        ListOfDirSizes.sort()

        #The total disk space available to the filesystem is 70000000.
        #To run the update, you need unused space of at least 30000000.
        FreeSpace = 70000000 - root.DirSize
        DeletionRequired = 30000000 - FreeSpace

        for x in ListOfDirSizes:
            if x >= DeletionRequired:
                print(x)

        pass









