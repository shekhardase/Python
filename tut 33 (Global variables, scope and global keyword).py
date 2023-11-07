# L = 50  #GLOBAL VARIABLE
# def function1(n):
#     print(n,"I have printed")
#     L = 20  #LOCAL VARIABLE                        python will print local variable which is in function
    # M = 10

    # global L       # this line shows global keyword used to change value of global variable
                    # i removed local variable L so it will take value of global variable and change its value
    # L = L +10
    #
    # print(L,M)
    #
    # print(L)                          #function if there is o local variable then it will print global variable.
# //
#
# function1("This is me")
# print(L)                        # Here i printed L in out of function hence it gives me value of Global varaible
                   # After using global keyword value of L is completely changed even when we print it out of function it gives changed value.


x = 89
def harry():
    x = 20
    def rohan():
        global x
        x = 88
    # print("before calling rohan()",x)
    rohan()
    print("after calling rohan()", x)
harry()
print(x)


# SCOPE :
"""
   Scope refers to coding area where a perticular python variable is accessible.
  Hence one cannot access any particular variable from anywhere from code."""

# Local variables:
"""
     A variable that is decleared inside a function or loop is called a local variable.
    In case of functions , when we define a variable within a function, its scope lies within the function only. 
   It is accessible from point where it is defined until end of function.
  It will exist for as long as the function is executing.
 Local variable cannot be accessed outside the function.
The parameter names in function, they behaves like local variable"""

# Global variables:
"""It is not decleared inside the function and can be accessed anywhere within a program.
  It can be also defined as variable in main body of program.
 Any function or loop can access it, Its scope is anywhere within program."""

# Want to modify global inside function:
"""For this purpose we use global keyword. In python, the global keyword allow us to modify global variable.
   It is used to create a global variable and make changes to variable in local scope. """

# Rules of global keyword:
"""
(1) If we assigned a value to variable within the function body, it would be local unless explicitly decleared as global.
(2) Those variables that are referenced onlu inside a function are implicitly global.
(3) There is no need to use the global keyword outside function.
"""

# Nested function :
"""        When we define a function inside another function, it becomes a nested function.
      A nested function also has its own workspaces of all function in which it is nested.
      But it can be accessed to workspace of all functions in which it is nested."""

# How does the scope changes in nested function:
"""
    When we declered a local variable in function, its scope usually restricted to that function alone.
  This is because each function and subfunction stores its variables in its separate workspace.
A variable whose value is assigned by primary function can be read or overwritten by function nested at any level within primary.
"""