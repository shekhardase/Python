"""
# Range :- to loop through a set of code a specified number of times, we can use the range() function,
            range function returns sequence of numbers, starting from 0 by default and
            increment by 1 and ends at a specific number.
"""

for x in range(0,4):
    print(x)
for i in range(4,0,-1):
    print(i)
for y in range(1,31,1):
    print("*"*y)


"""
range() function defaults to 0 as a starting value, however it is possible to specify the starting value by adding a parameter:
 range(2,6) ,which means values from 2 to 6 (but not including 6)
 """

"""
The range has default increment by 1 however it is possible to change / specify increment value by adding a third parameter :
range(2,30,3) here value starts from 2 and end at 30 but with gap of 3 (LAST VALUE 29)
"""