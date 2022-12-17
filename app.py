from flask import Flask, redirect, url_for, render_template
import pandas as pd
import numpy as np
import json
import plotly
import plotly.express as px

app = Flask(__name__)


@app.route("/")
def energy():
    data = pd.read_csv("energy.csv")
    US = data.loc[data['Entity'] == "United States"]
    USA = US.rename(
        columns={"Primary energy consumption per capita (kWh/person)": "kWh"})
    chart = px.line(USA, x="Year", y="kWh",
                    title="US Energy Consumption from 1965 to 2021")
    chart.update_xaxes(showline=True, linewidth=2,
                       linecolor='black', mirror=True)
    chart.update_yaxes(showline=True, linewidth=2,
                       linecolor='black', mirror=True)
    graphJSON = json.dumps(chart, cls=plotly.utils.PlotlyJSONEncoder)
    return render_template("energy.html", graphJSON=graphJSON)


if __name__ == "__main__":
    app.run(debug=True)
# Todo: change bar to line graph, consider adding more graphs, consider adding input to toggle country, customize front end with html/css
