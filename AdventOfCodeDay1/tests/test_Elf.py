from unittest import TestCase
import src

class TestElf(TestCase):
    def test_greet(self):
        TestElf = src.Elf()
        TestElf.greet()

