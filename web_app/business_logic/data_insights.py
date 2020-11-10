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
        generation_type (string) - Type of generation to determine minimum for.
        df_original (DataFrame) - Dataframe with time-series generation data.
        
    Returns:
        min_generation (float64) - Minimum value determined for generation type.
    """

    # Copy dataframe
    df_min = df_original.copy()

    # Filter dataframe for generation type
    df_min = df_min[(df_min['powType'] == generation_type)]

    # Calculate minimum generation for type
    min_generation = df_min['quantity'].min()

    # Return minimum
    return min_generation

def return_max(generation_type, df_original):
    """Return Max
    ======================================
    Returns the maximum generation of a particular generation type, calculated from a supplied dataframe.
    
    Args:
        generation_type (string) - Type of generation to determine maximum for.
        df_original (DataFrame) - Dataframe with time-series generation data.
        
    Returns:
        max_generation (float64) - Maximum value determined for generation type.
    """

    # Copy dataframe
    df_max = df_original.copy()

    # Filter dataframe for generation type
    df_max = df_max[(df_max['powType'] == generation_type)]

    # Calculate maximum generation for type
    max_generation = df_max['quantity'].max()

    # Return maximum
    return max_generation

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

def return_sum(generation_type, df_original):
    """Return Sum
    ======================================
    Returns the generation sum of a particular generation type, calculated from a supplied dataframe.
    
    Args:
        generation_type (string) - Type of generation to be summed.
        df_original (DataFrame) - Dataframe with time-series generation data.
        
    Returns:
        sum_generation (float64) - Summed output determined for generation type.
    """

    # Copy dataframe
    df_sum = df_original.copy()

    # Filter dataframe for generation type
    df_sum = df_sum[(df_sum['powType'] == generation_type)]

    # Calculate summed generation for type
    sum_generation = df_sum['quantity'].sum()

    # Return sum
    return sum_generation

def return_total_sum(df_original):
    """Return Total Sum
    ======================================
    Returns the total sum of generation from a supplied dataframe.
    
    Args:
        df_original (DataFrame) - Dataframe with time-series generation data.
        
    Returns:
        total_sum_generation (float64) - Total summed output determined for dataframe.
    """

    # Copy dataframe
    df_total_sum = df_original.copy()

    # Calculate summed generation
    total_sum_generation = df_total_sum['quantity'].sum()

    # Return sum
    return total_sum_generation

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
    df_timeseries = df_original.copy()
    df_timeseries.sort_values(by = ['setDatetime'], inplace = True)
    
    # Mask dataframe between start and end dates
    start_date = datetime.datetime(2020,3,1, 0, 0, 0)
    end_date = datetime.datetime(2021,1,1, 0, 0, 0)
    
    df_timeseries = df_timeseries[(df_timeseries['setDatetime'] > start_date)]
    df_timeseries = df_timeseries[(df_timeseries['setDatetime'] < end_date)]
    
    # Calculate total generation across whole time series
    total_generation = return_total_sum(df_timeseries)

    # Create dict for new dataframe, containing each parameter of interest
    data_summary = {
        "Solar": [0, 0, 0, 0, 0],
        "Wind Offshore": [0, 0, 0, 0, 0],
        "Wind Onshore": [0, 0, 0, 0, 0],
        "Hydro Run-of-river and poundage": [0, 0, 0, 0, 0],
        "Hydro Pumped Storage": [0, 0, 0, 0, 0],
        "Other": [0, 0, 0, 0, 0], 
        "Nuclear": [0, 0, 0, 0, 0], 
        "Fossil Oil": [0, 0, 0, 0, 0], 
        "Fossil Gas": [0, 0, 0, 0, 0], 
        "Fossil Hard coal": [0, 0, 0, 0, 0], 
        "Biomass": [0, 0, 0, 0, 0]
        }

    # Iterate over dict keys and populate stats
    for key in data_summary:

        # Determine statistics for each generation type
        generation_min = return_mean(key, df_timeseries)
        generation_mean = return_mean(key, df_timeseries)
        generation_max = return_max(key, df_timeseries)
        generation_sum = return_sum(key, df_timeseries)
        generation_percent = (generation_sum / total_generation) * 100

        # Update dict with generation statistics
        data_summary[key][0] = generation_min
        data_summary[key][1] = generation_mean
        data_summary[key][2] = generation_max
        data_summary[key][3] = generation_sum
        data_summary[key][4] = generation_percent

    # Create and return df from dict
    df_summary = pd.DataFrame.from_dict(data_summary, orient='index')

    # Update column labels
    df_summary.rename(columns = {0: "Min", 1:"Mean", 2:"Max", 3:"Sum", 4:"% Total"}, inplace=True)

    return df_summary

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
