import numpy as np #type: ignore

prices=np.array([100,200,300,400])
Discount=10
new_prices=prices-(prices*Discount/100)                   
print(new_prices)

arr=np.array([100,200,300,400])
new_arr=arr+100                    #Adds 100 to every element
print(new_arr)

arr1=np.array([100,200,300,400])
arr2=np.array([10,20,30,40])
print(arr1+arr2)                   #Adds 2 Different Arrays

arr1=np.array([[100,200,300,400],[50,60,70,80]])
arr2=np.array([10,20,30,40])
print(arr1+arr2)                   #Adds 2 Different Arrays

arr1=np.array([100,200,300,400])
arr2=np.array([10,20,30])
print(arr1+arr2)                   #It is not valid


