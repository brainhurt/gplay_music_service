'''
Created on Dec 29, 2016

@author: christian
'''

class Error:
    message = None
    type = None
    
    def __init__(self, message, type):
        self.message = message
        self.type = type