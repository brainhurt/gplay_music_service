'''
Created on Dec 24, 2016

@author: christian
'''
import unittest
import requests
import json


class AboutRSTest(unittest.TestCase):

    def test_about(self):
        response = requests.get('http://localhost:5000/about')
        j = json.loads(response._content)
        self.assertTrue(response)
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.ok, True)
        self.assertEqual(response.reason, 'OK')
        
        self.assertEqual(j["version"], "v0.1")
        self.assertEqual(j["documentationUrl"], "http://notImplemented.com")
        self.assertEqual(j["description"], "This service allows the user to connect to google play services")
        self.assertEqual(j["copyright"], "copyright 2016")

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()