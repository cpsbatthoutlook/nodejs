import pandas as pd,numpy as np
from dash import dash, html, dcc
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
import plotly.express as px

css='https://codepen.io/chriddyp/pen/bWLwgP.css'
css2='https://stackpath.bootstrapcdn.com/bootswatch/4.5.0/cyborg/bootstrap.min.css'

## Source: https://dash-bootstrap-components.opensource.faculty.ai/docs/themes/#available-themes
## Theme explorer: https://dash-bootstrap-components.opensource.faculty.ai/docs/themes/explorer/
##   External resources : https://dash.plotly.com/external-resources


app = dash.Dash(external_stylesheets=[dbc.themes.CYBORG])
app.layout = html.Div(children=[
    html.H1("my H1 "), html.P(['First P', html.Br(), html.A('explorer themes',href='https://dash-bootstrap-components.opensource.faculty.ai/docs/themes/explorer/',target='_blank')]),
    dcc.Input(id='input1', type='text', value='Canada'),html.Button(id='button-submit', n_clicks=0, children='Submit')
    ])

#app.layout = html.Div(children=[
#    html.H1("my H1 ", style={'textAlign':'cener','fontFamily':'fantasy','fontSize':98,'color':'blue'}), html.P(['First P', html.Br(), html.A('explorer themes',href='https://dash-bootstrap-components.opensource.faculty.ai/docs/themes/explorer/',target='_blank')]),
#    dcc.Input(id='input1', type='text', value='Canada'),html.Button(id='button-submit', n_clicks=0, children='Submit')
#    ])



if __name__=='__main__':
    app.run(debug=True)
    
