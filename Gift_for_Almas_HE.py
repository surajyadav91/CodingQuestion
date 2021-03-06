#Problem Link : https://www.hackerearth.com/practice/data-structures/arrays/multi-dimensional/practice-problems/algorithm/gift-for-almas-3-33d2f7c7/


n=int(input())
array=[]
for i in range(n):
    tmp=list(map(int,input().split()))
    array.append(tmp)

string=input()

import numpy as np 

n_arr=np.array(array)


#only 3 rotations , will check if we cancel LR or RL rotation
value = sum([1 if i == 'L' else -1  for i in string])
if value in [-3,1]:
    #left 90 degree / counter clock wise / axis 0 to 1
    n_arr=np.rot90(n_arr,1,(0,1))
else:
    n_arr=np.rot90(n_arr,1,(1,0))

for i in n_arr:
    print(*i)
