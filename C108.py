import plotly.figure_factory as ff
import csv
import pandas as pd

df = pd.read_csv("C:\Python\phone.csv")


fig = ff.create_distplot([df["Mobile Brand"].tolist()], ["Mobile Brand"], show_hist=False)
fig.show()

fig1 = ff.create_distplot([df["Avg Rating"].tolist()], ["Avg Rating"], show_hist=False)
fig1.show()