from unittest import TestCase
import src


class TestTextParser(TestCase):

    def test_read_file_case1(self):
        Test = src.TextParser()
        Test.ReadFile("../input_files/case1.txt")

        Score = 0

        ThreeBackpacks = []
        Count = 0
        for x in Test.FileReadIn :
            x = x.strip("\n")
            ThreeBackpacks += [x]

            Count+=1
            if Count>=3:
                A =                 src.Backpack(ThreeBackpacks[0],ThreeBackpacks[1],ThreeBackpacks[2])
                Score += A.GetScore()
                Count = 0
                ThreeBackpacks  = []


        print(Score)
