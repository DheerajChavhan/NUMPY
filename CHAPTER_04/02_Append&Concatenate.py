import numpy as np #type:ignore

arr=np.array([1,23,45,64,77])
new_arr=np.append(arr,[3,4])  #Insert at last
print(new_arr)

A=np.array([1,2,3,4])
B=np.array([5,6,7,8])
print(np.concatenate((A,B),axis=0))    #Concatenation
