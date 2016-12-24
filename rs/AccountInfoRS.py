'''
Created on Dec 24, 2016

@author: christian
'''
from flask import Flask, request, Blueprint, Response
from rs import JsonHelper
from rs import GplayConnection
from rs import AccountInfo

app = Flask(__name__)

account_info = Blueprint('account_info', __name__)

@account_info.route('/info', methods=['GET'])
def getAccountInfo():
    args = request.args.to_dict()
    
    try:
        gplay = GplayConnection(args["un"], args["pw"])
        acctInfo = AccountInfo(gplay.getGplayInstance().is_authenticated(), gplay.getGplayInstance().is_subscribed)
    except:
        acctInfo = AccountInfo(False, False)   
         
    return Response(JsonHelper.toJSON(acctInfo), mimetype='application/json')
    return JsonHelper.toJSON(acctInfo)