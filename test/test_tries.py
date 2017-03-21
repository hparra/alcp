import os
import unittest

from src.tries import *

# dodge
# dog
# doge
ROOT1 = TrieNode(None, [
  TrieNode("d", [
    TrieNode("o", [
      TrieNode("d", [
        TrieNode("g", [
          TrieNode("e", None, True)
        ])
      ]),
      TrieNode("g", [
        TrieNode("e", None, True)
      ], True)
    ]),
  ])
])

class TestTries(unittest.TestCase):

  def test_find_recursive(self):
    self.assertEqual(False, find("dod", ROOT1))
    self.assertEqual(True, find("dodge", ROOT1))
    self.assertEqual(True, find("dog", ROOT1))
    self.assertEqual(True, find("doge", ROOT1))
    self.assertEqual(False, find("dogg", ROOT1))

  def test_find_iterative(self):
    self.assertEqual(False, findi("dod", ROOT1))
    self.assertEqual(True, findi("dodge", ROOT1))
    self.assertEqual(True, findi("dog", ROOT1))
    self.assertEqual(True, findi("doge", ROOT1))
    self.assertEqual(False, findi("dogg", ROOT1))

  def test_add_iterative(self):
    root = add("dog")
    add("dodge", root)
    add("doge", root)
    add("doggy", root)
    self.assertEqual(False, findi("dod", root))
    self.assertEqual(True, findi("dodge", root))
    self.assertEqual(True, findi("dog", root))
    self.assertEqual(True, findi("doge", root))
    self.assertEqual(False, findi("dogg", root))
    self.assertEqual(True, findi("doggy", root))
