import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import plotly.express as px
import pandas as pd

DF_SAVE_STRING = 'D:\Developer Area\e-grid_analytics\data_analytics\data\interim\dash_data.pkl'

app = dash.Dash(__name__)

df_new = pd.read_pickle(DF_SAVE_STRING)

def build_banner():
    """
    Builds banner displayed at top of page.
    """
    return html.Div(
        id="banner",
        className="banner",
        children=[
            html.Div(
                id="banner-text",
                children=[
                    html.H5('Electricity Grid Analytics'),
                    html.H6('UK Electrical Generation Data'),
                ],
            ),
            html.Div(
                id="banner-logo",
                children=[
                    html.Button(
                        id="cloudforest-button", children="Cloudforest", n_clicks=0
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
                        label = "Time Series Data",
                        value = "tab1",
                        className = "custom-tab",
                        selected_className = "custom-tab--selected",
                    ),
                ],
            )
        ],
    )

def build_chart_panel():
    """
    Builds chart panel with data visualisations.
    """
    return html.Div(
        id = "control-chart-container",
        children = [
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
                     "powType": "Generation Type"
                     },
                 )
    
    # Adjust figure styling
    fig.update_layout(
        paper_bgcolor = "rgba(0,0,0,0)",
        plot_bgcolor = "rgba(0,0,0,0)",
        legend = dict(
            orientation = "h",
            yanchor = "bottom",
            y = 1.02,
            xanchor = "left",
            x = 0
            )
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
        id = "top-section-container",
        children = [
            # Energy Piechart
            html.Div(
                id = "ooc-piechart-outer",
                className = "three columns",
                children = [
                    generate_piechart(),
                    ],
                ),
            ],
        )

def generate_piechart():
    """
    Build and return a piechart.
    """
    return dcc.Graph(
        id="piechart",
        figure={
            "data": [
                {
                    "labels": ['Solar', 'Wind', 'Hydro'],
                    "values": [15, 12, 18],
                    "type": "pie",
                    "marker": {"line": {"color": "white", "width": 1}},
                    "hoverinfo": "label",
                    "textinfo": "label",
                }
            ],
            "layout": {
                "showlegend": True,
                "paper_bgcolor": "rgba(0,0,0,0)",
                "plot_bgcolor": "rgba(0,0,0,0)",
                "font": {"color": "white"},
                "autosize": True,
            },
        },
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
            id = "graphs-container",
            className = "row",
            children = [
                build_chart_panel(),
                build_side_panel(),
                ],
            ),
        )

app.layout = html.Div(
    id = "main-app-container",
    children=[
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