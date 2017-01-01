# GPlay API

This api serves as a wrapper for the gmusicapi written by Simon Webber. This wraps the python api and functions as a REST api allowing the user to run and make api calls to be returned in JSON format. This is all written in python.

### Libraries Used
gmusicapi -
flask - 


### Uses
Run the server by using the command

`python run.py server`

Test Using

`python run.py unittest`

Get Help using
`python run.py help`


## Configuration

You must create a file called config.py for this to run correctly a sample file will be shown below

```
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
gplayUsername='test@gmail.com'
gplayPassword='mypassword'
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
```