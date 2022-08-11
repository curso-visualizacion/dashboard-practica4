from dash import Dash, html, dcc, Input, Output, register_page, callback
import dash_bootstrap_components as dbc
from data import gapminder, migrantes
from scatter import get_scatter, get_bubble, get_animated
from heatmap import get_heatmap
import os
from navbar import navbar

register_page(__name__)


content = dbc.Container(
    children=[
        html.H1("Práctica 4: Dashboard"),
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.H1("Ejercicio 1 de la tarea 2"),
                        dbc.Card(
                            [
                                html.H4("Controles", className="card-title"),
                                html.Div(
                                    [
                                        dbc.Label("Año"),
                                        dcc.Dropdown(
                                            id="year1",
                                            options=[
                                                {"label": y, "value": y}
                                                for y in gapminder.year.unique()
                                            ],
                                            value=2007,
                                        ),
                                    ]
                                ),
                            ]
                        ),
                    ],
                    width=3,
                ),
                dbc.Col(dcc.Graph(id="scatter", figure=get_scatter(gapminder, 2007))),
            ],
            align="center",
        ),
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.H1("Ejercicio 2 de la tarea 2"),
                        dbc.Card(
                            [
                                html.H4("Controles", className="card-title"),
                                html.Div(
                                    [
                                        dbc.Label("Año"),
                                        dcc.Dropdown(
                                            id="year2",
                                            options=[
                                                {"label": y, "value": y}
                                                for y in gapminder.year.unique()
                                            ],
                                            value=2007,
                                        ),
                                    ]
                                ),
                            ]
                        ),
                    ],
                    width=3,
                ),
                dbc.Col(dcc.Graph(id="bubble", figure=get_bubble(gapminder, 2007))),
            ],
            align="center",
        ),
        dbc.Row(
            [
                dbc.Col(html.H1("Ejercicio 3 de la tarea 2"), width=3),
                dbc.Col(dcc.Graph(id="animated", figure=get_animated(gapminder))),
            ],
            align="center",
        ),
        dbc.Row(
            [
                dbc.Col(html.H1("Ejercicio 5 de la tarea 2"), width=3),
                dbc.Col(dcc.Graph(id="heatmap", figure=get_heatmap(migrantes))),
            ],
            align="center",
        ),
    ],
    className="p-5",
)

layout = html.Div([navbar("Practica 4"), content])


@callback(Output("scatter", "figure"), [Input("year1", "value")])
def update_scatter(year):
    return get_scatter(gapminder, year)


@callback(Output("bubble", "figure"), [Input("year2", "value")])
def update_scatter(year):
    return get_bubble(gapminder, year)
