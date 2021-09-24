'''
Authors:    Muhammad Abdullah, Chrissy Aman, & Nate Sommer
Topic:      Test-Driven Development using Pytest
Date:       9/24/2021
'''
###############################################################################

from code_base.String import *
import pytest
import random
import string

###############################################################################
###############################################################################

class print_test:
    ''' Class to be used in streamlining prints of each test in "test_..."
        pytest testing functions below.  Because this class only provides
        an __init__ method, it can be used as though it was simply a
        function call, e.g.,
            print_test('String("")._chars', ...)
        Because this is a class, each call to print_test can therefore track
        the total number of calls/tests to be displayed in the printing.

        Usage syntax:

            print_test([string representing the call being tested], \
                       result =   [result of the call being tested], \
                       expected = [expected result of the call teing tested])

        Usage example:
            print_test('String("")._chars', \
                       result   = String("")._chars,
                       expected = [])

    '''

    test_number = 0  # class-level (static) variable to track number of tests

    def __init__(self, what_test: str, *args: list, **kwargs: dict):
        ''' Defining print_test as a class with __init__ will allow the user
            call print_test like a funtion, when they're actually constructing
            a print_test object (but allows us to track the total number of
            tests).

        Args:
            what_test: str representation of what is being tested, e.g., of the
                form 'String("")._chars' when testing the contents of an
                instance variable _chars inside a newly created String object
            kwargs['result']: type varies (typically String or str or list or None).
                The actual result of the test being conducted.  For example, this
                would be [] for a correct implementation of String("")._chars.
            kwargs['expected']: type varies (typically String or str or list or None)
                The expected result of the test being conducted. For example, this
                should be [] when testing String("")._chars.

        Returns:
            None -- this is an __init__ method.
        '''

        # grab the required keyword arguments
        result   = kwargs['result']
        expected = kwargs['expected']

        # some setup for printing the test info below
        prefix = f'Test {print_test.test_number}: '
        # fish out the class name, which whould be String in this context,
        # and the argument to the String construction
        open1_idx  = what_test.index('(')
        close1_idx = what_test.index(')', open1_idx)
        class_name = what_test[0:open1_idx]
        argument1  = what_test[open1_idx + 2 : close1_idx - 1]  # account for quotes
        # create a string with string-indices for displaying
        indices = "".join(str(i % 10) for i in range(len(argument1)))

        argument2 = None; padding = ""
        # check whether String("...") appears twice for adding second arg's indices
        if class_name in what_test[close1_idx:]:
            open2_idx    = what_test.index('(', close1_idx)
            close2_idx   = what_test.index(')', open2_idx)
            argument2    = what_test[open2_idx + 2 : close2_idx - 1]  # account for quotes
            arg2_indices = "".join(str(i % 10) for i in range(len(argument2)))
            padding      = ' ' * (open2_idx - close1_idx + 1 + 2)     # account for quotes

        # indentation (accounting for # of tests) used in printing below
        indent = '    ' + (' ' * len(str(print_test.test_number)))

        # print the test info, a la 'Test 0: String("")._chars';
        # print indices below whenever the argument is not the empty string
        print(f'\n\n{prefix}{what_test}')
        if argument2 is None:
            if len(argument1) > 0:
                print(f'{indent}# indices: {indices} (length:{len(argument1)})')
        else:
            if len(argument1) > 0 or len(argument2) > 0:
                print(f'{indent}# indices: {indices}{padding}{arg2_indices}')

        try:
            if isinstance(result, String): result = result.__str__()
            assert(type(result) == type(expected))
        except:
            # if the provided result and expected mismatch in type,
            # let the user know...
            print(f"ERROR: mismatched list type in print_test's " + \
                  f"test #{print_test.test_number}:")
            print(f"\t result type: {type(result)}  expected type: {type(expected)}")
        else:
            if isinstance(expected, list):
                # remove spaces from between list items for compact printing
                print(f'{indent}Result:   {str(result).replace(", ", ",")}')
                print(f'{indent}Expected: {str(expected).replace(", ", ",")}')
            elif isinstance(expected, str):
                # include quotes when output is type str
                print(f'{indent}Result:   "{result}"')
                print(f'{indent}Expected: "{expected}"')
            else:
                print(f'{indent}Result:   {result}')
                print(f'{indent}Expected: {expected}')

        print_test.test_number += 1  # increment the static test count

###############################################################################
###############################################################################

