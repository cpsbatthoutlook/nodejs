import dash, pandas as pd, numpy as np
from dash import dcc, html, Input, Output
import plotly.express as px

## https://learning-oreilly-com.ezproxy.torontopubliclibrary.ca/videos/python-interactive-dashboards/9781803234267/9781803234267-video5_5/

### User can select Region > Country and then choose between "Happiness Index" or "Family" data columns for the graphs



app = dash.Dash()
df = pd.read_csv('happiness_index.csv')
region_options=[{'label':i, 'value':i} for i in df.Region.unique()]
#country_options=[{'label':i, 'value':i} for i in df.Country.unique()]
country_options=[]
line_fig=px.line(df[df['Country']=='Denmark'], x='year', y='Happiness Score', title='Index for Chander')

app.layout = html.Div([ html.H1('This is me'), html.P([
            html.Br(),html.A('link is',href='https://www.yahoo.com',target='_blank')
       ]),
        dcc.RadioItems(id='radioRegion',options=region_options, value='North America'),
        dcc.Checklist(options=region_options, value=['North America']),
        dcc.Dropdown(id='country',options=country_options, value=['United States']),
            dcc.RadioItems(id='radio_happiness_family',options=[{'label':i,'value':i} for i in ['Happiness Rank','Family']],value='Happiness Rank'),
        #dcc.Graph(id='Graph',figure=line_fig)
                        html.Div(id='average_div'),
        dcc.Graph(id='Graph',figure=line_fig)
    ]
 )


@app.callback(
    Output('country','options'),
    Output('country','value'),
    Input('radioRegion', 'value')
    )
def update_Country_list(selected_region):
    country_options=[{'label':i, 'value':i} for i in df.loc[df.Region.isin([selected_region]),'Country']]
    return country_options, country_options[0]['value']


@app.callback(
    Output('Graph','figure'),
    Input('country','value'),
    Input('radio_happiness_family','value')
    )
def update_graph(selected_country,selected_col):
    modified_df = df.loc[df.Country.isin([selected_country])]
    line_fig = px.line(modified_df, x='year',y=selected_col, title=f' {selected_col} for {selected_country}')
    return line_fig

if __name__=='__main__':
    app.run_server(debug=True)
    
