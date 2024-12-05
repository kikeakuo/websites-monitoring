#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
__author__ = 'kikeakuo'
__version__ = '1.0.0'
# ----------------------------------------------------------------------------

"""
wsm.py:
This Python script to monitor website uptime and display it in an HTML dashboard, 
you'll need to use a library like requests to check the website's status and BeautifulSoup to parse the HTML.
However, a more suitable approach would be to use a library like scrapy or selenium 
for scraping and dash or flask for creating the dashboard.
"""

# ----------------------------------------------------------------------------
# Install required libraries
# ----------------------------------------------------------------------------
pip install requests dash

# ----------------------------------------------------------------------------
# Import
# ----------------------------------------------------------------------------
import requests
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

# List of websites to monitor
websites = [
    {'name': 'Google', 'url': 'https://www.google.com'},
    {'name': 'Brave', 'url': 'https://brave.com'},
    {'name': 'Stack Overflow', 'url': 'https://stackoverflow.com'}
]

# Function to check website uptime
def check_uptime(url):
    try:
        response = requests.head(url, timeout=5)
        return response.status_code == 200
    except requests.RequestException:
        return False

# Create a Dash app
app.layout = html.Div([
    html.H1('Website Uptime Monitor'),
    html.Table([
        html.Tr([html.Th('Website'), html.Th('Uptime')]),
        html.Tbody([
            html.Tr([html.Td(website['name']), html.Td(website['uptime'])]) for website in websites
        ])
    ])
])

# Update website uptime in real-time
@app.callback(
    Output('uptime-table', 'children'),
    [Input('interval-component', 'n_intervals')]
)
def update_uptime(n):
    for website in websites:
        website['uptime'] = check_uptime(website['url'])
    return html.Table([
        html.Tr([html.Th('Website'), html.Th('Uptime')]),
        html.Tbody([
            html.Tr([html.Td(website['name']), html.Td(website['uptime'])]) for website in websites
        ])
    ])

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)

# import os               # For file and folder operations

