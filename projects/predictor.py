
# This is a template for your project 2 submission. 
# Please fill in the get_predictions method to return key-value pairs 
# for each parcelid and the predicted log-error. 

# Import the libraries and give them abbreviated names:
import pandas as pd
import numpy as np
import statsmodels.api as sm

# load the data, use the directory where you saved the data: (please do not change)
df_properties = pd.read_csv('properties_2017.csv') 
df_train = pd.read_csv('train_2017.csv', parse_dates=["transactiondate"])


def get_predictions():
    predictions = {}
    # write code here
    # fill in your algorithm to calculate predicted log-error values here
    return predictions

