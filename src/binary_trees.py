

class BSTNode(object):
  """Node for Binary (Search) Tree"""
  def __init__(self, value=None, left=None, right=None):
    super(BSTNode, self).__init__()
    self.value = value # anything
    self.left = left # BSTNode
    self.right = right # BSTNode

def traverse_preorder(node):
  """Return array of binary tree elements pre-order"""
  if node is None:
    return []
  else:
    return [node.value] + traverse_preorder(node.left) + traverse_preorder(node.right)

def traverse_inorder(node):
  """Return array of binary tree elements in-order"""
  if node is None:
    return []
  else:
    return traverse_inorder(node.left) + [node.value] + traverse_inorder(node.right)

def traverse_postorder(node):
  """Return array of binary tree elements post-order"""
  if node is None:
    return []
  else:
    return traverse_postorder(node.left) + traverse_postorder(node.right) + [node.value]

def height(node):
  """Return the (max) height of the tree."""
  if node is None:
    return 0
  else:
    return 1 + max(height(node.left), height(node.right))

def is_height_balanced(root):
  """Check if binary tree is height balanced.
  A tree whose subtrees differ in height by no more than one and the subtrees are height-balanced.
  An empty tree is height-balanced.
  """
  def balanced_height(node):
    """Return height of tree if height balanced, -1 otherwise"""
    if node is None:
      return 0 # height
    else:
      left = balanced_height(node.left)
      right = balanced_height(node.right)
      if left == -1 or right == -1:
        return -1
      if abs(left-right) > 1:
        return -1
      return 1 + max(left, right)

  return balanced_height(root) != -1

# TODO: Can this also be done with BFS?
def traverse_level(level, node, is_root=True):
  """Return array of binary tree elements at tree level"""
  if node is None and is_root:
    return []
  if node is None:
    return [None] * pow(2, level)
  if level == 0:
    return [node.value]
  else:
    return traverse_level(level-1, node.left, False) + traverse_level(level-1, node.right, False)

# def traverse_leveli(level, root):
#   if node is None:
#     return []
#   values = []
#   queue = [root]
#   curr_level = 0
#   while len(queue) > 0:
#     max_items = pow(2, curr_level)
#

def is_full(node):
  """Check if binary tree is full"""
  if node is None:
    return True
  elif node.left and node.right is None:
    return False
  elif node.left is None and node.right:
    return False
  else:
    return is_full(node.left) and is_full(node.right)

def is_fulli(root):
  """Check if binary tree is full, iteratively"""
  if root is None:
    return True
  queue = [root]
  while len(queue) > 0:
    node = queue.pop(0)
    if node:
      if node.left and node.right is None:
        return False
      if node.left is None and node.right:
        return False
      queue.append(node.left)
      queue.append(node.right)
  return True

def is_equal(node1, node2):
  """Check if two binary trees are equal"""
  if node1 is None and node2 is None:
    return True
  elif node1 and node2 is None:
    return False
  elif node1 is None and node2:
    return False
  elif node1.value != node2.value:
    return False
  else:
    return is_equal(node1.left, node2.left) and is_equal(node1.right, node2.right)

def is_equali(root1, root2):
  queue = [(root1, root2)]
  while len(queue) > 0:
    nodes = queue.pop(0)
    node1 = nodes[0]
    node2 = nodes[1]
    if node1 is None and node2:
      return False
    if node1 and node2 is None:
      return False
    if node1 and node2:
      if node1.value != node2.value:
        return False
      queue.append((node1.left, node2.left))
      queue.append((node1.right, node2.right))
    # if both None then still True -- continue
  return True

# if A is subtree of B, and B is subtree of A, then A = B
# NOTE: This assume unique values in tree
def is_subtree(sub_node, node, found_root=False):
  """Check if binary tree sub_node is subtree of node"""
  if sub_node is None and node is None:
    return True
  if sub_node and node is None: # nothing left in tree for subtree
    return False
  if sub_node is None and node: # tree still has children
    return False
  if sub_node.value != node.value:
    if found_root: # assume values do not repeat further down tree
      return False
    else: # keep searching for subtree root in tree
      return is_subtree(sub_node, node.left) or is_subtree(sub_node, node.right)
  else:
    return is_subtree(sub_node.left, node.left, True) and is_subtree(sub_node.right, node.right, True)

