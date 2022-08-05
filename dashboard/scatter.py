import plotly.express as px


def get_scatter(data, year):
    return px.scatter(
        data[data.year == year],
        x="gdpPercap",
        y="lifeExp",
        hover_name="country",
    )


def get_bubble(data, year):
    return px.scatter(
        data[data.year == year],
        x="gdpPercap",
        y="lifeExp",
        size="pop",
        color="continent",
        hover_name="country",
        size_max=60,
    )


def get_animated(data):
    return px.scatter(
        data,
        x="gdpPercap",
        y="lifeExp",
        size="pop",
        color="continent",
        hover_name="country",
        size_max=60,
        animation_frame="year",
        range_y=[25, 90],
        range_x=[-1000, 50000],
    )
