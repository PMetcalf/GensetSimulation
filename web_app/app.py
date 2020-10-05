import dash
import dash_core_components as dcc
import dash_html_components as html
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

def build_banner():
    return html.Div(
        id="banner",
        className="banner",
        children=[
            html.Div(
                id="banner-text",
                children=[
                    html.H5("Manufacturing SPC Dashboard"),
                    html.H6("Process Control and Exception Reporting"),
                ],
            ),
            html.Div(
                id="banner-logo",
                children=[
                    html.Button(
                        id="learn-more-button", children="LEARN MORE", n_clicks=0
                    ),
                    html.Img(id="logo", src=app.get_asset_url("dash-logo-new.png")),
                ],
            ),
        ],
    )

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

app.layout = html.Div(
    id = "main-app-container",
    children=[
        build_banner(),
        html.H1(children='Electricity Grid Analytics',
                style = {
                    'textAlign': 'left',
                    'color': colors['text']
                    }
                ),
        html.Div(children = 'UK Electricity Generation Data', style = {
            'textAlign': 'left',
            'color': colors['text']
            }),
        dcc.Graph(
            id = 'example-graph',
            figure = fig
        )
])

if __name__ == '__main__':
    app.run_server(debug=True)