import plotly.express as px


def get_line(data, country, y_axis):
    fig = px.line(data[data.country == country], x="year", y=y_axis)
    fig.update_layout(title_text=country)
    return fig
