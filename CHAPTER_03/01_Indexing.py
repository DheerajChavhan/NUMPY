import numpy as np #type:ignore

arr=np.array([1,23,45,64,77])

print(arr[2])   #3rd Element
print(arr[-1])  #3Last Element

# Indexing of 2_D array
arr=np.array([[1,23,45,64,77],[1,2,3,4,5]])
print(arr[(1,3)])  #2nd Row and 4th Column