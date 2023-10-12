import pandas as pd
import plotly.express as px
import dash
from dash import dcc, html
from dash.dependencies import Input, Output

# Read the .txt file using 3 spaces as the delimiter
df = pd.read_csv('nea_data.csv', sep=';', header=0, encoding='UTF-8')

app = dash.Dash(__name__)

# Define external CSS stylesheet for improved styling
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    html.Div([
        html.H1('NEA Data Heatmap', style={'textAlign': 'center'}),
        html.P('This app allows you to visualize the density of NEA data for two selected variables.',
            style={'textAlign': 'center'}),
        html.Div([
            html.Label('Select first variable'),
            dcc.Dropdown(
                id='variable-dropdown-1',
                options=[{'label': col, 'value': col} for col in df.columns[1:]],
                value='Absolute magnitude, H'
            ),
        ], style={'width': '48%', 'display': 'inline-block'}),
        html.Div([
            html.Label('Select second variable'),
            dcc.Dropdown(
                id='variable-dropdown-2',
                options=[{'label': col, 'value': col} for col in df.columns[1:]],
                value='Slope parameter, G'
            ),
        ], style={'width': '48%', 'display': 'inline-block'}),
        html.Button('Reset', id='reset-button', n_clicks=0, style={'margin-top': '10px'}),
    ], style={'max-width': '800px', 'margin': '0 auto'}),
    dcc.Graph(id='heatmap', style={'margin-top': '20px'}),
    
    # Footer Section
    html.Footer([
        html.P('About Us', style={'color': 'white'}),
        html.P('This is the Voyagers Visionary project for The Space Apps Challenge Hackathon 2023', style={'color': 'white'}),
    ], style={'textAlign': 'center', 'background-color': 'black', 'padding': '10px'}),
])

@app.callback(
    Output('heatmap', 'figure'),
    [Input('variable-dropdown-1', 'value'),
     Input('variable-dropdown-2', 'value')]
)
def update_heatmap(variable_1, variable_2):
    fig = px.density_heatmap(
        df, x=variable_1, y=variable_2,
        title=f'Density Heatmap for {variable_1} vs {variable_2}',
        marginal_x='histogram',  # Use histogram for increased detail
        marginal_y='histogram'
    )

    fig.update_traces(
        hovertemplate='Designation: %{text}<br>Type: %{customdata[0]}<br>%{xaxis.title.text}: %{x}<br>%{yaxis.title.text}: %{y}'
    )

    fig.update_layout(
        coloraxis_colorbar=dict(
            title='Density'
        )
    )

    return fig

@app.callback(
    [Output('variable-dropdown-1', 'value'), Output('variable-dropdown-2', 'value')],
    [Input('reset-button', 'n_clicks')]
)
def reset_variable_dropdown(n_clicks):
    if n_clicks > 0:
        return 'Absolute magnitude, H', 'Slope parameter, G'
    return dash.no_update

if __name__ == '__main__':
    app.run_server(port=8050, debug=True)
