'''
data_munging

This file supports data cleaning and preprocessing operations.

'''

# Module Importations
import pandas as pd

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
        1.0 : '0000', 2.0 : '0000', 3.0 : '0000', 4.0 : '0000', 5.0 : '0000',
        6.0 : '0000', 7.0 : '0000', 8.0 : '0000', 9.0 : '0000', 10.0 : '0000',
        11.0 : '0000', 12.0 : '0000', 13.0 : '0000', 14.0 : '0000', 15.0 : '0000',
        16.0 : '0000', 17.0 : '0000', 18.0 : '0000', 19.0 : '0000', 20.0 : '0000',
        21.0 : '0000', 22.0 : '0000', 23.0 : '0000', 24.0 : '0000', 25.0 : '0000',
        26.0 : '0000', 27.0 : '0000', 28.0 : '0000', 29.0 : '0000', 30.0 : '0000',
        31.0 : '0000', 32.0 : '0000', 33.0 : '0000', 34.0 : '0000', 35.0 : '0000',
        36.0 : '0000', 37.0 : '0000', 38.0 : '0000', 39.0 : '0000', 40.0 : '0000',
        41.0 : '0000', 42.0 : '0000', 43.0 : '0000', 44.0 : '0000', 45.0 : '0000',
        46.0 : '0000', 47.0 : '0000', 48.0 : '0000', 49.0 : '0000', 50.0 : '0000'
    }

    setTime = setPeriods[setPeriod]

    # Create datetime string

    # Convert to datetime

    # Return datetime





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