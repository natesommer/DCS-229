'''
Author:     Nate Sommer
Topic:      Python ctypes
Date:       8 October 2021
'''
###############################################################################
###############################################################################

from code_base.MyArray import *
from tests.print_test import *
import pytest
import random

###############################################################################
###############################################################################

##########
@pytest.fixture
def empty_array():
    ''' fixture to return an empty Pyton list '''
    return []

##########
@pytest.fixture
def empty_MyArray():
    ''' returns an empty MyArray object'''
    return MyArray()

##########
@pytest.fixture
def one_element_array():
    ''' returns a one-element Python list containing a random integer '''
    return [random.randint(1,100)]

##########
@pytest.fixture
def five_element_array():
    ''' returns a five-element Python list containing random integers '''
    return [random.randint(1,100) for i in range(1,6,1)]

##########
@pytest.fixture
def six_element_array():
    ''' returns a six-element Python list containing random integers '''
    return [random.randint(1,100) for i in range(1,7,1)]

##########
@pytest.fixture
def one_element_MyArray(one_element_array):
    ''' returns a one-element MyArray object matching the one_element_array fixture '''
    array = MyArray()
    array.append(one_element_array[0])
    return array

##########
@pytest.fixture
def five_element_MyArray(five_element_array):
    ''' returns a five-element MyArray object matching the five_element_array fixture '''
    array = MyArray()
    for i in range(len(five_element_array)):
        array.append(five_element_array[i])
    return array

##########
@pytest.fixture
def six_element_MyArray(six_element_array):
    ''' returns a six-element MyArray object matching the five_element_array fixture '''
    array = MyArray()
    for i in range(len(six_element_array)):
        array.append(six_element_array[i])
    return array

###############################################################################
###############################################################################

##########
def test_empty_MyArray_len(empty_MyArray):
    assert(empty_MyArray.len() == 0)

##########
def test_one_element_MyArray_len(one_element_MyArray):
    assert(one_element_MyArray.len() == 1)

##########
def test_five_element_MyArray_len(five_element_MyArray):
    assert(five_element_MyArray.len() == 5)

##########
def test_six_element_MyArray_len(six_element_MyArray):
    assert(six_element_MyArray.len() == 6)

##########
def test_str_empty_MyArray(empty_MyArray, empty_array):
    eval_str = "empty_MyArray.__str__() == str(empty_array)"
    result = eval(eval_str)
    print_test(eval_str, result = result, expected = True)
    assert(result == True)

##########
def test_one_element_MyArray(one_element_MyArray, one_element_array):
    eval_str = "one_element_MyArray.__str__() == str(one_element_array)"
    result = eval(eval_str + ".replace(', ',',')")
    print_test(eval_str, result = result, expected = True)
    assert(result == True)

##########
def test_five_element_MyArray(five_element_MyArray, five_element_array):
    eval_str = "five_element_MyArray.__str__() == str(five_element_array)"
    result = eval(eval_str + ".replace(', ',',')")
    print_test(eval_str, result = result, expected = True)
    assert(result == True)

##########
def test_six_element_MyArray(six_element_MyArray, six_element_array):
    eval_str = "six_element_MyArray.__str__() == str(six_element_array)"
    result = eval(eval_str + ".replace(', ',',')")
    print_test(eval_str, result = result, expected = True)
    assert(result == True)

###########
def test_invalid_index_in_one_element_MyArray(one_element_MyArray, one_element_array):
    exec_str = f"one_element_MyArray[one_element_MyArray.len()] = {one_element_array[0]}"
    with pytest.raises(IndexError) as error:
        exec(exec_str)
    result = type(error.value)
    print_test(exec_str, result = result, expected = IndexError)
    assert(result == IndexError)

###########
def test_invalid_index_in_five_element_MyArray(five_element_MyArray, five_element_array):
    exec_str = f"five_element_MyArray[five_element_MyArray.len()] = {five_element_array[0]}"
    with pytest.raises(IndexError) as error:
        exec(exec_str)
    result = type(error.value)
    print_test(exec_str, result = result, expected = IndexError)
    assert(result == IndexError)

