'''
Author:     Nate Sommer
Topic:      Python Review
Date:       9/3/2021
'''
###############################################################################

import statistics

###############################################################################

def read_file(filename, use_dict = False):
    '''
    Parameters
    ----------
    filename : string
        the name of a text file
    use_dict : boolean
        enter parameter as 'True' to return a dictionary

    Returns
    -------
    If use_dict = False:

        unique_words : list
            list of the unique words of the text file
        word_counts : list
            list of the word count of each unique word in the text file

    If use_dict = True:

        words_dict : dictionary
            a dictionary of unique words as keys and their corresponding count as values
    '''

    with open(filename, 'r') as infile: # reads in a text file
        words = infile.read().lower().split() # cleans the text and stores it in a list

        words_dict = {} # initializing a dictionary to store unique words and their counts
        for word in words: # iterating through the words list

            punctuation = '''!()-[]{};:'"\, <>./?@#$%^&*_~''' # initializing string of punctuation
            for letter in word: # iterating through letters in word
                if letter in punctuation: word = word.replace(letter, "") # conditional for replacing punctuation

            if word not in words_dict.keys(): words_dict[word] = 1 # conditional for establishing keys
            else: words_dict[word] += 1 # conditional for updating key values

        unique_words = [ key for key,value in words_dict.items() ] # building a list for unique words
        word_counts = [ value for key,value in words_dict.items() ] # building a list for word counts

    if use_dict == False: return unique_words,word_counts # returning lists
    if use_dict == True: return words_dict # returning dictionary

###############################################################################

def read_hist(words_dict):
    '''
    Parameters
    ----------
    words_dict : dictionary
        a dictionary containing keys of words and values of their
        corresponding count

    Returns
    -------
    None
    '''

    value_list = [] # initializing list for values
    key_list = [] # initializing list for keys
    for i in range(10): # iterating through the top 10 largest words

        max_value = max(words_dict.values()) # storing max word count
        max_key = max(key for key,value in words_dict.items() if value == max_value) # storing corresponding word
        value_list.append(max_value) # appending max value to list
        key_list.append(max_key) # appending corresponding key to list
        del words_dict[max_key] # removing max key for next iteration

    mean = statistics.mean(value_list) # storing mean of largest word counts
    stdev = statistics.stdev(value_list) # storing standard deviation of largest word counts

    scaled_values = [] # initializing list for scaled values
    for value in value_list: # iterating through non-scaled values
        value = (value-mean)/stdev # computing z-score for scaling
        scaled_values.append(value) # appending scaled value to list

    for i in range(len(key_list)): # iterating through largest word counts

        if value_list[i] <= 100: histogram = '*' * value_list[i] # creating a non-scaled histogram display
        else: histogram = '*' * scaled_values[i] # creating a scaled histogram display

        print(f"{key_list[i]}\t\t{histogram}") # printing histogram

###############################################################################

def main():

    words_dict = read_file("wilco.txt", True)
    read_hist(words_dict)

###############################################################################

if __name__ == "__main__":
    main()
