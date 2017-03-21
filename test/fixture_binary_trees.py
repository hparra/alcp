
from src.binary_trees import BSTNode

### Size 1

# 0
TREE_1 = BSTNode(0)

### Size 2

#  0
# 1
TREE_2_1 = BSTNode(0,
  BSTNode(1),
  None
)
# complete

#  0
#   2
TREE_2_2 = BSTNode(0,
  None,
  BSTNode(2)
)

#
# Size 3
# There are 5 perms -- why?

#    0
#  1
# 3
TREE_3_1 = BSTNode(0,
  BSTNode(1, BSTNode(3))
)

#    0
#  1
#   4
TREE_3_2 = BSTNode(0,
  BSTNode(1, None, BSTNode(4))
)

#    0
#      2
#     5
TREE_3_3 = BSTNode(0,
  None,
  BSTNode(2, BSTNode(5))
)

#    0
#      2
#       6
TREE_3_4 = BSTNode(0,
  None,
  BSTNode(2, None, BSTNode(6))
)

#  0
# 1 2
TREE_3_5 = BSTNode(0,
  BSTNode(1),
  BSTNode(2)
)
# Complete, Full, Perfect


### Size 4

#     0
#   1
#  3
# 7
TREE_4_1 = BSTNode(0,
  BSTNode(1, BSTNode(3, BSTNode(7)))
)

#     0
#   1
#  3
#   8
TREE_4_2 = BSTNode(0,
  BSTNode(1,
    BSTNode(3,
      None,
      BSTNode(8)
)))

#     0
#   1
#    4
#   9
TREE_4_3 = BSTNode(0,
  BSTNode(1,
    None,
    BSTNode(4,
      BSTNode(9))
  )
)

#     0
#   1
#    4
#     A
TREE_4_4 = BSTNode(0,
  BSTNode(1,
    None,
    BSTNode(4,
      None,
      BSTNode('A')
)))

#    0
#      2
#     5
#    B
TREE_4_5 = BSTNode(0,
  None,
  BSTNode(2,
    BSTNode(5,
      BSTNode('B'))
  )
)

#    0
#      2
#     5
#      C
TREE_4_6 = BSTNode(0,
  None,
  BSTNode(2,
    BSTNode(5,
      None,
      BSTNode('C'))
  )
)

#    0
#      2
#       6
#      D
TREE_4_7 = BSTNode(0,
  None,
  BSTNode(2,
    None,
    BSTNode(6,
      BSTNode('D')),
  )
)

#    0
#      2
#       6
#        E
TREE_4_8 = BSTNode(0,
  None,
  BSTNode(2,
    None,
    BSTNode(6,
      None,
      BSTNode('E')),
  )
)

#     0
#   1
#  3 4
TREE_4_9 = BSTNode(0,
  BSTNode(1,
    BSTNode(3),
    BSTNode(4))
)


#    0
#  1   2
# 3
# COMPLETE
TREE_4_A = BSTNode(0,
  BSTNode(1,
    BSTNode(3)),
  BSTNode(2)
)

#    0
#  1   2
#   4
TREE_4_B = BSTNode(0,
  BSTNode(1,
    None,
    BSTNode(4)
  ),
  BSTNode(2)
)

#    0
#  1   2
#     5
TREE_4_C = BSTNode(0,
  BSTNode(1),
  BSTNode(2,
    BSTNode(5)
  )
)

#    0
#  1   2
#       6
TREE_4_D = BSTNode(0,
  BSTNode(1),
  BSTNode(2,
    None,
    BSTNode(6),
  )
)

#     0
#       2
#      5 6
TREE_4_E = BSTNode(0,
  None,
  BSTNode(2,
    BSTNode(5),
    BSTNode(6)
  )
)

### Size 5 (3 levels)

#    0
#  1   2
# 3 4
# FULL + COMPLETE
Tree_5_1 = BSTNode(0,
  BSTNode(1,
    BSTNode(3),
    BSTNode(4),
  ),
  BSTNode(2,
    None,
    None
  )
)

#    0
#  1   2
# 3   5
Tree_5_2 = BSTNode(0,
  BSTNode(1,
    BSTNode(3),
    None,
  ),
  BSTNode(2,
    BSTNode(5),
    None
  )
)

#    0
#  1   2
# 3     6
Tree_5_3 = BSTNode(0,
  BSTNode(1,
    BSTNode(3),
    None,
  ),
  BSTNode(2,
    None,
    BSTNode(6),
  )
)


#    0
#  1   2
#   4 5

#    0
#  1   2
#   4   6

#    0
#  1   2
#     5 6
# FULL

### SIZE 6 (3 levels)

#    0
#  1   2
# 3 4 5
# COMPLETE

#    0
#  1   2
# 3 4   6

#    0
#  1   2
# 3   5 6

#    0
#  1   2
#   4 5 6

# SIZE 7 (3 levels)

#    0
#  1   2
# 3 4 5 6
# PERFECT



# QUESTION: Is a tree that is complete also height-balanced?


#        0
#    1       2
#  3   4   5   6
# 7 8 9 A B C D E

# Catalan Numbers
# C(2) = 2
# C(3) = 5
# C(4) = 14
# C(5) = 42
