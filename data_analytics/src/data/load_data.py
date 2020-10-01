'''
load_data

This file supports load and save operations.

'''

# Module Importations
import pandas as pd

# CONSTANTS
DF_SAVE_STRING = 'C:\Developer\PMetcalf\GensetSimulation\GensetSimulation\data_analytics\data\interim\interim_data.pkl'

def convert_dict_to_dataframe(items_dict):
    """Convert to Dataframe
    ======================================
    Converts dict of raw database items into dataframe.
    
    Args:
        items_dict (dict) - Dict of items from database container.
        
    Returns:
        df (dataframe) - Dataframe containing items from container list.
    """
    
    # Convert directly into dataframe
    df_items = pd.DataFrame(items_dict)

    print("Converted to dataframe ...")

    # Return dataframe
    return df_items

def save_local_dataframe(df):
    """Save Local Dataframe
    ======================================
    Saves dataframe locally using pickle format.
    
    Args:
        df (DataFrame) - Dataframe to be pickled locally.
        
    Returns:
        None.
    """
    df.to_pickle(DF_SAVE_STRING)

    print("Saved dataframe locally ...")

def save_dash_dataframe(df):
    """Save Local Dataframe
    ======================================
    Saves dataframe for dash development using pickle format.
    
    Args:
        df (DataFrame) - Dataframe to be pickled locally.
        
    Returns:
        None.
    """

    DASH_STRING = 'C:\Developer\PMetcalf\GensetSimulation\GensetSimulation\data_analytics\data\interim\dash_data.pkl'

    df.to_pickle(DASH_STRING)

    print("Saved dataframe for Dash ...")

def load_local_dataframe():
    """Save Local Dataframe
    ======================================
    Saves dataframe locally using pickle format.
    
    Args:
        None.
        
    Returns:
        df (DataFrame) - Dataframe loaded from local pickle.
    """

    df_new = pd.read_pickle(DF_SAVE_STRING)
 
    print("Loaded local dataframe ...")

    # Print information about dataframe
    print(df_new.info())

    return df_new  