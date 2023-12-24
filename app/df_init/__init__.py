import pandas as pd
import time

pd.options.plotting.backend = "plotly"


df = pd.read_csv('SberData.csv')
df = df.pivot_table(index = ["region", "date"], columns = "name", values = "value", aggfunc = "mean", fill_value = 0).reset_index()
df = df[df["region"] != "Russia"]
df['month'] = df["date"].apply(lambda t: time.strptime(t, '%Y-%m-%d').tm_mon)
df['year'] = df["date"].apply(lambda t: time.strptime(t, '%Y-%m-%d').tm_year)
