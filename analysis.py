import pandas as pd
import numpy as np
import plotly.express as px

data = pd.read_csv("energy.csv")
# print(data.columns)
# print(data.values)
US = data.loc[data['Entity'] == "United States"]
USA = US.rename(
    columns={"Primary energy consumption per capita (kWh/person)": "kWh"})
print(USA.head())
