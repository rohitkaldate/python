import unittest

from Add_numbers import add

class Add_Numbers(unittest.TestCase):
    def test_add_positive(self):
        result = add(2,3)
        self.assertEqual(result,8)
        
    # def test_add_negative(self):
    #     result= Add_numbers.add(-2,-3)
    #     self.assertEqual(result,-5)
        
    # def test_add_mixed(self):
    #     result= Add_numbers.add(3,-5)
    #     self.assertEqual(result,-2)
        
if __name__=='__main__':
    unittest.main()