@pytest.fixture
def empty_string():
    ''' pytest fixture to return an empty string

     Returns:
         empty string
    '''
    return ""

##########
@pytest.fixture
def empty_list():
    ''' pytest fixture to return an empty list

     Returns:
         empty list
    '''
    return []

##########
@pytest.fixture
def characters():
    ''' pytest fixture to provide a list of characters for generating random strings

     Returns:
         a string of characters consisting of letters, digits, and punctuation,
             but with parentheses and quotes removed (to make output comparison
             easier in printed output)
    '''
    return string.digits + string.ascii_letters + \
           "!#$%&*+,-./:;<=>?@[\\]^_`{|}~"

##########
@pytest.fixture
def random_string(characters):
    ''' pytest fixture to generate a random string between length 2 and 20

    Args:
        characters:  pytest fixture (above) for generating a random character string

    Returns:
        an str consisting of randomly-selected characters
    '''
    length = random.randint(2,20)
    return "".join(random.choice(characters) for i in range(length))

##########
@pytest.fixture
def different_random_string(characters):
    ''' pytest fixture to generate a different random string between length 2 and 20
        (e.g., for using random_string and different_random_string as argument to
        the same subsequent fixture)

        see RonnyPfannschmidt 1 Oct 2019 comment here:
        https://github.com/pytest-dev/pytest/issues/5896

    Args:
        characters:  pytest fixture (above) for generating a random character string

    Returns:
        an str consisting of randomly-selected characters
    '''
    length = random.randint(2,20)
    return "".join(random.choice(characters) for i in range(length))

###############################################################################
###############################################################################

def test_empty_constructor(empty_string):
    ''' pytest test for String construction of an empty string
        (1) stores the actual result of the construction, grabbing internal list
        (2) calls print_test with string version of test, result of the actual
            test, and expected result
        (3) assert required by pytest
    '''
    result = String(empty_string)._chars
    expected = []
    print_test(f'String("{empty_string}")._chars', \
               result = result, expected = expected)
    assert(result == expected)

##########
def test_basic_constructor(random_string):
    ''' pytest test for String construction of a random string
        (1) stores the actual result of the construction, grabbing internal list
        (2) calls print_test with string version of test, result of the actual
            test, and expected result
        (3) assert required by pytest
    '''
    result   = String(random_string)._chars
    expected = [c for c in random_string]
    print_test(f'String("{random_string}")._chars', \
               result = result, expected = expected)
    assert(result == expected)

##########
def test_new_empty_constructor(empty_string):
    ''' pytest test for String construction of an empty string
        (1) stores the actual result of the construction, grabbing the string
        (2) calls print_test with string version of test, result of the actual
            test, and expected result
        (3) assert required by pytest
    '''
    result = String(empty_string)._string
    expected = empty_string
    print_test(f'String("{empty_string}")._string', \
                result = result, expected = expected)
    assert(result == expected)

##########
def test_new_basic_constructor(random_string):
    ''' pytest test for String construction of a random string
        (1) stores the actual result of the construction, grabbing the string
        (2) calls print_test with string version of test, result of the actual
            test, and expected result
        (3) assert required by pytest
    '''
    result = String(random_string)._string
    expected = random_string
    print_test(f'String("{random_string}")._string', \
                result = result, expected = expected)
    assert(result == expected)

##########
def test_string_constructor_empty_string(empty_string):
    ''' pytest test for String construction of an empty string
        (1) stores a string version of the construction
        (2) calls print_test with string version of test, result of the actual
            test, and expected result
        (3) assert required by pytest
    '''
    result = str(String(empty_string))
    expected = empty_string
    print_test(f'str(String("{empty_string}"))', \
                result = result, expected = expected)
    assert(result == expected)

##########
def test_string_constructor_random_string(random_string):
    ''' pytest test for String construction of a random string
        (1) stores a string version of the construction
        (2) calls print_test with string version of test, result of the actual
            test, and expected result
        (3) assert required by pytest
    '''
    result = str(String(random_string))
    expected = random_string
    print_test(f'str(String("{random_string}"))', \
                result = result, expected = expected)
    assert(result == expected)

##########
def test_len_constructor_empty_string(empty_string):
    ''' pytest test for String construction of an empty string
        (1) stores the length of the construction
        (2) calls print_test with string version of test, result of the actual
            test, and expected result
        (3) assert required by pytest
    '''
    result = String(empty_string).len()
    expected = len(empty_string)
    print_test(f'String("{empty_string}").len()', \
                result = result, expected = expected)
    assert(result == expected)

