a = 9
b = 8
c = sum((a,b))          # Built in function
print(c)

def function1(a,b):
    print("hello you are in function", a+b)

print(function1(a,b))
function1(a,b)

def function2(p,q):
    """this is function which will calculate average of two numbers
           This function is only for two numbers"""
    average= (p+q)/2                #Doc string is used as hightlight o a information about function we can you as we want
    print(average)                  #  First line after function written in ("""   """)
    return average                 # To print Doc string use .__doc__ after function in print command
                                  # If we want to use variable for function use RETURN
v = function2(4,5)
print(v)
print(function2.__doc__)
function2(1,2)