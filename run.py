'''
Created on Dec 24, 2016

@author: christian
'''
from flask import Flask
from rs.AccountInfoRS import account_info
from rs.AboutRS import about
from unitTesting import UnitRunner
from integrationTesting import IntegrationRunner
import sys
import config
from config import log

app = Flask(__name__)

app.register_blueprint(account_info, url_prefix='/account')
app.register_blueprint(about, url_prefix='/about')

if __name__ == "__main__":
    if(sys.argv[1]):
        if(sys.argv[1] == "server"):
            app.run(host=config.host, port=config.port)
        elif(sys.argv[1] == "test"):
            unitResult = UnitRunner.runUnitTests()
            inteResult = IntegrationRunner.runIntegrationTests()
            log.info('Unit Tests: '+str(unitResult.failures.__len__())+' failed out of '+str(unitResult.testsRun))
            log.info('Integration Tests: '+str(inteResult.failures.__len__())+' failed out of '+str(inteResult.testsRun))
        elif(sys.argv[1] == "integrationtest"):
            IntegrationRunner.runIntegrationTests()
            log.info('Integration Tests: '+str(inteResult.failures.__len__())+' failed out of '+str(inteResult.testsRun))
        elif(sys.argv[1] == "unittest"):
            UnitRunner.runUnitTests()
            log.info('Unit Tests: '+str(unitResult.failures.__len__())+' failed out of '+str(unitResult.testsRun))
        elif(sys.argv[1] == "help"):
            log.info("The options are as follows: ")
            log.info("server: begins running the server")
            log.info("integrationtest: runs the integration tests")
            log.info("unittest: runs the unit tests")
        else:
            log.warn('The argument \''+sys.argv[0]+'\' is not applicable, please run with the help ' \
             + 'argument to view available options')