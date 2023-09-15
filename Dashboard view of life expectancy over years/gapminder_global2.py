import plotly.express as px
import os
import pandas as pd




# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash('gapminder')

# Make Dataframe

# uses plotly express to create bar plot
import plotly.express as px

df = px.data.gapminder()
df=df.sort_values(by=['year'])

fig = px.choropleth(
    data_frame=df, locations="iso_alpha", projection='orthographic',
    color="lifeExp", # lifeExp is a column of gapminder
    hover_name="country", # column to add to hover information
    color_continuous_scale="Viridis",
    animation_frame='year',
    range_color=(0,100),
    width=1800, height=800
)
fig.write_html('lifeexpectancy.html', include_plotlyjs='cdn')

                    
app.layout = html.Div(children=[
    html.H1(children='Visualization of gapminder data', style={'color': 'black'}), # black font color

    html.Div(children='Interactive plot', style={'color': 'green'}), # green font color

    dcc.Graph(
        id='example-graph',
        figure=fig
    ) # adds graph to the Div
])



if __name__ == '__main__':
    app.run_server(debug=True) # runs a local server for the website to run on
