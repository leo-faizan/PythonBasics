import random

lst = (random.sample(range(1, 100, 2), 50))
lst.sort()

key = int(input("enter the number to be searched: "))

l,r = -1,len(lst)+1

while(l <= r):
    mid = (l + (r-1)) // 2

    if lst[mid] == key :
        print("number found in position", mid+1)
        break

    elif lst[mid] < key :
        l = mid + 1
        

    elif lst[mid] > key:
        r = mid - 1
    else: 
        print("the element was not found")