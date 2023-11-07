print("pattern printing")
num = int(input("Enter how many rows you want:"))
print("Enter 0 or 1")
var1 = input("1 for True value or 0 for False:")
if var1 == "1":
    for i in range(0 ,num+1):
        print("*"*i)

if var1 == "0":
    for i in range(num,0,-1):
        print("*"*i)