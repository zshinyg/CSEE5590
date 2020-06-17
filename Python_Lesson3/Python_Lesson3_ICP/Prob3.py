#Using NumPy create random vector of size 20 having only float in the range 1-20. 
#Then reshape the array to 4 by 5
#Then replace the max in each row by 0 (axis=1)
#(you can NOT implement it via for loop)


import numpy as np

randomVector = np.random.uniform(1.0, 20.0 , size = 20)


resizedVector = np.resize(randomVector,(4,5))

print("RESIZED VECTOR TO (4,5)\n",resizedVector)

newArray = np.where(resizedVector == np.max(resizedVector, axis=1).reshape(-1,1), 0, resizedVector)

print("MAX OF EACH ROW MINUS 0\n", newArray)