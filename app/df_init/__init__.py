import pandas as pd
import time

pd.options.plotting.backend = "plotly"


df = pd.read_csv('SberData.csv')
df = df.pivot_table(index = ["region", "date"], columns = "name", values = "value", aggfunc = "mean", fill_value = 0).reset_index()
df = df[df["region"] != "Russia"]
df['month'] = df["date"].apply(lambda t: time.strptime(t, '%Y-%m-%d').tm_mon)
df['year'] = df["date"].apply(lambda t: time.strptime(t, '%Y-%m-%d').tm_year)

def match_month(month_str):
    match month_str:
        case 'January':
            return '01'
        case 'February':
            return '02'
        case 'March':
            return '03'
        case 'April':
            return '04'
        case 'May':
            return '05'
        case 'June':
            return '06'
        case 'July':
            return '07'
        case 'August':
            return '08'
        case 'September':
            return '09'
        case 'October':
            return '10'
        case 'November':
            return '11'
        case 'December':
            return '12'
        case _:
            return '13'