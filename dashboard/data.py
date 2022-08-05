import pandas as pd

data_url = "https://raw.githubusercontent.com/holtzy/The-Python-Graph-Gallery/master/static/data/gapminderData.csv"
gapminder = pd.read_csv(data_url)

migrantes = pd.read_excel("static/MigrantesChile (2005-2016)-Copy1.xlsx")
