import random
import time

lst = ["computer", "program", "python"]
picked = random.choice(lst)

right = ["_"] * len(picked)
wrong = []
chances = 6

print("the word has", len(picked), "letters")

def update():
    for i in right :
        print(i, end=' ')
    print()

while chances > 0 :
    guess = input("Enter a letter: ")

    if guess in picked :
        index = 0
        for i in picked :
            if i == guess :
                right[index] = guess
            index += 1
        update()


    else :
        if guess not in wrong :
            wrong.append(guess)
            print("you have entered a wrong letter, Try again" )
        else :
            print("you have already guessed that")
        chances -= 1
    if "_" not in right :
        print(" You Have Won!")
        break
    if chances == 0 :
        print("You lose!")