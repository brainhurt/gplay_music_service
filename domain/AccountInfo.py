'''
Created on Dec 24, 2016

@author: christian
'''

class AccountInfo:
    '''
    classdocs
    '''
    isSubscribed = None
    canLogIn = None

    def __init__(self, canLogIn, isSubscribed):
        if(canLogIn):
            self.canLogIn = True
        else:
            self.canLogIn = False
            
        if(isSubscribed):
            self.isSubscribed = True
        else:
            self.isSubscribed = False
        