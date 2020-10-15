import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import plotly.express as px
import pandas as pd
#import sys

#sys.path.append('D:\Developer Area\e-grid_analytics\web_app\business_logic')
import app_data_munging as munging 

DF_SAVE_STRING = 'D:\Developer Area\e-grid_analytics\data_analytics\data\interim\dash_data.pkl'

app = dash.Dash(__name__,
                meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}],
)

df_new = pd.read_pickle(DF_SAVE_STRING)

def build_banner():
    """
    Builds banner displayed at top of page.
    """
    return html.Div(
        id = "banner",
        className = "banner",
        children = [
            html.Div(
                id = "banner-text",
                children = [
                    html.H5('Electricity Grid Analytics'),
                    html.H6('UK Electrical Generation Data'),
                ],
            ),
            html.Div(
                id = "banner-logo",
                children = [
                    html.Button(
                        id = "cloudforest-button", children="Cloudforest", n_clicks=0
                    ),
                ],
            ),
        ],
    )

def build_tabs():
    """
    Builds tab used to contain data visualisation collections.
    """
    return html.Div(
        id = "tabs",
        className = "tabs",
        children = [
            dcc.Tabs(
                id = "app-tabs",
                value = "tab1",
                className = "custom-tabs",
                children = [
                    dcc.Tab(
                        id = "Time-series-tab",
                        label = "Historic Data",
                        value = "tab1",
                        className = "custom-tab",
                        selected_className = "custom-tab--selected",
                    ),
                 #   dcc.Tab(    # Remove once solution validated
                  #      id = "Prediction-tab",
                  #      label = "Prediction Data",
                  #      value = "tab2",
                  #      className = "custom-tab",
                  #      selected_className = "custom-tab--selected",
                    #),
                ],
            )
        ],
    )

def generate_section_banner(title):
    """
    Returns a styled section banner with title.
    """
    return html.Div(
        className = "section-banner",
        children = title
                    )

def build_chart_panel():
    """
    Builds chart panel with data visualisations.
    """
    return html.Div(
        id = "timeseries-chart-container",
        className = "eight columns",
        children = [
            generate_section_banner("Generation Time Series"),
            generate_time_series_scatter()
            ]
        )

def generate_time_series_scatter():
    """
    Generates time-series scatter graph.
    """

    # Create figure using plotly express
    fig = px.scatter(df_new, x = "setDatetime", y = "quantity", color = "powType",
                 labels = {
                     "setDatetime": "Date",
                     "quantity": "Generation (MW)",
                     },
                 )
    
    # Adjust figure styling
    fig.update_layout(
        paper_bgcolor = "rgba(0,0,0,0)",
        plot_bgcolor = "rgba(0,0,0,0)",
        font_color = "white",
        legend = dict(
            orientation = "h",
            yanchor = "bottom",
            y = 1.02,
            xanchor = "left",
            x = 0,
            ),
        legend_title_text =""
        )

    # Wrap and return figure
    return dcc.Graph(
        id = "time-series-chart",
        figure = fig
        )

def build_side_panel():
    """
    Builds panel containing piecharts.
    """
    return html.Div(
        id = "aggregates-container",
        className="row",
        children = [
            # Energy Piechart
            html.Div(
                id = "rem-piechart-outer",
                className = "four columns",
                children = [
                    generate_section_banner("Renewable Energy Mix"),
                    generate_piechart(),
                    ],
                ),
            html.Div(
                id = "aam-piechart-outer",
                className = "four columns",
                children = [
                    generate_section_banner("Aggregated Annual Mix"),
                    generate_aggregate_piechart(),
                    ],
                ),
            ],
        )

def generate_piechart():
    """
    Build and return a piechart.
    """

    # df for prototyping
    labels = ['Wind Offshore','Solar','Wind Onshore','Hydro']
    values = [4500, 2500, 1053, 500]
    d = { 'Generation': labels, 'Amount': values}
    df_1 = pd.DataFrame(d)
   
    # Create figure using plotly express
    fig = px.pie(df_1, 
                 values = "Amount", 
                 names = "Generation", 
                 color = "Generation")
    
    # Adjust figure styling
    fig.update_layout(
        autosize = True,
        margin = dict(l=50, r=120, t=50, b=120),
        paper_bgcolor = "rgba(0,0,0,0)",
        plot_bgcolor = "rgba(0,0,0,0)",
        font_color = "white",
        )

    # Wrap and return figure
    return dcc.Graph(
        id = "piechart",
        figure = fig
        )


def generate_aggregate_piechart():
    """
    Build and return an aggregate piechart.
    """

    # df for prototyping
    aggregate_df = munging.return_aggregate_df(df_new)
   
    # Create figure using plotly express
    fig = px.pie(aggregate_df, 
                 values = "Amount", 
                 names = "Generation", 
                 color = "Generation")
    
    # Adjust figure styling
    fig.update_layout(
        autosize = True,
        margin = dict(l=50, r=120, t=50, b=120),
        paper_bgcolor = "rgba(0,0,0,0)",
        plot_bgcolor = "rgba(0,0,0,0)",
        font_color = "white",
        )

    # Wrap and return figure
    return dcc.Graph(
        id = "piechart",
        figure = fig
        )


@app.callback(
    [Output("app-content", "children")],
    [Input("app-tabs", "value")],
)
def render_tab_content(tab_switch):
    """
    Render content of tab upon request.
    """
    return (
        html.Div(
            id = "status-container",
            #className = "row",
            children = [
                html.Div(
                    id = "graphs-container",
                    children = [build_chart_panel(), build_side_panel()],
                    ),                
                ],
            ),
        )

app.layout = html.Div(
    id = "big-app-container",
    children = [
        build_banner(),
        html.Div(
            id = "app-container",
            children = [
                build_tabs(),
                html.Div(id = "app-content"),
                ],
            ),
        ]
    )

if __name__ == '__main__':
    app.run_server(debug=True)