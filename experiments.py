'''
Author:     Nate Sommer
Topic:      Python ctypes
Date:       8 October 2021
'''
###############################################################################
###############################################################################

from code_base.MyArray import *
from time import perf_counter
from progress.bar import Bar
import random

###############################################################################
###############################################################################

def one_experiment(min_list_size, max_list_size):
    array = MyArray() # storing low-level array object
    size = random.randint(min_list_size, max_list_size) # storing array size for testing
    for i in range(size): # iterating through array size
        array.append(random.randint(1,1000)) # appending random integers to array

    return array # return array object

###############################################################################
###############################################################################

def main():

    random.seed(8675309) # setting seed for testing

    size_counter    = 0 # initialize size counter for metrics
    resize_counter  = 0 # initialize resize counter for metrics
    copy_counter    = 0 # initialize copy counter for metrics
    unused_counter  = 0 # initialize unused counter for metrics
    elapsed_time    = 0 # initialize time counter for metrics

    bar = Bar("Running Experiments: ", max = 30) # setting progress bar for experiment testing
    for i in range(30): # iterating through number of experiments

        start = perf_counter() # starting performance counter
        array = one_experiment(100000,999999) # running and storing experiment
        end = perf_counter() # ending performance counter

        size_counter += array.stats()[0] # updating size counter
        resize_counter += array.stats()[1] # updating resize counter
        copy_counter += array.stats()[2] # updating copy counter
        unused_counter += array.stats()[3] # updating unused counter
        elapsed_time += end - start # updating time counter

        bar.next() # moving progress to next iteration
    bar.finish() # ending progress bar

    print(f"Average MyArray size produced: \t\t{round(size_counter/30, 2)}")
    print(f"Average number of resizes required: \t{round(resize_counter/30, 2)}")
    print(f"Average number of copies required: \t{round(copy_counter/30, 2)}")
    print(f"Average proportion of unused elements: \t{round(unused_counter/30, 2)}")
    print(f"Average time to load MyArray: \t\t{round(elapsed_time/30, 2)}")

###############################################################################
###############################################################################
'''
Experiments
-----------
Grow MyArray by factor of 2:

    Average MyArray size produced:              599902.43
    Average number of resizes required:         19.27
    Average number of copies required:          751478.47
    Average proportion of unused elements:      0.19
    Average time to load MyArray:               2.06

##########
Grow MyArray by factor of 1.5:

    Average MyArray size produced:              599902.43
    Average number of resizes required:         31.70
    Average number of copies required:          1461445.40
    Average proportion of unused elements:      0.18
    Average time to load MyArray:               2.59

##########
Grow MyArray by factor of 1.25:

    Average MyArray size produced:              599902.43
    Average number of resizes required:         54.93
    Average number of copies required:          2685214.57
    Average proportion of unused elements:      0.11
    Average time to load MyArray:               3.51

##########
Grow MyArray by 1024 elements:

    Average MyArray size produced:              599902.43
    Average number of resizes required:         586.27
    Average number of copies required:          217675406.53
    Average proportion of unused elements:      0.00
    Average time to load MyArray:               168.62

##########
Grow MyArray by 4096 elements:

    Average MyArray size produced:              599902.43
    Average number of resizes required:         146.90
    Average number of copies required:          54394890.37
    Average proportion of unused elements:      0.00
    Average time to load MyArray:               42.88

##########
Grow MyArray by 16384 elements:

    Average MyArray size produced:              599902.43
    Average number of resizes required:         37.10
    Average number of copies required:          13593295.77
    Average proportion of unused elements:      0.02
    Average time to load MyArray:               12.69
    '''

###############################################################################
###############################################################################

if __name__ == "__main__":
    main()
