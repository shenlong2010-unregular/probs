import validateSubsequence as program
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        array = [5, 1, 22, 25, 6, -1, 8, 10]
        sequence = [1, 6, -1, 10]
        self.assertTrue(program.isValidSubsequence1(array, sequence))

if __name__ == "__main__":
	unittest.main()