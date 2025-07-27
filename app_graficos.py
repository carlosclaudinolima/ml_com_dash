from ucimlrepo import fetch_ucirepo
import plotly.express as px
from dash import Dash, dcc, html


heart_disease = fetch_ucirepo(id=45)
dados = heart_disease.data.features

figura_histograma = px.histogram(dados, x='age', title='Histograma de idades')

dados["doenca"] = (heart_disease.data.targets > 0) * 1
figura_boxplot = px.box(dados, x='doenca', y='age', title='Boxplot de idades', color='doenca')

div_do_histograma = html.Div([
        html.H2('Histograma de idades'),
        dcc.Graph(figure=figura_histograma)
])

div_do_boxplot = html.Div([
        html.H2('Boxplot de idades'),
        dcc.Graph(figure=figura_boxplot)
])

app = Dash(__name__)
app.layout = html.Div([
    html.H1("Análise de Doenças Cardíacas"),
    div_do_histograma,
    div_do_boxplot
    
])

# app.layout.children.append(div_do_boxplot) # Pode adicionar dinamicamente

app.run_server(debug=True)





