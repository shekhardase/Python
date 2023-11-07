# F strings

# me = "Harry"
# a1=3
# a = "this is %s %s"%(me, a1)
# print(a)


# F Strings and String Formatting In Python :
"""    string formatting is used to design the string using formatting techniques provided by the particular programming language.
    From the % formatting to format() method, to format string literals, there is no limit as to potential of string crafting.
    There are four significant ways to do string formatting in Python.
"""

#1 string formatting (% Operator):-
"""
  Python has built-in operation that we can access with the % operator. This will help us to do simple positional formatting.
  In Python, we can perform string formatting using the % operator.
  The problem with this method when we have to deal with large strings.
  If we specify the wrong type of input type operator, then it will throw an error.
  For example , %d will throw a TypeError if input is not an integer  
 """
# eg:
name = "Jack"
n = " My name is %s" %name
print(n)

#2 Using Tuple():
""" 
 The string formatting syntax, which uses % operator changes slightly if we want to make multiple substitutions in single string.
  The %operator takes only one argument, to mention more than multiple argument, use tuple.
  Tuples are better than using the old formatting string method. However, it is not an ideal way to
  deal with large strings. 
"""
# eg:
name = "Jack"
Class = 3
s="%s is in class %d" %(name,Class)
print(s)

#3 String formatting (str.format)
"""
Python 3 introduced a new way to do string formatting. format() string formatting method eliminates the % operator special syntax and makes the syntax
for string formatting more regular. str.format() allows multiple substitutions and value formatting. We can use format() to do simple positional formatting,
just like you could with old-style formatting.

In str.format(), we put one or more replacement fields and placeholders defined by pair of curly braces{} into string.
This string formatting is preferred over %-style formatting. Using the format() method, we can deal ith large strings, and the code will become more readable

# Syntax: {}.format(values)
"""

# eg:
str = "This article is written in {}"
print (str.format("Python"))


#4 Using f-strings (f):
"""
Pyhton added a new string formatting approach called formatting string literals or "f-strings". 
This is new way of formatting strings. A much more simple and intuitive solution is use of Formatting string literals. F-string has easy syntax as compared to previous 
string formatting of python. They are indicated by an "f" before the first quotation mark of string. Purt the expression inside{} To evaulate the result.
"""

# eg :
str1 = "Python "
str2 = "Programming"
print(f"Welcome to our {str1}{str2} tutorial")

# Time module:-
"""The time module provides time related functions. It handles the time related tasks.
To use functions that are defined in this module, we need to import the module first.
It is mostly used in measuring the time elapsed during program execution.
"""
import math
me = "Harry"
a1 = 3
a = f"this is {me} {a1} {math.cos(65)}"
print(a)
