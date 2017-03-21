# Arrays

**Essential Functions:**
  - [x] `isempty` (null?)
  - [x] `first` (car)
  - [x] `rest` (cdr)
  - [x] `push` (cons)
  - [ ] `inc` (add1)
  - [ ] `dec` (sub1)

**More Basic Stuff:**
  - `repeat`
    - [x] recursive
    - [x] iterative
  - `last`
    - [x] recursive
    - [x] iterative
  - `initial`
    - [x] recursive
    - [x] iterative
  - `range`
    - [x] recursive
    - [x] iterative
  - `remove`
    - [x] recursive
    - [x] iterative
  - `slice`
    - [x] recursive
    - [x] iterative
  - `middle`
    - [ ] recursive
    - [ ] iterative

**Reversing**
  - `reverse`
    - [x] recursive
    - [x] iterative + pure
    - [x] iterative + in-place
  
**Using Linear Search**
  - `indexof`
    - [x] recursive
    - [x] iterative
  - `includes`
    - [x] recursive
    - [x] iterative
  - `find`
    - [x] recursive
    - [x] iterative
  - `some`
    - [x] recursive
    - [x] iterative
  - `every`
    - [x] recursive
    - [x] iterative
  - `equals`
    - [x] recursive
    - [x] iterative
  - `issorted`
    - [ ] recursive
    - [ ] iterative
    
**Intro to Map/Reduce**
  - `filter`
    - [x] recursive
    - [x] iterative
  - `map`
    - [x] recursive
    - [x] iterative
  - `reduce` (fold)
    - [x] recursive
    - [x] iterative
  - `reduceRight`
    - [ ] recursive
    - [x] iterative

**Partitioning**
  - `flatten`
    - [ ] recursive
    - [x] iterative
  - `partition`
    - [ ] recursive
    - [x] iterative
  - `interleave`
    - [ ] recursive
    - [x] iterative
  - `deinterleave`
    - [ ] recursive
    - [x] iterative
  - `zip`
    - [ ] recursive
    - [x] iterative
  - `unzip`
    - [ ] recursive
    - [x] iterative
  - `groups_of`
    - [ ] recursive
    - [x] iterative
  - `groups_prioritized`
    - [ ] recursive
    - [x] iterative
  - `groups`
    - [ ] recursive
    - [x] iterative
  - `groups_weighted`
    - [ ] recursive
    - [x] iterative
  - `partition_at_pivot`
    - [ ] recursive
    - [x] iterative
  - `concat`
    - [ ] recursive
    - [x] iterative

**Working with a Sorted List**
  - [x] unique_sorted
  - [x] merge_sorted
  - [x] binary_search

**Sorting**
  - [x] bubble_sort
  - [x] selection_sort
  - [x] insertion_sort
  - [x] quick_sort
  - [x] merge_sort

**A Little Set Theory (Part 1?)**
  - `unique` (set)
    - [ ] recursive
    - [x] iterative
  - `subset`
    - [ ] recursive
    - [x] iterative
  - `union`
    - [ ] recursive
    - [x] iterative
  - `intersection`
    - [ ] recursive
    - [x] iterative
  - `xor` (symmetric difference)
    - [ ] recursive
    - [x] iterative
  - `difference`
    - [ ] recursive
    - [x] iterative
  - `combinations`
    - [ ] recursive
    - [ ] iterative
  - `permutations`
    - [ ] recursive
    - [ ] iterative
  - `powerset`
    - [ ] recursive
    - [ ] iterative

- Some Statistics
  - [ ] sample
  - [ ] mean
  - [ ] medium
  - [ ] mode
  - [ ] shuffle
- Extra
  - [ ] unique_chunk
  - [ ] sorted_unique
- (IDK where to put these yet)
  - [ ] bucket_sort
  - [ ] radix_sort
  
---

### Essential Functions

Write these basic functions but don't forget them!

`isarray(obj)`
  - return whether the obj is an array
  - e.g. `isarray(1) = False`

`isempty(array)`
  - return whether the array is empty
  - e.g. `isempty([]) = True`
  - aka _null?_

