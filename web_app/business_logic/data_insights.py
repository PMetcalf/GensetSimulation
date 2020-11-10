'''
data_insights

This file supports data calculation and processing operations.

'''

# Module Importations
import datetime
import pandas as pd

def return_min(generation_type, df_original):
    """Return Min
    ======================================
    Returns the minimum generation of a particular generation type, calculated from a supplied dataframe.
    
    Args:
        generation_type (string) - Type of generation to determine mean for.
        df_original (DataFrame) - Dataframe with time-series generation data.
        
    Returns:
        min (float64) - Minimum value determined for generation type.
    """

    # Copy dataframe
    df_min = df_original.copy()

    # Filter dataframe for generation type
    df_min = df_min[(df_min['powType'] == generation_type)]

    # Calculate minimum generation for type
    min = df_min['quantity'].min()

    # Return minimum
    return min

def return_mean(generation_type, df_original):
    """Return Mean
    ======================================
    Returns the mean of a particular generation type, calculated from a supplied dataframe.
    
    Args:
        generation_type (string) - Type of generation to determine mean for.
        df_original (DataFrame) - Dataframe with time-series generation data.
        
    Returns:
        mean (float64) - Arithmetic mean determined for generation type.
    """

    # Copy dataframe
    df_mean = df_original.copy()

    # Filter dataframe for generation type
    df_mean = df_mean[(df_mean['powType'] == generation_type)]

    # Calculate mean generation for type
    mean = df_mean['quantity'].mean()

    # Return mean
    return mean

def return_summary_df(df_original, 
                      start_date = datetime.datetime(2020,1,1, 0, 0, 0), 
                      end_date = datetime.datetime(2021,1,1, 0, 0, 0)):
    """Return Stats Summary Dataframe
    ======================================
    Returns a new dataframe summarising generation data stats.
    
    Args:
        df_original (DataFrame) - Dataframe with time-series generation data.
        start_date (Datetime) - Earliest date for inclusion in stats calculations.
        end_date (Datetime) - Latest date for inclusion in stats calculations.
        
    Returns:
        df_summary_stats (DataFrame) - New dataframe containing aggregated data.
    """
    
    # Copy dataframe

    # Trim dataframe to start and end dates

    # Create dict for new dataframe, containing each parameter of interest

    # Iterate over dict keys and populate stats

    # Create and return df from dict

    pass

def return_aggregate_df(df_original):
    """Return Aggregate Dataframe
    ======================================
    Returns a new dataframe of aggregated generation.
    
    Args:
        df_original (DataFrame) - Dataframe with time-series generation data.
        
    Returns:
        df_aggregated (DataFrame) - New dataframe containing aggregated data.
    """

    # Copy time-series dataframe
    df_time_series = df_original.copy()

    # Create dict for generation types and aggregate total
    aggregated_generation = {
        "Solar": 0,
        "Wind Offshore": 0,
        "Wind Onshore": 0,
        "Hydro Run-of-river and poundage": 0,
        "Hydro Pumped Storage": 0,
        "Other": 0, 
        "Nuclear": 0, 
        "Fossil Oil": 0, 
        "Fossil Gas": 0, 
        "Fossil Hard coal": 0, 
        "Biomass": 0
        }

    # Iterate over time-series dataframe and populate aggregate dict
    for key in aggregated_generation:

        df_generation = df_time_series[df_time_series['powType'] == key]

        generation_sum = df_generation['quantity'].sum()

        aggregated_generation[key] = generation_sum

    # Convert aggregate dict to dataframe
    aggregate_df = pd.DataFrame.from_dict(aggregated_generation, orient = 'index')
    
    aggregate_df.index.rename('powType', inplace=True)
    aggregate_df.columns = ['quantity']

    # Return dataframe
    return aggregate_df

def return_renewable_aggregate_df(df_original):
    """Return Renewable Aggregate Dataframe
    ======================================
    Returns a new dataframe of aggregated renewable generation.
    
    Args:
        df_original (DataFrame) - Dataframe with time-series generation data.
        
    Returns:
        df_renewable_aggregated (DataFrame) - New dataframe containing aggregated data.
    """

    # Copy time-series dataframe
    df_time_series = df_original.copy()

    # Create dict for generation types and aggregate total
    aggregated_generation = {
        "Solar": 0,
        "Wind Offshore": 0,
        "Wind Onshore": 0,
        "Hydro Run-of-river and poundage": 0,
        "Hydro Pumped Storage": 0,
        "Biomass": 0
        }

    # Iterate over time-series dataframe and populate aggregate dict
    for key in aggregated_generation:

        df_generation = df_time_series[df_time_series['powType'] == key]

        generation_sum = df_generation['quantity'].sum()

        aggregated_generation[key] = generation_sum

    # Convert aggregate dict to dataframe
    aggregate_df = pd.DataFrame.from_dict(aggregated_generation, orient = 'index')
    
    aggregate_df.index.rename('powType', inplace=True)
    aggregate_df.columns = ['quantity']

    # Return dataframe
    return aggregate_df
