from unittest import TestCase
import src

class TestTextParser(TestCase):

    #1 Thing that needs to happen for Day 1's challenge is to read in the data from the test file.
    def test_read_file_case1(self):
        Test = src.TextParser()
        Test.ReadFile("../input_files/case1.txt")
        if len(Test.FileReadIn) != 15:
            self.fail()
            return
        pass

    def test_split_list_into_elves(self):
        Test = src.TextParser()
        Test.ReadFile("../input_files/case1.txt")
        List = Test.SplitFileIntoElves()
        print(List)

    def test_runcase2(self):
        Test = src.TextParser()
        Test.ReadFile("../input_files/case2.txt")
        List = Test.SplitFileIntoElves()
        print(List)

    def test_runcase3(self):
        Test = src.TextParser()
        Test.ReadFile("../input_files/case3.txt")
        List = Test.SplitFileIntoElves()

        Test.DoExtendedChallenge()