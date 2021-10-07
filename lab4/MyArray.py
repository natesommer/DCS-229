'''
Author:     Nate Sommer
Topic:      Python ctypes
Date:       8 October 2021
'''
###############################################################################
###############################################################################

from ctypes import *
from math import ceil

###############################################################################
###############################################################################

class MyArray:

    __slots__ = ('_n', '_capacity', '_array', '_size_counter', '_resize_counter', '_copy_counter', '_unused_counter')

    ##########
    def __init__(self):
        self._n                 = 0
        self._capacity          = 1
        self._size_counter      = 0
        self._resize_counter    = 0
        self._copy_counter      = 0
        self._unused_counter    = 1
        self._array             = self._make_array(self._capacity)

    ##########
    def _make_array(self, capacity: int) -> 'ctypes array':
        ''' private method to reserve space for a low-level array of the
            given capacity
        Args:
            capacity: integer size of the array
        Returns:
            a ctypes low-level array
        '''
        return (capacity * py_object)()

    ##########
    def len(self) -> int:
        ''' returns number of actual elements in the array
        Args:
        Returns:
            integer count of number of elements in the array
        '''
        return self._n

    ##########
    def __getitem__(self, index: int) -> 'T':
        ''' returns the item in the array at the given index
        Args:
            index: integer index between 0 and self.len() - 1
        Returns:
            item of type T at given index
        Raises:
            IndexError exception of index is invalid
        '''
        if index < 0 or index >= self._n: raise IndexError(f"invalid index {index} for size {self._n}")
        else: return self._array[index]

    ##########
    def __setitem__(self, index: int, item: 'T') -> None:
        ''' sets the entry in the array at the given index to the given item
        Args:
            index: integer index between 0 and self.len() - 1
            item:  type-T element (must match type of entry in list)
        Returns:
            None
        Raises:
            IndexError exception of index is invalid
            TypeError exception if type of item does not match types in array
        '''
        if index < 0 or index >= self._n:
            raise IndexError(f"invalid index {index} for size {self._n}")
        if type(self._array[0]) != type(item):
            raise TypeError(f"invalid item type {type(item)} -- " \
                          + f"expected type {type(self._array[0])}")
        else: self._array[index] = item

    ##########
    def append(self, item: 'T') -> None:
        ''' appends the given item to the array, increasing the capacity of
            the array as necessary
        Args:
            item: type-T element to append to the array
        Return:
            None
        '''
        if self._n == self._capacity:

            self._resize(self._capacity * 2)
            #self._resize(ceil(self._capacity * 1.5))
            #self._resize(ceil(self._capacity * 1.25))
            #self._resize(self._capacity + 1024)
            #self._resize(self._capacity + 4096)
            #self._resize(self._capacity + 16384)

            self._resize_counter += 1
        self._array[self._n] = item
        self._n += 1
        self._unused_counter = (self._capacity - self._n) / self._capacity

    ##########
    def _resize(self, capacity: int) -> None:
        ''' private method to resize the array to a specific capacity,
            copying elements from the old array into the new
        Args:
            capacity: integer size of the new array
        Returns:
            None
        '''
        array = self._make_array(capacity)
        for i in range(self._n):
            array[i] = self._array[i]
            self._copy_counter += 1
        self._array = array
        self._capacity = capacity

    ##########
    def __str__(self) -> str:
        ''' returns a string representation of this array
        Args:
        Returns:
            a string
        '''
        string = ",".join(str(a) for a in self._array[0:self._n])
        return "[" + string + "]"

    def stats(self):
        ''' returns experiment counters
        Args:
        Returns:
            four counter instance variables
        '''
        return self._n, self._resize_counter, self._copy_counter, self._unused_counter

###############################################################################
###############################################################################
