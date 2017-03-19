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

  def test_is_palindrome(self):
    self.assertEqual(True, is_palindrome(None))
    self.assertEqual(True, is_palindrome(""))
    self.assertEqual(True, is_palindrome("a"))
    self.assertEqual(False, is_palindrome("ab"))
    self.assertEqual(True, is_palindrome("aba"))
    self.assertEqual(True, is_palindrome("abba"))
    self.assertEqual(False, is_palindrome("abbaa"))

  def test_is_palindrome_recursive(self):
    self.assertEqual(True, is_palindromer(None))
    self.assertEqual(True, is_palindromer(""))
    self.assertEqual(True, is_palindromer("a"))
    self.assertEqual(False, is_palindromer("ab"))
    self.assertEqual(True, is_palindromer("aba"))
    self.assertEqual(True, is_palindromer("abba"))
    self.assertEqual(False, is_palindromer("abbaa"))

  def test_split(self):
    self.assertEqual([], split(None, None))
    self.assertEqual([], split("", None))
    with self.assertRaises(ValueError): split("","")
    self.assertEqual([""], split("", "a"))
    self.assertEqual(["a"], split("a", None))
    self.assertEqual(["",""], split("a", "a"))
    self.assertEqual(["a"], split("a", "ab"))
    self.assertEqual(["", "b"], split("ab", "a"))
    self.assertEqual(["a", ""], split("ab", "b"))
    self.assertEqual(["ab", ""], split("abc", "c"))
    self.assertEqual(["a", "c"], split("abc", "b"))
    self.assertEqual(["", "bc"], split("abc", "a"))
    self.assertEqual(["", "c"], split("abc", "ab"))
    self.assertEqual(["a", ""], split("abc", "bc"))
    self.assertEqual(["abc"], split("abc", "ac"))
    self.assertEqual(["",""], split("abc", "abc"))

  def test_split_recursive(self):
    self.assertEqual([], splitr(None, None))
    self.assertEqual([], splitr("", None))
    with self.assertRaises(ValueError): splitr("","")
    self.assertEqual([""], splitr("", "a"))
    self.assertEqual(["a"], splitr("a", None))
    self.assertEqual(["",""], splitr("a", "a"))
    self.assertEqual(["a"], splitr("a", "ab"))
    self.assertEqual(["", "b"], splitr("ab", "a"))
    self.assertEqual(["a", ""], splitr("ab", "b"))
    self.assertEqual(["ab", ""], splitr("abc", "c"))
    self.assertEqual(["a", "c"], splitr("abc", "b"))
    self.assertEqual(["", "bc"], splitr("abc", "a"))
    self.assertEqual(["", "c"], splitr("abc", "ab"))
    self.assertEqual(["a", ""], splitr("abc", "bc"))
    self.assertEqual(["abc"], splitr("abc", "ac"))
    self.assertEqual(["",""], splitr("abc", "abc"))
