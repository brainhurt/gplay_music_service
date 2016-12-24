'''
Created on Dec 23, 2016

@author: christian
'''
import unittest
from connection import JsonHelper

class Person:
    name = None
    email = None
    
    def __init__(self):
        self.name = "Bob"
        self.email = "bob@email.com"
        
        

class JsonHelperTest(unittest.TestCase):


    def test_toJson(self):
        p = Person()
        j = JsonHelper.toJSON(p)
        self.assertTrue(j)
        self.assertEqual(j, '{"email": "bob@email.com", "name": "Bob"}')
        
    def test_toJson_none(self):
        j = JsonHelper.toJSON(None)
        self.assertFalse(j)   



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()