from flask import Flask, redirect, url_for, render_template, request
import pandas as pd
import numpy as np
import json
import plotly
import plotly.express as px

app = Flask(__name__)


@app.route('/callback', methods=['POST', 'GET'])
def dyn():
    return energy(request.args.get('data'))


@app.route('/')
def plot():
    return render_template('energy.html', graphJSON=dyn())


def energy(country="United States"):
    data = pd.read_csv("energy.csv")
    countries = data['Entity'].unique()
    countryplot = data.loc[data['Entity'] == country]
    countryplot = countryplot.rename(
        columns={"Primary energy consumption per capita (kWh/person)": "kWh"})
    chart = px.line(countryplot, x="Year", y="kWh",
                    title="Energy Consumption from 1965 to 2021")
    chart.update_xaxes(showline=True, linewidth=2,
                       linecolor='black', mirror=True)
    chart.update_yaxes(showline=True, linewidth=2,
                       linecolor='black', mirror=True)
    graphJSON = json.dumps(chart, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON


@app.route('/yearly')
def yearly():
    data = pd.read_csv("energy.csv")
    aggregate = data.rename(
        columns={"Primary energy consumption per capita (kWh/person)": "kWh"})
    aggregate = aggregate.groupby(['Year']).sum().reset_index()
    chart = px.line(aggregate, x="Year", y="kWh",
                    title="Energy Consumption from 1965 to 2021")
    chart.update_xaxes(showline=True, linewidth=2,
                       linecolor='black', mirror=True)
    chart.update_yaxes(showline=True, linewidth=2,
                       linecolor='black', mirror=True)
    graphJSON = json.dumps(chart, cls=plotly.utils.PlotlyJSONEncoder)
    return render_template('yearly.html', graphJSON=graphJSON)


# todo: link the pages
if __name__ == "__main__":
    app.run(debug=True)
