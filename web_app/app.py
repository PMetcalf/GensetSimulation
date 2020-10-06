import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import plotly.express as px
import pandas as pd

DF_SAVE_STRING = 'D:\Developer Area\e-grid_analytics\data_analytics\data\interim\dash_data.pkl'

app = dash.Dash(__name__)

colors = {
    'text':'#002366'    # Royal Blue
    }

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df_new = pd.read_pickle(DF_SAVE_STRING)

fig = px.scatter(df_new, x = "setDatetime", y = "quantity", color = "powType",
                 labels = {
                     "setDatetime": "Date",
                     "quantity": "Generation (MW)",
                     "powType": "Generation Type"
                 },
                 height=600)

fig.update_layout(
    font_color = colors['text'],
    legend = dict(
        orientation = "h",
        yanchor = "bottom",
        y = 1.02,
        xanchor = "left",
        x = 0
        ))

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
                    html.H6('UK Electricity Generation Data'),
                ],
            ),
            html.Div(
                id="banner-logo",
                children=[
                    html.Button(
                        id="learn-more-button", children="LEARN MORE", n_clicks=0
                    ),
                ],
            ),
        ],
    )

def build_tab():
    """
    Builds tab used to contain data visualisation collections.
    """
    return html.Div(
        id = "tab",
        className = "tab",
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
            dcc.Graph(
                id = "time-series-chart",
                figure = fig)
            ]
        )

@app.callback(
    [Output("app-content", "children"), Output("interval-component", "n_intervals")],
    [Input("app-tabs", "value")],
    # [State("n-interval-stage", "data")],
)
def render_tab_content():
    """
    Render content of tab upon request.
    """
    return (
        html.Div(
            id = "graphs-container",
            children = [
                #build_top_panel(),
                build_chart_panel()
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
                build_tab(),
                html.Div(id = "app-content"),
                ],
            ),
        dcc.Graph(
            id = 'example-graph',
            figure = fig
        )
])

if __name__ == '__main__':
    app.run_server(debug=True)