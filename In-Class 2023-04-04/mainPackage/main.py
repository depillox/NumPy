import numpy as np 
from functionsPackage.functions import *

#write code to test your function
#cobble up a numpy array
#invoke your function

my = np.arange(100).reshape(20,5) #20 rows 5 columns
print_odd_rows(my)

my = make_numpy_array(4,5)
print(my)
print(type(my))

my = np.arange(100).reshape(20,5)
sum_odd_numbers(sum(my))