#LEARNING LOG


````

2020-08-10

Planning for next day

1. Extension of board (old board)
	-[T, L, D, B]

	[T, L, B, D]

	return list

2. Arrangement (board)
	Based on the list, we expand the board

	D - row + 1
	R - column + 1
	L - column + 1, all column values will add up + 1
	T - row + 1, all row values will add up + 1


	return new board with rearranged.



new generation(new board)
	
	return updated_new_board	

print

2020-07-08

- How to automate trivial task using Makefile
- [Vishva] Confusion about representation of matrix, (rows/column)
- Abstraction of classes 

2020-07-07

- Test Cases name start with "test"
- A class without instantiating objects are static class
- How to make enums

2020-07-05

- Issue in initializing 2D matrix in python 
- Changing one value of cell, changes entire columns
    >>> a = [[0]*3]*3
    >>> a[1][1] = 3
    >>> a
    [[0, 3, 0], [0, 3, 0], [0, 3, 0]]
- No use in writing tests for getter and setter
- Google Meet has serious issues
- Design before writing code

2020-07-04

- import class from a different directory
https://stackoverflow.com/questions/4383571/importing-files-from-different-folder

2020-06-29

- Use aliases for speed up the things
e.g switch [github_username] to switch between different github users

- how to write unit test in python 
https://www.youtube.com/watch?v=1Lfv5tUGsn8
python3 -m unittest [filename].py
````