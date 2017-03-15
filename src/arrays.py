#
#
# - Instead of the pythonic `for i in array` I use while loops
#


# i = 0
# while i < len(array):
#   print array[i]
#   i += 1
#
# for i in range(len(array)):
#   print array[i]
#
# # iterators -- "proper python"
# for i in array:
#   print i


# random()
# Returns float n where 0 <= n < 1
# https://docs.python.org/2/library/random.html
# https://en.wikipedia.org/wiki/Mersenne_Twister
from random import random
import sys
import math

def rangerand(start, stop, count):
  """Return array of C random numbers"""
  array = [] # len = stop - start / count
  i = 0
  while i < count:
    array.append(int(random() * (stop - start)) + start) # randint(a,b)
    i += 1
  return array

#
# Spells for Recursion
#

# nil
def isempty(array):
  return len(array) == 0

# car
def first(array):
  if len(array) < 1:
    return None
  return array[0]

# cdr
def rest(array):
  # return array[1:]
  newarray = [] # len = len(array) - 1
  i = 1
  while i < len(array):
    newarray.append(array[i])
    i += 1
  return newarray

# cons
def push(array, val):
  newarray = []
  newarray.append(val)
  i = 0
  while i < len(array):
    newarray.append(array[i])
    i += 1
  return newarray

def cons(val, array):
  return push(array, val)

#
# Supporting Cast
#

def repeat(val, count):
  newarray = []
  i = 0
  while i < count:
    newarray.append(val)
    i += 1
  return newarray

def repeatr(val, count):
  if count < 1:
    return []
  else:
    return cons(val, repeatr(val, count-1))

def last(array):
  if len(array) < 1:
    return None
  return array[len(array)-1]

def lastr(array):
  if isempty(array):
    return None
  elif isempty(rest(array)):
    return first(array)
  else:
    return lastr(rest(array))

def initial(array):
  newarray = [] # len = len(array) - 1
  i = 0
  while i < len(array) - 1:
    newarray.append(array[i])
    i += 1
  return newarray

def initialr(array):
  if isempty(array):
    return []
  elif isempty(rest(array)):
    return []
  else:
    return cons(first(array), initialr(rest(array)))

def remove(array, val):
  newarray = []
  i = 0
  while i < len(array):
    if array[i] != val:
      newarray.append(array[i])
    i += 1
  return newarray

def remover(array, val):
  if isempty(array):
    return array
  elif first(array) == val:
    return rest(array)
  else:
    return push(remover(rest(array),val), first(array))

def range(*args):
  """Return array [start...stop]"""
  start = 0
  step = 1
  if len(args) == 3:
    start,stop,step = args
  elif len(args) == 2:
    start,stop = args
  elif len(args) == 1:
    stop = args[0]
  else:
    raise TypeError("Wrong number of arguments!")
  array = []
  i = start
  while i < stop:
    array.append(i)
    i += step
  return array

def ranger(*args):
  start = 0
  step = 1
  if len(args) == 3:
    start,stop,step = args
  elif len(args) == 2:
    start,stop = args
  elif len(args) == 1:
    stop = args[0]
  else:
    raise TypeError("Wrong number of arguments!")
  if start >= stop: # do not include stop
    return []
  else:
    return cons(start, ranger(start + step, stop, step))

def slice(array, start, stop, step=1):
  """Return portion or array"""
  newarray = [] # len = stop - start / step
  i = start
  while i < stop:
    newarray.append(array[i])
    i += step
  return newarray

def slicer(array, start, stop, step=1):
  if isempty(array):
    return []
  elif start >= stop:
    return []
  elif start == 0:
    return cons(first(array), slicer(rest(array), start, stop-step, step))
  else:
    return slicer(rest(array), start-step, stop-step, step)

#
# Reversing
#

def reverse(array):
  newarray = []
  i = 0
  while i < len(array):
    newarray.append(array[len(array) - 1 -i])
    i += 1
  return newarray

def reverser(array):
  if isempty(array):
    return array
  else:
    return cons(last(array), reverser(initial(array)))

def reversem(array):
  for i in range(len(array) / 2): # implicit floor
    j = len(array) - i - 1
    array[i], array[j] = array[j], array[i]

#
#
#

def includes(array, val):
  i = 0
  while i < len(array):
    if array[i] == val:
      return True
    i += 1
  return False

def includesr(array, val):
  if isempty(array):
    return False
  elif first(array) == val:
    return True
  else:
    return includesr(rest(array), val)

def indexof(array, val):
  i = 0
  while i < len(array):
    if array[i] == val:
      return i
    i += 1
  return -1

def indexofr(array, val, index=0):
  if isempty(array):
    return -1
  elif first(array) == val:
    return index
  else:
    return indexofr(rest(array), val, index + 1)

