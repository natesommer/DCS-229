'''
Authors:    Muhammad Abdullah, Chrissy Aman, & Nate Sommer
Topic:      Test-Driven Development using Pytest
Date:       9/24/2021
'''
###############################################################################

class String:
    '''DCS 229 implementation of a version of the built-in str class.

    This class implements a simple version corresponding to the str class,
    where a String object consists of a sequence of characters.

    Attributes:
        __str__    : returns an str version of this String object
        len        : returns the (int) number of characters in this String
        is_empty   : returns True if this String is an empty string; False o/w
        __eq__     : allows comparison of this String vs. either a String or str
        __getitem__: allows fetching a character using [] notation
        __setitem__: allows overwriting a character using [] assignment
        __add__    : returns a new String object that is the concatenation of
                        this String object and a given String or str object
        substring  : returns a new String object by specifying substring indices
    '''

    ''' Notes on type hints below:
        - A parameter type hint is specified by : and type following the param
                def method(self, param: type)
        - A method return type hint is specified by an arrow between ) and :
                def method(self) -> type:
        - Python itself does not enforce type hints, but these can be checked
          by type checkers such as mypy.
        - As the String class does not yet exist, the standard approach is
          to use 'String' which is understood by type checkers as a lookahead.
        - Python 3.10 allows "or" support a la 'String' | str.  To fake this
          support in the presence of < 3.10 versions of Python, we are using
          'String | str' here (rather than the suggested Union['String', str]
          approach) for convenience and brevity.
    '''

    __slots__ = ('_chars','_string') # storing slots for instance variables

###############################################################################

    def __init__(self, string: str) -> None:
        ''' initialization method for the String class

        Args:
            string: an str type used to initialize the String

        Returns:
            None
        '''
        self._chars = [c for c in string] # building instance variable list
        self._string = string # building instance variable string

###############################################################################

    def __str__(self) -> str:
        ''' overrides the __str__ special method for conversion to str

        Returns:
            an str version of the String object contents
        '''
        return self._string # return instance variable

###############################################################################

    def len(self) -> int:
        ''' returns the number of characters present in the String object

        Returns:
            an int representing the number of character in the String
        '''
        return len(self._chars) # return length of instance variable list

###############################################################################

    def is_empty(self) -> bool:
        ''' Boolean method indicating whether the String is an empty string

        Returns:
            True if no characters are present in the String; False o/w
        '''
        if len(self._chars) == 0: return True # conditional for empty string
        else: return False # conditional for non empty string

###############################################################################

    def __eq__(self, other: 'String | str') -> bool:
        ''' overrides the __eq__ special method for comparing two String
            objects, or for comparing a String object and an str object

        Args:
            other: a separate String or str object for comparing

        Returns:
            True if the two objects contain exactly the same characters in
            the same order; False o/w
        '''
        if self._string == other: return True # conditional for equality
        else: return False # conditional for inequality

###############################################################################

    def __getitem__(self, index: int) -> str:
        ''' overrides the __getitem__ special method, allowing [] access
            into a String object to access a single character (str)

        Args:
            index: an integer indicating the position of the character to fetch

        Returns:
            the character (a str in Python) at the indicated position

        Raises:
            IndexError: if the index value is invalid relative to String length
        '''
        if index+1 > len(self._chars): raise IndexError # conditional for empty string
        else: return self._chars[index] # conditional for returning list item

###############################################################################

    def __setitem__(self, index: int, char: str) -> None:
        ''' overrides the __setitem__ special method, allowing one to overwrite
            a character at a specific index in the String

        Args:
            index: an integer indicating the position of the character to overwrite

        Returns:
            None

        Raises:
            IndexError: if the index value is invalid relative to String length
        '''
        if index+1 > len(self._chars): raise IndexError # conditional for empty string
        else: self._chars[index] = char # conditional to set list item

###############################################################################

    def __add__(self, other: 'String | str') -> 'String':
        ''' overrides the __add__ special method, allowing one to add
            (concatenate) two String objects, or to concatenate an str object
            to a String object; this String and other should remain unchanged

        Args:
            other: a String or str object to append to this String

        Returns:
            a String object represent the concatenation of the two strings
        '''
        return self._string + other # return concatenation of strings

###############################################################################

    def substring(self, start: int, end: int) -> 'String':
        ''' overrides the __add__ special method, allowing one to add
            (concatenate) two String objects, or to concatenate an str object
            to a String object; this String and other should remain unchanged

        Args:
            other: a String or str object to append to this String

        Returns:
            a String object represent the concatenation of the two strings
        '''
        substring = "" # initialize empty substring
        if len(self._string) == 0 or len(self._string) == 1: return IndexError # conditional for bad index lengths
        elif end == -1: return self._string[start:end] # conditional for returning full string
        else: return substring.join(self._chars[i] for i in range(start, end)) # conditional for building substring
