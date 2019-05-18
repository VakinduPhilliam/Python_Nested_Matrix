# Python Nested List Comprehensions
# In the real world, you should prefer built-in functions to complex flow statements. 
# The zip() function would do a great job for this use case:

matrix = [
        [1, 2, 3, 4],
         [5, 6, 7, 8],
          [9, 10, 11, 12],
   ]

list(zip(*matrix))
