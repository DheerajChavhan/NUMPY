import numpy as np #type:ignore

arr=np.array([1,23,45,64,77,34,24,67])

print(arr[0:3])     #Last is included
print(arr[:4])      #Starting to end
print(arr[4:])      #Index 4 to end
print(arr[1:4])     #Last is included but element 1 is not
print(arr[::2])     #Start with first element and prints every second element
print(arr[::-1])    #Reverse the Array  

# Slicing with Conditions

print(arr[arr>40])  
reshaped=arr.reshape(4,2)
print(reshaped)