def find(array, fn):
  i = 0
  while i < len(array):
    val = array[i]
    if fn(val):
      return val
    i += 1
  return None

def findr(array, fn):
  if isempty(array):
    return None
  elif fn(first(array)):
    return first(array)
  else:
    return findr(rest(array), fn)

def some(array, fn):
  i = 0
  while i < len(array):
    val = array[i]
    if fn(val):
      return True
    i += 1
  return False

def somer(array, fn):
  if isempty(array):
    return False
  elif fn(first(array)):
    return True
  else:
    return somer(rest(array), fn)

def every(array, fn):
  i = 0
  while i < len(array):
    val = array[i]
    if not fn(val):
      return False
    i += 1
  return True

def everyr(array, fn):
  if isempty(array):
    return True
  elif fn(first(array)):
    return everyr(rest(array), fn)
  else:
    return False

def equals(array1, array2):
  if len(array1) != len(array2):
    return False
  else:
    for i in range(len(array1)):
      if array1[i] != array2[i]:
        return False
    return True

def equalsr(array1, array2):
  if isempty(array1) and isempty(array2):
    return True
  elif first(array1) != first(array2):
    return False
  else:
    return equalsr(rest(array1), rest(array2))

#
#
#

def filter(array, fn):
  newarray = []
  i = 0
  while i < len(array):
    if fn(array[i]):
      newarray.append(array[i])
    i += 1
  return newarray

def filterr(array, fn):
  if isempty(array):
    return array
  elif fn(first(array)):
    return cons(first(array), filterr(rest(array), fn))
  else:
    return filterr(rest(array), fn)

def map(fn, array):
  newarray = [] # len(array)
  i = 0
  while i < len(array):
    newarray.append(fn(array[i]))
    i += 1
  return newarray

def mapr(fn, array):
  if isempty(array):
    return array
  else:
    return cons(fn(first(array)), mapr(fn, rest(array)))

# min/max are just reduce(min, array), etc.
def reduce(fn, array, initial=None):
  """Reduce the array"""
  if initial:
    i = 0
    ans = initial
  elif len(array) >= 2:
    i = 1
    ans = array[0]
  else:
    raise TypeError("Invalid call?")
  while i < len(array):
    ans = fn(ans, array[i])
    i += 1
  return ans

def reducer(fn, array, initial=None):
  if isempty(array):
    return initial
  elif initial is None and isempty(rest(rest(array))):
    return fn(first(array), first(rest(array)))
  else:
    return fn(first(array), reducer(fn, rest(array), initial))

def reduce_right(fn, array, initial=None):
  """Reduce the array form the right"""
  lenarray = len(array)
  if initial:
    i = lenarray - 1
    ans = initial
  elif len(array) >= 2:
    i = lenarray - 2
    ans = array[lenarray - 1]
  else:
    raise TypeError("Invalid call?")
  while i >= 0:
    ans = fn(ans, array[i])
    i -= 1
  return ans

# stable
def unique(array):
  memo = {}
  newarray = [] # len = unknown but <= len(array)
  i = 0
  while i < len(array):
    if array[i] not in memo:
      memo[array[i]] = i
      newarray.append(array[i])
    i += 1
  return newarray

def subset(a,b, strict=False):
  """Is A a subset of B?"""
  if len(a) > len(b) or (strict and len(a) == len(b)):
    return False
  memo = {}
  i = 0
  while i < len(b):
    val = b[i]
    memo[val] = val
    i += 1
  i = 0
  while i < len(a):
    val = a[i]
    if val not in memo:
      return False
    i += 1
  return True

def union(*arrays):
  memo = {}
  newarray = []
  i = 0
  while i < len(arrays):
    j = 0
    while j < len(arrays[i]):
      val = arrays[i][j]
      if val not in memo:
        memo[val] = val # value can be anything
        newarray.append(val)
      j += 1
    i += 1
  return newarray

# assumes arrays are sets (no repeated values)
def intersection(*arrays):
  memo = {}
  i = 0
  while i < len(arrays):
    j = 0
    while j < len(arrays[i]):
      val = arrays[i][j]
      if val not in memo:
        memo[val] = 1
      else:
        memo[val] += 1
      j += 1
    i += 1
  newarray = []
  for k in memo:
    if memo[k] == len(arrays):
      newarray.append(k)
  return newarray

# TODO: Not sure if this ia proper definition of multi-XOR
def xor(*arrays): # aka symmetric difference
  memo = {}
  i = 0
  while i < len(arrays):
    j = 0
    while j < len(arrays[i]):
      val = arrays[i][j]
      if val not in memo:
        memo[val] = 1
      else:
        memo[val] += 1
      j += 1
    i += 1
  newarray = []
  for k in memo:
    if memo[k] != len(arrays):
      newarray.append(k)
  return newarray

