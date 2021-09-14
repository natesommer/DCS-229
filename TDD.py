'''
Author:     Nate Sommer
Topic:      Test-Driven Development
Date:       9/15/2021
'''
###############################################################################

def calculate_purchase_total(list_of_prices, sales_tax_rate):
    '''
    Parameters
    ----------
    list_of_prices : list
        a list of given integer values corresponding to item prices
    sales_tax_rate : int
        an integer corresponding to the given sales tax rate

    Returns
    -------
    purchase_total : int
        an integer corresponding to the total value of the purchases
    '''

    ###### ORIGIONAL IMPLEMENTATION FOR TESTS 1 AND 2 #####
    '''
    purchase_total = 0
    for price in list_of_prices:
        purchase_total += price + (price * (sales_tax_rate/100))

    return purchase_total
    '''

    ##### REFACTORED IMPLEMENTATION FOR TEST 3-6 #####
    purchase_total = 0
    for price in list_of_prices:
        purchase_total += price + (price * (sales_tax_rate/100))

    return round(purchase_total, 2)

###############################################################################

def test_calculate_purchase_total_with_one_item():

    list_of_prices = [10.00]
    sales_tax_rate = 10

    result = calculate_purchase_total(list_of_prices, sales_tax_rate)

    if result != 11: print('TEST 1 FAILED')

###############################################################################

def test_calculate_purchase_total_with_two_items():

    list_of_prices = [10.00, 5.00]
    sales_tax_rate = 10

    result = calculate_purchase_total(list_of_prices, sales_tax_rate)

    if result != 16.5: print('TEST 2 FAILED')

###############################################################################

def test_calculate_purchase_total_with_more_than_two_decimals():

    list_of_prices = [10.00, 5.00]
    sales_tax_rate = 2.5

    result = calculate_purchase_total(list_of_prices, sales_tax_rate)

    if result != 15.38: print('TEST 3 FAILED')

###############################################################################

def test_calculate_purchase_total_with_0_sales_tax():

    list_of_prices = [10.00, 5.00]
    sales_tax_rate = 0

    result = calculate_purchase_total(list_of_prices, sales_tax_rate)

    if result != 15: print('TEST 4 FAILED')

###############################################################################

def test_calculate_purchase_total_with_100_sales_tax():

    list_of_prices = [10.00, 5.00]
    sales_tax_rate = 100

    result = calculate_purchase_total(list_of_prices, sales_tax_rate)

    if result != 30: print('TEST 5 FAILED')

###############################################################################

def test_calculate_purchase_total_with_10_items():

    list_of_prices = [10.00, 5.00, 18.25, 22.69, 2.44, 12.65, 99.99, 3.12, 17.76, 19.41]
    sales_tax_rate = 10

    result = calculate_purchase_total(list_of_prices, sales_tax_rate)

    if result != 232.44: print('TEST 6 FAILED')

###############################################################################

def main():

    test_calculate_purchase_total_with_one_item()
    test_calculate_purchase_total_with_two_items()
    test_calculate_purchase_total_with_more_than_two_decimals()
    test_calculate_purchase_total_with_0_sales_tax()
    test_calculate_purchase_total_with_100_sales_tax()
    test_calculate_purchase_total_with_10_items()

###############################################################################

if __name__ == '__main__':
    main()
