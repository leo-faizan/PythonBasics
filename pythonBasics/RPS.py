import random

while(True):
    comp_choice = random.randint(1, 3)
    user_choice = int(input("Select An Option \n * Enter 1 For Rock \n * Enter 2 For Paper \n * Enter 3 For Scissors: \n"))
    if (comp_choice == user_choice):
        print("Draw!!")
    elif(comp_choice == 1 and user_choice == 2):
        print("You Win!!")
    elif (comp_choice == 2 and user_choice == 3):
        print("You Win!!")
    elif (comp_choice == 3 and user_choice == 1):
        print("You Win!!")
    else:
        print("Computer Wins!!")
    iterator = int(input("Enter 1 to continue and 0 to exit: "))
    if iterator == 1 :
        continue
    else:
        break 
