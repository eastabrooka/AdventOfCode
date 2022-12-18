from unittest import TestCase
import src


class TestTextParser(TestCase):
    def test_read_file_case1(self):
        Test = src.TextParser()
        Test.ReadFile("../input_files/case1.txt")

        Forest =  src.Forest()
        for row in Test.FileReadIn:
            row = row.strip("\n")
            Forest.AddRow([*row])
        #Done Adding Rows. Lets "Flip" it into normal coordiante form.
        pass

        FlippedYForest = []
        for Flipped in Forest.Forest :
            print(Flipped)
            FlippedYForest.insert(0,Flipped)
        Forest.Forest = FlippedYForest


        TotalYLen = len(Forest.Forest)
        TotalXLen = len(Forest.Forest[0])
        ForestGrid = src.GridStorage(TotalXLen,TotalYLen)

        yindex = 1
        xindex = 1

        for Y in Forest.Forest:
            for X in Y:
                ForestGrid.SetValue(xindex,yindex,int(X))
                xindex+=1
            yindex+=1
            xindex= 1

        Forest.Forest  = ForestGrid


        Forest.GenerateVisibleGraph()

        print("Getting Perimiter")
        print( Forest.Forest.GetX())
        print( Forest.Forest.GetY())
        Perimiter = (Forest.Forest.GetX() * 2 ) + (Forest.Forest.GetY() *2) - 4
        temp = Forest.VisibleCount + Perimiter
        print("Total Trees Visible", temp)

        pass





