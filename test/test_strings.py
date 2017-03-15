import os
import unittest

from src.strings import *

class TestFun(unittest.TestCase):

  def test_trim(self):
    self.assertEqual("hello", trim("  hello "))
    self.assertEqual("hello", trim("***hello**", "*"))

  def test_parse_int(self):
    self.assertEqual(1234, parse_int("1234"))
    self.assertEqual(-1234, parse_int("-1234"))
    with self.assertRaises(ValueError):
      parse_int("number")
