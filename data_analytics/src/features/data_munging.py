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
    """Remove quotations
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