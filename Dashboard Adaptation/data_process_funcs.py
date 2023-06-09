"""
the functions that fuel the data cleaning process
"""

# imports
import ast
from copy import copy
import math

def clean_list(lst):
    """
    cleans list by removing brackets, apostrophes, and commas from string and
    appending it to a new list

    Args:
    lst(list) : a list

    Returns;
    cleaned_feature_list
    """
    cleaned_feature_list = []
    for i in lst:
        i = i.strip("]").strip("[").strip("'").strip(",").strip("'")
        if i not in cleaned_feature_list:
            cleaned_feature_list.append(i)

    return cleaned_feature_list


def clean_str(string):
    """
    cleans string by removing brackets, apostrophes, and commas

    Args:
    str(str) : a string

    Returns:
    string(str) : a cleaned string

    """

    string = string.strip("]").strip("[]").strip("'").strip(",").strip("'")
    return string


def get_variable_list(dataframe, col_name):
    """
    Takes a column of lists in a dataframe, and creates a list of all variables
      mentioned in the column

    Args:
        dataframe(dataframe): the dataframe we want to add dummy columns to
        col_name(str): the name of the column that holds the lists of each
            trait or variable

    Returns:
       clean_variable_list (list): a list of all variables present in the column
    """
    # cleaning variable list to get a list of all vars
    variable_list = []

    # want to get all of the features within the dataset
    for row in range(len(dataframe)):
        list_test = dataframe[col_name][row].split()

        for variable_idx in range(len(list_test)):
            if list_test[variable_idx] not in variable_list:
                variable_list.append(list_test[variable_idx])

    # this is the list of all variables mentioned in the column
    clean_variable_list = clean_list(variable_list)

    return clean_variable_list


def add_dummy_variables(dataframe, col_name):
    """
    Takes a list of variables in a column of a dataset and adds each to
        a dataframe as unique dummy variable columns

    Args:
        dataframe(dataframe): the dataframe we want to add dummy columns to
        col_name(str): the name of the column that holds the lists of each
            trait or variable
    """
    # cleaning variable list to get a list of all vars
    clean_variable_list = get_variable_list(dataframe, col_name)

    # adding dummy variables for the feat_list
    for var in clean_variable_list:
        var_list = []

        for idx in range(0, len(dataframe)):
            if var in dataframe.loc[idx, col_name]:
                var_list.append(1)
            else:
                var_list.append(0)
        # add a column of these dummy values to the dataframe
        dataframe[var] = var_list


def convert_dict_like_string(df, col):
    """ converts a dict-like string to a dict

    Args:
        df (Pandas DataFrame): some dataframe
        col (pd df column): some column in the df where each row is a dict-like string

    Returns:
        dict_list (list): a list of the converted dicts
    """
    # initialize empty list
    dict_list = []

    # loop through every row in col and convert each value to a dict
    for item in df.loc[:, col]:
        dict_list.append(ast.literal_eval(item))

    return dict_list


def value_lists(lst):
    """ creates lists of values from a list of dicts with 2 values

    Args:
        lst (list): some list of dicts with 2 values

    Returns:
        val0_list (list): list of the first val in all dicts in lst
        val1_list (list): list of the second val in all dicts in lst
        val2_list (list): list of the populairty of all values in dict
    """

    # initialize empty lists
    val0_list = []
    val1_list = []
    val2_list = []

    # loop through larger list
    for i in range(len(lst)):
        # add first value of the dict lst[i] to a list
        val0_list.append(list(lst[i].values())[0])
        # add second value of the dict lst[i] to a list
        val1_list.append(list(lst[i].values())[1])
        # add color to list
        # val2_list.append(df.loc[i, 'avg_rating'])

    return val0_list, val1_list, val2_list


def continental_us_coords(lat_list, long_list):
    """ IDs coords from within the continental US from lists

    Args:
        lat_list (list): some list of lattitudes
        long_list (list): some list of longitudes

    Returns:
        continental_lat_list (list): list of lats only including those within the continental US
        continental_long_list (list): list of longs only including those within the continental US
        continental_popularity_list (list): a list of popularity only including the popularity of parks within the
                                continental US
    """
    # initialize continential lat, lon, and popularity lists
    continental_long_list = []
    continental_lat_list = []
    continental_popularity_list = []

    # loop through the longitude list
    for i in range(len(long_list)):
        # if the index is greater than -130, append onto new continental lists
        if long_list[i] > -130:
            continental_long_list.append(long_list[i])
            continental_lat_list.append(lat_list[i])
            continental_popularity_list.append(df.loc[i, 'avg_rating'])
            # return
    return continental_lat_list, continental_long_list, continental_popularity_list



