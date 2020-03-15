import dash
import dash_daq as daq
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# external_stylesheets = ['./style.css']

app = dash.Dash(__name__)

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
    html.Div([
        html.H1('Knapsach'),
        html.Div(
                className="app-header",
                children=[
                    html.Div('Plotly Dash', className="app-header--title")
                ]
            ),
        dcc.Dropdown(
            id='knapsack',
            options=[
                {'label': 'v={} w={}: {}'.format(objs[k]['v'], objs[k]['w'], k) , 'value': k} for k in objs.keys()
            ],
            value=[],
            multi=True,
            className="dcc_control"
            # style={'display':'inline','height':'2px', 'width':'1000px'}
        ),
        html.Div(
            [
                daq.Indicator(
                        id='led',
                        color="#00cc96",
                        value=True,
                        style={'display':'inline-block', 'background-color':'blue', 'vertical-align':'middle',
                        'transform' : 'scale(3)'}
                ),
                html.Div(
                    id='result',
                    style={'margin-left':'25px', 'display':'inline-block', 'background-color':'blue', 'color':'white', 'vertical-align':'middle'}
                    # className='offset-by-one-third column'
                )
            ],
            style={'background-color':'hotpink', 'padding' : '30px'}
        )
    ], className = "pretty_container col_container four columns",
    style={'display':'flex', 'flex-direction': 'column'}
    ),
    html.Div(
        html.H1('Knap2'),
        className = "pretty_container col_container eight columns"
    )
    ],
    className="row flex-display",
)

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
