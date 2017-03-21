import os
import unittest

from src.binary_trees import *
from test.fixture_binary_trees import *

class TestBinaryTrees(unittest.TestCase):
  """
  [0,1,2,3,4,5,6]

      0
    1   2
   3 4 5 6
  """

  def test_bst_node(self):
    node1 = BSTNode()
    self.assertEqual(None, node1.left)
    self.assertEqual(None, node1.right)
    self.assertEqual(None, node1.value)
    node2 = BSTNode(10)
    self.assertEqual(None, node2.left)
    self.assertEqual(None, node2.right)
    self.assertEqual(10, node2.value)

  def test_traverse_preorder(self):
    root1 = BSTNode(0,
      BSTNode(1,
        BSTNode(3),
        BSTNode(4)
      ),
      BSTNode(2,
        BSTNode(5),
        BSTNode(6)
      )
    )
    self.assertEqual([0,1,3,4,2,5,6], traverse_preorder(root1))

  def test_traverse_inorder(self):
    root1 = BSTNode(0,
      BSTNode(1,
        BSTNode(3),
        BSTNode(4)
      ),
      BSTNode(2,
        BSTNode(5),
        BSTNode(6)
      )
    )
    self.assertEqual([3,1,4,0,5,2,6], traverse_inorder(root1))

  def test_traverse_postorder(self):
    root1 = BSTNode(0,
      BSTNode(1,
        BSTNode(3),
        BSTNode(4)
      ),
      BSTNode(2,
        BSTNode(5),
        BSTNode(6)
      )
    )
    self.assertEqual([3,4,1,5,6,2,0], traverse_postorder(root1))

  def test_height(self):
    self.assertEqual(0, height(None))
    self.assertEqual(1, height(TREE_1))
    # 2
    self.assertEqual(2, height(TREE_2_1))
    self.assertEqual(2, height(TREE_2_2))
    # 3
    self.assertEqual(3, height(TREE_3_1))
    self.assertEqual(3, height(TREE_3_2))
    self.assertEqual(3, height(TREE_3_3))
    self.assertEqual(3, height(TREE_3_4))
    self.assertEqual(2, height(TREE_3_5))
    # 4
    self.assertEqual(4, height(TREE_4_1))
    self.assertEqual(4, height(TREE_4_2))
    self.assertEqual(4, height(TREE_4_3))
    self.assertEqual(4, height(TREE_4_4))
    self.assertEqual(4, height(TREE_4_5))
    self.assertEqual(4, height(TREE_4_6))
    self.assertEqual(4, height(TREE_4_7))
    self.assertEqual(4, height(TREE_4_8))
    self.assertEqual(3, height(TREE_4_9))
    self.assertEqual(3, height(TREE_4_A))
    self.assertEqual(3, height(TREE_4_B))
    self.assertEqual(3, height(TREE_4_C))
    self.assertEqual(3, height(TREE_4_D))
    self.assertEqual(3, height(TREE_4_E))

  def test_is_height_balanced(self):
    self.assertEqual(True, is_height_balanced(None))
    self.assertEqual(True, is_height_balanced(TREE_1))
    # 2
    self.assertEqual(True, is_height_balanced(TREE_2_1))
    self.assertEqual(True, is_height_balanced(TREE_2_2))
    # 3
    self.assertEqual(False, is_height_balanced(TREE_3_1))
    self.assertEqual(False, is_height_balanced(TREE_3_2))
    self.assertEqual(False, is_height_balanced(TREE_3_3))
    self.assertEqual(False, is_height_balanced(TREE_3_4))
    self.assertEqual(True, is_height_balanced(TREE_3_5))
    # 4
    self.assertEqual(False, is_height_balanced(TREE_4_1))
    self.assertEqual(False, is_height_balanced(TREE_4_2))
    self.assertEqual(False, is_height_balanced(TREE_4_3))
    self.assertEqual(False, is_height_balanced(TREE_4_4))
    self.assertEqual(False, is_height_balanced(TREE_4_5))
    self.assertEqual(False, is_height_balanced(TREE_4_6))
    self.assertEqual(False, is_height_balanced(TREE_4_7))
    self.assertEqual(False, is_height_balanced(TREE_4_8))
    self.assertEqual(False, is_height_balanced(TREE_4_9))
    self.assertEqual(True, is_height_balanced(TREE_4_A))
    self.assertEqual(True, is_height_balanced(TREE_4_B))
    self.assertEqual(True, is_height_balanced(TREE_4_C))
    self.assertEqual(True, is_height_balanced(TREE_4_D))
    self.assertEqual(False, is_height_balanced(TREE_4_E))


  def test_traverse_level(self):
    root1 = BSTNode(0,
      BSTNode(1,
        BSTNode(3),
        BSTNode(4)
      ),
      BSTNode(2,
        BSTNode(5),
        BSTNode(6)
      )
    )
    root2 = BSTNode(0,
      BSTNode(1,
        BSTNode(3),
        None, # BSTNode(4)
      ),
      BSTNode(2,
        BSTNode(5),
        BSTNode(6)
      )
    )
    root3 = BSTNode(0,
      BSTNode(1,
        BSTNode(3,
          BSTNode(7),
          BSTNode(8)
        ),
        None, # BSTNode(4)
      ),
      BSTNode(2,
        BSTNode(5,
          BSTNode(11),
          BSTNode(12)
        ),
        BSTNode(6)
      )
    )
    self.assertEqual([], traverse_level(0, None))
    self.assertEqual([0], traverse_level(0, root1))
    self.assertEqual([1,2], traverse_level(1, root1))
    self.assertEqual([3,4,5,6], traverse_level(2, root1))
    #self.assertEqual([], traverse_level(3, root1))
    self.assertEqual([None,None,None,None,None,None,None,None], traverse_level(3, root1))
    self.assertEqual([0], traverse_level(0, root2))
    self.assertEqual([1,2], traverse_level(1, root2))
    self.assertEqual([3,None,5,6], traverse_level(2, root2))
    self.assertEqual([7,8,None,None,11,12,None,None], traverse_level(3, root3))

  def test_is_full(self):

    root1 = BSTNode(0)

    root2 = BSTNode(0,
      BSTNode(1))

    root3 = BSTNode(0,
      None,
      BSTNode(2))

    root4 = BSTNode(0,
      BSTNode(1,
        BSTNode(3),
        BSTNode(4)),
      BSTNode(2,
        BSTNode(5),
        BSTNode(6)))

    root5 =BSTNode(0,
      BSTNode(1,
        None,
        BSTNode(4)
      ),
      BSTNode(2,
        BSTNode(5),
        BSTNode(6)
      )
    )

    root6 = BSTNode(0,
      BSTNode(1),
      BSTNode(2,
        BSTNode(5),
        BSTNode(6)
      )
    )

    root7 = BSTNode(0,
      BSTNode(1, BSTNode(3), BSTNode(4)),
      BSTNode(2))

    root8 = BSTNode(0,
      BSTNode(1, BSTNode(3, BSTNode(7))))

    self.assertEqual(True, is_full(root1))
    self.assertEqual(False, is_full(root2))
    self.assertEqual(False, is_full(root3))
    self.assertEqual(True, is_full(root4))
    self.assertEqual(False, is_full(root5))
    self.assertEqual(True, is_full(root6))
    self.assertEqual(True, is_full(root7))
    self.assertEqual(False, is_full(root8))

    self.assertEqual(True, is_fulli(root1))
    self.assertEqual(False, is_fulli(root2))
    self.assertEqual(False, is_fulli(root3))
    self.assertEqual(True, is_fulli(root4))
    self.assertEqual(False, is_fulli(root5))
    self.assertEqual(True, is_fulli(root6))
    self.assertEqual(True, is_fulli(root7))
    self.assertEqual(False, is_fulli(root8))

  def test_is_equal(self):
    root1 = BSTNode(0,
      BSTNode(1,
        BSTNode(3),
        BSTNode(4)
      ),
      BSTNode(2,
        BSTNode(5),
        BSTNode(6)
      )
    )
    root2 = BSTNode(0,
      BSTNode(1,
        None,
        BSTNode(4)
      ),
      BSTNode(2,
        BSTNode(5),
        BSTNode(6)
      )
    )
    self.assertEqual(True, is_equal(None, None))
    self.assertEqual(False, is_equal(None, root2))
    self.assertEqual(False, is_equal(root1, None))
    self.assertEqual(False, is_equal(root1, root2))
    self.assertEqual(True, is_equal(root1, root1))
    self.assertEqual(True, is_equal(root2, root2))

    self.assertEqual(True, is_equali(None, None))
    self.assertEqual(False, is_equali(None, root2))
    self.assertEqual(False, is_equali(root1, None))
    self.assertEqual(False, is_equali(root1, root2))
    self.assertEqual(True, is_equali(root1, root1))
    self.assertEqual(True, is_equali(root2, root2))


  def test_is_subtree(self):
    root1 = BSTNode(0,
      BSTNode(1,
        BSTNode(3),
        BSTNode(4)
      ),
      BSTNode(2,
        BSTNode(5),
        BSTNode(6)
      )
    )
    root2 = BSTNode(2,
      BSTNode(5),
      BSTNode(6)
    )
    root3 = BSTNode(2,
      BSTNode(5),
    )
    self.assertEqual(True, is_subtree(None, None))
    self.assertEqual(True, is_subtree(root1, root1))
    self.assertEqual(True, is_subtree(root2, root1))
    self.assertEqual(False, is_subtree(root3, root1))
    self.assertEqual(False, is_subtree(root1, root2))

  def test_is_perfect(self):
    root1 = BSTNode(0)

    root2 = BSTNode(0,
      BSTNode(1))

    root3 = BSTNode(0,
      None,
      BSTNode(2))

    root4 = BSTNode(0,
      BSTNode(1,
        BSTNode(3),
        BSTNode(4)),
      BSTNode(2,
        BSTNode(5),
        BSTNode(6)))

    root5 =BSTNode(0,
      BSTNode(1,
        None,
        BSTNode(4)
      ),
      BSTNode(2,
        BSTNode(5),
        BSTNode(6)
      )
    )

    root6 = BSTNode(0,
      BSTNode(1),
      BSTNode(2,
        BSTNode(5),
        BSTNode(6)
      )
    )

    root7 = BSTNode(0,
      BSTNode(1, BSTNode(3), BSTNode(4)),
      BSTNode(2))

    root8 = BSTNode(0,
      BSTNode(1, BSTNode(3, BSTNode(7))))

    self.assertEqual(True, is_perfect(root1))
    self.assertEqual(False, is_perfect(root2))
    self.assertEqual(False, is_perfect(root3))
    self.assertEqual(True, is_perfect(root4))
    self.assertEqual(False, is_perfect(root5))
    self.assertEqual(False, is_perfect(root6))
    self.assertEqual(False, is_perfect(root7))
    self.assertEqual(False, is_perfect(root8))

    # self.assertEqual(True, is_perfecti(root1))
    # self.assertEqual(False, is_perfecti(root2))
    # self.assertEqual(False, is_perfecti(root3))
    # self.assertEqual(True, is_perfecti(root4))
    # self.assertEqual(False, is_perfecti(root5))
    # self.assertEqual(False, is_perfecti(root6))
    # self.assertEqual(False, is_perfecti(root7))
    # self.assertEqual(False, is_perfecti(root8))

  def test_is_complete(self):
    root1 = BSTNode(0)

    root2 = BSTNode(0,
      BSTNode(1))

    root3 = BSTNode(0,
      None,
      BSTNode(2))

    root4 = BSTNode(0,
      BSTNode(1,
        BSTNode(3),
        BSTNode(4)),
      BSTNode(2,
        BSTNode(5),
        BSTNode(6)))

    root5 =BSTNode(0,
      BSTNode(1,
        None,
        BSTNode(4)
      ),
      BSTNode(2,
        BSTNode(5),
        BSTNode(6)
      )
    )

    root6 = BSTNode(0,
      BSTNode(1),
      BSTNode(2,
        BSTNode(5),
        BSTNode(6)
      )
    )

    root7 = BSTNode(0,
      BSTNode(1, BSTNode(3), BSTNode(4)),
      BSTNode(2))

    root8 = BSTNode(0,
      BSTNode(1, BSTNode(3, BSTNode(7))))

    self.assertEqual(True, is_complete(root1))
    self.assertEqual(True, is_complete(root2))
    self.assertEqual(False, is_complete(root3))
    self.assertEqual(True, is_complete(root4))
    self.assertEqual(False, is_complete(root5))
    self.assertEqual(False, is_complete(root6))
    self.assertEqual(True, is_complete(root7))
    self.assertEqual(False, is_complete(root8))

    self.assertEqual(True, is_completer(root1))
    self.assertEqual(True, is_completer(root2))
    self.assertEqual(False, is_completer(root3))
    self.assertEqual(True, is_completer(root4))
    self.assertEqual(False, is_completer(root5))
    self.assertEqual(False, is_completer(root6))
    self.assertEqual(True, is_completer(root7))
    self.assertEqual(False, is_completer(root8))

  #
  #
  #

  def test_traverse_levelorder(self):
    root1 = BSTNode(0,
      BSTNode(1,
        BSTNode(3),
        BSTNode(4)
      ),
      BSTNode(2,
        BSTNode(5),
        BSTNode(6)
      )
    )
    root2 = BSTNode(0,
      BSTNode(1,
        None,#BSTNode(3),
        None, # BSTNode(4)
      ),
      BSTNode(2,
        BSTNode(5),
        BSTNode(6)
      )
    )
    #self.assertEqual([0,1,2,3,4,5,6], traverse_levelorder(root1))
    #self.assertEqual([0,1,2,None,None,5,6], traverse_levelorder(root2))

  def test_create_binary_tree_array(self):
    root1 = BSTNode(0,
      BSTNode(1,
        BSTNode(3),
        BSTNode(4)
      ),
      BSTNode(2,
        BSTNode(5),
        BSTNode(6)
      )
    )
    root2 = BSTNode(0,
      BSTNode(1,
        None,
        BSTNode(4)
      ),
      BSTNode(2,
        BSTNode(5),
        BSTNode(6)
      )
    )
    expected1 = [0,1,2,3,4,5,6]
    expected2 = [0,1,2,None,4,5,6]
    self.assertEqual(expected1, create_binary_tree_array(root1))
    self.assertEqual(expected2, create_binary_tree_array(root2))

  def test_create_binary_tree(self):
    pass
