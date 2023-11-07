

# def add(a,b):
#     return a+b                      # Line 4,5 and line 7 are same thats how we use lambda function

# add = lambda a, b: a+b

# print(add(3, 5))

# a =[[9, 42], [12, 54], [342, 62]]

# a.sort(key=lambda x:[x])
# print(a)

# def a_first(a):
#     return a[1]
# a.sort(key=a_first)
# print(a)


#Lambda/ anonymous functions:-
"""   They are only for convinence.
     In python programming, an anonymous function and lambda expression is a function definition is not bound to an identifier (def)
    The anonymous function is inline function, they are created using lambda operator and cannot contain multiple expressions.

The following will show how lambda works:

Result = lambda n1, n2, n3, n3: n1 + n2 +n3
print("Sum of three values:", Result(10, 20, 25)

    In above code, we have created an anonymous function that adds three numbers.
   The function is stored in variable named as Result. The function can be then be called using this variable.
  In above code, the function has been called with three different parameter values for function call.
 Anonymous fuctions can accept inputs and return outputs, just like other functions do.
"""

# Why do we use Python Lambda function ??
"""
    When we need function just once anonymous functions come in handy.
   Lambda operator is not only used to create anonymous functions, but there are many other uses of lambda expression.
  We can create anonymous functions whenever they needed. 
 Due to this reason, Python Lambda Functions are also called as throw-away functions which are used along with other predefined functions such as reduce(), filter() and map().
"""


# Significant Differences Between Lambda Expressions And Simple Functions :
"""
(1) Can be passed immediately with or without variables.
(2) They can be inline functions.
(3) Automatic return of results.
(4) There is neither a document string nor a name.
"""

#Python List sort():
"""
   Sorting means aranging data systematically. If data we want to work with is not sorted, we will face problems finding the desired element.
  The Python language, like other programming languages, can sort data.
 Pythons has inbulid method i.e. sort(), which is used to sort elements of given list is specified ascending or descending order. 
There is also a build-in function i.e.sorted(), that builds a new sorted list from an iterable like list, dictionary, etc.
"""

# Parameter values :

"""
# 1. Key :
    In key parameter, we specify a function that is called on each list element before making comparisions.

# 2. Reverse :
    This is optional. False will sort the list in ascending order,and true will sort the list in descendong order.
  Default is reverse = false.
"""

# NOTE: sort() does not return any value, but it changes from the original list

