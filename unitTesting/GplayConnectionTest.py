'''
Created on Dec 23, 2016

@author: christian
'''
import unittest
import config
from unitTesting import GplayConnection

class GplayConnectionTest(unittest.TestCase):


    def test_init(self):
        gplay = GplayConnection(config.gplayUsername, config.gplayPassword)
        self.assertTrue(gplay.getGplayInstance().is_authenticated())
        self.assertFalse(gplay.getGplayInstance().is_subscribed)
        
    def test_init_invalid(self):
        gplay = GplayConnection('foo', 'bar')
        self.assertTrue(gplay)
        self.assertFalse(gplay.getGplayInstance().is_authenticated())
        
    def test_init_nonecreds(self):
        gplay = GplayConnection(None, None)
        self.assertFalse(gplay.getGplayInstance().is_authenticated())
         
    def test_close(self):
        gplay = GplayConnection(config.gplayUsername, config.gplayPassword)
        self.assertTrue(gplay.getGplayInstance().is_authenticated())
        gplay.close()
        self.assertFalse(gplay.getGplayInstance().is_authenticated())
         
    def test_search(self):
        gplay = GplayConnection(config.gplayUsername, config.gplayPassword)
        results = gplay.search('foo', 5)
        self.assertTrue(results)
        self.assertEqual(results.__len__(), 8)
        self.assertLessEqual(results.get('album_hits').__len__(), 5)
        self.assertLessEqual(results.get('artist_hits').__len__(), 5)
        self.assertLessEqual(results.get('playlist_hits').__len__(), 5)
        self.assertLessEqual(results.get('podcast_hits').__len__(), 5)
        self.assertLessEqual(results.get('situation_hits').__len__(), 5)
        self.assertLessEqual(results.get('song_hits').__len__(), 5)
        self.assertLessEqual(results.get('video_hits').__len__(), 20)
        self.assertLessEqual(results.get('station_hits').__len__(), 20)
         
    def test_search_None(self):
        gplay = GplayConnection(config.gplayUsername, config.gplayPassword)
        results = gplay.search(None, 5)
        self.assertFalse(results)
         
    def test_search_nologin(self):
        gplay = GplayConnection(None, None)
        results = gplay.search('foo', 5)
        self.assertFalse(results)                 
        
    def test_playlist(self):
        gplay = GplayConnection(config.gplayUsername, config.gplayPassword)
        results = gplay.getPlaylists(False)
        self.assertTrue(results)
        
    def test_playlist_deleted(self):
        gplay = GplayConnection(config.gplayUsername, config.gplayPassword)
        results = gplay.getPlaylists(True)
        self.assertTrue(results)   

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()