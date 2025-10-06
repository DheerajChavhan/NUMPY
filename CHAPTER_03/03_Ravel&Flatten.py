import numpy as np #type:ignore

arr=np.array([[1,23,45,64,77],[1,2,3,4,5]])
print(arr.ravel())     #Returns the View
print(arr.flatten())   #Returns the Copy

# NOTE: BOTH OF THEM WILL CONVERT THE 2_D/3_D ARRAY INTO 1_D ARRAY