print("Welcome to my simple AF calculator\nThis will be simple two number addition, subtraction, multiplication, division calculator")
print("Please choose your first number")
n1=int(input())
print("Nice, now choose next number")
n2=int(input())
print("SUGOI , now please select the operation +,-,*,/")
n3=input("")
if n3=="+":
    print(n1+n2)
elif n3=="*":
    print(n1*n2)
elif n3=="-":
    print(n1-n2)
elif n3=="/":
    print(n1/n2)

print("I hope you got your answer")
