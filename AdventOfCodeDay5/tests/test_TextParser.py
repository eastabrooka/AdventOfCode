from unittest import TestCase
import src


class TestTextParser(TestCase):

    def test_read_file_case1(self):
        Test = src.TextParser()
        Test.ReadFile("../input_files/case1.txt")

        Crane = src.CraneOperations(Test.FileReadIn)
        #FindTheLine that is blank.

        GridLen = Crane.FindColsOfContainers()

        Crane.GenerateStacks()

        ReadInCrates = True
        ReadInOperations = False
        Iterator = 0
        for x in Test.FileReadIn:
            if ReadInCrates:
                Crane.AddCrates(x)
                Iterator+=1
                if Iterator >= GridLen:
                    print("Hit ")
                    ReadInCrates = False
            else :
                Crane.AddOperations(x)

        checksum =[]
        for x in Crane.Collums:
            temp = x
            lentemp = len(x)-1
            temp2 = x[lentemp]
            checksum += [temp2]
            pass

        print(checksum)
