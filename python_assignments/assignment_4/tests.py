import unittest

from exercise_1 import bounded_subsets

class TestStringMethods(unittest.TestCase):


    # EXERCISE 1

    def test_wrong_bounded_subsets(self):
        S = [-1, 20, 3, 1, 50]
        C = 100
        try:
            for s in bounded_subsets(S, C):
                print(s)
        except Exception as error:
            self.assertEqual(str(error), 'input must be positive only.')


    def test_bounded_subsets(self):
        S = [1, 2, 3, 40, 50]
        C = 6

        all_subsets = []
        for s in bounded_subsets(S, C):
            all_subsets.append(s)
        self.assertEqual(all_subsets, [[], [1], [1, 2], [1, 3], [1, 2, 3], [2], [2, 3], [3]])
    

    def test_bounded_subsets_2(self):
        S = [1, 2, 3, 40, 50]
        C = 100

        all_subsets = []
        for s in bounded_subsets(S, C):
            all_subsets.append(s)
        results = [[], [1], [1, 2], [1, 3], [1, 40], [1, 50], [1, 2, 3], [1, 2, 40], [1, 2, 50], [1, 3, 40], [1, 3, 50], [1, 40, 50], [1, 2, 3, 40], [1, 2, 3, 50], [1, 2, 40, 50], [1, 3, 40, 50], [1, 2, 3, 40, 50], [2], [2, 3], [2, 40], [2, 50], [2, 3, 40], [2, 3, 50], [2, 40, 50], [2, 3, 40, 50], [3], [3, 40], [3, 50], [3, 40, 50], [40], [40, 50], [50]]
        self.assertEqual(all_subsets, results)




if __name__ == '__main__':
    unittest.main()