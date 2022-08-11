from dash import Dash, html, dcc, Input, Output, register_page, callback
import dash_bootstrap_components as dbc
from navbar import navbar
from data import gapminder
from scatter import get_bubble
from line import get_line

register_page(__name__)


scatter = dcc.Graph(id="scatter", figure=get_bubble(gapminder, 2007))
time_series_a = dcc.Graph(id="time_series_a")
time_series_b = dcc.Graph(id="time_series_b")

content = dbc.Container(
    [
        dbc.Row(scatter),
        dbc.Row(
            [
                dbc.Col([time_series_a]),
                dbc.Col([time_series_b]),
            ],
        ),
    ]
)

layout = html.Div([navbar("Practica 5"), content])


@callback(
    Output("time_series_a", "figure"),
    Output("time_series_b", "figure"),
    Input("scatter", "hoverData"),
)
def update_time_series(hover_data):
    a_series = "lifeExp"
    b_series = "gdpPercap"
    if not hover_data:
        return (
            get_line(gapminder, "Chile", a_series),
            get_line(gapminder, "Chile", b_series),
        )
    country = hover_data["points"][0]["hovertext"]
    return (
        get_line(gapminder, country, a_series),
        get_line(gapminder, country, b_series),
    )
