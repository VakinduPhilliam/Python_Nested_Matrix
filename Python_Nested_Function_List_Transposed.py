# Python Nested Function List Comprehensions
# The initial expression in a list comprehension can be any 
# arbitrary expression, including another list comprehension.
# Consider the following example of a 3x4 matrix implemented 
# as a list of 3 lists of length 4:

matrix = [
          [1, 2, 3, 4],
           [5, 6, 7, 8],
            [9, 10, 11, 12],
  ]

transposed = []
    for i in range(4):

        # the following 3 lines implement the nested listcomp

        transposed_row = []

          for row in matrix:
            transposed_row.append(row[i])
            transposed.append(transposed_row)

transposed
