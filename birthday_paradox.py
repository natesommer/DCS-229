import random # importing random library

def birthday_paradox(n,loops): # function takes number of birthdays 'n' and number of testing loops 'loops'

    result = [] # initialize list for containing results

    for i in range(loops): # loop through for testing
        bdays = [] # initializie list for containing birthday values

        for i in range(n): # loop through number of birthdays
            bday = random.randint(0,365) # initialize variable for random birthday

            if bday in bdays: # conditional for birthday matching another birthday in testing loop
                result.append('match') # appending value for testing calculations
                break # cancel testing loop if condition is met

            else: bdays.append(bday) # append birthday value if condition is not met

    probability = round(((len(result)/loops)*100),1) # calculating probability from testing results

    return probability # return probability integer

def main(): # function used for calling birthday_paradox function and printing result statement

    n = 23 # initialize variable for number of birthdays
    loops = 10000 # initializie variable for number of testing loops
    probability = birthday_paradox(n,loops) # call and store result of birthday_paradox function

    print(f"The probability of two people in a group of {n} people having the same birthday is {probability}%")

main()
