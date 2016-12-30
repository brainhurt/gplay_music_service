'''
Created on Dec 25, 2016

@author: christian
'''
from flask import Flask, Blueprint, request, Response
from rs import GplayConnection
from rs import JsonHelper
from config import log
import config


app = Flask(__name__)
search_bp = Blueprint('search', __name__)

@search_bp.route('/', methods=['GET'])
def search():
    args = request.args.to_dict()
    
    try:
        gplay = GplayConnection(args["un"], args["pw"])
        try:
            result = gplay.search(args["q"], args["max-results"])
        except:
            result = gplay.search(args["q"], config.maxResults)
        return Response(JsonHelper.toJSON(result), mimetype='application/json')
    except Exception, e:
        log.error(e)
        err = Error(e, 'error occurred searching')
        return Response(err,status=400)
    finally:
        if(gplay):
            gplay.close()