##########
def test_len_constructor_random_string(random_string):
    ''' pytest test for String construction of a random string
        (1) stores the length of the construction
        (2) calls print_test with string version of test, result of the actual
            test, and expected result
        (3) assert required by pytest
    '''
    result = String(random_string).len()
    expected = len(random_string)
    print_test(f'String("{random_string}").len()', \
                result = result, expected = expected)
    assert(result == expected)

##########
def test_is_empty_constructor_empty_string(empty_string):
    ''' pytest test for String construction of an empty string
        (1) stores the equality evaluation of the construction
        (2) calls print_test with string version of test, result of the actual
            test, and expected result
        (3) assert required by pytest
    '''
    result = String(empty_string).is_empty()
    expected = True
    print_test(f'String("{empty_string}").is_empty()', \
                result = result, expected = expected)
    assert(result == expected)

##########
def test_is_empty_constructor_random_string(random_string):
    ''' pytest test for String construction of a random string
        (1) stores the equality evaluation of the construction
        (2) calls print_test with string version of test, result of the actual
            test, and expected result
        (3) assert required by pytest
    '''
    result = String(random_string).is_empty()
    expected = False
    print_test(f'String("{random_string}").is_empty()', \
                result = result, expected = expected)
    assert(result == expected)

##########
def test_equality_constructor_two_different_strings(random_string, different_random_string):
    ''' pytest test for String construction of a random string
        (1) stores the equality evaluation of the construction
        (2) calls print_test with string version of test, result of the actual
            test, and expected result
        (3) assert required by pytest
    '''
    result = String(random_string)==(different_random_string)
    expected = False
    print_test(f'String("{random_string}")==("{different_random_string}")', \
                result = result, expected = expected)
    assert(result == expected)

##########
def test_equality_constructor_same_string(random_string):
    ''' pytest test for String construction of a random string
        (1) stores the equality evaluation of the construction
        (2) calls print_test with string version of test, result of the actual
            test, and expected result
        (3) assert required by pytest
    '''
    result = String(random_string)==(random_string)
    expected = True
    print_test(f'String("{random_string}")==("{random_string}")', \
                result = result, expected = expected)
    assert(result == expected)

##########
def test_equality_constructor_string_empty_string(random_string, empty_string):
    ''' pytest test for String construction of an empty string
        (1) stores the equality evaluation of the construction
        (2) calls print_test with string version of test, result of the actual
            test, and expected result
        (3) assert required by pytest
    '''
    result = String(random_string)==(empty_string)
    expected = False
    print_test(f'String("{random_string}")==("{empty_string}")', \
                result = result, expected = expected)
    assert(result == expected)

##########
def test_equality_constructor_empty_strings(empty_string):
    ''' pytest test for String construction of an empty string
        (1) stores the equality evaluation of the construction
        (2) calls print_test with string version of test, result of the actual
            test, and expected result
        (3) assert required by pytest
    '''
    result = String(empty_string)==(empty_string)
    expected = True
    print_test(f'String("{empty_string}")==("{empty_string}")', \
                result = result, expected = expected)
    assert(result == expected)

##########
def test_getitem_first_on_empty_string(empty_string):
    ''' pytest test for accessing [0] entry in an empty string
        (1) uses 'with pytest.raises' to look for appropriate raised exception,
            which is raised by the indented code
        (2) stores the type of the value of the raised exception
        (3) calls print_test with string version of test, result of the actual
            test, and expected result
        (4) assert required by pytest
    '''
    with pytest.raises(IndexError) as exception_info:
        String(empty_string)[0]
    result   = type(exception_info.value)
    expected = IndexError
    print_test(f'String("{empty_string}")[0]', \
               result = result, expected = expected)
    assert(result == expected)

##########
def test_getitem_first_on_random_string(random_string):
    ''' pytest test for accessing [0] entry in a random string
        (1) stores the item of the given index
        (2) calls print_test with string version of test, result of the actual
            test, and expected result
        (3) assert required by pytest
    '''
    result   = String(random_string)[0]
    expected = random_string[0]
    print_test(f'String("{random_string}")[0]', \
               result = result, expected = expected)
    assert(result == expected)

