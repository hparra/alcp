# Matrices

## Note regarding Space Matrices

for any `[M][N]` array (Rows x Columns)

```python
# assuming array[m][n]
for m in xrange(array): # rows
  for n in xrange(array[m]): # columns
    print array[m][n]  
```

```

1 x N = [1,2,3]
M x 1 = [
  [1],
  [2],
  [3],
]


The problem with this is that it 

How we usually think of arrays in code:
[
  [1,2,3],
  [4,5,6]
  [7,8,9]
]

Translates to these [M][N] pairs:
[
  [(0,0),(0,1),(0,2)],
  [(1,0),(1,1),(1,2)],
  [(2,0),(2,1),(2,2)],
]

If the center is the origin then move like this.
[
  [(-1,-1),(-1,0),(-1,+1)],
  [( 0,-1),( 0,0),( 0,+1)],
  [(+1,-1),(+1,0),(+1,+1)],
]

```


Just picture the matrix!
- FORGET the Cartesian plane! this is Column x Row with origin at bottom-left
- FORGET the image plane! this is column Column x Row with origin at top-left
- FORGET latitude and longitude. I can't even remember which is which or how it works!

See https://en.wikipedia.org/wiki/Row-_and_column-major_order
