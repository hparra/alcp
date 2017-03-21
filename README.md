A Little Computer Programming (ALCP)
====================================

(This is WIP)

This is a little workbook on computer programming.
It falls somewhere between beginner and intermediate.
I am not an expert.

This workbook is meant to be followed sequentially.
I recommend Python or Javascript.
If you use a Lisp you will identify things you can skip.

Computer programming is a skill.
Deliberate practice is necessary to improve this skill.
Only with skill and effort can we achieve.

Computer programming is fun.
Enjoy these challenges for what they are.
Forget about everything else.

## Table of Contents

(See doc/)

Dimension 0:
- Math

Dimension 1:
- Arrays
- Strings
- Bit Strings
- Lists
- Queues
- Stacks
- Hash Tables
- Bloom Filters
- Skip Lists

Dimension 1.5:
- Binary Trees
- Binary Heaps
- Binary Search Trees
- General Trees
- Tries

Dimension 2:
- 2D Arrays (Matrices)
- Graphs

## Tips

- Determine function specific features: defaults, etc.
- Determine whether you are mutating source or returning a new object.
  - If you are mutating will you do so in-place?
- Define behavior for 0 or empty list, for each parameter.
- Define behavior for 1 or list with one item, for each parameter.
- Calculate dimension of subarrays within the destination array, if necessary.
  - This is usually a min/max reduction. Go ahead, O(n) is cheap.
- Calculate the dimensions of a destination array ahead of time, if necessary.
  - with language like C you may have to! See `malloc`.
  - if you don't you will need to determine when to create subarrays within a loop
- Determine how you are going to iterate: `for`, `while`?
- Determine if you will iterate over source array or the destination array.
  - One may be easier to think about than the other.

Gotchas:
- Python: `[[]] * num` does weird stuff! Don't use it.

## History

After various failed online, phone, and on-site technical interviews I made this workbook.
It is the culmination of lessons learned the hard way. HGPA
