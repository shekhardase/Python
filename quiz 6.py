while(True):
    v1 = int(input("enter a number\n"))
    if v1==100:
        print("congrats you have entered a number hundred")
        break
    elif v1<100:
        print("little high value")
        continue
    elif v1>100:
        print("little lower value")
        continue

#I Can't add no of tries or limit of trials
#eg= guess number within 10 gusses