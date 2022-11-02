import dash
from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import dash_bootstrap_components as dbc
import plotly
import pandas_ta as ta
import numpy as np

#Data 

dataAAPL =  pd.read_csv('AAPL.csv')
dataGOOG =  pd.read_csv('GOOG.csv')
dataPBR =  pd.read_csv('PBR.csv')

dataAAPL.ta.macd(close='Close', fast=12, slow=26, signal=9, append=True)
dataGOOG.ta.macd(close='Close', fast=12, slow=26, signal=9, append=True)
dataPBR.ta.macd(close='Close', fast=12, slow=26, signal=9, append=True)

dataAAPL.ta.rsi(close = 'Close',legth =14, append = True)
dataGOOG.ta.rsi(close = 'Close',legth =14, append = True)
dataPBR.ta.rsi(close = 'Close',legth =14, append = True)

#Gráficos 

layout = go.Layout(dict(xaxis=dict(showgrid=True,ticks= 'inside',gridcolor = 'black',showline = True),
                     yaxis = dict(showgrid=True,ticks= 'inside',gridcolor = 'black',showline =True)))

colors = np.where(dataAAPL['MACDh_12_26_9'] < 0, '#000', '#ff9900')

figap = make_subplots(rows = 3, cols = 1,shared_xaxes = True)

figap.add_trace(go.Candlestick(x=dataAAPL['Date'],
                                        open = dataAAPL['Open'],
                                        high = dataAAPL['High'],
                                        low = dataAAPL['Low'],
                                        close = dataAAPL['Close'],
                                        showlegend = False,
                                        name = 'Ação'
                                        ),
                                        
                                        row = 1,
                                        col = 1,
                                        )
figap.add_trace(go.Scatter(
                x=dataAAPL.index,
                y=dataAAPL['MACD_12_26_9'],
                line=dict(color='#ff9900', width=2),
                name = 'MACD',
                legendgroup='2'
            ), row=2, col=1
        )
figap.add_trace(
    go.Scatter(
        x=dataAAPL.index,
        y=dataAAPL['MACDs_12_26_9'],
        line=dict(color='#000000', width=2),
        # showlegend=False,
        legendgroup='2',
        name='signal'
    ), row=2, col=1
)

figap.add_trace(
    go.Bar(
        x=dataAAPL.index,
        y=dataAAPL['MACDh_12_26_9'],
        name='histogram',
        marker_color=colors,
        showlegend=False,
    ), row=2, col=1
)

figap.add_trace(
    go.Scatter(
        x = dataAAPL.index,
        y = dataAAPL['RSI_14'],
        name = 'RSI',
        line = dict(color = 'blue',width =2),
        legendgroup = '2'),
    row = 3, col = 1)

figap.add_hline(y=30, line_width=1, line_dash="dash", line_color="green", row=3, col=1)
figap.add_hline(y=70, line_width=1, line_dash="dash", line_color="red", row=3, col=1)

######################################################################

colors = np.where(dataGOOG['MACDh_12_26_9'] < 0, '#000', '#ff9900')

figgo = make_subplots(rows = 3, cols = 1,shared_xaxes = True)

figgo.add_trace(go.Candlestick(x=dataGOOG['Date'],
                                        open = dataGOOG['Open'],
                                        high = dataGOOG['High'],
                                        low = dataGOOG['Low'],
                                        close = dataGOOG['Close'],
                                        showlegend = False,
                                        name = 'Ação'
                                        ),
                                        
                                        row = 1,
                                        col = 1,
                                        )
figgo.add_trace(go.Scatter(
                x=dataGOOG.index,
                y=dataGOOG['MACD_12_26_9'],
                line=dict(color='#ff9900', width=2),
                name = 'MACD',
                legendgroup='2'
            ), row=2, col=1
        )
figgo.add_trace(
    go.Scatter(
        x=dataGOOG.index,
        y=dataGOOG['MACDs_12_26_9'],
        line=dict(color='#000000', width=2),
        legendgroup='2',
        name='signal'
    ), row=2, col=1
)

figgo.add_trace(
    go.Bar(
        x=dataGOOG.index,
        y=dataGOOG['MACDh_12_26_9'],
        name='histogram',
        marker_color=colors,
        showlegend=False,
    ), row=2, col=1
)

figgo.add_trace(
    go.Scatter(
        x = dataGOOG.index,
        y = dataGOOG['RSI_14'],
        name = 'RSI',
        line = dict(color = 'blue',width =2),
        legendgroup = '2'),
    row = 3, col = 1)

figgo.add_hline(y=30, line_width=1, line_dash="dash", line_color="green", row=3, col=1)
figgo.add_hline(y=70, line_width=1, line_dash="dash", line_color="red", row=3, col=1)

############################################################

