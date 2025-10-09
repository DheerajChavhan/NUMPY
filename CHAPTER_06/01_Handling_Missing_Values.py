import numpy as np #type: ignore

arr=np.array([100,np.nan,300,400])

# Finding the missing values
print(np.isnan(arr))                    # isnan() function tells whether the function is "not a number" or not. It returns the boolean value

# Replacing the missing values
cleaned_arr= np.nan_to_num(arr,nan=200)   #nan_to_num() function replace the nan value with the specific number
print(cleaned_arr)


arr1=np.array([100,-np.inf,300,400,np.inf])

# Finding the infinite value
print(np.isinf(arr1))

# Replacing the infinite values
print(np.nan_to_num(arr1,posinf=500,neginf=200))   # posinf means plus infinity and neginf means nagative infinity
