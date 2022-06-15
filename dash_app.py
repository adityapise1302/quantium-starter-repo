from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
app = Dash(__name__)
df = pd.read_csv("final_data.csv")
df = df.sort_values(by="Date")
fig = px.line(df, x="Date", y="Sales", title="Sales of Pink Morsel")
app.layout = html.Div(children=[html.H1(children='Sales of Pink Morsel'),
                                dcc.Graph(
                                    id='visualization',
                                    figure=fig
                                )])

if __name__ == '__main__':
    app.run_server(debug=True)

