from dash import Dash, html, dcc
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

app = Dash(__name__, requests_pathname_prefix=requests_pathname_prefix)
server = app.server

app.layout = html.Div(
    children=[
        html.H1("Ejercicio 1 de la tarea 2"),
        dcc.Graph(id="scatter", figure=get_scatter(gapminder, 2007)),
        html.H1("Ejercicio 2 de la tarea 2"),
        dcc.Graph(id="bubble", figure=get_bubble(gapminder, 2007)),
        html.H1("Ejercicio 3 de la tarea 2"),
        dcc.Graph(id="animated", figure=get_animated(gapminder)),
        html.H1("Ejercicio 5 de la tarea 2"),
        dcc.Graph(id="heatmap", figure=get_heatmap(migrantes)),
    ]
)


if __name__ == "__main__":
    app.run_server(debug=True, host="0.0.0.0", port="5000")
