from unittest import TestCase
import src


class TestTextParser(TestCase):
    def test_read_file_case1(self):
        Test = src.TextParser()
        Test.ReadFile("../input_files/case1.txt")

        Forest =  src.Forest()








