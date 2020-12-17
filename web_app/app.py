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

# Load data
df_new = pd.read_pickle(os.path.join(APP_PATH, os.path.join("data", "dash_data.pkl")))
df_new = data_insights.rename_dataframe_powertypes(df_new)

# Create summary dataframes
summary_df = data_insights.return_summary_df(df_new, is_renewable = False)
renewable_summary_df = data_insights.return_summary_df(df_new, is_renewable = True)

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
    Builds tabs used for About, Visualisation & Prediction (Beta).
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
                        id = "About-tab",
                        label = "About",
                        value = "tab1",
                        className = "custom-tab",
                        selected_className = "custom-tab--selected",
                    ),
                    dcc.Tab(
                        id = "Time-series-tab",
                        label = "Historic Data",
                        value = "tab2",
                        className = "custom-tab",
                        selected_className = "custom-tab--selected",
                    ),
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

def build_intro_panel():
    """
    Builds intro panel for historic data panel
    """
    return html.Div(
        id = "quick-stats",
        className = "row",
        children = [
            html.Div(
                id = "card-1",
                children = [
                    generate_section_banner("Electricity Generation Data"),
                    html.P('This tab contains historic electricity generation data.'),
            ],
                ),
            html.Div(
                id = "card-1",
                children = [
                    html.P('Select start and end dates below.')
            ],
                ),
            ],
        )

def build_chart_panel():
    """
    Builds chart panel with data visualisations
    """
    return html.Div(
        id = "general-section-container",
        className = "eight columns",
        children = [
            generate_section_banner("Time-Series Data"),
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

def build_table_panel():
    """
    Builds table panel with generation data table.
    """
    return html.Div(
        id = "data-summary-outer",
        className = "row",
        children = [
            generate_section_banner("Generation Summary Statistics"),
            html.Div(
                id = "metric-div",
                children = [
                    generate_metric_list_header(),
                    html.Div(
                        id = "metric-rows",
                        children = [
                            generate_metric_row_helper(0),
                            generate_metric_row_helper(1),
                            generate_metric_row_helper(2),
                            generate_metric_row_helper(3),
                            generate_metric_row_helper(4),
                            generate_metric_row_helper(5),
                            generate_metric_row_helper(6),
                            generate_metric_row_helper(7),
                            generate_metric_row_helper(8),
                            generate_metric_row_helper(9),
                            generate_metric_row_helper(10)
                            ]
                        )
                    ]
                )
            ]
        )

    
def generate_metric_list_header():
    '''
    Generates data table header using row generator helper method.
    '''
    return generate_metric_row(
        "metric_header",    # Object Id
        {"height": "3rem", "margin": "1rem 0", "textAlign": "center"},  # The style
        {"id": "m_header_1", "children": html.Div("Generation Type")},
        {"id": "m_header_2", "children": html.Div("Min. [MW]")}, 
        {"id": "m_header_3", "children": html.Div("Mean [MW]")},
        {"id": "m_header_4", "children": html.Div("Max. [MW]")}, 
        {"id": "m_header_5", "children": html.Div("Total [GWhr]")},  
        {"id": "m_header_6", "children": html.Div("% Contribution")},   
    )

def generate_metric_row_helper(pow_type_index):
    '''
    Populates data in row objects returned to the data table.
    '''

    params = summary_df.index.unique()

    # Retrieve data for generation type
    item = params[pow_type_index]
    min_value = round(summary_df[summary_df.index == item]['Min'], 1)
    mean_value = round(summary_df[summary_df.index == item]['Mean'], 1)
    max_value = round(summary_df[summary_df.index == item]['Max'], 1)
    sum_value = round(summary_df[summary_df.index == item]['Sum'], 1)
    percent_value = round(summary_df[summary_df.index == item]['% Total'], 1)

    # Create ids for data elements
    div_id = item
    min_id = item + "_min"
    mean_id = item + "_mean"
    max_id = item + "_max"
    total_id = item + "_sum"
    percent_contribution_id = item + "_perc"

    # Generate row for generation type
    return generate_metric_row(
        div_id,
        None,
        {"id": div_id, "children": div_id}, 
        {"id": min_id, "children": min_value},   
        {"id": mean_id, "children": mean_value},   
        {"id": max_id, "children": max_value},   
        {"id": total_id, "children": sum_value},   
        {"id": percent_contribution_id, "children": percent_value},   
        )
    

def generate_metric_row(id, style, col1, col2, col3, col4, col5, col6):
    '''
    Returns html objects generated as rows to go in a table.
    '''

    if style is None:
        style = {"height": "8rem", "width": "100%"}

    return html.Div(
        id = id,
        className = "row metric-row",
        style = style,
        children = [
            html.Div(
                id = col1["id"],
                className = "one column",
                style = {"margin-right": "2.5rem", "minWidth": "50px"},
                children = col1["children"],
            ),
            html.Div(
                id = col2["id"],
                style = {"textAlign": "center"},
                className = "one column",
                children = col2["children"],
            ),
            html.Div(
                id = col3["id"],
                style = {"textAlign": "center"},
                className = "one column",
                children = col3["children"],
            ),
            html.Div(
                id = col4["id"],
                style = {"textAlign": "center"},
                className = "one column",
                children = col4["children"],
            ),
            html.Div(
                id = col5["id"],
                style = {"textAlign": "center"},
                className = "one column",
                children = col5["children"],
            ),
            html.Div(
                id = col6["id"],
                style = {"textAlign": "center"},
                className = "one column",
                children = col6["children"],
            ),
        ],
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
                    generate_renewable_aggregate_piechart(),
                    ],
                ),
            html.Div(
                id = "aam-piechart-outer",
                className = "four columns",
                children = [
                    generate_section_banner("Full Energy Mix"),
                    generate_aggregate_piechart(),
                    ],
                ),
            ],
        )

