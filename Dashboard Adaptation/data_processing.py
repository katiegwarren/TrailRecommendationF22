"""
takes in the raw dataset and cleans columns
into usable formats for ML and dashboard
"""

# imports
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
import data_process_funcs as dpf
import ast
from copy import copy
import math


# importing data
df = pd.read_csv('AllTrails data - nationalpark.csv')

# remove unnecessary unit column
del df['units']

# call in data processing functions

# make features and activities dummy variables
dpf.add_dummy_variables(df, 'features')
dpf.add_dummy_variables(df, 'activities')

# initialize dict_list
dict_list = dpf.convert_dict_like_string(df, '_geoloc')
# initialize list_tuple
list_tuple = dpf.value_lists(dict_list)
# add lat and long colums
df['lat'] = list_tuple[0]
df['long'] = list_tuple[1]

# drop geoloc column
df.drop('_geoloc', inplace=True, axis=1)

# removing rows that have empty spots
df = df.dropna()

# make a column for dogs-yes to be opposite of dogs-no
# set default of column to be true
df['dogs-yes'] = 1
dogs_yes_idx = df.columns.get_loc('dogs-yes')
dogs_no_idx = df.columns.get_loc('dogs-no')

# iterate through the dataframe
for i in range(len(df.index)):
    # if dogs-no is true, change dogs-yes to false
    if df.iloc[i, dogs_no_idx] == 1:
        df.iloc[i, dogs_yes_idx] = 0

# reset index
df.reset_index(inplace = True,drop = True)

# export to final dataset
df.to_csv('trail dataset.csv')