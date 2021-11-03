'''
Author:     Nate Sommer
Topic:      BFS Algorithm
Date:       22 October 2021
'''
###############################################################################
###############################################################################

from typing import Generic, List, TypeVar

T = TypeVar("T") # initializing generic type 'T' variable

###############################################################################
###############################################################################

class EmptyError(Exception):
    ''' class extending Exception to better document queue errors '''
    def __init__(self, message: str):
        self.message = message

###############################################################################
###############################################################################

class Queue(Generic[T]):
    ''' class to implement a stack ADT using a Python list '''

    __slots__ = ("_data")

    ##########
    def __init__(self):
        self._data: List[T] = []

    ##########
    def __len__(self) -> int:
        ''' allows the len function to be called using a Queue object, e.g.,
               stack = Queue()
               print(len(queue))
        Returns:
            number of elements in the stack, as an integer
        '''
        return len(self._data)

    ##########
    def push(self, item: T) -> None:
        ''' pushes a given item of arbitrary type into the queue
        Args:
            item: an item of arbitrary type
        Returns:
            None
        '''
        self._data.append(item)

    ##########
    def pop(self) -> T:
        ''' removes the leftmost element from the queue and returns that element
        Returns:
            the leftmost item, of arbitrary type
        Raises:
            EmptyError exception if the queue is empty
        '''
        if len(self._data) == 0:
            raise EmptyError('Error in Queue.pop(): queue is empty')
        return self._data.pop(0)

    ##########
    def top(self) -> T:
        ''' returns the leftmost element from the queue without modifying the queue
        Returns:
            the leftmost item, of arbitrary type
        Raises:
            EmptyError exception if the queue is empty
        '''
        if len(self._data) == 0:
            raise EmptyError('Error in Queue.top(): queue is empty')
        return self._data[0]

    ##########
    def is_empty(self) -> bool:
        ''' indicates whether the queue is empty
        Returns:
            True if the queue is empty, False otherwise
        '''
        return len(self._data) == 0

    ##########
    def __str__(self) -> str:
        ''' returns an str implementation of the Queue '''
        string = str(self._data)
        return string

###############################################################################
###############################################################################
