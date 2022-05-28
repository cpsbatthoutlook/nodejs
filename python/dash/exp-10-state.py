import dash, pandas as pd, numpy as np
from dash import dcc, html
from dash.dependencies import Input, Output, State
import plotly.express as px

## https://learning-oreilly-com.ezproxy.torontopubliclibrary.ca/videos/python-interactive-dashboards/9781803234267/9781803234267-video5_5/
## https://dash.plotly.com/basic-callbacks#dash-app-with-state

## Keep the state { # of clicks on the page } user/data or Session info
##   Had to change the Input to State



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
                        html.Br(), html.Button(id='submit-button-state', n_clicks=0, children='Update button'),  ## n_clicks, is predefined
        dcc.Graph(id='Graph',figure=line_fig)
    ]
 )

## Other Button variables
#Allowed arguments: accessKey, aria-*, autoFocus, children, className, contentEditable, contextMenu, data-*, dir, disabled,
##     draggable, form, formAction, formEncType, formMethod, formNoValidate, formTarget, hidden, id, key, lang, loading_state,
##          n_clicks, n_clicks_timestamp, name, role, spellCheck, style, tabIndex, title, type, value

# https://dash.plotly.com/sharing-data-between-callbacks  ## Better info on sharing the session
@app.callback(
    Output('country','options'),
    Output('country','value'),
    Input('radioRegion', 'value')
    )
def update_Country_list(selected_region):
    country_options=[{'label':i, 'value':i} for i in df.loc[df.Region.isin([selected_region]),'Country']]
    return country_options, country_options[0]['value']

## ORDER of arguments in the callback definition matters
@app.callback(
    Output('Graph','figure'),
    Output('average_div','children'),
    #Input('country','value'),
    #Input('radio_happiness_family','value'),
    State('country','value'),
    State('radio_happiness_family','value'),
    Input('submit-button-state','n_clicks')    
    )
def update_graph(selected_country,selected_col,button_click):
    modified_df = df.loc[df.Country.isin([selected_country])]
    line_fig = px.line(modified_df, x='year',y=selected_col, title=f' {selected_col} for {selected_country}')
    selected_avg=modified_df[selected_col].mean()
    
    return line_fig,f' Avarage of {selected_col} is {selected_avg} '

if __name__=='__main__':
    app.run_server(debug=True)
    
