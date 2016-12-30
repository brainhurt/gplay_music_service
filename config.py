'''
Created on Dec 24, 2016

@author: christian
'''
import logging
import sys
from logging import handlers

# Level for the logger to log to the console.
loggingLevel=logging.INFO

# name of the logging file
loggingFile='gplayservice.log'

# gplay login credentials
gplayUsername='c.andersen2012@gmail.com'
gplayPassword='Abs14qp99z!'
maxResults=5

# Flask options
port = 5000
host='0.0.0.0'

# Testing options
server = "http://localhost"

# logging logging configuration
log = logging.getLogger('__name__')
log.setLevel(loggingLevel)
format = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

ch = logging.StreamHandler(sys.stdout)
ch.setFormatter(format)
log.addHandler(ch)

fh = handlers.RotatingFileHandler(loggingFile, maxBytes=(1048576*5), backupCount=7)
fh.setFormatter(format)
log.addHandler(fh)