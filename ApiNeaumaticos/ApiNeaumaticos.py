"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
from ApiNeaumaticos.Pages import *
from ApiNeaumaticos.Pages.Custom404 import create_404_page
from ApiNeaumaticos.Api.Api import router, raiz
from ApiNeaumaticos.styles import stylesheet_url

app = rx.App(stylesheets=stylesheet_url)
app.add_custom_404_page(create_404_page(),title="TireAPI")
app.api.add_api_route("/", raiz)
app.api.include_router(router=router)
""" 
app.api.add_api_route("/pirelli", api_neumaticos_pirelli_file)
app.api.add_api_route("/bridgestone", api_neumaticos_bgristone_file)
app.api.add_api_route("/michelin", api_neumaticos_michelin_file)
"""
