import dash, pandas as pd, numpy as np
from dash import dcc
from dash import html
import plotly.express as px

app = dash.Dash()
df = pd.read_csv('happiness_index.csv')
region_options=[{'label':i, 'value':i} for i in df.Region.unique()]
country_options=[{'label':i, 'value':i} for i in df.Country.unique()]
line_fig=px.line(df[df['Country']=='Denmark'], x='year', y='Happiness Score', title='Index for Chander')

df.Country.unique()
df.Region.unique()


app.layout = html.Div([ html.H1('This is me'), html.P([
            html.Br(),html.A('link is',href='https://www.yahoo.com',target='_blank')
       ]),
        dcc.RadioItems(options=region_options, value='North America'),
        dcc.Checklist(options=region_options, value=['North America']),
        dcc.Dropdown(options=country_options, value=['United States']),
        dcc.Graph(figure=line_fig)
    ]
 )



if __name__=='__main__':
    app.run_server(debug=True)
    
