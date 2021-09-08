'''
Author:     Nate Sommer
Topic:      Python Review #2
Date:       9/6/2021
'''
###############################################################################

import numpy as np # importing numpy library

###############################################################################

class Matrix:

    __slots__ = ('rows', 'cols', 'data') # storing explicit instance attributes

###############################################################################

    def __init__(self, rows, cols, data): # method constructor for class instance variables

        if rows * cols != len(data): raise Exception('MATRIX DATA DOES NOT MATCH DIMENSIONS') # conditional to raise exception
        self.rows,self.cols,self.data = rows,cols,data # storing class instance variables

###############################################################################

    def getNumRows(self): return self.rows # class method for getting row instance variable

###############################################################################

    def getNumCols(self): return self.cols # class method for getting column instance variable

###############################################################################

    def __str__(self): # class method for printing array

        array = np.reshape(np.array(self.data), (self.rows, self.cols)) # reshape array to fit dimensions
        return str(array) # return string of array

###############################################################################

    def __add__(self, other): # class method for adding two matracies

        if self.rows != other.rows and self.cols != other.cols: raise Exception('MATRIX DATA DOES NOT MATCH DIMENSIONS') # conditional to raise exception
        new_data = [] # initialize list for new matrix data
        for i in range(len(self.data)): # iterate through length of matrix data
            sum = self.data[i] + other.data[i] # sum matrix values
            new_data.append(sum) # append new matrix values

        new_array = np.reshape(np.array(new_data), (self.rows, self.cols)) # reshape array to fit dimensions
        return new_array # return sum of arrays

###############################################################################

    def __eq__(self, other): # class method for finding equivalent matracies

        if self.rows != other.rows and self.cols != other.cols: raise Exception('MATRIX DATA DOES NOT MATCH DIMENSIONS') # conditional to raise exception
        eq_list = [] # initialize list for storing equalities
        for i in range(len(self.data)): # iterate through matrix data length
            if self.data[i] == other.data[i]: eq_list.append(True) # conditional for matrix value equality
            else: eq_list.append(False) # conditional for matrix value inequality

        if False in eq_list: return False # conditional for inequality return
        else: return True # conditional for equality return

###############################################################################

    def transpose(self): # class method for transposing array

        array = np.reshape(np.array(self.data), (self.rows, self.cols)) # reshape array to fit dimensions
        t_array = np.transpose(array) # transpose array
        return t_array # return transposed array

###############################################################################

    def __mul__(self, other): # class method for two multiplying matracies

        if self.rows != other.cols and self.cols != other.rows: raise Exception('MATRIX DATA DOES NOT MATCH DIMENSIONS') # conditional to raise exception
        array = np.reshape(np.array(self.data), (self.rows, self.cols)) # reshape array to fit dimensions
        other_array = np.reshape(np.array(other.data), (other.rows, other.cols)) # reshape other array to fit dimensions
        mul_array = np.matmul(array, other_array) # multiply matrix values
        return mul_array # return product of arrays

###############################################################################

def main():

    m = Matrix(3, 3, [1,2,3,4,5,6,7,8,9])
    m2 = Matrix(3, 3, [9,8,7,6,5,4,3,2,1])

    print(f"\nNumber of rows in Matrix 'm': {m.getNumRows()}\n")
    print(f"Number of columns in Matrix 'm': {m.getNumCols()}\n")
    print(f"Matrix 'm':\n\n{m}\n")
    print(f"The sum of Matrix 'm' and Matrix 'm2':\n\n{m + m2}\n")
    print(f"Matrix 'm' is equal to Matrix 'm2': {m == m2}\n")
    print(f"The transpose of Matrix 'm':\n\n{m.transpose()}\n")
    print(f"The product of Matrix 'm' and Matrix 'm2':\n\n{m * m2}\n")

###############################################################################

if __name__ == "__main__":
    main()