###########
def test_invalid_index_in_six_element_MyArray(six_element_MyArray, six_element_array):
    exec_str = f"six_element_MyArray[six_element_MyArray.len()] = {six_element_array[0]}"
    with pytest.raises(IndexError) as error:
        exec(exec_str)
    result = type(error.value)
    print_test(exec_str, result = result, expected = IndexError)
    assert(result == IndexError)

##########
def test_invalid_type_in_one_element_MyArray(one_element_MyArray, one_element_array):
    item = '"' + str(one_element_array[0]) + '"' \
        if not isinstance(one_element_array[0], str) else None
    exec_str = f"one_element_MyArray[0] = {item}"
    with pytest.raises(TypeError) as error:
        exec(exec_str)
    result = type(error.value)
    print_test(exec_str, result = result, expected = TypeError)
    assert(result == TypeError)

##########
def test_invalid_type_in_five_element_MyArray(five_element_MyArray, five_element_array):
    item = '"' + str(five_element_array[0]) + '"' \
        if not isinstance(five_element_array[0], str) else None
    exec_str = f"five_element_MyArray[0] = {item}"
    with pytest.raises(TypeError) as error:
        exec(exec_str)
    result = type(error.value)
    print_test(exec_str, result = result, expected = TypeError)
    assert(result == TypeError)

##########
def test_invalid_type_in_six_element_MyArray(six_element_MyArray, six_element_array):
    item = '"' + str(six_element_array[0]) + '"' \
        if not isinstance(six_element_array[0], str) else None
    exec_str = f"six_element_MyArray[0] = {item}"
    with pytest.raises(TypeError) as error:
        exec(exec_str)
    result = type(error.value)
    print_test(exec_str, result = result, expected = TypeError)
    assert(result == TypeError)

##########
def test_invalid_type_float_in_one_element_MyArray(one_element_MyArray, one_element_array):
    item = float(one_element_array[0]) \
        if not isinstance(one_element_array[0], str) else None
    exec_str = f"one_element_MyArray[0] = {item}"
    with pytest.raises(TypeError) as error:
        exec(exec_str)
    result = type(error.value)
    print_test(exec_str, result = result, expected = TypeError)
    assert(result == TypeError)

##########
def test_invalid_type_float_in_five_element_MyArray(five_element_MyArray, five_element_array):
    item = float(five_element_array[0]) \
        if not isinstance(five_element_array[0], str) else None
    exec_str = f"five_element_MyArray[0] = {item}"
    with pytest.raises(TypeError) as error:
        exec(exec_str)
    result = type(error.value)
    print_test(exec_str, result = result, expected = TypeError)
    assert(result == TypeError)

##########
def test_invalid_type_float_in_six_element_MyArray(six_element_MyArray, six_element_array):
    item = float(six_element_array[0]) \
        if not isinstance(six_element_array[0], str) else None
    exec_str = f"six_element_MyArray[0] = {item}"
    with pytest.raises(TypeError) as error:
        exec(exec_str)
    result = type(error.value)
    print_test(exec_str, result = result, expected = TypeError)
    assert(result == TypeError)

##########
def test_get_item_first_empty_MyArray(empty_MyArray, empty_array):
    exec_str = "empty_MyArray[0]"
    with pytest.raises(IndexError) as error:
        exec(exec_str)
    result   = type(error.value)
    expected = IndexError
    print_test(exec_str, result = result, expected = expected)
    assert(result == expected)

##########
def test_get_first_in_one_element_MyArray(one_element_MyArray, one_element_array):
    exec_str = f"one_element_MyArray[0] = {one_element_array[0]}"
    result   = eval(one_element_MyArray[0].__str__())
    expected = eval(str(one_element_array[0]).replace(', ',','))
    print_test(exec_str, result = result, expected = expected)
    assert(result == expected)

