import plotly.express as px
from utils import get_top5


def get_heatmap(data):
    top5 = get_top5(data)
    top5.set_index("Country", inplace=True)
    heatmap = px.imshow(
        top5[range(2005, 2016)],
        labels={"x": "Year", "y": "Country", "color": "Migrantes"},
        x=list(range(2005, 2016)),
        y=top5.index.values,
    )
    return heatmap