`first(array)`
  - return first element of the array
  - e.g. `first([1,2,3]) = 1`
  - What should we return if the array is empty?
  - aka _car_

`rest(array)`
  - return the array with the first element removed
  - e.g. `rest([1,2,3]) = [2,3]` 
  - What if there is only one item?
  - What if there are no items?
  - Built into Python as `array[1:]`
  - aka _cdr_

`push(val, array)`
  - return copy of array with val prepended to it
  - e.g. `push([1,2], 0) = [0,1,2]`
  - aka _cons_
  - in fact, name this function `cons` instead

### Useful Functions

`repeat(val, count)`
  - return an array with count elements of val 
  - e.g. `repeat(1, 5) = [1,1,1,1,1]`

`last(array)`
  - return last element of the array
  - e.g. `last([1,2,3]) = 3`
  - What should we return if the array is empty?

`initial(array)`
  - return the array with the last element removed
  - e.g. `initial([1,2,3]) = [1,2]`
  - What if there is only one item?
  - What if there are no items?
  - Built into Python as `array[:-1]`

`range(start, stop, step=1)`
  - return an array consisting of sequential numbers starting at start and ending at (but not including) stop, incrementing by step each time
  - e.g. `range(1,5,1) = [1,2,3,4]`

`remove(array, val)`
  - return a new array with the first instance of val removed, if it exists
  - e.g. `remove([1,2,3,2,1], 2) = [1,3,2,1]`

`slice(array, start, stop, step=1)`
  - return a new subarray of array consisting of elements starting at start and ending at (but not including) stop, incrementing by step each time
  - e.g. `slice([1,2,3,4],1,3) = [2,3]`

Now implement all of these recursively without using loops.
Use the _Essential Functions_.
You do not need to know the length of the array!

### Reversing

`reverse(array)`
  - reverse the array!
  - e.g. `reverse([1,2,3,4,5]) = [5,4,3,2,1]`

Please do this three ways:
  - iteratively, returning a new array
  - recursively, returning a new array
  - iteratively, mutating the original array
      
```python
# python example for testing mutation
array = [1,2,3,4,5]
expected = [5,4,3,2,1]
reverse(array) # doesn't return a value but mutates array
self.assertEqual(expected, array)
```
  
**From here on out please implement each function twice: iteratively and recursively!**

### Linear Search

- indexOf
- includes
- find
- some
- every
- equal

### Map/Reduce

- filter
- map:          `array = map(function, array)`
- reduce:       `value = reduce(function, array, initial_value)`
- reduceRight:  `value = reduce_right(function, array, initial_value)`

Use `reduce` to calculate some common reductions:
  - sum
  - min/max
  - includes
  - some
  - every
  - factorial
  - gcd

Noticing a recurring theme here? 😂

`filter_weighted`

### Partitioning

This is a challenging group. No joke intended.

`flatten(array)`
  - flatten an array of arrays into a single array
  - e.g. `flatten([[0,1],[2],[3,4,5]]) = [0,1,2,3,4,5]`
  - e.g. "flatten this paged data into a single array"
  - What happens if a subarray has arrays too?
    - e.g. `flatten([[0,[1]],[2],[3,[4],5]]) = [0,1,2,3,4,5]`

`partition(fn, array)`
  - partition an array into array of two arrays using predicate function
  - e.g. `partition(lambda x: x % 2 == 0, [1,2,3,4,5]) = [[2,4],[1,3,5]]`

`partition_at_pivot(fn, array)`
  - partition an array in-place such that when some value is selected from the array:
    - all other values less than it are to the left
    - all other values greater than it are to the right
    - the value itself is in it's proper location should the array be sorted
  - e.g. `partition(lambda a,b: a-b, [2,1,9,8,4,5,7,0,3,6]) = [2,1,3,0,4,5,6,7,8,9]`
  - ```python
    # python example test
    comp = lambda a,b: a-b
    array = [2,1,9,8,4,5,7,0,3,6]
    expected = [2,1,3,0,4,5,6,7,8,9]
    self.assertEqual(6, paritition_at_pivot(comp, array))
    self.assertEqual(expected, array)
    ```

