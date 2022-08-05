from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
from data import gapminder, migrantes
from scatter import get_scatter, get_bubble, get_animated
from heatmap import get_heatmap
import os

is_gunicorn = "gunicorn" in os.environ.get("SERVER_SOFTWARE", "")
if is_gunicorn:
    grupo = os.environ.get("GRUPO", "")
    requests_pathname_prefix = f"/{ grupo }"
else:
    requests_pathname_prefix = "/"

app = Dash(
    __name__,
    requests_pathname_prefix=requests_pathname_prefix,
    external_stylesheets=[dbc.themes.BOOTSTRAP],
)
server = app.server

app.layout = dbc.Container(
    children=[
        dbc.Row(
            [
                dbc.Col(html.H1("Ejercicio 1 de la tarea 2"), width=3),
                dbc.Col(dcc.Graph(id="scatter", figure=get_scatter(gapminder, 2007))),
            ],
            align="center",
        ),
        dbc.Row(
            [
                dbc.Col(html.H1("Ejercicio 2 de la tarea 2"), width=3),
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


if __name__ == "__main__":
    app.run_server(debug=True, host="0.0.0.0", port="5000")
