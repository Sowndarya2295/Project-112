import pandas as pd

import plotly.express as px


df = pd.read_csv(r"csv1.csv")
fig = px.scatter(df, x='quant_saved', y='highschool_completed',color='wealthy')
fig.show()