`groups_of(array, n)`
  - partition an array into an array of arrays with n items each
  - e.g. `groups_of([1,2,3,4,5], 3) = [[1,2,3],[4,5]]`
  - e.g. "paginate with each page having n items"
  - also known as _paginate_ or _chunk_
  - What happens when not every array can have n items?
  - You may have programmed this by iterating over either the source or the destination. Now try it the other way. Which looks better?

`groups_prioritized(array, n)`
  - partition a prioritized array into an array of n prioritized arrays
  - e.g. `groups([1,2,3,4,5], 3) = [[1,4],[2,5],[3]]`
  - e.g. "split m prioritized jobs amongst n workers"

`groups(array, n)`
  - partition an array into an array of n arrays
  - e.g. `groups([1,2,3,4,5], 3) = [[1,2],[3,4],[5]]`
  - e.g. "split items into n columns (left to right)"
  - if n > length of array then include empty arrays
  - aka _groups_sequential_
  - I found this one difficult!

`interleave(*arrays)`
  - interleaves two or more arrays and into single array
  - e.g. `interleave([0,2,4],[1,3,5]) = [0,1,2,3,4,5]`

`deinterleave(array, n)`
  - deinterleave an array into an array of n arrays
  - e.g. `deinterleave([0,1,2,3,4,5], 2) = [[0,2,4],[1,3,5]]`

`zip(*arrays)`
  - interleave m arrays with n items and return array of n arrays with m items
  - e.g. `zip([0,1,2],[3,4,5]]) = [[0,3],[1,4],[2,5]]`
  - think of "zipper"
  - technically also _transpose_
  - similar to _interleave_
  - What happens if there is only one subarray?
  - What happens when subarrays are not equal size, e.g. `[0,1,2],[3,4,5,6]`?

`unzip(array[])`
  - deinterleave array of n array with m items into array of m arrays with n items
  - e.g. `unzip([[0,3],[1,4],[2,5]]) = [[0,1,2],[3,4,5]]`
  - What happens if there is only one subarray?
  - What if happens when subarrays are not equal size, e.g. `[[0,3],[1,4],[2]]`?
  
This last one is special!

`groups_balanced(array, n)`
  - partition a weighted array into an array of n arrays such that total weights are relatively balanced
  - e.g. `groups_balanced([1,2,3,4,5,6,7,8,9], 3) = [[1,2,3,4,5],[6,7],[8,9]]`
  - e.g. "split work sequentially and fairly amongst n workers"

### Sorted Lists

- unique
- binary_search
- sorted_merge
- sorted_unique
- sorted_intersection
- mean 
- median
- mode

### Sorting

All these should mutate the array, i.e. do the work in-place.

Use the following arrays to test:
  ```
  actual = [2,1,9,8,4,5,7,0,3,6]
  expected = [0,1,2,3,4,5,6,7,8,9]
  ```

`bubble_sort(array)`
  - sort the array by comparing each pair of items and swapping them if necessary
  - At most how many times do you need to do this? (worst-case scenario)
  - How do you know when array is sorted?
  
`selection_sort(array)`
  - sort the array by:
    - selecting the left-most value
    - searching the remaining items for the smallest value
    - swapping the left-most value and smallest value
    - repeating by selecting the second left-most value, etc.

`insertion_sort(array)`
  - "card sort"
  - sort the array by:
    - selecting the first two adjacent values
    - swapping them if necessary

The following two are naturally recursive.
They can be implemented iteratively but it's easier to understand them recursively,
and they are generally implemented as such.
Come back and implement iteratively later.
    
`quick_sort`
  - sort the array by:
    - selecting a pivot and partitioning the array at that pivot (rememeber `partition_at_pivot`)
    - calling quicksort again on each of the two partitions

Merge sort should _not_ be done in-place.
Create a new array.
You _could_ mergesort in-place but that's above and beyond this workbook.

`merge_sort`
  - sort the array by:
    - calling merge_sort on each half of the array
    - merging each list in order

### Set Theory

A _set_ is an unordered collection of unique items.
In other words, there are no duplicates.
Hint: Dictionaries can help you remember things!

- unique (set)
- subset
- union
- intersection
- xor
- difference
