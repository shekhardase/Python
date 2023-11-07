no_of_gusses=1
print("No of gusses is limited only to 9 times:-")
while(no_of_gusses<=9):
    guess_number=int(input("Guess the number: \n"))
    if guess_number<100:
        print("You have entered smaller number please enter greater number:-")
    elif guess_number>100:
        print("You have entered greater number please enter smaller number:_")
    else:
        print("YOU WON \n")
        print(no_of_gusses,"No gusses took to finish")
        break
    print(9-no_of_gusses,"no of gusses left")
    no_of_gusses = no_of_gusses+1
if (no_of_gusses>9):
    print("GaMe OvEr")