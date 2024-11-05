#!/usr/bin/env python3

"""
A Basic flask application
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    """
    Renders a basic html template
    """
    render_template('0-index.html')
