import plotly.express as px


def get_scatter(data, year):
    return px.scatter(
        data[data.year == year],
        x="gdpPercap",
        y="lifeExp",
        size="pop",
        color="continent",
        hover_name="country",
        size_max=60,
    )
