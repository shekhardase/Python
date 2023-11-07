# ROCK , PAPER , SCISSOR game:
import random
List = ["Rock","Paper","Scissor"]
var1 = random.choice(List)
print(var1)
print("PC has made his choice now choose among Rock, Paper and Scissor")
var2 = input("Type here:-")
i = 1
while(i<=10):
    if (var1 == "Rock"):
        if var2 == "Paper":
            print("Congo you won")
            break

        elif var2 == "Scissor":
            print("Congo you lose")

        elif var2 == "Rock":
            print("this is tie")

    elif (var1 == "Paper"):
        if var2 == "Paper":
            print("this is tie")

        elif var2 == "Rock":
            print("Congo you lose")

        elif (var2 == "Scissor"):
            print("Congo you won")
            break

    elif (var1 == "Scissor"):
        if var2 == "Paper":
            print("congo you lose")

        elif var2 == "Rock":
            print("congo you won")
            break

        elif var2 == "Scissor":
            print("TIEE")
    i = i+1



















