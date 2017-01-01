'''
Created on Dec 23, 2016

@author: christian
'''

from gmusicapi import Mobileclient

class GplayConnection:
    '''
    classdocs
    '''
    api = None
    log = None

    def __init__(self, username, password):
        '''
        Constructor
        '''
        
        self.api = Mobileclient()
        if(username and password):
                isLoggedIn = self.api.login(username, password, self.api.FROM_MAC_ADDRESS, 'en_us')
        else:
            isLoggedIn = False
        
    
    def close(self):
        return self.api.logout()
    
    def getGplayInstance(self):
        return self.api
    
    def search(self, searchTerm, maxResults):
        if(searchTerm):
            try:
                results = self.api.search(searchTerm, max_results=maxResults)
            except:
                results = False    
        else:
            results = False    
        return results
    
    def getGenres(self, parentGenre):
        results = self.api.search(parentGenre)
        
    def getPlaylists(self, includeDeleted):
        return self.api.get_all_playlists(False, includeDeleted)    
        