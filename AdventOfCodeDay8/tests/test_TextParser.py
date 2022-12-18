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


        Forest.GetInnerGridXY()

        Forest.GenerateVisibleGraph()





