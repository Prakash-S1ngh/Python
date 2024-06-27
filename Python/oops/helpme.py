import numpy as np;


n_arr = np.array([[10.5, 22.5, 3.8], 
                  [41, np.nan, np.nan]])

rows , cols = n_arr.shape
print(rows)
    
for i in range(rows) :
    if np.isnan(n_arr[i]).any():
        n_arr = np.delete(n_arr , i , axis=0) 

print(n_arr)