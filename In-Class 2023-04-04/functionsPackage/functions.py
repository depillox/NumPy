import numpy as np
#write a function that accepts a numpy array and prints the odd-numbered rows only
#for example, if it has 5 rows
    #print rows 1,3 then just return 
#0 is neither odd or even

def print_odd_rows(myArray):
    row_counter = 0 # 0 is my first row
    for row in myArray:
        if row_counter % 2 == 1:
            print(row)
        row_counter = row_counter +1
        
#write a function that accepts two integers, rows & columns 
#and returns a numpy array of those dimensions randomly initalized with integer values 

def make_numpy_array(rows,columns):
    newArray = np.random.rand(rows,columns)
    return newArray

#write a function that sums the odd-numbered elements in a numpy array of 2-dimension, return the sum 
#hint:reshape into a 1-D array before you start summing
def sum_odd_numbers(array):
    row_counter = 0
    for row in array:
        if row_counter % 2 == 1:
            print(row)
        row_counter = row_counter +1