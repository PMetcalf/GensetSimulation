import os
import pathlib
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import plotly.express as px
import pandas as pd

# Custom module imports
from business_logic import data_insights

app = dash.Dash(__name__,
                meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}],
)

server = app.server

APP_PATH = str(pathlib.Path(__file__).parent.resolve())

df_new = pd.read_pickle(os.path.join(APP_PATH, os.path.join("data", "dash_data.pkl")))

df_summary = data_insights.return_summary_df(df_new)

print(df_summary)
