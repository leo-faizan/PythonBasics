import string as st
import random

len = int(input("enter the length of the password: "))
passcode = ''

numbers = int(input("enter the number of integers needed in the password: "))
letters = int(input("enter the number of letters neede in the password: "))

for i in range(numbers):
    passcode += st.printable[random.randint(0,9)]

for i in range(numbers, numbers+letters):
    passcode += st.printable[random.randint(11, 58)]

for i in range(numbers+letters, len):
    passcode += st.printable[random.randint(62, 85)]



print(passcode)