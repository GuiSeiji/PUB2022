from dash import Dash, html, dcc, Input, Output
import dash
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import dash_bootstrap_components as dbc

from dash import Dash, dcc, html, Input, Output

dataAAPL =  pd.read_csv('AAPL.csv')
dataAAPL['Empresa'] = 'Apple'
dataGOOG =  pd.read_csv('GOOG.csv')
dataGOOG['Empresa'] ='Google'
dataPBR =  pd.read_csv('PBR.csv')
dataPBR['Empresa'] = 'Petrobrás'

df = [dataAAPL,dataGOOG,dataPBR]

df = pd.concat(df)

opcoes = list(df['Empresa'].unique())

fig = go.Figure(go.Scatter(x=[], y = []))
fig.update_layout(template = None)
fig.update_xaxes(showgrid = False, showticklabels = False, zeroline=False)
fig.update_yaxes(showgrid = False, showticklabels = False, zeroline=False)


app = dash.Dash(__name__,external_stylesheets=[dbc.themes.LUX])

app.layout = dbc.Container(
    dbc.Row([
        dbc.Col([
            html.Div([
            html.H1(children='Parâmetros',
                style = {'color':'blue',
                         'textAlign': 'center',
                        
                        
                        }),
            
            html.H2(children='Empresa',
                style = {'textAlign': 'center',
                         'margin-top':60,
                   }),
            
            dcc.Dropdown(
                opcoes,
                id ='empresa',
                value =[],
                multi=True,
                style = {'box-sizing':'border-box'},
            ),
            
            
            html.H2(children='Informações',
                style = {'textAlign': 'center',
                         'margin-top':60,
                   }),
            
            dcc.Dropdown(
                ['Drawndown','Matriz de Correlação','Sharpe Ratio','Gráfico da Ação'],
                id='tipo',
                multi =True,
                
                style = {'box-sizing':'border-box'},
                ),
            ])
            
        ],md = 3,style = {'padding': '10px',
                         'border-style':'solid'}),
        
        dbc.Col([
            
            html.Div([
            html.H1(children='Meu Portifólio',
                style = {'textAlign': 'center',}),
                
            dbc.Row([
                dbc.Col([
                    dcc.Graph(id='valorizacao',
                    figure = fig
                    ),
                    
                ],width = {'size':10,'offset':1})
            ])
            
            
            ])
        
        ],md = 9,style ={'padding':'10px'})
            
    ]),    
fluid = True)



@app.callback(
    Output('valorizacao', 'figure'),
    Input('empresa', 'value')     
)

def update_graph(value):
    
    if len(value)==0:
        
        return dash.no_update 
                
    else:
    
        dff = df[(df['Empresa'].isin(value))]
        
        fig = px.line(dff,x='Date',y='Close', color = 'Empresa')
    
    return fig


if __name__ == '__main__':
    app.run_server(debug=False)
