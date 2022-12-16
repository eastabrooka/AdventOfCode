from unittest import TestCase
import src


class TestTextParser(TestCase):

    #1 Thing that needs to happen for Day 1's challenge is to read in the data from the test file.
    def test_read_file_case3(self):
        Test = src.TextParser()
        Test.ReadFile("../input_files/case2.txt")

        Score = 0
        for x in Test.FileReadIn :
            x = x.strip("\n")
            Pair = x.split(" ")
            print(Pair)
            Round = src.RockPaperSissorsRound(Pair[0],Pair[1])
            Score += Round.WinLossCheck()

        print("Total Scores : ", Score)