import string as st
import random

len = int(input("enter the length of the password: "))
passcode = ''

numbers = int(input("enter the number of integers needed in the password: "))
letters = int(input("enter the number of letters neede in the password: "))

for i in range(1, numbers):
    passcode += st.printable[0]

for i in range(numbers, letters):
    passcode += st.printable[1]

for i in range(numbers+letters, len):
    passcode += st.printable[random.randint(58, 70)]


print(passcode)