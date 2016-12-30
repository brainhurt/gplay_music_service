'''
Created on Dec 23, 2016

@author: christian
'''

import json

def toJSON(object):
    if(object):
        if(type(object) is dict):
            return json.dumps(object, sort_keys=True)
        else:    
            return json.dumps(object.__dict__, sort_keys=True)
    else:
        return None