from dash import Dash, html, dcc, Input, Output, register_page
import dash_bootstrap_components as dbc
from navbar import navbar

register_page(__name__)

content = dbc.Container("Practica 5")

layout = html.Div([navbar("Practica 5"), content])
