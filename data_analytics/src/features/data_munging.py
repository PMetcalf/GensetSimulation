'''
data_munging

This file supports data cleaning and preprocessing operations.

'''

# Module Importations
import pandas as pd
from dateutil import parser

def remove_unused_columns(df_original):
    """Remove Unused Columns
    ======================================
    Removes unused / unecessary columns from base dataframe, returning a new dataframe.
    
    Args:
        df_original (DataFrame) - Dataframe to have columns removed.
        
    Returns:
        df_modified (DataFrame) - New dataframe to have columns removed.
    """

   # Create copy of original dataframe
    df_modified = df_original.copy()

    print("Removing unused columns ...")

    # Remove column names from dataframe
    df_modified = df_modified.drop("_rid", axis = 1)
    df_modified = df_modified.drop("_self", axis = 1)
    df_modified = df_modified.drop("_etag", axis = 1)
    df_modified = df_modified.drop("_attachments", axis = 1)
    
    print("Unused columns removed.")

    # Return dataframe copy
    return df_modified

def remove_quotations(quotation_string):
    """Remove Quotations
    ======================================
    Removes quotations around string objects.
    
    Args:
        quotation_string (str) - String to have quotations removed.
        
    Returns:
        dequoted_string (str) - String with quotations removed.
    """

    # Remove quotations
    dequoted_string = quotation_string.strip('"')

    # Return string
    return dequoted_string

def convert_string_to_float(numeric_string):
    """Convert String to Float
    ======================================
    Converts a (numeric) string object to floating point number.
    
    Args:
        numeric_string (str) - String to be converted.
        
    Returns:
        numeric_float (float) - float cast from string.
    """

    # Convert string
    numeric_float = float(numeric_string)

    # Return float
    return numeric_float

def return_datetime_id(setDate, setPeriod):
    """Return Datetime Id
    ======================================
    Returns a datetime id based on date and settlement period from data instance.
    
    Args:
        setDate (str) - Settlement date.
        setPeriod (float) - Settlement period.
        
    Returns:
        datetime_id (str) - Datetime (UTC) stamp returned as a string.
    """

    # Convert settlement period to hour
    setPeriods = {
        1.0 : '0000', 2.0 : '0030', 3.0 : '0100', 4.0 : '0130', 5.0 : '0200',
        6.0 : '0230', 7.0 : '0300', 8.0 : '0330', 9.0 : '0400', 10.0 : '0430',
        11.0 : '0500', 12.0 : '0530', 13.0 : '0600', 14.0 : '0630', 15.0 : '0700',
        16.0 : '0730', 17.0 : '0800', 18.0 : '0830', 19.0 : '0900', 20.0 : '0930',
        21.0 : '1000', 22.0 : '1030', 23.0 : '1100', 24.0 : '1130', 25.0 : '1200',
        26.0 : '1230', 27.0 : '1300', 28.0 : '1330', 29.0 : '1400', 30.0 : '1430',
        31.0 : '1500', 32.0 : '1530', 33.0 : '1600', 34.0 : '1630', 35.0 : '1700',
        36.0 : '1730', 37.0 : '1800', 38.0 : '1830', 39.0 : '1900', 40.0 : '1930',
        41.0 : '2000', 42.0 : '2030', 43.0 : '2100', 44.0 : '2130', 45.0 : '2200',
        46.0 : '2230', 47.0 : '2300', 48.0 : '2330', 49.0 : '2300', 50.0 : '2330'
    }

    setTime = setPeriods[setPeriod]

    # Create datetime string
    datetime_string = setDate + " " + setTime

    # Convert to datetime
    datetime_date = parser.parse(datetime_string)

    # Return datetime
    return datetime_date




    # Convert date string to time


    # Determine year

    # Look up GMT/BST dates for year

    # Determine if date is GMT or BST (impacts UTC hour)

        # If GMT-winter

            # Look-up UTC hour from period

            # Return date-setPeriod concatenation

        # If BST

            # Look-up UTC hour from period

            # Correct date, if required (Periods 1 & 2)

            # Return date-setPeriod concatenation

    pass