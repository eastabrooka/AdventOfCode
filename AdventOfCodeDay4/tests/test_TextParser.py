from unittest import TestCase
import src


class TestTextParser(TestCase):

    def test_read_file_case1(self):
        Test = src.TextParser()
        Test.ReadFile("../input_files/case1.txt")

        TotalOverlapCount = 0
        for x in Test.FileReadIn:
            x = x.strip("\n")
            x = x.split(",")
            a = src.SpaceCleaner(x)
            if (a.CheckForOverlap()):
                print ("Overlap Detected")
                TotalOverlapCount +=1
            else:
                print("No Overlap")
        print(TotalOverlapCount)