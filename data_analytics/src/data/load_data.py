'''
load_data

This file supports load and save operations.

'''

# Module Importations

# CONSTANTS

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

def save_local_dataframe():
    pass

def load_local_dataframe():
    pass