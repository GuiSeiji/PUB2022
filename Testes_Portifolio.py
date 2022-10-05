from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

from dash import Dash, dcc, html, Input, Output

app = Dash(__name__)

app.layout = html.Div([
    html.Div([

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
                ['New York City', 'Montreal', 'San Francisco'],
                ['Montreal', 'San Francisco'],
                multi=True,
                style = {'box-sizing':'border-box',
                        'width':'95%',
                        'justify-content': 'center',
                        },
            ),
            
            html.H2(children='Tempo de Consulta',
                style = {'textAlign': 'center',
                         'margin-top':60,
                   }),
            
            dcc.RangeSlider(15,22,1),
            
            html.H2(children='Tipo de Gráfico',
                style = {'textAlign': 'center',
                         'margin-top':60,
                   }),
            
            dcc.Dropdown(
                ['New York City', 'Montreal', 'San Francisco'],
                ['Montreal', 'San Francisco'],
                style = {'box-sizing':'border-box',
                         'width':'95%',
                        'justify-content': 'center'},
            ),
            
            html.Button('Aplicar',
                       style = {'margin-top':60,'margin':'30%',
                                'background-color':'red',
                               'color':'white',
                               'border':'none',
                               'padding':15}),
           
        
        ],style={'display':'block',
                 'float':'left',
                 'max-width':220,
                 'min-width':220,
                 'border-style':'outset'}),

        html.Div([
            html.H1(children='Teste',
                style = {'textAlign': 'center',}),
            
        ])
    ]),
])




    
if __name__ == '__main__':
    app.run_server(debug=False)
