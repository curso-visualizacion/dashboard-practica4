def get_top5(data):
    data.loc[:, "total"] = data.loc[:, range(2005, 2016)].sum(axis=1)
    data2 = data.sort_values("total", ascending=False)
    return data2.iloc[:5]
