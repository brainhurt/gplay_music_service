'''
Created on Dec 24, 2016

@author: christian
'''
# tests/runner.py
import unittest

# import your test modules
from unitTesting import JsonHelperTest
from unitTesting import GplayConnectionTest


def runUnitTests():
    # initialize the test suite
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    # add tests to the test suite
    suite.addTests(loader.loadTestsFromModule(JsonHelperTest))
    suite.addTests(loader.loadTestsFromModule(GplayConnectionTest))
    
    # initialize a runner, pass it your suite and run it
    runner = unittest.TextTestRunner(verbosity=3)
    return runner.run(suite)