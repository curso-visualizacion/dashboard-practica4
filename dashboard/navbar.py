import dash_bootstrap_components as dbc


def navbar(title):
    return dbc.NavbarSimple(
        children=[
            dbc.NavItem(dbc.NavLink("Practica 4", href="/practica4")),
            dbc.NavItem(dbc.NavLink("Practica 5", href="/practica5")),
        ],
        brand=title,
        color="primary",
        dark=True,
    )
