L=[1,2,3,4,5]                #In Python
print("In Python")
print(L)

import numpy as np           # type: ignore

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

# With Default Values
print("Default Value")

Zeros_Array= np.zeros((2,3)) #For Default Value = 0
print("For Default Value=0")
print(Zeros_Array)

Ones_Array= np.ones(3) #For Default Value = 1
print("For Default Value=1")
print(Ones_Array)

Any_Array=np.full((2,3),5) 
print("For Specific Default Value") 
print(Any_Array)