def generate_renewable_aggregate_piechart():
    """
    Build and return a renewable aggregate piechart.
    """

    # Create figure using plotly express
    fig = px.pie(renewable_summary_df, 
                 values = "Sum", 
                 names = renewable_summary_df.index, 
                 color = renewable_summary_df.index)
    
    # Adjust figure styling
    fig.update_layout(
        autosize = True,
        margin = dict(l = 50, r = 120, t = 50, b = 120),
        paper_bgcolor = "rgba(0,0,0,0)",
        plot_bgcolor = "rgba(0,0,0,0)",
        font_color = "white",
        )

    # Wrap and return figure
    return dcc.Graph(
        id = "ren_agg_piechart",
        figure = fig
        )

def generate_aggregate_piechart():
    """
    Build and return an aggregate piechart.
    """
   
    # Create figure using plotly express
    fig = px.pie(summary_df, 
                 values = "Sum", 
                 names = summary_df.index, 
                 color = summary_df.index)
    
    # Adjust figure styling
    fig.update_layout(
        autosize = True,
        margin = dict(l = 50, r = 120, t = 50, b = 120),
        paper_bgcolor = "rgba(0,0,0,0)",
        plot_bgcolor = "rgba(0,0,0,0)",
        font_color = "white",
        )

    # Wrap and return figure
    return dcc.Graph(
        id = "agg_piechart",
        figure = fig
        )

def build_tab_1():
    return html.Div(
            id = "set-specs-intro-container",
            children = html.Div(className = 'control-tab', 
                                children=[
                html.H4(className='', children="UK Power Generation"),
                html.P('This data analytics project collects, analyses ' 
                   'and visualises a variety of electrical generation ' 
                   'data from UK power networks, using the Elexon BMRS web API, ' 
                   'with the aim of developing predictive and analytical models ' 
                   'for power generation from different sources.'),
                html.P( 'Output data from a variety of different generation ' 
                   'assets is collected and analysed to identify contributions '
                   'from renewable and non-renewable sources, statistics for '
                   'each generation type, and characterisation of generation '
                   'profiles. The UK energy grid contains a wide-ranging mix '
                   'of generation types, from nuclear and fossil fuels through '
                   'to renewable and low-carbon systems such as solar, wind and '
                   'hydro-electric.' ),
                html.P('Each of the different generation types produces different '
                   'quantities of electricity for the UK market, and does so '
                   'using different generation profiles. '
                   )
                ]))

@app.callback(
    Output("app-content", "children"),
    Input("app-tabs", "value")
    )
def render_tab_content(tab_switch):
    """
    Render content of tab upon request.
    """
    if tab_switch == "tab1":
        return build_tab_1()
    return (
        html.Div(
            id = "status-container",
            children = [
                build_intro_panel(),
                html.Div(
                    id = "graphs-container",
                    children = [
                        build_chart_panel(),
                        build_table_panel(),
                        build_side_panel()
                       ],
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

# Use for docker release
#if __name__ == '__main__':
 #   app.run_server(debug = True, host = '0.0.0.0', port = 5000)

# Use for dev & debug
if __name__ == '__main__':
    app.run_server(debug = True)
