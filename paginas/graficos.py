from ucimlrepo import fetch_ucirepo
import plotly.express as px
from dash import Dash, dcc, html
import dash_bootstrap_components as dbc


heart_disease = fetch_ucirepo(id=45)
dados = heart_disease.data.features

figura_histograma = px.histogram(dados, x='age', title='Histograma de idades')

dados["doenca"] = (heart_disease.data.targets > 0) * 1
figura_boxplot = px.box(dados, x='doenca', y='age', title='Boxplot de idades', color='doenca')

div_do_histograma = html.Div([
        dcc.Graph(figure=figura_histograma)
])

div_do_boxplot = html.Div([
        dcc.Graph(figure=figura_boxplot)
])


layout = html.Div([
    html.H1("Análise de dados do UCI Repository Heart Disease", className='text-center mb-5'),
        dbc.Container([
            dbc.Row([
            dbc.Col([div_do_histograma], md=6), #o md representa quanto do total (12 no padrão) vc disponibiliza proporcional pra cada coluna
            dbc.Col([div_do_boxplot], md=6),
        ])
    ])
        
])






