# import statements
from collections import Counter
from dash import Dash, dcc, html, Input, Output, State
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import load_figure_template
from dash.dependencies import Input, Output
from sklearn.neighbors import NearestNeighbors
import dash
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.subplots as ps

# start running dash app with a stylesheet
app = Dash(__name__, external_stylesheets=[dbc.themes.LUX])
load_figure_template('LUX')

# import full dataset
full_df = pd.read_csv('trail dataset.csv')

yn_list = ['Yes', 'No', 'No Preference']
num_list = [1,2,3,4,5,6,7,8,9,10,'No Preference']
len_list = [1,2,3,4,5,6,7,8,9,10,12,15,20,30,40,50,75,100, 'No Preference']
ele_list = list(range(0,4500,100))

# initialize interactive elements
# Wildlife
wl_pref_label = html.H4('Do you want there to be wildlife on the trail?')
wl_pref = dcc.Dropdown(yn_list, id='wl_pref', value='No Preference')
wl_importance_label = html.H4('On a scale of 1 to 5, how much do you value seeing wildlife on the trail?')
wl_importance = dcc.Slider(1,5,step=1, marks=None, id='wl_importance',
                           tooltip={"placement": "bottom", "always_visible": True}, value=3)
# Dog Friendly
dog_pref_label = html.H4('Do you want the trail to be dog-friendly?')
dog_pref = dcc.Dropdown(yn_list, id='dog_pref', value='No Preference')
dog_importance_label = html.H4('On a scale of 1 to 5, how much do you value dog friendliness in a trail?')
dog_importance = dcc.Slider(1,5,step=1, marks=None, id='dog_importance',
                           tooltip={"placement": "bottom", "always_visible": True}, value=3)
# Kid Friendly
kid_pref_label = html.H4('Do you want the trail to be kid-friendly?')
kid_pref = dcc.Dropdown(yn_list, id='kid_pref', value='No Preference')
kid_importance_label = html.H4('On a scale of 1 to 5, how much do you value kid-friendliness in a trail?')
kid_importance = dcc.Slider(1,5,step=1, marks=None, id='kid_importance',
                           tooltip={"placement": "bottom", "always_visible": True}, value=3)

# Views
view_pref_label = html.H4('Do you want the trail to have views?')
view_pref = dcc.Dropdown(yn_list, id='view_pref', value='No Preference')
view_importance_label = html.H4('On a scale of 1 to 5, how much do you value a trail having views?')
view_importance = dcc.Slider(1,5,step=1, marks=None, id='view_importance',
                           tooltip={"placement": "bottom", "always_visible": True}, value=3)

# Popularity
pop_pref_label = html.H4('On a scale of 1 to 10, how popular do you want the trail to be?')
pop_pref = dcc.Dropdown(num_list, id='pop_pref', value='No Preference')
pop_importance_label = html.H4('On a scale of 1 to 5, how much do you value the popularity of a trail?')
pop_importance = dcc.Slider(1,5,step=1, marks=None, id='pop_importance',
                           tooltip={"placement": "bottom", "always_visible": True}, value=3)

# Length
len_pref_label = html.H4('In miles(CHECK), how long do you want the trail to be?')
len_pref = dcc.Dropdown(len_list, id='len_pref', value='No Preference')
len_importance_label = html.H4('On a scale of 1 to 5, how much do you value the length of a trail?')
len_importance = dcc.Slider(1,5,step=1, marks=None, id='len_importance',
                           tooltip={"placement": "bottom", "always_visible": True}, value=3)

# Visitor Usage
use_pref_label = html.H4('On a scale of 1 to 10, how much usage do you want the trail to have?')
use_pref = dcc.Dropdown(num_list, id='use_pref', value='No Preference')
use_importance_label = html.H4('On a scale of 1 to 5, how much do you value the usage of a trail?')
use_importance = dcc.Slider(1,5,step=1, marks=None, id='use_importance',
                           tooltip={"placement": "bottom", "always_visible": True}, value=3)

# Elevation Gain
ele_pref_label = html.H4('In feet, how much elevation gain do you want the trail to have?')
ele_pref = dcc.Dropdown(ele_list, id='ele_pref', value='No Preference')
ele_importance_label = html.H4('On a scale of 1 to 5, how much do you value the length of a trail?')
ele_importance = dcc.Slider(1,5,step=1, marks=None, id='ele_importance',
                           tooltip={"placement": "bottom", "always_visible": True}, value=3)
# Difficulty


app.layout = html.Div([
    dbc.Row([
        html.P('test dashboard'),
        wl_pref_label, wl_pref, wl_importance_label, wl_importance
        ])
])




# deploy dashboard
if __name__ == '__main__':
    app.run_server(debug=True)