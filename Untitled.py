#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

app = Dash(__name__)

dataAMZ = pd.read_csv('AMZN.csv', usecols=['Date','Adj Close'])
dataMETA = pd.read_csv('META.csv', usecols=['Date','Adj Close'])
dataTSL = pd.read_csv('TSLA.csv', usecols=['Date','Adj Close'])
dataAMZ['Empresa'] = 'Amazon'
dataMETA['Empresa'] = 'META'
dataTSL['Empresa'] = 'Tesla'

tudo = pd.concat([dataAMZ,dataMETA,dataTSL])

fig = px.line(tudo,x = 'Date',y='Adj Close',color = 'Empresa')

opcoes = list(tudo['Empresa'].unique())


app.layout = html.Div(children=[
    html.H1(children='Database de Grandes Empresas',
            style = { 'textAlign':'Center',
                     'fontFamily':'Roboto',
                     'paddingTop':20}),

    html.Div(children='''
        Fechamento das grandes Empresas
    ''',
            style = {'textAlign':'Center',}),
    
        html.Div([
        dcc.Checklist(opcoes,
            id = 'checklist',
            
            )
        
    ]),
    
    dcc.Graph(
        id='grafico',
        figure=fig,
        style = {'width':'80%',
                 'paddingLeft':'20%'
            
        }),

        
])


@app.callback(
    Output('grafico', 'figure'),
    Input('checklist', 'value')
)
def update_graph(options_chosen):
    
    df = tudo[tudo['Empresa'].isin(options_chosen)]
    fig = px.line(df,x = 'Date',y='Adj Close',color = 'Empresa')
    return fig






if __name__ == '__main__':
    app.run_server(debug=False)


# In[ ]:





# In[ ]:




