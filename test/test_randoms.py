import os
import unittest

from src.randoms import *

class TestFun(unittest.TestCase):

  # NOTE: How else would you test something like this?
  def test_randint(self):
    """randint(start,stop)"""
    a = 0
    b = 10
    ans = True
    for i in range(10): # idk
      r = randint(a,b)
      ans = ans and (r >= a and r < b)
    self.assertEqual(True, ans)
