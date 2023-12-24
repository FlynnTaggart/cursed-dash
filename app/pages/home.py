import dash
from dash import html

dash.register_page(__name__, path='/', title="Amazing Region Banking")

layout = html.Div([
    html.H1('This is our Home page', style={"font-family": "'Anonymous Pro'"}),
    html.Div('This is our Home page content.', style={"font-family": "'Anonymous Pro'"}),
])