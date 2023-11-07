# def print2(str1):
#     print2(str1)
#     print("This is "+str1)

# print2("Harry")


# def factorial(n):
"""
    # :param n: Integer
    # :return: n * n-1 * n-2 * n-3 *.............1
"""
#     pass
# def factorial_iterative(n):
#     n1 = 1
#     for n in range(n):
#         n1 = n1*(n+1)
#     return n1

# number=int(input("enter your number"))
# print(factorial_iterative(number))


# n! = n * n-1 * n-2 * n-3 .......1
# n! = n * (n-1)!



# n = int(input("Enter your number"))
# 0,1,1,2,3,5,8,13,21...
# def fibonacchi(n):
#     if n==1:
#         return 0
#     elif n==2:
#         return 1
    # else:
        # return fibonacchi(n-1) + fibonacchi(n-2)
# print(fibonacchi(n))



#Recursion:
"""
    Two essential parts and significant parts of recursive function. The first one is the base case, and second one is recursive case.
In base case conditional statement is written, within the program executes at end, just before returning values to users. In recursive cases
, the formula or logic function is based upon is written. A recursive function terminates to get closer to its base case or base condition.
As in case of loops, if condition does not satisfy the loop could easily endlessly , the same is in recursion that if base case is not met in call,
 the function will repeatedly run , causing the system to crash.
"""
""" 
     In case of recursion, each recursion call is stored into stack until it reaches the base condition, then the stack will one by one return the call printing 
a series or sequence of numbers onto the screen. It is worth nothing that stack is a LIFO data structure i.e., last in first out.
 This means that the call that is sent into the stack at end will be executed first,and the first one was inserted into stack will be executed first.
"""

# Iteration :
"""Iteration runs a block of code again and again, depending on user defined condition.
Many of function that recursion performs can also be achieved by using iterration but not all, and vice versa."""


# Recursion vs. Iteration:
"""
(1) Recursion can be only applied to function, while iteration can be used for number if lines of code, we want to repeat.
(2) Lesser coding has to be done in case of recursion thn iteration.
(3) Back tracing or reverse engineering in case of recursion can be different.
(4) In case of recursion, if condition is not met, the system will repeat a few times and then crash while in case of iteration it will continue to run endlessly.
(5) Even through less coding has to written in case of recursion, it is still slower in execution because the function has to be called again, and again, storing data into
the stacks also increases time of execution.
"""