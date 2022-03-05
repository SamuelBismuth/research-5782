import unittest
import io
import sys

from exercise_2 import f
from exercise_3 import List


class TestStringMethods(unittest.TestCase):


    # EXERCISE 2


    def test_1(self):
        self.assertEqual(4, f(2))

    def test_2(self):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput   
        f(2)
        sys.stdout = sys.__stdout__
        self.assertEqual(capturedOutput.getvalue(), "I already told you that the answer is 4\n")

    def test_3(self):
        self.assertEqual(9, f(3))

    def test_4(self):
        self.assertEqual(16, f(4))

    def test_5(self):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput  
        f(4) 
        sys.stdout = sys.__stdout__
        self.assertEqual(capturedOutput.getvalue(), "I already told you that the answer is 16\n")

    def test_6(self):
        self.assertEqual(4, f(2))


    # EXERCISE 3

    
    def test_7(self):
        # Example of List (which is not a regular python list).   
        mylist = List([
            [[1, 2, 3, 33], [4, 5, 6, 66]],
            [[7, 8, 9, 99], [10, 11, 12, 122]],
            [[13, 14, 15, 155], [16, 17, 18, 188]]
        ])
        self.assertEqual([[1, 2, 3, 33], [4, 5, 6, 66]], mylist[0])

    def test_8(self):
        mylist = List([
            [[1, 2, 3, 33], [4, 5, 6, 66]],
            [[7, 8, 9, 99], [10, 11, 12, 122]],
            [[13, 14, 15, 155], [16, 17, 18, 188]]
        ])
        self.assertEqual(66, mylist[0, 1, 3])

    def test_9(self):
        mylist = List([
            [[1, 2, 3, 33], [4, 5, 6, 66]],
            [[7, 8, 9, 99], [10, 11, 12, 122]],
            [[13, 14, 15, 155], [16, 17, 18, 188]]
        ])
        self.assertEqual([4, 5, 6, 66], mylist[0, 1])

    def test_10(self):
        mylist = List([
            [[1, 2, 3, 33], [4, 5, 6, 66]],
            [[7, 8, 9, 99], [10, 11, 12, 122]],
            [[13, 14, 15, 155], [16, 17, 18, 188]]
        ])
        self.assertEqual([[1, 2, 3, 33], [4, 5, 6, 66]], mylist[0])

    def test_11(self):
        mylist = List([
            [[1, 2, 3, 33], [4, 5, 6, 66]],
            [[7, 8, 9, 99], [10, 11, 12, 122]],
            [[13, 14, 15, 155], [16, 17, 18, 188]]
        ])
        self.assertEqual([[7, 8, 9, 99], [10, 11, 12, 122]], mylist[1])

    def test_12(self):
        mylist = List([
            [[1, 2, 3, 33], [4, 5, 6, 66]],
            [[7, 8, 9, 99], [10, 11, 12, 122]],
            [[13, 14, 15, 155], [16, 17, 18, 188]]
        ])
        self.assertEqual([[[1, 2, 3, 33], [4, 5, 6, 66]],
            [[7, 8, 9, 99], [10, 11, 12, 122]],
            [[13, 14, 15, 155], [16, 17, 18, 188]]], mylist)


if __name__ == '__main__':
    unittest.main()
    