# A - B - C
def difference(*arrays):
  if arrays is None or len(arrays) == 0:
    return arrays # None or []
  if len(arrays) == 1:
    return arrays[0] # identity: A - 0
  memo = {}
  i = 0
  while i < len(arrays):
    j = 0
    while j < len(arrays[i]):
      val = arrays[i][j]
      if i == 0: # first set -- add to memo
        memo[val] = val
      elif val in memo: # set to subtract from first
        del memo[val]
      j += 1
    i += 1
  newarray = []
  for k in memo:
    newarray.append(k)
  return newarray

#
# Partitioning
#



def partition(fn, array):
  newarray = [[],[]]
  for i in range(len(array)):
    b = fn(array[i]) # boolean
    newarray[int(not b)].append(array[i])
  return newarray

# TODO: move me
def partition_at_pivot(comp, array, start=0, stop=None):
  if stop is None:
    stop = len(array)
  if start >= stop:
    return # nothing to do
  pivot = array[stop-1]
  l = start    # left
  r = stop - 1 # right
  while l < r:
    while comp(array[l], pivot) < 0:
      l += 1
    while comp(array[r], pivot) > 0:
      r -= 1
    array[r], array[l] = array[l], array[r]
  return l # or r -- they're both on the pivot

# TODO: recursion
def flatten(array):
  newarray = []
  i = 0
  while i < len(array):
    j = 0
    while j < len(array[i]): # check me
      newarray.append(array[i][j])
      j += 1
    i += 1
  return newarray

# I first solved with two arrays first, iterating over destination
def groups_of(array, item_count):
  newarray = []
  i = 0
  # chunks = math.ceil(len(array) / float(item_count)) # e.g. pages
  # while i < chunks:
  #   newarray.append([])
  #   j = 0
  #   offsetj = i * item_count
  #   while j < item_count and offsetj + j < len(array):
  #     newarray[i].append(array[offsetj + j])
  #     j += 1
  #   i += 1
  while i < len(array):
    array_num = i / item_count # implicit floor
    if i % item_count == 0: # start new chunk
      newarray.append([])
    newarray[array_num].append(array[i])
    i += 1
  return newarray

def groups_prioritized(array, count):
  newarray = []
  i = 0
  while i < len(array):
    if i < count:
      newarray.append([])
    newarray[i % count].append(array[i])
    i += 1
  return newarray

# This one was hard
# first solved with left-leaning fairwork but interleaved
def groups(array, count):
  newarray = []
  i = 0
  j = 0
  while i < count:
    # after fillin a group you calculate new group len based on what REMAINS
    items_rem = len(array) - j
    groups_rem = count - i
    group_len = int(math.ceil(items_rem / float(groups_rem)))
    newarray.append([])
    k = 0
    while j < len(array) and k < group_len:
      newarray[i].append(array[j])
      j += 1
      k += 1
    i += 1
  return newarray

def groups_weighted(array, count):
  if len(array) < 1:
    return []
  elif count < 1:
    return []
  elif count > len(array):
    return map(lambda x: [x], array) + [[]] * (count - len(array))
  elif count == 1:
    return [array]
  else:
    group = [] # group with lowest max weight
    group_diff = None # NOTE: lowest diff between max weight and min weight
    i = 1
    while i <= len(array) - count + 1: # TODO: WHY +1?
      potential_group = [array[0:i]] + groups_weighted(array[i:], count-1)
      potential_group_values = map(lambda a: sum(a), potential_group)
      potential_group_diff = max(potential_group_values) - min(potential_group_values)
      if group_diff is None or potential_group_diff < group_diff:
        group = potential_group
        group_diff = potential_group_diff
      i += 1
    return group

# TODO: def groups_weightedb(array, count): # bottom-up


def interleave(*arrays):
  if arrays is None or len(arrays) == 0:
    return arrays # None or []
  if len(arrays) == 1:
    return arrays[0] # identity

  # find len of largest sub-array
  # my reduce does not support sets, of which *arrays is
  # maxj = reduce(lambda p,c: max(p, len(c)), arrays, 0)
  maxj = 0
  i = 0
  while i < len(arrays):
    maxj = max(maxj, len(arrays[i]))
    i += 1

  newarray = []
  j = 0
  while j < maxj:
    i = 0
    while i < len(arrays):
      if j < len(arrays[i]):
        val = arrays[i][j]
        newarray.append(val)
      i += 1
    j += 1
  return newarray

def deinterleave(array, array_count):
  if array_count < 1:
    raise TypeError("Array count needs to be > 1")
  if array_count == 1:
    return array
  # newwarray = []
  newarray = [[] for i in range(array_count)]
  i = 0
  while i < len(array):
    array_num = i % array_count
    # if array_num >= len(newarray):
      # newarray.append([])
    newarray[array_num].append(array[i])
    i += 1
  return newarray

