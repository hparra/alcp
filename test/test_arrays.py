import os
import unittest

from src.arrays import *

class TestFun(unittest.TestCase):

  #
  #
  #

  def test_isempty(self):
    self.assertEqual(True, isempty([]))
    self.assertEqual(False, isempty([1,2]))

  def test_first(self):
    """first(array)"""
    self.assertEqual(1, first([1,2,3]))

  def test_rest(self):
    """rest(array)"""
    self.assertEqual([2,3], rest([1,2,3]))

  def test_push(self):
    self.assertEqual([0,1,2], push([1,2],0))

  #
  #
  #

  def test_repeat(self):
    self.assertEqual([1,1,1,1,1], repeat(1, 5))

  def test_repeatr(self):
    self.assertEqual([1,1,1,1,1], repeatr(1, 5))

  def test_last(self):
    """last(array)"""
    self.assertEqual(3, last([1,2,3]))

  def test_lastr(self):
    """last(array)"""
    self.assertEqual(3, lastr([1,2,3]))

  def test_initial(self):
    """initial(array)"""
    self.assertEqual([1,2], initial([1,2,3]))

  def test_initialr(self):
    """initial(array)"""
    self.assertEqual([1,2], initialr([1,2,3]))

  def test_range(self):
    """range(start,stop,step)"""
    self.assertEqual([0,1,2,3,4], range(5))
    self.assertEqual([1,2,3,4,5], range(1,6))
    self.assertEqual([0,2,4,6,8], range(0,10,2))

  def test_ranger(self):
    """range(start,stop,step)"""
    self.assertEqual([0,1,2,3,4], ranger(5))
    self.assertEqual([1,2,3,4,5], ranger(1,6))
    self.assertEqual([0,2,4,6,8], ranger(0,10,2))

  def test_remove(self):
    self.assertEqual([1,3], remove([1,2,3], 2))
    self.assertEqual([1,2,3], remove([1,2,3], 4))
    self.assertEqual([], remove([], 4))

  def test_remover(self):
    self.assertEqual([1,3], remover([1,2,3], 2))
    self.assertEqual([1,2,3], remover([1,2,3], 4))
    self.assertEqual([], remover([], 4))

  def test_slice(self):
    """slice(array, start, stop, step)"""
    self.assertEqual([1,2,3], slice([0,1,2,3,4],1,4))

  def test_slicer(self):
    """slice(array, start, stop, step)"""
    self.assertEqual([1,2,3], slicer([0,1,2,3,4,5,6],1,4))

  def test_concat(self):
    """concat(*arrays)"""
    self.assertEqual(concat(range(3),range(3)), [0,1,2,0,1,2])

  #
  #
  #

  def test_includes(self):
    self.assertEqual(True, includes([1,2,3], 2))
    self.assertEqual(False, includes([1,2,3], 4))

  def test_includesr(self):
    self.assertEqual(True, includesr([1,2,3], 2))
    self.assertEqual(False, includesr([1,2,3], 4))

  def test_indexof(self):
    self.assertEqual(1, indexof([1,2,3], 2))
    self.assertEqual(-1, indexof([1,2,3], 4))

  def test_indexofr(self):
    self.assertEqual(1, indexofr([1,2,3], 2))
    self.assertEqual(-1, indexofr([1,2,3], 4))

  def test_find(self):
    fn = lambda x: x > 10
    self.assertEqual(20, find([1,20,3], fn))
    self.assertEqual(None, find([1,2,3], fn))

  def test_findr(self):
    fn = lambda x: x > 10
    self.assertEqual(20, findr([1,20,3], fn))
    self.assertEqual(None, findr([1,2,3], fn))

  def test_some(self):
    fn = lambda x: x > 10
    self.assertEqual(True, some([1,20,3], fn))
    self.assertEqual(False, some([1,2,3], fn))

  def test_somer(self):
    fn = lambda x: x > 10
    self.assertEqual(True, somer([1,20,3], fn))
    self.assertEqual(False, somer([1,2,3], fn))

  def test_every(self):
    fn = lambda x: x > 10
    self.assertEqual(True, every([11,20,30], fn))
    self.assertEqual(False, every([1,20,3], fn))

  def test_everyr(self):
    fn = lambda x: x > 10
    self.assertEqual(True, everyr([11,20,30], fn))
    self.assertEqual(False, everyr([1,20,3], fn))

  def test_equals(self):
    self.assertEqual(True, equals([1,2,3], [1,2,3]))
    self.assertEqual(False, equals([1,2,3], [1,3]))

  def test_equalsr(self):
    self.assertEqual(True, equalsr([1,2,3], [1,2,3]))
    self.assertEqual(False, equalsr([1,2,3], [1,3]))

  #
  # Map/Reduce
  #

  def test_filter(self):
    fn = lambda x: x % 2 == 0
    self.assertEqual([0,2,4], filter([0,1,2,3,4], fn))
    self.assertEqual([], filter([1,3,5], fn))

  def test_filterr(self):
    fn = lambda x: x % 2 == 0
    self.assertEqual([0,2,4], filterr([0,1,2,3,4], fn))
    self.assertEqual([], filterr([1,3,5], fn))

  def test_map(self):
    """map(function, array)"""
    self.assertEqual(map(lambda x: x * 2, range(3)), [0,2,4])

  def test_mapr(self):
    self.assertEqual(mapr(lambda x: x * 2, range(3)), [0,2,4])

  def test_reduce(self):
    """reduce(function, array, initial_value)"""
    self.assertEqual(reduce(max, [], 1000), 1000)
    self.assertEqual(reduce(lambda x,y: x+y, range(1,101)), 5050)
    self.assertEqual(reduce(lambda x,y: str(x) + str(y), [1,2,3]), "123")

  def test_reducer(self):
    """reduce(function, array, initial_value)"""
    self.assertEqual(reducer(max, [], 1000), 1000)
    self.assertEqual(reducer(lambda x,y: x+y, range(1,101)), 5050)
    self.assertEqual(reducer(lambda x,y: str(x) + str(y), [1,2,3]), "123")

  def test_reduce_right(self):
    """reduce_right(function, array, initial_value)"""
    self.assertEqual(reduce_right(lambda x,y: str(x) + str(y) , [1,2,3]), "321")

  #
  # A Little Set Theory
  #

  def test_unique(self):
    self.assertEqual([1,2,3], unique([1,2,1,3,2,1]))

  def test_subset(self):
    self.assertEqual(True, subset([1,2,3],[1,2,4,3]))
    self.assertEqual(False, subset([1,2,3],[2,1]))
    self.assertEqual(True, subset([1,2,3],[2,3,1]))
    self.assertEqual(False, subset([1,2,3],[2,3,1], strict=True))

  def test_union(self):
    self.assertEqual([1,2,3,4], union([1,2,1], [3,2,1], [4,2]))

  def test_intersection(self):
    self.assertEqual([2,3], intersection([1,2,3],[2,4,3]))
    self.assertEqual([1], intersection([1,2,3],[2,4,1],[3,4,1]))

  def test_xor(self):
    self.assertEqual([1,4], xor([1,2,3],[2,4,3]))
    self.assertEqual([2,3,4], xor([1,2,3],[2,4,1],[3,4,1]))

  def test_difference(self):
    self.assertEqual([1], difference([1,2,3],[2,4,3]))
    self.assertEqual([], difference([1,2,3],[2,4,1],[3,4,1]))

  #
  # Partitioning
  #

  def test_partition(self):
    fn = lambda x: x % 2 == 0
    self.assertEqual([[2,4],[1,3,5]], partition(fn, [1,2,3,4,5]))

  def test_partition_at_pivot(self):
    comp = lambda a,b: a-b
    array = [2,1,9,8,4,5,7,0,3,6]
    expected = [2,1,3,0,4,5,6,7,8,9]
    self.assertEqual(6, partition_at_pivot(comp, array))
    self.assertEqual(expected, array)

  def test_flatten(self):
    self.assertEqual([0,1,2,3,4,5], flatten([[0,1,2],[3,4,5]]))
    self.assertEqual([0,1,2,3,4,5], flatten([[0,1],[2,3],[4],[5]]))

  def test_groups_of(self):
    self.assertEqual([[1,2,3],[4,5]], groups_of([1,2,3,4,5], 3))

  def test_groups_prioritized(self):
    self.assertEqual([[1,3,5],[2,4]], groups_prioritized([1,2,3,4,5], 2))
    self.assertEqual([[1,4],[2,5],[3]], groups_prioritized([1,2,3,4,5], 3))
    self.assertEqual([[1,5],[2],[3],[4]], groups_prioritized([1,2,3,4,5], 4))
    # self.assertEqual([[1],[2],[3],[4],[5],[]], groups_prioritized([1,2,3,4,5], 6))

  def test_groups(self):
    self.assertEqual([[1,2,3],[4,5]], groups([1,2,3,4,5], 2))
    self.assertEqual([[1,2],[3,4],[5]], groups([1,2,3,4,5], 3))
    self.assertEqual([[1,2],[3],[4],[5]], groups([1,2,3,4,5], 4))
    self.assertEqual([[1],[2],[3],[4],[5],[]], groups([1,2,3,4,5], 6))

  def test_groups_weighted(self):
    array1 = [10, 20, 30, 40, 50, 60, 70, 80, 90]
    expected1_3 = [[10, 20, 30, 40, 50], [60, 70], [80, 90]]
    expected1_5 = [[10, 20, 30, 40], [50, 60], [70], [80], [90]]
    array2 = [568, 712, 412, 231, 241, 393, 865, 287, 128, 457, 238, 98, 980, 23, 782]
    expected2 = [[568, 712, 412], [231, 241, 393, 865], [287, 128, 457, 238, 98], [980, 23, 782]]
    self.assertEqual(expected1_3, groups_weighted(array1, 3))
    self.assertEqual(expected1_5, groups_weighted(array1, 5))
    self.assertEqual(expected2, groups_weighted(array2, 4))
    self.assertEqual([[1],[2],[]], groups_weighted([1,2], 3))

  def test_interleave(self):
    self.assertEqual([0,1,2,3,4,5], interleave([0,2,4],[1,3,5]))
    self.assertEqual([0,1,2,3,4,5], interleave([0,4],[1,5],[2],[3]))

  def test_deinterleave(self):
    self.assertEqual([[0,2,4],[1,3,5]], deinterleave([0,1,2,3,4,5], 2))
    self.assertEqual([[0,3],[1,4],[2,5]], deinterleave([0,1,2,3,4,5], 3))
    self.assertEqual([[0,4],[1,5],[2],[3]], deinterleave([0,1,2,3,4,5], 4))

  def test_zip(self):
    self.assertEqual([[]], zip([]))
    self.assertEqual([[0,1,2]], zip([0,1,2]))
    self.assertEqual([[0,3]], zip([0],[3]))
    self.assertEqual([[0,3],[1,4]], zip([0,1],[3,4]))
    self.assertEqual([[0,3],[1,4],[2,5]], zip([0,1,2],[3,4,5]))
    self.assertEqual([[0,3],[1,4],[2,5]], zip([0,1,2],[3,4,5,6]))

  def test_unzip(self):
    self.assertEqual([[0,3]], unzip([[0,3]]))
    self.assertEqual([[0,1,2],[3,4,5]], unzip([[0,3],[1,4],[2,5]]))
    self.assertEqual([[0,1,2]], unzip([[0,3],[1,4],[2]]))
    self.assertEqual([[0,1,2],[3,4,5]], unzip([[0,3],[1,4],[2,5,8]]))

  #
  # Sorted Lists
  #

  def test_merge_sorted(self):
    self.assertEqual([0,1,2,3,4,5,6,7,8,9], merge_sorted([1,2,4,8,9], [0,3,5,6,7]))
    self.assertEqual([0,1,2,3,4,5,6,7], merge_sorted([1,2,4], [0,3,5,6,7]))
    self.assertEqual([1,2,4,8,9], merge_sorted([1,2,4,8,9], []))
    self.assertEqual([0,3,5,6,7], merge_sorted([], [0,3,5,6,7]))

  def test_binary_search(self):
    self.assertEqual(2, binary_search(2, [0,1,2,3,4,5,6,7,8,9])) # 2 is in [2]
    self.assertEqual(7, binary_search(7, [0,1,2,3,4,5,6,7,8,9]))
    self.assertEqual(-1, binary_search(10, [0,1,2,3,4,5,6,7,8,9]))

  def test_unique_sorted(self):
    self.assertEqual([1,2,3], unique_sorted([1,1,2,2,3]))
    self.assertEqual([1,2,3], unique_sorted([1,1,2,3,3]))
    self.assertEqual([1,2,3], unique_sorted([1,2,2,3,3]))

  #
  # Sorting
  #

  def test_reverse(self):
    array = [1,2,3,4,5]
    expected = [5,4,3,2,1]
    self.assertEqual(expected, reverse(array))

  def test_reverser(self):
    array = [1,2,3,4,5]
    expected = [5,4,3,2,1]
    self.assertEqual(expected, reverser(array))

  def test_reversem(self):
    array = [1,2,3,4,5]
    expected = [5,4,3,2,1]
    reversem(array)
    self.assertEqual(expected, array)

  def test_bubble_sort(self):
    array = [2,1,9,8,4,5,7,0,3,6]
    expected = [0,1,2,3,4,5,6,7,8,9]
    bubble_sort(array)
    self.assertEqual(expected, array)

  def test_selection_sort(self):
    array = [2,1,9,8,4,5,7,0,3,6]
    expected = [0,1,2,3,4,5,6,7,8,9]
    selection_sort(array)
    self.assertEqual(expected, array)

  def test_insertion_sort(self):
    array = [2,1,9,8,4,5,7,0,3,6]
    expected = [0,1,2,3,4,5,6,7,8,9]
    insertion_sort(array)
    self.assertEqual(expected, array)

  def test_quick_sort(self):
    array = [2,1,9,8,4,5,7,0,3,6]
    expected = [0,1,2,3,4,5,6,7,8,9]
    quick_sort(array)
    self.assertEqual(expected, array)

  def test_merge_sort(self):
    array = [2,1,9,8,4,5,7,0,3,6]
    expected = [0,1,2,3,4,5,6,7,8,9]
    self.assertEqual(expected, merge_sort(array))

if __name__ == '__main__':
  unittest.main()
