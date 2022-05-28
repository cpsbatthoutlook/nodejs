import dash
import dash_html_components as html

app = dash.Dash()

app.layout=html.Div(children=[
    html.H1(children="World Happiness Dashboard"),
    html.P(children=['this dashboard shows hapiness',html.Br(),html.A('report link', href='http://www.yahoo.com',target='_blank')])
    ])

## Added myself
app.layout=html.Div([html.H1('This is my attempt'), html.P([ 'Something else', html.Br(),
                                                             html.A('link',href='http://www.google.com',target='_blank')
      ])
    ])

if __name__ == '__main__':
    app.run_server(debug=True)
