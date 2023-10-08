import pandas as pd
import plotly.express as px
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output

df = pd.read_csv('datafile.txt', sep = '\s{3,}', header = 0, engine='python')

df.columns = df.columns.str.replace(' ', '_')

app = dash.Dash(__name__)

app.layout = html.Div

