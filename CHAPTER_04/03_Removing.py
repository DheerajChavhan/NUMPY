import numpy as np #type:ignore

arr=np.array([1,23,45,64,77])
print(np.delete(arr,0))

arr2=np.array([[1,23,45,64,77],[1,2,3,4,5]])
print(np.delete(arr2,0,axis=0))  #Remove First Row
print(np.delete(arr2,0,axis=1))  #Remove First Column