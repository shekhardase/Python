# Using with block to open python files:-
# Sytax is simple : with open("file_name.txt") as f:

# Advantages of using With block:
"""  (1)Multiple files can be opened.
     (2)The files that are opened together can have different modes.
     (3)Automatically closes file.
     (4)Saves processing power by opening and closing file only when running code inside the block.
     (5)Creates a context manager, so lesser chances of an exception occuring.
"""

with open("Tut 26 part1.py") as f:
    print(f.readlines())
