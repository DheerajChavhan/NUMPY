import numpy as np #type:ignore

# INSERT in 1_D Array
arr=np.array([1,23,45,64,77])
new_arr=np.insert(arr,1,2)        #Syntax: insert(name,index,value)
print(new_arr)

# INSERT in 2_D Array
arr=np.array([[1,23,45,64,77],[1,2,3,4,5]])
new_arr=np.insert(arr,1,[6,7,8,9,10],axis=0)        #Syntax: insert(name,index,value,axis)
print(new_arr)

# NOTE: axis=0 means Horizontaly,axis=1 means Verically ,axis=none means flatten