import numpy as np #type: ignore

# 1_D Array
A=np.array([1,2,3,4,5])      # Using Numpy
print("1_D Array")
print(A)

# 2_D Array
B=np.array([[1,2,3,4,5],[6,7,8,9,10]])      
print("2_D Array")
print(B)

# 3_D Array
C=np.array([[[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]]])      
print("3_D Array")
print(C)
   
  
print(A.ndim)   #Give the no of dimensions of the array
print(B.ndim)   
print(C.ndim)   