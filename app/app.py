from dash import Dash, html, dcc, callback, Output, Input, page_container, page_registry
import plotly.express as px
import pandas as pd
import flask
import df_init
import time
import os

debug = False if os.environ["DASH_DEBUG_MODE"] == "False" else True

server = flask.Flask(__name__, template_folder='static')

external_stylesheets = [
    "https://fonts.googleapis.com/css2?family=Anonymous+Pro&display=swap"
]


app = Dash(name=__name__, server=server, title="Amazing Region Banking", use_pages=True, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    html.Img(src='assets/paw.png',style={'display':'inline-block', 'width': '32pt', 'height': '32pt','margin-right':'16pt'}),
    html.H1('Welcome to my banking region analytics system', style={"font-family": "'Anonymous Pro'", 'display':'inline-block'}),
    html.Div([
        html.Div(
            dcc.Link(f"{page['name']}", href=page["relative_path"])
        ) for page in page_registry.values()
    ], style={"font-family": "'Anonymous Pro'"}),
    page_container
])

if __name__ == '__main__':
    df_init.df = pd.read_csv('SberData.csv')
    df_init.df = df_init.df.pivot_table(index = ["region", "date"], columns = "name", values = "value", aggfunc = "mean", fill_value = 0).reset_index()
    df_init.df = df_init.df[df_init.df["region"] != "Russia"]
    df_init.df['month'] = df_init.df["date"].apply(lambda t: time.strptime(t, '%Y-%m-%d').tm_mon)
    df_init.df['year'] = df_init.df["date"].apply(lambda t: time.strptime(t, '%Y-%m-%d').tm_year)

    app.run_server(host="0.0.0.0", port="8050", debug=debug)    