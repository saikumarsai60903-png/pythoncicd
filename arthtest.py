 from arth import *
import unittest
class ArthTest(unittest.TestCase):
 def test_add(self):
    self.assertEqual(add(10,5),15)
def test_sub(self):
    self.assertEqual(sub(10,5),5)
def test_mul(self):
    self.assertEqual(mul(10,5),50)
if__name__=="__main__"
   unittest.main()