from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
app = Dash(__name__)
df = pd.read_csv("final_data.csv")
fig = px.line(df, x="Date", y="Sales")
app.layout = html.Div(children=[html.H1(children='Sales of Pink Morsel'),
                                dcc.Graph(
                                    id='example-graph',
                                    figure=fig
                                )])

if __name__ == '__main__':
    app.run_server(debug=True)

