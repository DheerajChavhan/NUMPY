import numpy as np #type:ignore

A=np.array([1,2,3,4])
B=np.array([5,6,7,8])

print(np.hstack((A,B)))   #Stacks Horizontally
print(np.vstack((A,B)))   #Stacks Vertically