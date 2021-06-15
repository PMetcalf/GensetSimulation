# Module Importations
import pandas as pd

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
        "Hydro Pumped Storage": 0
        }

    # Iterate over time-series dataframe and populate aggregate dict
    for key in aggregated_generation:

        df_generation = df_time_series[df_time_series['powType'] == key]

        generation_sum = df_generation['quantity'].sum()

        aggregated_generation[key] = generation_sum

    print(aggregated_generation)

    # Convert aggregate dict to dataframe
    aggregate_df = pd.DataFrame.from_dict(aggregated_generation, orient = 'index')
    
    aggregate_df.index.rename('powType', inplace=True)
    aggregate_df.columns = ['quantity']

    # Return dataframe
    return aggregate_df
