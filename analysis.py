import pandas as pd
import numpy as np
import plotly.express as px

data = pd.read_csv("energy.csv")
# United States energy consumption
US = data.loc[data['Entity'] == "United States"]
USA = US.rename(
    columns={"Primary energy consumption per capita (kWh/person)": "kWh"})


# Total energy consumption grouped by year
aggregate = data.rename(
    columns={"Primary energy consumption per capita (kWh/person)": "kWh"})
aggregate = aggregate.groupby(['Year']).sum().reset_index()
