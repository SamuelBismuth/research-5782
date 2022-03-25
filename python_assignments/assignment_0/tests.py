import unittest
import io
import sys

from exercise_1 import f, safe_call
from exercise_2 import print_sorted
from exercise_3 import find_root


class TestStringMethods(unittest.TestCase):


    # EXERCISE 1

    def test_working_safe_call(self):
        self.assertEqual(safe_call(f, x=5, y=7.0, z=3), 15.0)
    

    def test_working_safe_call_but_not_logical(self):
        try:
            safe_call(f, x=5, y=7.0, z="3")
        except TypeError:
            pass
        except Exception:
            self.fail('unexpected exception raised')
        else:
            self.fail('TypeError not raised')


    def test_safe_call_exception(self):
        try:
            safe_call(f, x=5, y="abc", z=3)
        except Exception as error:
            self.assertEqual(str(error), "Check the arguments.")
        else:
            self.fail('TypeError not raised')

    
    # EXERCISE 2

    def test_1(self):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput   
        x = {"a":5, "c":6, "b":[(1, 3, 2, 5, 4), 3, 2, 4]}
        print_sorted(x)
        sys.stdout = sys.__stdout__
        self.assertEqual(capturedOutput.getvalue(), "{a,:5,b,:((1,2,3,4,5,),2,3,4,),c,:6,} ")
        
        
    def test_2(self):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput   
        x = {"a":5, (3, (3, 1)):(8, 4, 3), "b":[(1, 3, 2, 5, 4), 3, 2, 4]}
        print_sorted(x)
        sys.stdout = sys.__stdout__
        self.assertEqual(capturedOutput.getvalue(), "{a,:5,b,:((1,2,3,4,5,),2,3,4,),((1,3,),3,),:(3,4,8,),} ")
        

    def test_3(self):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput   
        x = (3, [4, 3, 2], 9)
        print_sorted(x)
        sys.stdout = sys.__stdout__
        self.assertEqual(capturedOutput.getvalue(), "(3,9,(2,3,4,),),")
        

    def test_4(self):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput   
        x = {"a":5, "c":6, "b":[1, 3, 2, 4]}
        print_sorted(x)
        sys.stdout = sys.__stdout__
        self.assertEqual(capturedOutput.getvalue(), "{a,:5,b,:(1,2,3,4,),c,:6,} ")
        

    def test_5(self):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput   
        x = {"a":5, "c":6, "b":{"a":5, "c":6, "b":[1, 3, 2, 4]}}
        print_sorted(x)
        sys.stdout = sys.__stdout__
        self.assertEqual(capturedOutput.getvalue(), "{a,:5,b,:{a,:5,b,:(1,2,3,4,),c,:6,} c,:6,} ")
        

    def test_6(self):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput   
        x = {"a":5, "c":set(["A", "b", "a"]), "b":[9, 3, 2, 4]}
        print_sorted(x)
        sys.stdout = sys.__stdout__
        self.assertEqual(capturedOutput.getvalue(), "{a,:5,b,:(2,3,4,9,),c,:(A,a,b,),} ")
        

    def test_7(self):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput   
        x = {"a":5, "c":set(["A", "b", "a"]), "b":(9, 3, 2, 4)}
        print_sorted(x)
        sys.stdout = sys.__stdout__
        self.assertEqual(capturedOutput.getvalue(), "{a,:5,b,:(2,3,4,9,),c,:(A,a,b,),} ")
        

    def test_8(self):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput   
        x = [1, 2, 4, 3, 2]
        print_sorted(x)
        sys.stdout = sys.__stdout__
        self.assertEqual(capturedOutput.getvalue(), "(1,2,2,3,4,),")
        

    def test_9(self):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput   
        x = set([1, 2, 4, 3, 2])
        print_sorted(x)
        sys.stdout = sys.__stdout__
        self.assertEqual(capturedOutput.getvalue(), "(1,2,3,4,),")
        

    def test_10(self):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput   
        x = (1, 2, 4, 3, 2)
        print_sorted(x)
        sys.stdout = sys.__stdout__
        self.assertEqual(capturedOutput.getvalue(), "(1,2,2,3,4,),")


    # EXERCISE 3
        
    def test_11(self):
        self.assertEqual(find_root(lambda x: x**2-4, 1, 3), 2)
            
    def test_12(self):
        self.assertEqual(find_root(lambda x: x * x * x - x * x + 2, 0, 2), 1)
    
    def test_13(self):
        self.assertEqual(find_root(lambda x: x * x * x * x - x * x + 2, 0, 2), 1)


if __name__ == '__main__':
    unittest.main()