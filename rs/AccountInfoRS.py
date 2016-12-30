'''
Created on Dec 24, 2016

@author: christian
'''
from flask import Flask, request, Blueprint, Response
from rs import JsonHelper
from rs import GplayConnection
from rs import AccountInfo
from rs import Error

app = Flask(__name__)

account_info = Blueprint('account_info', __name__)

@account_info.route('/info', methods=['GET'])
def getAccountInfo():
    args = request.args.to_dict()
    
    try:
        gplay = GplayConnection(args["un"], args["pw"])
        acctInfo = AccountInfo(gplay.getGplayInstance().is_authenticated(), gplay.getGplayInstance().is_subscribed)
    except:
        err = Error('error occurred, log in or account info retrieval failed', 'gplay connection failed')
        Response(err, 400)
    finally:
        if(gplay):
            gplay.close()
         
    return Response(JsonHelper.toJSON(acctInfo), mimetype='application/json')
    return JsonHelper.toJSON(acctInfo)