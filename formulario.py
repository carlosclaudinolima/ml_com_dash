from dash import Dash, dcc, html
from dash.dependencies import Input, Output, State

app = Dash(__name__)

app.layout = html.Div([
    html.Label('Idade'),
    dcc.Input(id='idade', type='number', value=0),
    html.Button('Submeter', id='botao-submeter', n_clicks=0),
    html.Div(id='output-meses')
])



@app.callback(
    output = Output('output-meses', 'children'),
    #inputs = Input('idade', 'value'),
    inputs = Input('botao-submeter', 'n_clicks'),
    state = State('idade', 'value'),
    prevent_initial_call = True
)
def calcula_meses(n_clicks, idade):
    if n_clicks == 0 or idade == None:
        return ''
    else:
        return idade * 12

app.run_server()