# If we want to print or Run important code after some other code then we use try and except.
#EXAMPLE:

print("enter a number")
n1 = (input())                             #Now I want to print important line but what if code before goes wrong So i must use try and except
print("enter another number")
n2 = (input())
try:
    print("then the sum of n1 and n2 is",
          int(n1) +int(n2))

except Exception as e:
    print(e)

print("This is important line No matter what ths line should be printed")
