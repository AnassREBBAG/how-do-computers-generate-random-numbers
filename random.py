import random
F,P=0,0
n=10000000         #modify
for i in range(n):
    x=random.randint(0,1)
    if x==1:
        F+=1
P=n-F

print('nbr de P=',P,'nbr de F=',F)
