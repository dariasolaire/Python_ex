import random

n = int(input())
mylist = [random.randint(1,99) for i in range(n)]

print(mylist)

my_result = mylist[::2]
print(my_result)