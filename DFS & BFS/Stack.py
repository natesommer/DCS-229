'''
Author:     Nate Sommer
Topic:      DFS Algorithm
Date:       22 October 2021
'''
###############################################################################
###############################################################################

from typing import Generic, List, TypeVar

T = TypeVar("T") # initializing generic type 'T' variable

###############################################################################
###############################################################################

class EmptyError(Exception):
    ''' class extending Exception to better document stack errors '''
    def __init__(self, message: str):
        self.message = message

###############################################################################
###############################################################################

class Stack(Generic[T]):
    ''' class to implement a stack ADT using a Python list '''

    __slots__ = ("_data")

    ##########
    def __init__(self):
        self._data: List[T] = []

    ##########
    def __len__(self) -> int:
        ''' allows the len function to be called using a Stack object, e.g.,
               stack = Stack()
               print(len(stack))
        Returns:
            number of elements in the stack, as an integer
        '''
        return len(self._data)

    ##########
    def push(self, item: T) -> None:
        ''' pushes a given item of arbitrary type onto the stack
        Args:
            item: an item of arbitrary type
        Returns:
            None
        '''
        self._data.append(item)

    ##########
    def pop(self) -> T:
        ''' removes the topmost element from the stack and returns that element
        Returns:
            the topmost item, of arbitrary type
        Raises:
            EmptyError exception if the stack is empty
        '''
        if len(self._data) == 0:
            raise EmptyError('Error in Stack.pop(): stack is empty')
        return self._data.pop()  # calling Python list pop()

    ##########
    def top(self) -> T:
        ''' returns the topmost element from the stack without modifying the stack
        Returns:
            the topmost item, of arbitrary type
        Raises:
            EmptyError exception if the stack is empty
        '''
        if len(self._data) == 0:
            raise EmptyError('Error in Stack.top(): stack is empty')
        return self._data[-1]

    ##########
    def is_empty(self) -> bool:
        ''' indicates whether the stack is empty
        Returns:
            True if the stack is empty, False otherwise
        '''
        return len(self._data) == 0

    ##########
    def __str__(self) -> str:
        ''' returns an str implementation of the ArrayStack '''
        string = "\nSTACK TOP\n---------\n\n"
        for i in range(len(self._data)-1,-1,-1):
           string += str(self._data[i]) + "\n"
        string += "\n------------\nSTACK BOTTOM\n"
        return string

###############################################################################
###############################################################################
