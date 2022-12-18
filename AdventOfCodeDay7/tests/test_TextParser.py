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


def Traverse(Root):
    for Element in CheckForTree(Root):
        if Element is None:
            pass
        else :
            if (CheckForDirectories(Element)):
                Traverse(Element)
            else:
                print("Sum")

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








