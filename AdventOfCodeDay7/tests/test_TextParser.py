from unittest import TestCase
import src

def ProcessSpace(Handle):
    pass


def GetDirs(Tree):
    Dir = []
    try:
        if (isinstance(Tree.Tree, src.Directory)):
            print("Directory")
            return Tree.Tree

        for Element in Tree.Tree:
            print(Element)
            if (isinstance(Element, str)):
                print("String")
            else:
                print("Directory")
                Dir += [Element]
        if (len(Dir) > 0):
            return Dir
    except:
        for Element in Tree:
            print(Element)
            if (isinstance(Element, str)):
                print("String")
            else:
                print("Directory")
                Dir += [Element]
        else:
            return False
    return Dir


def CheckForDirs(Tree):
    Dir = []
    try:
        for Element in Tree.Tree:
            print(Element)
            if (isinstance(Element, str)):
                print("String")
            else:
                print("Directory")
                return True
        else:
            return False
    except:
        try:
            for Element in Tree:
                print(Element)
                if (isinstance(Element, str)):
                    print("String")
                else:
                    print("Directory")
                    return True
            else:
                return False
        except:
            pass


def Recurse(Handle):
    if (CheckForDirs(Handle)):
        print("Dirs Found")
        Temp = GetDirs(Handle)
        Recurse(Temp)
        ProcessSpace(Temp)
    else:
        print("SpaceCalculate")
        ProcessSpace(Handle)


class TestTextParser(TestCase):

    def test_read_file_case1(self):
        Test = src.TextParser()
        Test.ReadFile("../input_files/case1.txt")

        root = src.Directory("Root",None)
        CurrentHandle = root
        ReportInProgress = False

        for x in Test.FileReadIn:
            if ("$" in x):
                print("Command",x)

                if ("$ cd /" in x):
                    print("Set Hndl to Root")
                    CurrentHandle = root

                elif ("$ ls" in x):
                    print("Starting Read In")
                    ReportInProgress = True

                elif ("$ cd .." in x):
                    print("Change Directory Up")
                    CurrentHandle = CurrentHandle.CDUp()

                elif ("$ cd" in x):
                    print("Change Directory")
                    #Check For Dir, If No Dir, Then create one.
                    CurrentHandle = CurrentHandle.FindDirectory(x,CurrentHandle)


            else:
                print("Result",x)
                CurrentHandle.AddTreeResult(x,CurrentHandle)

        print("Done")
        Recurse(root)






