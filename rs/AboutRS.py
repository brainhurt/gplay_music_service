'''
Created on Dec 24, 2016

@author: christian
'''

from flask import Flask, Blueprint, Response
from rs import JsonHelper
from domain.About import About

app = Flask(__name__)

about = Blueprint('about', __name__)

@about.route('/')
def getAbout():
    about = About()
    return Response(JsonHelper.toJSON(about), mimetype='application/json')