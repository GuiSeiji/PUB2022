import dash
from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import dash_bootstrap_components as dbc
import plotly

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

app = dash.Dash(__name__,external_stylesheets=[dbc.themes.MORPH])

app.layout = dbc.Container(
    dbc.Row([
        dbc.Col([
            html.Div([
            html.H1(children='Parâmetros',
                style = {'color':'rgb(4,15,15)',
                         'textAlign': 'center'}),
            
            html.H2(children='Empresa',
                style = {'textAlign': 'center',
                         'margin-top':60,
                        'color':'rgb(4,15,15)'}),
            
            dcc.Dropdown(
                opcoes,
                id ='empresa',
                value =[],
                multi=False,
                style = {'box-sizing':'border-box'},
            ),
            
            
            html.H2(children='Informações',
                style = {'textAlign': 'center',
                         'margin-top':60,
                        'color':'rgb(4,15,15)'}),
            
            dcc.Dropdown(
                ['Drawdown','Matriz de Correlação','RSI','MACD'],
                id='informacao',
                multi =True,
                style = {'box-sizing':'border-box'},
                ),
            ])
            
        ],md = 3,style = {'padding': '10px',
                         'border-style':'solid',
                         'border-color':'rgb(0,0,0)',
                         'background-color':'rgb(247,243,227)',
                         'border-radius':'15px'}),
        
        dbc.Col([
            
            html.Div([
            html.H1(children='Meu Portifólio',
                style = {'textAlign': 'center',
                        'color': 'rgb(00,00,00)'}),
            dbc.Row([
                dbc.Col([
                    dcc.Graph(id='grafico-acao',
                    figure = fig,
                    ),
                    
                ],width = {'size':10,'offset':1})
                
                    ]),
                
                 ])
        
        ],md = 9,style ={'padding':'10px',
                        'background-color':'white',
                        'border-style':'solid',
                        'border-color':'black',
                        'border-radius':'15px'}),
            
    ],style = {'background-color':'rgb(236,240,241)'}),    
fluid = True)


@app.callback(
    Output('grafico-acao', 'figure'),
    Input('empresa', 'value')
     
     
     
)

def update_empresa(empresa):
    
    if len(empresa)==0:
        
        return dash.no_update 
    else:            
        dff = df.loc[df['Empresa']== empresa,:]
        
        layout = dict(xaxis=dict(title='Data',showgrid=True,ticks= 'inside',gridcolor = 'black',showline = True),
                     yaxis = dict(title='Fechamento',showgrid=True,ticks= 'inside',gridcolor = 'black',showline =True))
        
        fig = go.Figure(data = go.Candlestick(x=dff['Date'],
                                             open = dff['Open'],
                                             high = dff['High'],
                                             low = dff['Low'],
                                             close = dff['Close']),
                       layout=layout)
        
        fig.update_layout(plot_bgcolor='white',height=600)
        fig.update_layout(xaxis_rangeslider_visible=False)

        
    
    return fig





if __name__ == '__main__':
    app.run_server(debug=False)
