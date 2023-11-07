print("enter 1st your number")
n1 = int(input())
print("enter your 2nd number")
n2 = int(input())
print("choose operator you want among *,+,_,/")
n3 = input()

if n1==45 and n2==3 and n3=="*":
    print(555)
elif n1==56 and n2==9 and n3=="+":
    print(77)
elif n1==56 and n2==6 and n3=="/":
    print(4)
elif n3=="+" :
    n4=n1+n2
    print(n4)
elif n3=="/":
    n4=n1/n2
    print(n4)
elif n3=="*":
    n4=n1*n2
    print(n4)
