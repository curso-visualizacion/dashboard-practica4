import plotly.express as px


def get_scatter(data, year):
    return px.scatter(
        data[data.year == year],
        x="gdpPercap",
        y="lifeExp",
        hover_name="country",
    )
