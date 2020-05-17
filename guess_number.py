import random

rand = random.randint(1, 20)

cond = True

while(cond):
    number = int(input("Guess a Number: "))
    
    if(number > rand):
        print(" the guessed number is higher than the generated number!")

    elif (number < rand):
        print(" the guessed number is smaller than the generated number!")

    else:
        print("Precise!")
        cond = False