def is_perfect(root):
  """Check if binary tree is perfect"""
  def perfect_height(node):
    """Return height of tree if it is perfect, -1 otherwise"""
    if node is None:
      return 0
    if node.left is None and node.right:
      return -1
    if node.left and node.right is None:
      return -1
    left = perfect_height(node.left)
    right = perfect_height(node.right)
    if left == -1 or right == -1:
      return -1
    if left != right:
      return -1
    else:
      return 1 + left # or right
  return perfect_height(root) != -1

#
# 2^n - 1 = 2^(n-1) + ... + 2^1 + 2^0
#
#    0    (2,0)
#   1 2   (2,1)
# 3 4     (2,2)
#
# TODO
def is_perfecti(root):
  """Check if binary tree is pefect, iteratively"""
  if root is None:
    return True
  queue = [root]
  height = 0
  count = 0
  none_found_count = 0
  while len(queue) > 0:
    node = queue.pop(0)
    if node and none_found_count > 0:
      return False
    elif node:
      if node.left and node.right is None:
        return False
      if node.left is None and node.right:
        return False
      if count == pow(2, height):
        height += 1
      count += 1
      queue.append(node.left)
      queue.append(node.right)
    else:
      none_found_count += 1

  return count == pow(2, height) # check if full (and maybe complete), but not perfect

def is_complete(root):
  """Check if binary tree is complete"""
  if root is None:
    return True
  queue = [root]
  saw_first_none = False
  while len(queue) > 0:
    node = queue.pop(0)
    if node is None and not saw_first_none:
      saw_first_none = True
    elif node and saw_first_none:
      return False
    if node:
      queue.append(node.left)
      queue.append(node.right)
  return True

def is_completer(root):
  def complete_height(node):
    """Return height of binary tree if it is complete, -1 otherwise"""
    if node is None:
      return 0
    if node.left is None and node.right:
      return -1
    left = complete_height(node.left)
    right = complete_height(node.right)
    if left == -1 or right == -1:
      return -1
    elif left - right < 0: # right is complete but taller than left
      return -1
    elif left - right > 1: # left is complete but too tall
      return -1
    else:
      return 1 + left # left because it may be taller by 1
  return complete_height(root) != -1


### TODO

def traverse_levelorder(root):
  """Return array of binary tree element in level-order"""
  if root is None:
    return []
  array = []
  queue = [root]
  while len(queue) > 0:
    node = queue.pop(0)
    if node is None:
       array.append(None)
    else:
      array.append(node.value)
      queue.append(node.left)
      queue.append(node.right)
  return array

def create_binary_tree_array(root):
  """Create an array-based binary tree from a linked-based root node"""
  if root is None:
    return []
  array = []
  queue = [root]
  while len(queue) > 0:
    node = queue.pop(0)
    if node is None:
      array.append(None)
    else:
      array.append(node.value)
      queue.append(node.left)
      queue.append(node.right)

  # slice array so there are no unnecessary None's at end
  i = len(array) - 1
  while i >= 0 and array[i] is None:
    i -= 1
  if i != len(array) - 1:
    return array[:i+1]

  return array


def create_binary_tree(array, start=0, stop=None):
  """Create a linked-based binary tree from an array.
  Assume the array represents the tree.
  [0,1,2,3,4,5,6]
      0
    1   2
   3 4 5 6
  """
  if array is None or len(array) < 1:
    return None
  if stop is None:
    stop = len(array)
  if stop - start < 2:
    return None
  left_start = 2 * start + 1
  right_start = 2 * start + 2
  return BSTNode(
    array[start],
    binary_tree(array, left_start, stop),
    binary_tree(array, right_start, stop)
  )


def binary_treei(array):
  array = array.copy() # FIXME
  root_node = None
  for i in range(len(array)):
    l = 2 * i + 1
    r = 2 * i + 2
    array[i] = BSTNode(array[i])
  return root_node

def binary_tree_add(root_node, node):
  """Add a node to a complete linked-based binary tree.
  Returns root node."""
  if root_node == None:
    return node
  elif root_node.left and root_node.right is None:
    root_node.right = node
    return root_node
  elif root_node.left is None:
    root_node.left = node
    return root_node
  else: # FIXME
    return binary_tree_add(root_node.left)
