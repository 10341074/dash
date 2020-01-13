import dash
import dash_daq as daq
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

server = app.server
objs = {
    'apple' : {'w': 3, 'v': 2},
    'ball'  : {'w': 2, 'v': 2},
    'cap'   : {'w': 1, 'v': 3},
    'knife' : {'w': 2, 'v': 1},
    'pencil': {'w': 1, 'v': 3},
    'bottle': {'w': 4, 'v': 5},
    'rock'  : {'w': 3, 'v': 3},
    'phone' : {'w': 3, 'v': 5}
}

app.layout = html.Div([
    dcc.Dropdown(
        id='knapsack',
        options=[
            {'label': 'v={} w={}: {}'.format(objs[k]['v'], objs[k]['w'], k) , 'value': k} for k in objs.keys()
        ],
        value=[],
        multi=True
    ),
    daq.Indicator(
        id='led',
        color="#00cc96",
        value=True
    ),
    html.Div(
        id='result'
    )
], style={'columnCount': 2})

def value(items):
    return sum([objs[i]['v'] for i in items])
def weight(items):
    return sum([objs[i]['w'] for i in items])

@app.callback(
    Output(component_id='result', component_property='children'),
    [Input(component_id='knapsack', component_property='value')]
)
def sumknapsack(items):
    if len(items) == 0:
        return 'Weight is 0\n' + 'Value is 0'
    else:
        return 'Weight is "{}"\n'.format(weight(items)) + 'Value is "{}"'.format(value(items))

@app.callback(
    Output(component_id='led', component_property='color'),
    [Input(component_id='knapsack', component_property='value')]
)
def color(items):
    if len(items) == 0:
        return "#00cc96"
    else:
        return "#00cc96" if weight(items) < 10 else "#551A8B"

if __name__ == '__main__':
    app.run_server(debug=True)
