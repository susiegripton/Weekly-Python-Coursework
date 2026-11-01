from random import random
if random()<0.5:
    print("Heads")
else:
    print("Tails")
heads=0
counter=0
for j in range(10):
    heads=0
    for i in range(10):
        if random()<0.5:
            heads+=1
    print(heads)
if heads>=7:
    print("yes")
print(counter)
print(counter/10**4)


