var1 = 8
var2 = 88

var3 = int(input())
if var3 > var2:
    print("greater")
elif var3 ==var2:
    print("equal")
else:
    print("lesser")

list = [1,2,3,4,5]
print(15 in list )
print(15 not in list)
if 6 in list :
        print("yes it is in list")
else:
    print("no")


n=int(input("enter a number"))
for i in range(1,n+1):
    for j in range (1,i+1):
        print(j, end=' ')
    print()

