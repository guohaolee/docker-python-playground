## Notes
- create the logfile first before initalizing python log


## Guides
- https://fangpenlin.com/posts/2012/08/26/good-logging-practice-in-python/
- https://www.toptal.com/python/in-depth-python-logging
- http://zetcode.com/python/logging/
- https://realpython.com/python-logging/
- https://medium.com/better-programming/power-up-your-python-logging-6dd3ed38f322
- https://fangpenlin.com/posts/2012/08/26/good-logging-practice-in-python/
- https://www.loggly.com/ultimate-guide/python-logging-basics/

- Logging Source Code
    - https://realpython.com/python-logging-source-code/#toc

## Rotating & Time file handler
- http://www.blog.pythonlibrary.org/2014/02/11/python-how-to-create-rotating-logs/

## Formatters:
- change the format
```
{
    'format': '%(asctime)s - [%(name)s/%(levelname)s] - [%(processname)s/%(processid)s] - %(message)s', 'datefmt': '%Y-%m-%d %H:%M:%S'
}
or 

c_format = logging.Formatter('%(asctime)s - [%(name)s/%(levelname)s] - [%(processname)s/%(processid)s] - %(message)s', 'datefmt': '%Y-%m-%d %H:%M:%S')
```

## Handlers:
- create own handlers
- https://medium.com/@HLIBIndustry/python-logging-custom-handlers-f3ba784a9452
```
class MyNewHandler(logging.Handler):  # inherit from Handler class
    def __init__(self, special_args):
        logging.Handler.__init__(self)  # run parent __init__ class
        ## Do custom setup stuff 
        ## Save special_args, setup files, etc
    def emit(self, record):  # override Handler's `emit` method
        ## Do log-time actions here 
        ## Send to webhook, send to file, write an email, whatever
```

## Propogate
- if True, means parent/root logger will be use as well
- if False, only the logger will be used

## Choosing which loggers to use in log_config.py
```
import logging
import log_config

# example1 is defined in the log_config.py under loggers
log = logging.getLogger("example1") 

# if use __name__, it will use the root logger
log = logging.getLogger(__name__)
```

## Create config in script
```

import logging

# Create a custom logger
logger = logging.getLogger(__name__)

# Create handlers
c_handler = logging.StreamHandler()
f_handler = logging.FileHandler('file.log')
c_handler.setLevel(logging.WARNING)
f_handler.setLevel(logging.ERROR)

# Create formatters and add it to handlers
c_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
c_handler.setFormatter(c_format)
f_handler.setFormatter(f_format)

# Add handlers to the logger
logger.addHandler(c_handler)
logger.addHandler(f_handler)

logger.warning('This is a warning')
logger.error('This is an error')
```

## Create config from dict/yaml/json
- if load from json:
```
import json

with open("log_config.json",'r') as file:
    conf = json.load(file)
    logging.config.dictConfig(CONFIG)
```

- if load from yaml:
```
with open('logger_config.yaml', 'r') as stream:
  try:
    logging_config = yaml.load(stream, Loader=yaml.SafeLoader)
  except yaml.YAMLError as exc:
    print("Error Loading Logger Config")
    pass
```

```
import logging.config

CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,  # allow module level config to overwrite  
    'formatters': {
        'simple': {
            'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        },
        'custom': {
            'format': '%(asctime)s - [%(name)s/%(levelname)s] - [%(processname)s/%(processid)s] - %(message)s', 'datefmt': '%Y-%m-%d %H:%M:%S'
        }

    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'DEBUG',
            'formatter': 'simple',
            'stream': 'ext://sys.stdout'
        },
        'file': {
            'class': 'logging.FileHandler',
            'level': 'DEBUG',
            'formatter': 'simple',
            'filename': '/app/lib/log/logfile/logfile.log'
    },
    'loggers': {
        'example1': {
            'handlers': ['console', 'file'],
            'level': 'INFO',
            'propagate': False
        }
    },
    # default loggers for all class
    'root': {
        'handlers': ['console', 'time_rotating_log'],
        'level': 'INFO',
        'propagate': False
    }
}

# Initialize the config
logging.config.dictConfig(CONFIG)



logger = logging.getLogger(__name__)
logger.debug("HELLO)
```

## Queue Handler
- https://medium.com/@rob.blackbourn/how-to-use-python-logging-queuehandler-with-dictconfig-1e8b1284e27a

## Django Handler
- https://docs.djangoproject.com/en/dev/topics/logging/#configuring-logging


## Celery task log
- you can override the task's job to another log
- "fulcrum_celery" is the logger from log_config.py
```
from celery.utils.log import get_task_logger
self.logger = get_task_logger("fulcrum_celery")
```