def zip(*arrays):
  if len(arrays) < 1:
    return None
  if len(arrays) < 2:
    return [arrays[0]]
  newarray_len = reduce(lambda p,c: min(p, len(c)), arrays, sys.maxint)
  newsubarray_len = len(arrays)
  newarray = [] # newarray = [None] * newarray_len
  for i in range(newarray_len):
    if len(newarray) - 1 < i: # newarray is None
      newarray.append([]) # newarray[i] = [None] * subarray_len
    for j in range(newsubarray_len):
      val = arrays[j][i]
      newarray[i].append(val) # newarray[i][j] = arrays[j][i]
  return newarray

def unzip(array):
  if len(array) < 1:
    return None
  if len(array) < 2:
    return [array[0]]
  newarray_len = reduce(lambda p,c: min(p, len(c)), array, sys.maxint)
  newsubarray_len = len(array)
  newarray = [None] * newarray_len
  for i in range(newarray_len):
    if newarray[i] is None:
      newarray[i] = [None] * newsubarray_len
    for j in range(newsubarray_len):
      newarray[i][j] = array[j][i]
  return newarray

def concat(*args):
  """Return concatenations of arrays"""
  array = []
  if len(args) == 0:
    return array
  i = 0
  while i < len(args):
    j = 0
    while j < len(args[i]):
      array.append(args[i][j])
      j += 1
    i += 1
  return array

#
# Sorted Lists
#

def unique_sorted(array):
  """ Return array with duplicates removed.
  Input array is already sorted.
  """
  if len(array) < 2:
    return array
  i = 0
  j = 0
  newarray = []
  while i < len(array) - 1:
    if array[i] != array[i+1]:
      newarray.append(array[i])
    i += 1
  newarray.append(array[i]) # always append last one
  return newarray

def merge_sorted(left, right):
  i = 0
  j = 0
  newarray = []
  while i < len(left) and j < len(right):
    if left[i] > right[j]:
      newarray.append(right[j])
      j += 1
    else:
      newarray.append(left[i])
      i += 1
  while i < len(left):
    newarray.append(left[i])
    i += 1
  while j < len(right):
    newarray.append(right[j])
    j += 1
  return newarray

def binary_search(val, array, start=0, stop=None):
  if stop == None:
    stop = len(array)
  if len(array) < 1:
    return -1
  if stop - start <= 1:
    return -1
  middle = (stop - start) // 2 + start
  if array[middle] == val:
    return middle
  elif val < array[middle]:
    return binary_search(val, array, start, middle)
  else:
    return binary_search(val, array, middle, stop)

#
# Sorting
#

def bubble_sort(array):
  did_swap = False
  for i in range(len(array)-1):
    for j in range(len(array)-1):
      if array[j+1] < array[j]:
        array[j], array[j+1] = array[j+1], array[j]
        did_swap = True
    if not did_swap: # no swaps = sorted
      break

def selection_sort(array):
  for i in range(len(array)):
    mini = i
    for j in range(i+1, len(array)):
      if array[j] < array[mini]:
        mini = j
    if i != mini:
      array[i], array[mini] = array[mini], array[i]

def insertion_sort(array):
  for i in range(1, len(array)):
    j = i
    while j > 0 and array[j] < array[j-1]:
      array[j-1], array[j] = array[j], array[j-1]
      j -= 1

def quick_sort(array, start=0, stop=None):
  if stop is None:
    stop = len(array)
  if start >= stop-1: # single or no element
    return
  else:
    l = partition_at_pivot(lambda x,y: x-y, array, start, stop)
    quick_sort(array, start, l)
    quick_sort(array, l, stop)

def merge_sort(array):
  if len(array) < 2:
    return array
  middle = len(array) // 2
  left = merge_sort(array[0:middle])
  right = merge_sort(array[middle:])
  return merge_sorted(left, right)



# In-Place Merge Sort _is_ a thing,
# but it is very complex
# http://stackoverflow.com/questions/2126219/how-to-merge-two-sorted-integer-array-in-place-using-on-time-and-o1-space-co
#
# def merge_sort(array, start=0, stop=None): # mutates
#   if len(array) < 2:
#     return
#   if stop == None:
#     stop = len(array)
#   if start >= stop-1:
#     return
#   middle = (stop - start) // 2 + start
#   merge_sort(array, start, middle)
#   merge_sort(array, middle, stop)
#   merge_inplace(array, start, middle, stop)
#
# def merge_inplace(array, start, middle, stop):
#   if len(array) < 2:
#     return
#   if stop-start < 1: # [0]
#     return
#   # [0,1]
#   i = start
#   j = middle
#   # THIS IS WRONG -- SEE NOTES ABOVE
#   while i < middle and j < stop:
#     if array[i] > array[j]:
#       array[i], array[j] = array[j], array[i]
#       j += 1
#     else:
#       i += 1
