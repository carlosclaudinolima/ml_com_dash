from dash import Dash, dcc, html 
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
from app import app
import paginas


navegacao = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Gráficos", href="/graficos")),
        dbc.NavItem(dbc.NavLink("Formulário", href="/formulario")),
        
        # dbc.DropdownMenu(
        #     children=[
        #         dbc.DropdownMenuItem("More pages", header=True),
        #         dbc.DropdownMenuItem("Page 2", href="#"),
        #         dbc.DropdownMenuItem("Page 3", href="#"),
        #     ],
        #     nav=True,
        #     in_navbar=True,
        #     label="More",
        # ),
    ],
    brand="Dashboard",
    brand_href="/",
    color="primary",
    dark=True,
)

app.layout = html.Div([
   dcc.Location(id='url', refresh=False),
   navegacao,
   html.Div(id='conteudo')
])

@app.callback(
    Output('conteudo', 'children'),
    [
        Input('url', 'pathname')
    ]
)
def mostrar_pagina(pathname):
    if pathname == '/formulario':
        return paginas.formulario.layout
    elif pathname == '/graficos':
        return paginas.graficos.layout
    else:
        return 'pagina inicial'


app.run(debug=True)
