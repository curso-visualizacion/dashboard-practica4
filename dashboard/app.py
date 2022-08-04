from dash import Dash, html, dcc
from data import gapminder
from scatter import get_scatter
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
    ]
)


if __name__ == "__main__":
    app.run_server(debug=True, host="0.0.0.0", port="5000")
