import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd

DF_SAVE_STRING = 'D:\Developer Area\e-grid_analytics\data_analytics\data\interim\dash_data.pkl'

app = dash.Dash(__name__)

colors = {
    'background':'#111111',
    'text':'#7FDBFF'
    }

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df_new = pd.read_pickle(DF_SAVE_STRING)

fig = px.scatter(df_new, x="setDatetime", y="quantity", color="powType")

fig.update_layout(
    plot_bgcolor = colors['background'],
    paper_bgcolor = colors['background'],
    font_color = colors['text']
    )

app.layout = html.Div(style = {'backgroundColor': colors['background']}, children=[
    html.H1(children='Hello Dash',
            style = {
                'textAlign': 'center',
                'color': colors['text']
                }
            ),
    html.Div(children = 'Dash: A web application framework for Python.', style = {
        'textAlign': 'center',
        'color': colors['text']
        }),
    dcc.Graph(
        id = 'example-graph',
        figure = fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)