


class TrieNode(object):
  """Node for a general tree"""
  def __init__(self, value, children=[], is_terminal=False):
    super(TrieNode, self).__init__()
    self.value = value
    childmemo = {}
    if children:
      for node in children:
        childmemo[node.value] = node
    self.children = childmemo
    self.is_terminal = is_terminal

  def add_child(self, child):
    self.children[child.value] = child

  def __str__(self):
    SPACES = "  "
    def f(node, count=0):
      string = str(node.value) + ('*' if node.is_terminal else '')
      if node.children:
        string += "\n"
      for letter, child in node.children.items():
        string += SPACES * count + f(child, count+1) + "\n"
      return string
    return f(self)

#
#
#

def findi(word, root):
  """Find root to word in trie, if it exists"""
  if word is None or word == "":
    return False
  if root is None:
    return False
  node = root
  found_letter = True
  i = 0
  while found_letter and i < len(word):
    found_letter = False
    for child_letter, child in node.children.items():
      if word[i] == child_letter:
        found_letter = True
        if i + 1 >= len(word) and child.is_terminal:
          return True
        else:
          node = child
          break # no need to look at other children
    i += 1
  return False

def find(word, node, start=0, stop=None):
  """Find root to word in trie, if it exists"""
  if node is None:
    return False
  if word is None or word == "":
    return False
  if stop is None:
    stop = len(word)
  if start >= stop:
    return False
  for letter, child in node.children.items():
    if word[start] == letter:
      if start + 1 >= stop and child.is_terminal:
        return True
      else:
        return find(word, child, start + 1, stop)
  return False

def add(word, root=None):
  if word is None or word == "":
    return root # or raise?
  if root is None:
    root = TrieNode(None) # make trie
  node = root
  i = 0
  while i < len(word):
    for letter, child in node.children.items():
      if word[i] == letter:
        if i + 1 >= len(word):
          node.is_terminal = True
          return root
        else:
          node = child
          break
    else: # letter does not yet exist
      child = TrieNode(word[i])
      node.add_child(child)
      if i + 1 >= len(word):
        child.is_terminal = True
        return root
      else:
        node = child
    i += 1
  return root

# def addr(word, node=None, start=0, stop=None):
#   """Add word to trie at node, recursively.
#   Returns root of trie
#   """
#   if word is None or word == "":
#     return None
#   if node is None: # Tricky!
#     node = TrieNode(None)
#   if start + 1 >= stop:
#     return node
#   for i in len(word):
#     for
#       if word[i] == node.value and start + 1 < len(word):
