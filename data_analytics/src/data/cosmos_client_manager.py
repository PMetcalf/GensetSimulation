'''
cosmos_client_manager

This file connection and CRUD operations with the Cosmos DB storing data.

'''

# Module Importations
import azure.cosmos.cosmos_client as cosmos_client
import azure.cosmos.exceptions as exceptions
from azure.cosmos.partition_key import PartitionKey

# Project Modules
#import config

# Constants
HOST = "https://purple-finch.documents.azure.com:443/"
MASTER_KEY = "M3dHFbTy3F7ov7X2qbyxund4sMVtjC8PNGS25ocbFOpfDPG9iTG6euVOem7Kq3gTVB5LAoUaEW3HZayRsnhp1w=="
DATABASE_ID = "BMRS Data"
CONTAINER_ID = "DataElement"

#HOST = config.settings['host']
#MASTER_KEY = config.settings['master_key']
#DATABASE_ID = config.settings['database_id']
#CONTAINER_ID = config.settings['container_id']

def intialise_client():
    """Initialise Client Routine
    ======================================
    Initialise and return database connection client.
    
    Args:
        None.
        
    Returns:
        client (client) - Database connection client.
    """
    client = cosmos_client.CosmosClient(HOST, {'masterKey': MASTER_KEY})

    return client

def return_database(client):
    """Return Database
    ======================================
    Returns database via client.
    
    Args:
        client (client) - Database connection client.
        
    Returns:
        database (database) - Database.
    """
    # Try to find and return database
    try:
        database = client.get_database_client(DATABASE_ID)
        print("Database with id \'{0}\' was found, link is {1}".format(DATABASE_ID, database.database_link))

        return database

    # Manage if database cannot be found
    except exceptions.CosmosResourceNotFoundError:
        print("Database with id \'{0}\' was not found".format(DATABASE_ID))


def return_container(database):
    """Return Container
    ======================================
    Returns database container for CRUD operations.
    
    Args:
        database (database) - Database with client connection.
        
    Returns:
        container (container) - Container.
    """
    # Try to find and return container
    try:
        container = database.get_container_client(CONTAINER_ID)
        print("Container with id \'{0}\' was found, link is {1}".format(CONTAINER_ID, container.container_link))

        return container

    # Manage if container cannot be found
    except exceptions.CosmosResourceNotFoundError:
        print("Container with id \'{0}\' wasn not found".format(CONTAINER_ID))

def read_items(container):
    """Read Items
    ======================================
    Returns full list of items from container.
    
    Args:
        container (container) - Container.
        
    Returns:
        item_list (list) - List of items found in container.
    """
    print('Reading all items in container')

    # Read all items from container
    item_list = list(container.read_all_items(max_item_count=10))

    # Count items
    print('Found {0} items'.format(item_list.__len__()))

    # Return list
    return item_list

def query_items():
    """Query Items
    ======================================
    Returns list of items associated with query from container.
    
    Args:
        container (container) - Container.
        query (string) - Query, usually ID, associated with query.
        
    Returns:
        list (list) - List of items found from query.
    """
    pass

def convert_to_dataframe():
    """Convert to Dataframe
    ======================================
    Converts list of raw database items into dataframe.
    
    Args:
        list (list) - List of items from database container.
        
    Returns:
        df (dataframe) - Dataframe containing items from container list.
    """
    pass