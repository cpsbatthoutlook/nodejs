import dash, pandas as pd, numpy as np
from dash import dcc, html, Input, Output
import plotly.express as px

## https://learning-oreilly-com.ezproxy.torontopubliclibrary.ca/videos/python-interactive-dashboards/9781803234267/9781803234267-video5_5/

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
        dcc.Dropdown(id='country',options=country_options, value=['United States']),
        #dcc.Graph(id='Graph',figure=line_fig)
        dcc.Graph(id='Graph',figure=line_fig)
    ]
 )

@app.callback(
    Output('Graph','figure'),
    Input('country','value')
    )
def update_graph(selected_country):
    modified_df = df.loc[df.Country.isin([selected_country])]
    line_fig = px.line(modified_df, x='year',y='Happiness Score', title=f'Index for {selected_country}')
    return line_fig

if __name__=='__main__':
    app.run_server(debug=True)
    
