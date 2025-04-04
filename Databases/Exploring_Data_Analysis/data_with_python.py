#Exploring data arrays with NumPy
#Using NumPy module to work with the number dataset

import numpy as np

#Python List
data = [50,50,47,97,49,3,53,42,26,74,82,62,37,15,70,27,36,35,48,52,63,64]


#NumPy Array
grades = np.array(data)


#Comparing a NumPy Array and a Python List
print (type(data), 'x 2:', data * 2)
print('\n')
print( type(grades), 'x 2:', grades * 2)

"""By multiplying List with 2, it creates a new list that is twice the length of the original with the original list elements repeated
    By multiplying NumPy Array with 2, it performs the multiplication of each element. We get the same length of the array back, but each element is multipled by 2.
    The key takeaway is that NumPy arrays are made for mathematical operations on numeric data."""

#View the shape of the NumPy array
print(f"Printing the shape of the NumPy array: {grades.shape}")
"""This means that the array has 1 row and 22 columns
    """

#Accessing elements of the NumPy array
print(f"Printing the first element of the NumPy array: {grades[0]}")
print(f"Printing the sixth element of the NumPy array: {grades[5]}")

#Aggregating data in NumPy Array
print(f"Printing the mean of the NumPy array: {grades.mean()}")

