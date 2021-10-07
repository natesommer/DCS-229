###############################################################################

class print_test:
    ''' Class to be used in streamlining prints of each test in "test_..."
        pytest testing functions below.  Because this class only provides
        an __init__ method, it can be used as though it was simply a
        function call, e.g.,
            print_test(eval_str, ...)
        Because this is a class, each call to print_test can therefore track
        the total number of calls/tests to be displayed in the printing.

        Usage syntax:

            print_test([string representing the call being tested], \
                       result =   [result of the call being tested], \
                       expected = [expected result of the call being tested])
 
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
            what_test: str representation of what is being tested
            kwargs['result']: type varies 
                The actual returned result of the test being conducted.
            kwargs['expected']: type varies
                The expected result of the test being conducted.

        Returns:
            None -- this is an __init__ method.
        '''

        # grab the required keyword arguments
        result   = kwargs['result']
        expected = kwargs['expected']

        # some setup for printing the test info below
        prefix = f'Test {print_test.test_number}: '
        # indentation (accounting for # of tests) used to print (less checkmark)
        indent = ' ' * len(str(print_test.test_number))

        # print the test info
        print(f'\n\n{prefix}{what_test}')
        try:
            assert(type(result) == type(expected))
        except:
            # if the provided result and expected mismatch in type,
            # let the user know...
            print(f"ERROR: mismatched type in print_test's " + \
                  f"test #{print_test.test_number}:")
            print(f"\t result type: {type(result)}  expected type: {type(expected)}")
        else:
            correct = "[✓]" if result == expected else "[✘]"
            filler_ = ' ' * len(correct)
            if type(expected) == list:
                # remove spaces from between list items for compact printing
                print(f'{correct} {indent}Result:   {str(result).replace(", ", ",")}')
                print(f'{filler_} {indent}Expected: {str(expected).replace(", ", ",")}')
            elif type(expected) == str:
                # include quotes when output is type str
                print(f'{correct} {indent}Result:   "{result}"')
                print(f'{filler_} {indent}Expected: "{expected}"')
            else:
                print(f'{correct} {indent}Result:   {result}')
                print(f'{filler_} {indent}Expected: {expected}')

        print_test.test_number += 1  # increment the static test count

