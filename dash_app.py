from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd


app = Dash(__name__)
df = pd.read_csv("./final_data.csv")
df = df.sort_values(by="Date")
app.layout = html.Div(children=[html.H1(children='Sales of Pink Morsel', style={"textAlign": "center"}),
                                dcc.Graph(
                                    id='visualization',
                                    # figure=fig
                                ),
                                html.Br(),
                                html.Label(children="Region"),
                                dcc.RadioItems(["North", "South", "East", "West", "All"], "all",
                                               style={"padding": 10, "flex": 1},
                                               id="region")
                                ])


@app.callback(
    Output(component_id="visualization", component_property="figure"),
    Input(component_id="region", component_property="value")
)
def update_graph(input_value: str):
    if input_value.lower() == "all":
        filtered_df = df
    else:
        filtered_df = df[df["Region"] == input_value.lower()]
    fig = px.line(filtered_df, x="Date", y="Sales", title="Sales of Pink Morsels")
    fig.update_layout()
    return fig


if __name__ == '__main__':
    app.run_server(debug=True)
