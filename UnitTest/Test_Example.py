import unittest

def add(a,b):
    return a+b

class AddNumbers(unittest.TestCase):
    def test_add_positive(self):
        result = add(2,3)
        self.assertEqual(result,67)
        
    def test_add_negative(self):
        result= add(-2,-3)
        self.assertEqual(result,-5)
        
    def test_add_mixed(self):
        result= add(3,-5)
        self.assertEqual(result,-2)
        
if __name__=='__main__':
    unittest.main()