##########
def test_getitem_last_on_empty_string(empty_string):
    ''' pytest test for accessing [-1] entry in an empty string
        (1) uses 'with pytest.raises' to look for appropriate raised exception,
            which is raised by the indented code
        (2) stores the type of the value of the raised exception
        (3) calls print_test with string version of test, result of the actual
            test, and expected result
        (4) assert required by pytest
    '''
    with pytest.raises(IndexError) as exception_info:
        String(empty_string)[-1]
    result   = type(exception_info.value)
    expected = IndexError
    print_test(f'String("{empty_string}")[-1]', \
               result = result, expected = expected)
    assert(result == expected)

##########
def test_getitem_last_on_random_string(random_string):
    ''' pytest test for accessing [-1] entry in a random string
        (1) stores the item of the given index
        (2) calls print_test with string version of test, result of the actual
            test, and expected result
        (3) assert required by pytest
    '''
    result   = String(random_string)[-1]
    expected = random_string[-1]
    print_test(f'String("{random_string}")[-1]', \
               result = result, expected = expected)
    assert(result == expected)

##########
def test_setitem_first_on_empty_String(empty_string):
    ''' pytest test for setting [0] entry in an empty string
        (1) uses 'with pytest.raises' to look for appropriate raised exception,
            which is raised by the indented code
        (2) stores the type of the value of the raised exception
        (3) calls print_test with string version of the test, result of the
            actual test, and expected result
        (4) assert required by pytest
    '''
    string = String(empty_string)
    with pytest.raises(IndexError) as exception_info:
        string[0] = '❤'
    result   = type(exception_info.value)
    expected = IndexError
    print_test(f'String("{empty_string}")[0] = \'❤\'', \
               result = result, expected = expected)
    assert(result == expected)

##########
def test_setitem_first_on_random_string(random_string):
    ''' pytest test for setting [0] entry in a random string
        (1) stores the given string value
        (2) calls print_test with string version of the test, result of the
            actual test, and expected result
        (3) assert required by pytest
    '''
    string = String(random_string)
    string[0] = '❤'
    result   = None
    expected = None
    print_test(f'String("{random_string}")[0] = \'❤\'', \
               result = result, expected = expected)
    assert(result == expected)

##########
def test_setitem_multiple_characters_first_on_random_string(random_string):
    ''' pytest test for setting [0] entry in a random string
        (1) stores the given string value
        (2) calls print_test with string version of the test, result of the
            actual test, and expected result
        (3) assert required by pytest
    '''
    string = String(random_string)
    string[0] = 'DCS IS FUN!'
    result   = None
    expected = None
    print_test(f'String("{random_string}")[0] = DCS IS FUN!', \
               result = result, expected = expected)
    assert(result == expected)

##########
def test_setitem_last_on_empty_String(empty_string):
    ''' pytest test for setting [-1] entry in an empty string
        (1) uses 'with pytest.raises' to look for appropriate raised exception,
            which is raised by the indented code
        (2) stores the type of the value of the raised exception
        (3) calls print_test with string version of the test, result of the
            actual test, and expected result
        (4) assert required by pytest
    '''
    string = String(empty_string)
    with pytest.raises(IndexError) as exception_info:
        string[-1] = '❤'
    result   = type(exception_info.value)
    expected = IndexError
    print_test(f'String("{empty_string}")[-1] = \'❤\'', \
               result = result, expected = expected)
    assert(result == expected)

##########
def test_setitem_last_on_random_string(random_string):
    ''' pytest test for setting [-1] entry in a random string
        (1) stores the given string value
        (2) calls print_test with string version of the test, result of the
            actual test, and expected result
        (3) assert required by pytest
    '''
    string = String(random_string)
    string[-1] = '❤'
    result   = None
    expected = None
    print_test(f'String("{random_string}")[-1] = \'❤\'', \
               result = result, expected = expected)
    assert(result == expected)

##########
def test_setitem_multiple_characters_last_on_random_string(random_string):
    ''' pytest test for setting [-1] entry in a random string
        (1) stores the given string value
        (2) calls print_test with string version of the test, result of the
            actual test, and expected result
        (3) assert required by pytest
    '''
    string = String(random_string)
    string[-1] = 'DCS IS FUN!'
    result   = None
    expected = None
    print_test(f'String("{random_string}")[-1] = DCS IS FUN!', \
               result = result, expected = expected)
    assert(result == expected)

##########
def test_add_on_empty_strings(empty_string):
    ''' pytest test for adding to a string construction
        (1) stores the concatenation of strings
        (2) calls print_test with string version of the test, result of the
            actual test, and expected result
        (3) assert required by pytest
    '''
    result = String(empty_string)+empty_string
    expected = ""
    print_test(f'String("{empty_string}")+empty_string', \
               result = result, expected = expected)
    assert(result == expected)

