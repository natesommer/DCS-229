'''
Author:     Nate Sommer
Topic:      Stack ADT
Date:       15 October 2021
'''
###############################################################################
###############################################################################

import sys
import os.path as path

###############################################################################
###############################################################################

class EmptyError(Exception):

   def __init__(self, message):
      self.message = message

###############################################################################
###############################################################################

class ArrayStack:

   __slots__ = ("_data")

   ##########
   def __init__(self): self._data = []

   ##########
   def __len__(self): return len(self._data)

   ##########
   def push(self, e: 'T'): self._data.append(e)

   ##########
   def pop(self):
      if len(self._data) == 0:
         raise EmptyError('Error in ArrayStack.pop(): stack is empty')
      return self._data.pop()

   ##########
   def top(self):
      if len(self._data) == 0:
         raise EmptyError("error in ArrayStack.top(): stack is empty")
      return self._data[-1]

   ##########
   def sort(self):
       return self._data.sort()

   ##########
   def is_empty(self): return len(self._data) == 0

   ##########
   def __str__(self):
      string = "\nSTACK TOP\n---------\n\n"
      for i in range(len(self._data)-1,-1,-1):
         string += str(self._data[i]) + "\n"
      string += "\n------------\nSTACK BOTTOM\n"
      return string

###############################################################################
###############################################################################

def parse_html(text):

   front_stack = ArrayStack() # initializing stack object for front tags
   back_stack = ArrayStack() # initializing stack object for back tags

   for word in text.split(): # iterating through html text

       if word.startswith('<'): # conditional for tag
           if word[1] == '/': # conditional for back tag
               back_stack.push(word[2:-1]) # push tag onto back tag stack
       if word.startswith('<'): # conditional for tag
           if word[1] != '/': # conditional for front tag
               front_stack.push(word[1:-1]) # push tag onto front tag stack

   if front_stack.__len__() == back_stack.__len__(): # conditional for matched stack lengths

       front_stack.sort() # sort front tag stack
       back_stack.sort() # sort back tag stack

       compare_list = [] # initializing list for comparison
       while front_stack.__len__() != 0: # initializing iteration until stack is empty
           if front_stack.pop() == back_stack.pop(): # popping stacks to compare tags
               compare_list.append(True) # appending True is conditional is met
           else: compare_list.append(False) # appending False is conditional is not met

       if False not in compare_list: return True # conditional for matched tags return
       else: return False # conditional for unmatched tags return

   else: return False # conditional for unmatched tags return

###############################################################################
###############################################################################

def main():

        print(f"sys.argv = {sys.argv}") # printing command line arguments
        print(f"name of program = {sys.argv[0]}") # printing program name
        for i in range(1, len(sys.argv)): # iterating through command arguments
            print(f"arg {i} = {sys.argv[i]} \t type = {type(sys.argv[i])}") # printing command line arguments and types

        if len(sys.argv) < 2: # conditional for invalid command line argument length
            raise IndexError("INVALID NUMBER OF COMMAND LINE ARGUMENTS PASSED") # index error message
            sys.exit(2) # exit command line

        else: # conditional for valid command line arguments
            if path.exists(sys.argv[1]): # conditional for html file existing in directory
                with open(sys.argv[1], "r") as infile: # opening html file given by command line argument
                    text = infile.read() # reading and storing html text

            else: # conditional for html file not existing in directory
                raise FileNotFoundError("FILE DOES NOT EXIST IN DIRECTORY") # file not found error message
                sys.exit(1) # exit command line

        bool = parse_html(text) # call and store boolean returned by function passing in html file
        print(f"All html tags are matched: {bool}") # printing result

###############################################################################
'''
If I were to use a python list implementation instead of the built ArrayStack
class it would involve appending html tags to two lists, one for the front tags
and one for the back tags, iterating through the length of the lists, comparing
the items in the lists, and determining if they are a match. This method would
be efficient and arrive at the same solution as the ArrayStack implementation,
but using the stack ADT allows for better visualization of tags being pushed
onto a stack and popped off one at a time to remove them from the stack.
Although both implementations work well and are efficient, I would prefer to
use the built in python list class.
'''
###############################################################################

if __name__ == '__main__':
    main()
