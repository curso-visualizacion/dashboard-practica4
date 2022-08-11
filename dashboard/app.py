from dash import Dash, html, dcc, Input, Output
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
    use_pages=True,
)
server = app.server


if __name__ == "__main__":
    app.run_server(debug=True, host="0.0.0.0", port="5000")