colors = np.where(dataPBR['MACDh_12_26_9'] < 0, '#000', '#ff9900')

figpbr = make_subplots(rows = 3, cols = 1,shared_xaxes = True)

figpbr.add_trace(go.Candlestick(x=dataPBR['Date'],
                                        open = dataPBR['Open'],
                                        high = dataPBR['High'],
                                        low = dataPBR['Low'],
                                        close = dataPBR['Close'],
                                        showlegend = False,
                                        name = 'Ação'
                                        ),
                                        
                                        row = 1,
                                        col = 1,
                                        )
figpbr.add_trace(go.Scatter(
                x=dataPBR.index,
                y=dataPBR['MACD_12_26_9'],
                line=dict(color='#ff9900', width=2),
                name = 'MACD',
                legendgroup='2'
            ), row=2, col=1
        )
figpbr.add_trace(
    go.Scatter(
        x=dataPBR.index,
        y=dataPBR['MACDs_12_26_9'],
        line=dict(color='#000000', width=2),
        # showlegend=False,
        legendgroup='2',
        name='signal'
    ), row=2, col=1
)

figpbr.add_trace(
    go.Bar(
        x=dataPBR.index,
        y=dataPBR['MACDh_12_26_9'],
        name='histogram',
        marker_color=colors,
        showlegend=False,
    ), row=2, col=1
)

figpbr.add_trace(
    go.Scatter(
        x = dataPBR.index,
        y = dataPBR['RSI_14'],
        name = 'RSI',
        line = dict(color = 'blue',width =2),
        legendgroup = '2'),
    row = 3, col = 1)

figpbr.add_hline(y=30, line_width=1, line_dash="dash", line_color="green", row=3, col=1)
figpbr.add_hline(y=70, line_width=1, line_dash="dash", line_color="red", row=3, col=1)


#APP

#Abas

app_tabs = html.Div(
    [
        dbc.Tabs(
            [
                dbc.Tab(label="Apple", tab_id="tab-apple"),
                dbc.Tab(label="Google", tab_id="tab-google"),
                dbc.Tab(label="Petrobras", tab_id="tab-petro"),
            ],
            id="tabs",
            active_tab="tab-apple",
        ),
    ], className="mt-3"
)

#Layout

apple_layout = html.Div([
    dbc.Row([
        dbc.Col([
            dcc.Graph(
            figure = figap) 
        ],width = 7,)   
    ])    
])

google_layout = html.Div([
    dbc.Row([
        dbc.Col([
            dcc.Graph(
            figure = figgo) 
        ],width = 7,)   
    ])    
])

petrobras_layout = html.Div([
    dbc.Row([
        dbc.Col([
            dcc.Graph(
            figure = figpbr) 
        ],width = 7,)   
    ])    
])

#App em si

app = dash.Dash(__name__,external_stylesheets=[dbc.themes.MORPH])

app.layout = dbc.Container([
    dbc.Row(dbc.Col(html.H1("Portifolio",
                            style={"textAlign": "center"}), width=12)),
    html.Hr(),
    dbc.Row(dbc.Col(app_tabs, width=12), className="mb-3"),
    html.Div(id='content', children=[])

],style = {'background-color':'white'})

@app.callback(
    Output("content", "children"),
    [Input("tabs", "active_tab")]
)
def switch_tab(tab_chosen):
    if tab_chosen == "tab-apple":
             
        figap.update_layout(plot_bgcolor='white',xaxis_rangeslider_visible=False,height = 800)
        figap.update_layout(layout)
        figap.update_yaxes(title_text="Price", row=1, col=1)
        figap.update_yaxes(title_text="MACD", row=2, col=1)
        figgo.update_yaxes(title_text="RSI", row=3, col=1)
        
        
        return apple_layout
    elif tab_chosen == "tab-google":
        
        figgo.update_layout(plot_bgcolor='white',height=800,xaxis_rangeslider_visible=False)
        figgo.update_layout(layout)
        figgo.update_yaxes(title_text="Price", row=1, col=1)
        figgo.update_yaxes(title_text="MACD", row=2, col=1)
        figgo.update_yaxes(title_text="RSI", row=3, col=1)
        
        
        return google_layout
    elif tab_chosen == "tab-petro":
        
        figpbr.update_layout(plot_bgcolor='white',height=800,xaxis_rangeslider_visible=False)
        figpbr.update_layout(layout)
        figpbr.update_yaxes(title_text="Price", row=1, col=1)
        figpbr.update_yaxes(title_text="MACD", row=2, col=1)
        figgo.update_yaxes(title_text="RSI", row=3, col=1)
        
        return petrobras_layout
    return html.P("This shouldn't be displayed for now...")



if __name__=='__main__':
    app.run_server(debug=False)