##########
def test_add_on_empty_string_and_random_string(empty_string, random_string):
    ''' pytest test for adding to a string construction
        (1) stores the concatenation of strings
        (2) calls print_test with string version of the test, result of the
            actual test, and expected result
        (3) assert required by pytest
    '''
    result = String(empty_string)+random_string
    expected = random_string
    print_test(f'String("{empty_string}")+random_string', \
               result = result, expected = expected)
    assert(result == expected)

##########
def test_add_on_same_random_strings(random_string):
    ''' pytest test for adding to a string construction
        (1) stores the concatenation of strings
        (2) calls print_test with string version of the test, result of the
            actual test, and expected result
        (3) assert required by pytest
    '''
    result = String(random_string)+random_string
    expected = random_string+random_string
    print_test(f'String("{random_string}")+random_string', \
               result = result, expected = expected)
    assert(result == expected)

##########
def test_add_on_different_random_strings(random_string, different_random_string):
    ''' pytest test for adding to a string construction
        (1) stores the concatenation of strings
        (2) calls print_test with string version of the test, result of the
            actual test, and expected result
        (3) assert required by pytest
    '''
    result = String(random_string)+different_random_string
    expected = random_string+different_random_string
    print_test(f'String("{random_string}")+different_random_string', \
               result = result, expected = expected)
    assert(result == expected)

##########
def test_substring_on_end_indecies_empty_string(empty_string):
    ''' pytest test for creating a substring construction
        (1) stores the constructed substring
        (2) calls print_test with string version of the test, result of the
            actual test, and expected result
        (3) assert required by pytest
    '''
    result = String(empty_string).substring(0,-1)
    expected = IndexError
    print_test(f'String("{empty_string}").substring(0,-1)', \
               result = result, expected = expected)
    assert(result == expected)

##########
def test_substring_on_end_indecies_random_string(random_string):
    ''' pytest test for creating a substring construction
        (1) stores the constructed substring
        (2) calls print_test with string version of the test, result of the
            actual test, and expected result
        (3) assert required by pytest
    '''
    result = String(random_string).substring(0,-1)
    expected = random_string[0:-1]
    print_test(f'String("{random_string}").substring(0,-1)', \
               result = result, expected = expected)
    assert(result == expected)

##########
def test_substring_on_random_indecies_random_string(random_string):
    ''' pytest test for creating a substring construction
        (1) stores the constructed substring
        (2) calls print_test with string version of the test, result of the
            actual test, and expected result
        (3) assert required by pytest
    '''
    result = String(random_string).substring(1,3)
    expected = random_string[1:3]
    print_test(f'String("{random_string}").substring(1,3)', \
               result = result, expected = expected)
    assert(result == expected)

##########
def test_substring_on_other_indecies_random_string_1(random_string):
    ''' pytest test for creating a substring construction
        (1) stores the constructed substring
        (2) calls print_test with string version of the test, result of the
            actual test, and expected result
        (3) assert required by pytest
    '''
    result = String(random_string).substring(0+1,len(random_string)-1)
    expected = random_string[0+1:len(random_string)-1]
    print_test(f'String("{random_string}").substring(0+1,len(random_string)-1)', \
               result = result, expected = expected)
    assert(result == expected)

##########
def test_substring_on_other_indecies_random_string_2(random_string):
    ''' pytest test for creating a substring construction
        (1) stores the constructed substring
        (2) calls print_test with string version of the test, result of the
            actual test, and expected result
        (3) assert required by pytest
    '''
    result = String(random_string).substring(0+3,len(random_string)-3)
    expected = random_string[0+3:len(random_string)-3]
    print_test(f'String("{random_string}").substring(0+3,len(random_string)-3)', \
               result = result, expected = expected)
    assert(result == expected)

##########
def test_substring_on_other_indecies_random_string_3(random_string):
    ''' pytest test for creating a substring construction
        (1) stores the constructed substring
        (2) calls print_test with string version of the test, result of the
            actual test, and expected result
        (3) assert required by pytest
    '''
    result = String(random_string).substring(0+6,len(random_string)-6)
    expected = random_string[0+6:len(random_string)-6]
    print_test(f'String("{random_string}").substring(0+6,len(random_string)-6)', \
               result = result, expected = expected)
    assert(result == expected)

##############################################################################
##############################################################################
