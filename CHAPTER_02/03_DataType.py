import numpy as np           # type: ignore

A=np.array([1,2,3,4,5])    
B=np.array(["Dheeraj","Prem","Suraj"])
C=np.array([1.2,3.4,5,6])
D=np.array([True,False])

print(A.dtype)
print(B.dtype)
print(C.dtype)
print(D.dtype)

# Changing the DataType

print("DataType Before Changing")
arr=np.array([1,2.2,3])
print(arr.dtype)


print("DataType Before Changing")
int_arr=arr.astype(int)
print(int_arr.dtype)