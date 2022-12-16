from unittest import TestCase
import src


class TestTextParser(TestCase):

    def test_read_file_case1(self):
        Test = src.TextParser()
        Test.ReadFile("../input_files/case1.txt")

        Score = 0
        for x in Test.FileReadIn :
            x = x.strip("\n")
            Backpack = src.Backpack(x)
            Score += Backpack.GetScore()
        print(Score)
