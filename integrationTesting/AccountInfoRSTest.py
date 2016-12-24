'''
Created on Dec 24, 2016

@author: christian
'''
import unittest
import json
import requests
import config

class AccountInfoRSTest(unittest.TestCase):


    def test_login(self):
        response = requests.get('http://localhost:5000/account/info?un='+config.gplayUsername+'&pw='+config.gplayPassword)
        j = json.loads(response._content)
        self.assertTrue(response)
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.ok, True)
        self.assertEqual(response.reason, 'OK')
        
        self.assertEqual(j["isSubscribed"], False)
        self.assertEqual(j["canLogIn"], True)
    
    def test_nouser(self):
        response = requests.get('http://localhost:5000/account/info?pw='+config.gplayPassword)
        j = json.loads(response._content)
        self.assertTrue(response)
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.ok, True)
        self.assertEqual(response.reason, 'OK')
        
        self.assertEqual(j["isSubscribed"], False)
        self.assertEqual(j["canLogIn"], False)
    
    def test_nopass(self):
        response = requests.get('http://localhost:5000/account/info?un='+config.gplayUsername)
        j = json.loads(response._content)
        self.assertTrue(response)
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.ok, True)
        self.assertEqual(response.reason, 'OK')
        
        self.assertEqual(j["isSubscribed"], False)
        self.assertEqual(j["canLogIn"], False)
    
    def test_nocreds(self):
        response = requests.get('http://localhost:5000/account/info')
        j = json.loads(response._content)
        self.assertTrue(response)
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.ok, True)
        self.assertEqual(response.reason, 'OK')
        
        self.assertEqual(j["isSubscribed"], False)
        self.assertEqual(j["canLogIn"], False)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()