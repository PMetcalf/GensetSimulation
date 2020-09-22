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

def return_datetime_id():
    """Return Datetime Id
    ======================================
    Returns a datetime id based on date and settlement period from data instance.
    
    Args:
        setDate (str) - Settlement date.
        setPeriod (str) - Settlement period.
        
    Returns:
        datetime_id (str) - Datetime (UTC) stamp returned as a string.
    """

    # Determine if date is GMT or BST (impacts UTC hour)

        # If GMT-winter

            # Look-up UTC hour from period

            # Return date-setPeriod concatenation

        # If BST

            # Look-up UTC hour from period

            # Correct date, if required (Periods 1 & 2)

            # Return date-setPeriod concatenation

    pass