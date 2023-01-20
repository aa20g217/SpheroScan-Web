#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  14 17:17:42 2022

@author: akshay
"""

from app import app
from dash import dcc,html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

from UI_com import visualization,pred
from pathlib import Path
from zipfile import ZipFile

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!    
navigation_bar = dbc.Navbar(
    dbc.Container(        [            
            dbc.Col(dbc.NavbarBrand(html.Img(src="assets/logo-color.svg", height="80px")),width=1),
            dbc.Col(dbc.NavbarBrand(html.I("SpheroScan"), style={"margin-left": "0px","font-weight": "bold","font-size": "40px","color":"white"}),width=1,align="left"),
            dbc.Col(width=9),
            html.A(dbc.Col(html.Img(src="https://www.unibe.ch/media/logo-unibern-footer@2x.png", height="80px"),align="right"),
                href="https://www.unibe.ch/index_ger.html", target="_blank",
                style={"textDecoration": "none"}),
        ],fluid=True,
    ),
   color="black", 
   dark=True,style={"border-color": "white"}
)

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
about=dbc.Card([html.Div([
    dbc.Row(html.H6("SpheroScan",style={"font-weight": "bold","color":"black"})),
    dbc.Row(html.P("SpheroScan is a user-friendly deep learning tool designed for analyzing images of spheroids. It uses state-of-the-art techniques to detect and segment spheroids, making it easy for researchers to process large amounts of data. This user-friendly, interactive tool is designed to streamline the process of spheroid segmentation, area calculation, and downstream analysis of spheroid image data, and can help to standardize and accelerate the analysis of spheroid assay results. SpheroScan consists of two main modules: prediction and visualization. The prediction module uses previously trained Deep Learning (DL) models to mask the input spheroid images and generate a CSV file with the area and intensity of each detected spheroid. The visualization module allows the user to analyze the results of the prediction module through various types of plots and statistical analysis. The plots generated by the visualization module are ready for publication and can be saved as high-quality images in png format. Overall, SpheroScan is a powerful and user-friendly tool that can greatly simplify and enhance the analysis of spheroid image data.",
                    style={"text-align": "justify"})),
    html.Br(),
    dbc.Row(html.H6("Availability",style={"font-weight": "bold","color":"black"})),
    html.Div(["SpheroScan is developed by the ",
             html.A("Functional Urology group", href="http://www.urofun.ch/", target="_blank"),
             " at the ",
             html.A("University of Bern", href="https://www.unibe.ch/index_ger.html", target="_blank"),
             ". The source code and tutorial can be found on the ",
             html.A("SpheroScan GitHub repository", href="https://github.com/FunctionalUrology/SpheroScan.git", target="_blank"),
    ],style={"text-align": "justify"}),
    
    html.Br(),
    dbc.Row(html.H6("Contact",style={"font-weight": "bold","color":"black"})),
    html.P("Bug reports and new feature requests can be communicated via:"),
    html.Ul([html.Li(html.Div(["GitHub : ",html.A("https://github.com/FunctionalUrology/SpheroScan.git", href="https://github.com/FunctionalUrology/SpheroScan.git", target="_blank")]),)]),
    html.Ul([html.Li("Email : akshay.akshay@unibe.ch , ali.hashemi@dbmr.unibe.ch")]),
    html.Br(),
    dbc.Row(html.H6("Note",style={"font-weight": "bold","color":"black"})),
    html.P("If you are interested in using the SpheroScan for spheroid images from different platforms and are willing to share images from your dataset, please contact the development team for further information."),
    dbc.Row(html.H6("Citation",style={"font-weight": "bold","color":"black"})),
    html.Div(["If SpheroScan helps you in any way, please cite the SpheroScan article:"]),
    html.Ul([html.Li(html.A("", href="", target="_blank"))]),

    ],style={"margin-left": "10px","margin-right": "10px","margin-top": "10px","font-size": "14px"})],
    style={"margin-left": "5px","margin-right": "5px","margin-top": "10px"})



#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!    
tabs_main = dbc.Card(
    [
     dbc.CardHeader(
        dbc.Tabs(
            [
                dbc.Tab(label="Prediction", tab_id="pred"),
                dbc.Tab(label="Visualization", tab_id="visu"),
                dbc.Tab(label="About", tab_id="about"),
            ],
            id="tabs_main",
            active_tab="pred", 
            #card=True,
        ),style={"border-color":"black"}),
        dbc.CardBody(html.P(id="content_main", className="mt-3")),
        html.Div(["This webpage is generated by ",
                  html.A("SpheroScan.", href="https://github.com/FunctionalUrology/SpheroScan.git", target="_blank")],
                 style={"margin-left": "10px","font-size": "11px"}),
    ],color="dark", outline=True,    )

 
app.layout = html.Div([navigation_bar,
                       tabs_main, 
                       dcc.Store(id='filepath_init',data={}),
                       dcc.Store(id='filepath_data',data={}),
                      ]) 

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!    
@app.callback(Output("content_main", "children"), [Input("tabs_main", "active_tab")])
def switch_tab(at):
    if at == "pred":
        return pred
    elif at == "visu":
        return visualization 
    elif at == "about":
        return about 
    return html.P("This shouldn't ever be displayed. Please contact the developer.")



from waitress import serve
import webbrowser as web
server = app.server
#web.open_new_tab('http://127.0.0.1:4549/')

#if __name__ == '__main__':
 #   app.run_server(host='127.0.0.1', port=4549,debug=False,dev_tools_hot_reload=False)
    