##########
def test_get_first_in_five_element_MyArray(five_element_MyArray, five_element_array):
    exec_str = f"five_element_MyArray[0] = {five_element_array[0]}"
    result   = eval(five_element_MyArray[0].__str__())
    expected = eval(str(five_element_array[0]).replace(', ',','))
    print_test(exec_str, result = result, expected = expected)
    assert(result == expected)

##########
def test_get_first_in_six_element_MyArray(six_element_MyArray, six_element_array):
    exec_str = f"six_element_MyArray[0] = {six_element_array[0]}"
    result   = eval(six_element_MyArray[0].__str__())
    expected = eval(str(six_element_array[0]).replace(', ',','))
    print_test(exec_str, result = result, expected = expected)
    assert(result == expected)

##########
def test_get_last_in_five_element_MyArray(five_element_MyArray, five_element_array):
    exec_str = f"five_element_MyArray[4] = {five_element_array[4]}"
    result   = eval(five_element_MyArray[4].__str__())
    expected = eval(str(five_element_array[4]).replace(', ',','))
    print_test(exec_str, result = result, expected = expected)
    assert(result == expected)

##########
def test_get_last_in_six_element_MyArray(six_element_MyArray, six_element_array):
    exec_str = f"six_element_MyArray[5] = {six_element_array[5]}"
    result   = eval(six_element_MyArray[5].__str__())
    expected = eval(str(six_element_array[5]).replace(', ',','))
    print_test(exec_str, result = result, expected = expected)
    assert(result == expected)

##########
def test_set_item_first_empty_MyArray(empty_MyArray, empty_array):
    new_item = 999
    exec_str = f"empty_MyArray[0] = {new_item}"
    with pytest.raises(IndexError) as error:
        exec(exec_str)
    result   = type(error.value)
    expected = IndexError
    print_test(exec_str, result = result, expected = expected)
    assert(result == expected)

##########
def test_set_first_in_one_element_MyArray(one_element_MyArray, one_element_array):
    new_item = 999
    exec_str = f"one_element_MyArray[0] = {new_item}"
    exec(exec_str)
    result   = eval(one_element_MyArray.__str__())
    expected = eval(str([new_item] + one_element_array[1:]).replace(', ',','))
    print_test(exec_str, result = result, expected = expected)
    assert(result == expected)

##########
def test_set_first_in_five_element_MyArray(five_element_MyArray, five_element_array):
    new_item = 999
    exec_str = f"five_element_MyArray[0] = {new_item}"
    exec(exec_str)
    result   = eval(five_element_MyArray.__str__())
    expected = eval(str([new_item] + five_element_array[1:]).replace(', ',','))
    print_test(exec_str, result = result, expected = expected)
    assert(result == expected)

##########
def test_set_first_in_six_element_MyArray(six_element_MyArray, six_element_array):
    new_item = 999
    exec_str = f"six_element_MyArray[0] = {new_item}"
    exec(exec_str)
    result   = eval(six_element_MyArray.__str__())
    expected = eval(str([new_item] + six_element_array[1:]).replace(', ',','))
    print_test(exec_str, result = result, expected = expected)
    assert(result == expected)

##########
def test_set_last_in_five_element_MyArray(five_element_MyArray, five_element_array):
    new_item = 999
    exec_str = f"five_element_MyArray[4] = {new_item}"
    exec(exec_str)
    result   = eval(five_element_MyArray.__str__())
    expected = eval(str(five_element_array[:4] + [new_item]).replace(', ',','))
    print_test(exec_str, result = result, expected = expected)
    assert(result == expected)

##########
def test_set_last_in_six_element_MyArray(six_element_MyArray, six_element_array):
    new_item = 999
    exec_str = f"six_element_MyArray[5] = {new_item}"
    exec(exec_str)
    result   = eval(six_element_MyArray.__str__())
    expected = eval(str(six_element_array[:5] + [new_item]).replace(', ',','))
    print_test(exec_str, result = result, expected = expected)
    assert(result == expected)

###############################################################################
###############################################################################
