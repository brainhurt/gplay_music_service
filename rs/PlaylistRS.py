'''
Created on Dec 29, 2016

@author: christian
'''

from flask import Flask, Blueprint, Response, request
from rs import JsonHelper
from connection.GplayConnection import GplayConnection
from config import log
from rs import Error

app = Flask(__name__)

playlist = Blueprint("playlist", __name__)

@playlist.route('/')
def getPlaylists():
    args = request.args.to_dict()
    
    try:
        include_deleted = args["include-deleted"]
    except:
        include_deleted = False
    
    try:
        gplay = GplayConnection(args["un"], args["pw"])
        playlists = gplay.getPlaylists(include_deleted)
        return Response(JsonHelper.toJSON(playlists), mimetype='application/json')
        
    except Exception as e:
        log.error(e)
        err = Error(e, 'error occurred while getting playlists')
        return Response(err, status=400)
        
    finally:
        if(gplay):
            gplay.close()        